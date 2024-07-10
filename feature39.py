"""
Feature highlights for Matplotlib 3.9.0.
"""

import numpy as np

from mplslide import FONT, new_slide, slide_heading, annotate_pr_author

CODE = dict(fontfamily='monospace', fontsize=32, verticalalignment='top',
            alpha=0.7)


def bullet_level1(fig, y, text):
    """
    Create a level 1 list item.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.05, y, text,
                    fontproperties=FONT, fontsize=48, alpha=0.7,
                    verticalalignment='top')


def bullet_level2(fig, y, text, **kwargs):
    """
    Create a level 2 list item.

    This is roughly the same as level 1, but not bolded, and indented more.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.1, y, text,
                    **{'fontproperties': FONT, 'fontsize': 48, 'fontweight': 'normal',
                       'alpha': 0.7, 'verticalalignment': 'top', **kwargs})


def boxplot_legend():
    """
    Create slide for boxplot legends.
    """
    fig = new_slide()
    slide_heading(fig, '3.9: Legend support for boxplot')

    bullet_level2(fig, 0.80,
                  'ax.boxplot(fruit_weights,\n'
                  '           label=["peaches", "oranges", "tomatoes"])',
                  **CODE)

    np.random.seed(19680801)
    fruit_weights = [
        np.random.normal(130, 10, size=100),
        np.random.normal(125, 20, size=100),
        np.random.normal(120, 30, size=100),
    ]
    labels = ['peaches', 'oranges', 'tomatoes']
    colors = ['peachpuff', 'orange', 'tomato']

    ax = fig.subplots()

    bplot = ax.boxplot(fruit_weights,
                       patch_artist=True,  # fill with color
                       label=labels)

    # fill with colors
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    ax.legend()

    ax.set(xticks=[], yticks=[])
    fig.subplots_adjust(bottom=0.1, top=0.7)

    annotate_pr_author(fig, 'saranti', pr=27840)

    return fig


def stackplot_hatch():
    """
    Create slide for stackplot hatching.
    """
    fig = new_slide()
    slide_heading(fig, '3.9: Individual stackplot hatches')

    ax1, ax2 = fig.subplots(ncols=2)

    cols = 10
    rows = 4
    data = (
        np.reshape(np.arange(0, cols, 1), (1, -1)) ** 2 +
        np.reshape(np.arange(0, rows), (-1, 1)) +
        np.random.random((rows, cols))*5
    )
    x = range(data.shape[1])
    ax1.stackplot(x, data, hatch='x')
    ax2.stackplot(x, data, hatch=['//', '\\', 'x', 'o'])

    ax1.set_title("hatch='x'", fontsize=24)
    ax2.set_title("hatch=['//', '\\\\', 'x', 'o']", fontsize=24)

    for ax in (ax1, ax2):
        ax.set(xticks=[], yticks=[])
    fig.subplots_adjust(bottom=0.1, top=0.75)

    annotate_pr_author(fig, 'nbarlowATI', pr=27158)

    return fig


def violin_sides():
    """
    Create slide for violinplot sides.
    """

    fig = new_slide()
    slide_heading(fig, '3.9: Violinplot sides')

    np.random.seed(19680801)
    data = np.random.normal(0, 8, size=100)

    ax = fig.subplots()
    ax.violinplot(data, [0], showmeans=True, showextrema=True)
    ax.violinplot(data, [1], showmeans=True, showextrema=True, side='low')
    ax.violinplot(data, [2], showmeans=True, showextrema=True, side='high')

    ax.set_xticks([0, 1, 2], ['Default', 'side="low"', 'side="high"'], fontsize=24)
    ax.set_yticks([])
    fig.subplots_adjust(bottom=0.13, top=0.8)

    annotate_pr_author(fig, 'anjabeck', pr=27815)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        boxplot_legend(),
        stackplot_hatch(),
        violin_sides(),
    )
