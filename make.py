#!/usr/bin/env python3

"""
Generate slides for the presentation.

Usage: ./make.py /path/to/matplotlib/checkout

You must make a clone of the Matplotlib git repository available, and should
have the Carlito and/or Calibri font installed.
"""

import shutil
import subprocess
import sys

from matplotlib.backends.backend_pdf import PdfPages

from mplslide import check_requirements
# This must be called before importing other files to make the font available.
check_requirements()  # noqa: F402

from title import create_icon_axes, slides as title_slides
from timeline import slides as history_slides
from feature38 import slides as feature38_slides
from feature39 import slides as feature39_slides
from feature310 import slides as feature310_slides
from end import slides as end_slides


METADATA = {
    'Author': 'Elliott Sales de Andrade',
    'Title': 'Matplotlib Project Update for SciPy 2024',
}
MPL_PATH = sys.argv[1]
PAGES = [
    # Tuple of function + any arguments.
    (title_slides, ),
    (history_slides, MPL_PATH, ),
    (feature38_slides, ),
    (feature39_slides, ),
    (feature310_slides, ),
    (end_slides, ),
]

with PdfPages('slides.pdf', metadata=METADATA) as pdf:
    for page, *args in PAGES:
        figs = page(*args)
        if not isinstance(figs, (tuple, list)):
            figs = (figs, )
        for fig in figs:
            if not fig.mplslide_props['plain']:
                create_icon_axes(fig, (0.825, 0.825, 0.2, 0.15),
                                 0.3, 0.3, 0.3, [5])
            pdf.savefig(fig)

# Linearize the PDF if qpdf is available.
if shutil.which('qpdf') is not None:
    subprocess.run(['qpdf', 'slides.pdf', '--object-streams=generate',
                    '--linearize', 'scipy2024-mpl-update.pdf'])
else:
    shutil.copy('slides.pdf', 'scipy2024-mpl-update.pdf')
