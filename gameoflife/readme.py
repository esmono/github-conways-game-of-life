import base64
import re
import sys

from github import Github, GithubException


START_COMMENT = '<!--START_SECTION:gameoflife-->'
END_COMMENT = '<!--END_SECTION:gameoflife-->'
listReg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

repository = os.getenv('INPUT_REPOSITORY')
ghtoken = os.getenv('INPUT_GH_TOKEN')
show_title = os.getenv("INPUT_SHOW_TITLE")
commit_message = os.getenv("INPUT_COMMIT_MESSAGE")

def get_readme(readme):
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')

def new_readme(graph, readme):
    '''Generate a new Readme.md'''
    stats_in_readme = f"{START_COMMENT}\n{graph}\n{END_COMMENT}"
    return re.sub(listReg, stats_in_readme, readme)

if __name__ == '__main__':
    g = Github(ghtoken)
    try:
        repo = g.get_repo(repository)
    except GithubException:
        print("Authentication Error. Try saving a GitHub Token in your Repo Secrets or Use the GitHub Actions Token, which is automatically used by the action.")
        sys.exit(1)
    contents = repo.get_readme()
    # Need to generate the new README
    graph = ''
    readme = get_readme(contents.content)
    new_readme = new_readme(graph, readme)
    if new_readme != readme:
        repo.update_file(path=contents.path, message=commit_message,
                         content=new_readme, sha=contents.sha, branch='master')
