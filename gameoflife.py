import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numba as nb

@nb.njit(cache=True)
def iteration(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            idx = np.array([[i - 1, i - 1, i - 1, i, i, i + 1, i + 1, i + 1],
                            [j - 1, j, j + 1, j - 1, j + 1, j - 1 , j, j + 1]])
            neigh = 0
            for a, b in zip(idx[0], idx[1]):
                neigh += grid[a, b]

            if grid[i, j] and (neigh < 2 or neigh > 3):
                new_grid[i, j] = 0
            elif not grid[i, j] and neigh==3:
                new_grid[i, j] = 1
    return new_grid



def init(N):
    grid = np.zeros((N, N), dtype='bool')
    grid[:] = np.random.choice([1, 0], (N, N))
    return grid

if __name__ == '__main__':

    M = init(100)
    def update(i):
        new_M = iteration(matrice.get_array())
        matrice.set_array(new_M)


    fig, ax = plt.subplots(dpi=150)
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    matrice = ax.matshow(M, animated=True, cmap='Greys')
    ani = animation.FuncAnimation(fig, update, frames=2000, interval=100, repeat=True)
    writergif = animation.PillowWriter(fps=5)
    ani.save('./life.gif', writer=writergif)
