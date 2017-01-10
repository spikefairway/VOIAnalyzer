#!/usr/bin/env python
# coding : utf-8

"""
Utilities.
"""

import numpy as np
import nibabel as nib
import re

def loadImage(f):
    """ Load NIfTI image.
    """
    img = nib.load(f)
    mat = img.get_data()
    aff = img.get_affine()

    return mat, aff, img

def readLUTLine(line):
    """ Read line in VOI look-up table file.
    """
    reg = re.compile(r"(\d+)\s+(\S+)")
    res = reg.match(line)
    grps = res.groups()

    return {int(grps[0]) : grps[1]}

def loadLUT(f):
    """ Load VOI look-up table file.

    Format for look-up table file.
        <VOI No.>   <VOI name>

    for example,

        1   GM
        2   WM
        3   CSF

    if above, voxels with 1, 2 and 3 indicate gray matter (GM), 
    white matter (WM) and cerebrospinal fluid (CSF).

    It outputs dictionary {<VOI No.> : <VOI name>}.
    """
    with open(f, "r") as f:
        lines = f.readlines()

        retDict = {}
        [retDict.update(readLUTLine(line)) for line in lines]

    return retDict


