Matplotlib Project Update for SciPy 2024
========================================

This repository contains code to create the presentation for the Matplotlib
project update at SciPy 2024.

If you want to view the resulting PDF directly, you can [find a generated copy
in the release](https://github.com/QuLogic/scipy2024-mpl-update/releases).

Requirements
------------

* Python 3.7+
* NumPy
* Matplotlib >= 3.10.0dev, including a merge of
  [#26996](https://github.com/matplotlib/matplotlib/pull/26996)
* A git checkout of the `matplotlib` source code, to produce the timeline.
* The Carlito font.
* The [segno](https://pypi.org/project/segno/) library for QR codes.

Optionally, you may also make available:

* The font to match the Matplotlib logo, Calibri.
* [`qpdf`](http://qpdf.sourceforge.net/), to linearize the final PDF.

Building
--------

The slides can be created by running:

```bash
$ ./make.py /path/to/matplotlib/checkout
```

which will produce `slides.pdf` directly from Matplotlib and
`scipy2024-mpl-update.pdf` as either a copy or a linearized version, depending
on whether `qpdf` is installed.

Overview
--------

Some general setup is contained in `mplslide.py`, namely setting slide size,
picking the font (Calibri and Carlito), and headings and other shortcut
functions. Other styling is mostly consistent, but usually set in the
individual files.

All slides are produced in the remaining Python files:

* `title.py`: The title page.
* `news.py`: General news.
* `timeline.py`: A timeline of releases.
* `feature38.py`: Feature highlights for Matplotlib 3.8.0.
* `feature39.py`: Feature highlights for Matplotlib 3.9.0.
* `feature310.py`: Feature highlights for Matplotlib 3.10.0.
* `plan.py`: Future plans.
