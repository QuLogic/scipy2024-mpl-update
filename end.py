"""
End slide.
"""

from mplslide import FONT, new_slide, slide_heading, add_qrcode


def slides():
    """
    Create end slide.
    """
    fig = new_slide()

    slide_heading(fig, 'Thank You!')

    props = dict(fontproperties=FONT, fontsize=56, alpha=0.7,
                 horizontalalignment='center')

    fig.text(0.5, 0.7, 'This entire presentation was made in Matplotlib:',
             **props)

    t = fig.text(0.5, 0.6, '\nhttps://github.com/QuLogic/scipy2024-mpl-update',
                 **props)
    t.set_url('https://github.com/QuLogic/scipy2024-mpl-update')

    fig.text(0.15, 0.3, 'Slides', rotation=90, verticalalignment='center', **props)
    add_qrcode(fig, 'https://github.com/QuLogic/scipy2024-mpl-update',
               [0.0, 0.0, 0.6, 0.6])

    fig.text(0.55, 0.3, 'Release Notes', rotation=90, verticalalignment='center',
             **props)
    add_qrcode(fig, 'https://matplotlib.org/stable/users/release_notes',
               [0.4, 0.0, 0.6, 0.6])

    return fig
