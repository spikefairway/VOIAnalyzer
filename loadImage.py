#!/usr/bin/env python
# coding : utf-8

import numpy as np
import nibabel as nib

def loadImage(f):
    """ Load NIfTI image.
    """
    img = nib.load(f)
    mat = img.get_data()
    aff = img.get_affine()

    return mat, aff, img

