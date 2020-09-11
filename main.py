import argparse
from gameoflife.petri_dish import PetriDish


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('-h', '--height', help='Board Height', default=25)
    ap.add_argument('-w', '--width', help='Board Width', default=100)
    ap.add_argument('-i', '--inumber', help='Number of iterations', default=30)
    args = vars(ap.parse_args())

    height = int(args['height'])
    width = int(args['width'])
    i_number = args['inumber']
    petri_dish = PetriDish((height, width), i_number)
    petri_dish.animate()

if __name__ == '__main__':
    main()
