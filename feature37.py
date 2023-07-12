"""
Feature highlights for Matplotlib 3.7.0.
"""

from matplotlib.widgets import CheckButtons, RadioButtons

from mplslide import new_slide, slide_heading, annotate_pr_author


CODE = dict(fontfamily='monospace', fontsize=32, verticalalignment='top',
            alpha=0.7)

def mosaic_per_subplot_kw():
    fig = new_slide(layout='constrained')
    slide_heading(fig, '3.7: Mosaic per-subplot kwargs')

    top, bottom = fig.subfigures(2, 1, hspace=0)

    top.text(0.05, 0.65, '''\
axd = fig.subplot_mosaic(
    "AB;CD",
    subplot_kw={'facecolor': 'xkcd:slate grey'},
    per_subplot_kw={
        "A": {"projection": "polar"},
        ("C", "D"): {"xscale": "log"},
        "B": {"projection": "3d"},
    })''', **CODE)

    axd = bottom.subplot_mosaic(
        "AB;CD",
        subplot_kw={'facecolor': 'xkcd:steel grey'},
        per_subplot_kw={
            "A": {"projection": "polar"},
            ("C", "D"): {"xscale": "log"},
            "B": {"projection": "3d"},
        },
    )

    annotate_pr_author(fig, 'tacaswell', pr=24604)

    return fig


def button_styling():
    fig = new_slide()
    slide_heading(fig, '3.7: Widget styling')

    ax = fig.subplots(nrows=2, ncols=2)
    fig.subplots_adjust(top=0.75)

    default_rb = RadioButtons(ax[0, 0], ['Apples', 'Oranges'])
    styled_rb = RadioButtons(ax[0, 1], ['Apples', 'Oranges'],
                             label_props={'color': ['red', 'orange'],
                                          'fontsize': [48, 60]},
                             radio_props={'edgecolor': ['red', 'orange'],
                                          'facecolor': ['mistyrose', 'peachpuff']})

    default_cb = CheckButtons(ax[1, 0], ['Apples', 'Oranges'],
                              actives=[True, True])
    styled_cb = CheckButtons(ax[1, 1], ['Apples', 'Oranges'],
                             actives=[True, True],
                             label_props={'color': ['red', 'orange'],
                                          'fontsize': [48, 60]},
                             frame_props={'edgecolor': ['red', 'orange'],
                                          'facecolor': ['mistyrose', 'peachpuff']},
                             check_props={'color': ['darkred', 'darkorange']})

    ax[0, 0].set_title('Default', fontsize=32)
    ax[0, 1].set_title('Stylized', fontsize=32)

    annotate_pr_author(fig, 'QuLogic', pr=24838)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        mosaic_per_subplot_kw(),
        button_styling(),
    )
