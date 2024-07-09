"""
Feature highlights for Matplotlib 3.8.0.
"""

from functools import partial

import numpy as np

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


def ecdf():
    """
    Create slide for Empirical Cumulative Distribution Functions.
    """
    fig = new_slide()
    slide_heading(fig, '3.8: ECDFs')

    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.1, top=0.75)

    np.random.seed(19680801)
    ax.ecdf(np.random.randn(100), linewidth=5)

    fig.text(0.05, 0.8, 'ax.ecdf(np.random.randn(100))', **CODE)

    annotate_pr_author(fig, 'anntzer', pr=24728)

    return fig


def mathtext():
    """
    Create slide for 3.8 mathtext features.
    """
    fig = new_slide()
    slide_heading(fig, '3.8: Mathtext improvements')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    level1(0.8, 'Improvements lead by GSoC student @devRD (Ratnabali Dutta)')

    t = level1(
        0.7,
        f'{BULLET} \\boldsymbol support (PR#25661)')
    t.set_url('https://github.com/matplotlib/matplotlib/pull/25661')
    level2(0.7,
           '\n\\boldsymbol{a+2+\\alpha} $\\rightarrow \\boldsymbol{a+2+\\alpha}$')

    t = level1(0.55,
               f'{BULLET} More mathematical operators (PR#26024)')
    t.set_url('https://github.com/matplotlib/matplotlib/pull/26024')
    level2(0.55,
           '\n'
           r'\dagger $\dagger$, '
           r'\QED $\QED$, '
           r'\sinewave $\sinewave$, '
           r'\isinE $\isinE$, '
           'etc.')

    t = level1(0.4, f'{BULLET} More relational operators (PR#25933)')
    t.set_url('https://github.com/matplotlib/matplotlib/pull/25933')

    level2(0.4,
           '\n'
           r'\leqq $\leqq$, '
           r'\lessgtr $\lessgtr$, '
           r'\backsim $\backsim$, '
           r'\precsim $\precsim$, '
           '\n'
           r'\gtrapprox $\gtrapprox$, '
           r'\lll $\lll$, '
           r'\Vvdash $\Vvdash$, '
           r'\triangle $\triangle$, '
           'etc.')

    t = level1(0.2, f'{BULLET} Support for \\text (PR#22173 by @oscargus)')
    t.set_url('https://github.com/matplotlib/matplotlib/pull/22173')

    level2(0.2,
           '\n \\$math \\text{text}\\$ $\\rightarrow math \\text{text}$')

    return fig


def typing():
    """
    Create slide for miscellaneous 3.8 features.
    """
    fig = new_slide()

    slide_heading(fig, '3.8: Type hints (provisional)')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    level1(0.8, f'{BULLET} Simple signatures')
    level2(0.74,
           'bar(x: float | ArrayLike, height: float | ArrayLike,\n'
           '    width: float | ArrayLike, bottom: float | ArrayLike | None,\n'
           '    *, align: Literal["center", "edge"], data = ...,\n'
           '    **kwargs) -> BarContainer:',
           **CODE)

    level1(0.55, f'{BULLET} Complex (overloaded) signatures')
    level2(0.49,
           'def subplot_mosaic(mosaic: str, *,\n'
           '    empty_sentinel: str, subplot_kw: dict[str, Any] | None\n'
           ') -> dict[str, Axes]: ...\n'
           'def subplot_mosaic(mosaic: list[HashableList[_T]], *,\n'
           '    empty_sentinel: _T, subplot_kw: dict[str, Any] | None,\n'
           ') -> dict[_T, Axes]: ...\n'
           'def subplot_mosaic(mosaic: list[HashableList[Hashable]], *,\n'
           '    empty_sentinel: Any, subplot_kw: dict[str, Any] | None,\n'
           ') -> dict[Hashable, Axes]: ...\n',
           **CODE)
    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        ecdf(),
        mathtext(),
        typing(),
    )
