#!/usr/bin/env python
# coding : utf-8

"""
Utilities.
"""

import numpy as np
import nibabel as nib

def loadImage(f):
    """ Load NIfTI image.
    """
    img = nib.load(f)
    mat = img.get_data()
    aff = img.get_affine()

    return mat, aff, img


def loadLUT(f):
    """ Load VOI look-up table file.

    Format for look-up table file.
        <VOI No.>   <VOI name>

    for example,

        1   GM
        2   WM
        3   CSF

    the aboves mean 
