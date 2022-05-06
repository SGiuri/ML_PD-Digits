from math import ceil
import matplotlib.pyplot as plt
from numpy import unravel_index

def show_multiple_img(images, targets):
    """
    :param images:
    :param targets:
    :return:
    """

    if len(images) < 6:
        my_cols = len(images)
    else:
        my_cols = 6
    my_rows = ceil(len(images) / my_cols)

    fig_width = my_cols * 10 / 6
    fig_height = my_rows * 10 / 4

    fig = plt.figure(figsize=(fig_width, fig_height))
    gs = fig.add_gridspec(my_rows, my_cols)

    axes = []
    matrix_dimension = (my_rows, my_cols)
    for n, image in enumerate(images):
        subplot_position = unravel_index(n, matrix_dimension)

        axes.append(fig.add_subplot(gs[subplot_position]))

    for ax in axes:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    for ax, image, target in zip(axes, images, targets):
        ax.set_title(target)
        ax.imshow(image, cmap=plt.cm.gray_r)
    plt.tight_layout()
    plt.show()