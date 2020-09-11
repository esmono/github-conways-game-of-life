import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from gameoflife.game_of_life import GameOfLife


class PetriDish(object):
    def __init__(self, size, i_number, seed='Random'):
        if seed == 'Random':
            self.state = np.random.randint(2, size=size)
        else:
            self.state = seed
        self.engine = GameOfLife(self, size)
        self.size = size
        self.i_number = i_number

        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(self.size[0]/10)
        self.fig.set_figwidth(self.size[1]/10)
        self.ax.pcolormesh(self.state, vmin=0, vmax=2, cmap=plt.cm.hot)

    def update(self, i):
        self.state = self.engine.apply_rules()
        pc = self.ax.pcolormesh(self.state, vmin=0, vmax=2, cmap=plt.cm.viridis)
        return pc,

    def animate(self):
        plt.axis('off')
        plt.tight_layout(pad=0)

        im_ani = animation.FuncAnimation(self.fig, self.update, frames=self.i_number,
                                         interval=200, repeat_delay=1000, blit=True)
        writer_gif = animation.PillowWriter(fps=3)
        im_ani.save('./assets/game-of-life.gif', writer=writer_gif)