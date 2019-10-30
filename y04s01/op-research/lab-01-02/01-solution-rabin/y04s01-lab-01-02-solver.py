import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as pltticker

BOUNDS_X = (-2, 12)
BOUNDS_Y = (-2, 12)

LABEL_X = r'$x_1$'
LABEL_Y = r'$x_2$'


def format_axes(
        ax,
        xlim=BOUNDS_X,
        ylim=BOUNDS_Y,
        xlabel=LABEL_X,
        ylabel=LABEL_Y,
        tick_every=1.0,):
    """Formats the plot axes.

    Args:
        ax (:obj:`matplotlib.Axes`): an Axes object to be formatted.
        xlim (tuple): tuple of x limits in the form of (x_min, x_max)
        ylim (tuple): tuple of y limits in the form of (y_min, y_max)
        xlabel (str): OX axis label.
        ylabel (str): OY axis label.
        tick_every (float): create ticks using this period.
    """
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Tick every 1.0
    ticker = pltticker.MultipleLocator(base=tick_every)
    ax.xaxis.set_major_locator(ticker)
    ax.yaxis.set_major_locator(ticker)


def apply_restriction(x, y, restriction):
    """Applies the given restriction to the feasible region.

    Args:
        x (np.array): array of X values.
        y (np.array): array of Y values.
        restriction (callable): a restriction function.

    Returns:
        An `np.array` of True / False values corresponding to whether the
        solution applies here or not.
    """
    restricted = [restriction(x, y) for x, y in zip(x, y)]

    return restricted


# Create 2000 evenly spaced sample points in the BOUNDS_X interval
x1 = np.arange(
    *(BOUNDS_X),
    step=0.01,
)

# Create points for linear restrictions

x2_1 = 8 - 4 * x1
x2_2 = (10 - 2 * x1) / 5
x2_3 = (10 - 5 * x1) / -2

# zero values for y = 0, x = 0 restrictions
zeros = (0 * x1) + 0
# Array of ones for x2 > 1
ones = (0 * x1) + 1

# Plot restrictions
fig, ax = plt.subplots()
ax.plot(x1, x2_1, label=r'$4 x_1 + x_2 \leq 8$')
ax.plot(x1, x2_2, label=r'$2 x_1 + 5 x_2 \leq 10$')
ax.plot(x1, x2_3, label=r'$5 x_1 - 2 x_2 \geq 10$')

# Plot x_1 > 0
ax.plot(x1, zeros, label=r'$x_1 \geq 0$')
# Plot x_2 > 0
ax.plot(zeros, x1, label=r'$x_2 \geq 0$')

# Plot x_2 > 1
ax.plot(x1, ones, label=r'$x_2 \geq 1$')

# Create points for solution space polygon
solution_space_lim_hi = np.minimum(x2_1, x2_2)
solution_space_lim_lo = ones

feasible_region = solution_space_lim_lo < solution_space_lim_hi

# Apply x_1 >= 0 restriction
feasible_region = apply_restriction(
    x1,
    feasible_region,
    restriction=lambda x, y: False if x < 0 else y
)


# Plot solution space polygon
ax.fill_between(
    x1,
    solution_space_lim_lo,
    solution_space_lim_hi,
    where=feasible_region,
    color='grey',
    alpha=0.5,
)

format_axes(
    ax,
    xlim=BOUNDS_X,
    ylim=BOUNDS_Y,
)

plt.legend(
    # loc=2,
    borderaxespad=0.0,
)
plt.show()
