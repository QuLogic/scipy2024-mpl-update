"""
Feature highlights for Matplotlib 3.10.0.
"""

from functools import partial

import numpy as np
import matplotlib as mpl

from mplslide import BULLET, FONT, new_slide, slide_heading, annotate_pr_author

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


def multivariate_colormaps():
    """
    Create slide for upcoming 3.10 multivariate colormapping.
    """
    fig = new_slide()

    slide_heading(fig, '3.10: Upcoming features')

    level1 = partial(bullet_level1, fig)

    level1(0.8, f'{BULLET} Multivariate colormapping')

    left, right = fig.subplots(1, 2)
    fig.subplots_adjust(top=0.7)

    im_A = np.arange(200)[np.newaxis, :]*np.ones((200, 200))
    im_B = np.arange(200)[:, np.newaxis]*np.ones((200, 200))
    im_C = 0.9*im_A + 0.9*im_B

    im_A = np.sin(im_A**0.5)**2
    im_B = np.sin(im_B**0.5)**2
    im_C = np.sin(im_C**0.5)**2

    cmaps = mpl.multivar_colormaps['3VarAddA']

    cm = left.imshow((im_A, im_B, im_C), cmap=cmaps, vmin=(0, 0, 0), vmax=(1, 1, 1))
    cbar_A, cbar_B, cbar_C = fig.colorbars(cm)
    cbar_A.set_label('A', fontsize=24)
    cbar_B.set_label('B', fontsize=24)
    cbar_C.set_label('C', fontsize=24)
    for cb in (cbar_A, cbar_B, cbar_C):
        cb.set_ticks([])

    x = np.linspace(-1.5, 0.5, 200)
    y = np.linspace(-1, 1, 200)
    xx, yy = np.meshgrid(x, y)
    c = xx+1j*yy
    z = c
    for i in range(7):
        z = z**2+c

    cm = right.pcolormesh(xx, yy, (z.imag, z.real), cmap='BiCone', vmin=-1, vmax=1)
    right.set_xlabel('Re{$c$}', fontsize=24)
    right.set_ylabel('Im{$c$}', fontsize=24)
    right.set_title('Mandelbrot $z_{7}$ $z_i = z_{i-1}^2+c$', fontsize=24)

    cb_right = fig.colorbar_2D(cm)
    cb_right.set_ylabel('Im{$z$}', fontsize=24)
    cb_right.set_xlabel('Re{$z$}', fontsize=24)

    for ax in (left, right, cb_right):
        ax.set(xticks=[], yticks=[])

    annotate_pr_author(fig, 'trygvrad', pr=26996)

    return fig


def misc():
    """
    Create slide for miscellaneous 3.10 features.
    """
    fig = new_slide()

    slide_heading(fig, 'Sprint topics')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    level1(0.8, f'{BULLET} GSoD for example categorization (Eva Sibinga)')
    level1(0.7, f'{BULLET} Tagging examples with sphinx-tags (by @melissawm)')
    level2(0.7, '\n\n.. tags:: animation, component: axes', **CODE)
    level2(0.7, '\n\n\nCome to our Sprint!')

    level1(0.4, f'{BULLET} Your Contribution?')
    t = level2(
        0.4,
        f'\n{BULLET} New Contributors Meeting  (first Tuesday of month)')
    t.set_url('https://scientific-python.org/calendars/')

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        multivariate_colormaps(),
        misc(),
    )
