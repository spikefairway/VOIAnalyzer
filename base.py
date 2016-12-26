#!/usr/bin/env python
# coding : utf-8

"""
Basis for VOI analyzer.
"""

import pandas as pd
import numpy as np

import VOIAnalyzer.utils as utils

def _analysis(img_mat, voi_mat, voi_no, eps=1e-12):
    """ Extract VOI statistices for each VOI.
    """
    vec = img_mat[voi_mat == voi_no]
    vec2 = vec[~np.isnan(vec)]

    # Statistics
    v_mean = float(vec2.mean())
    v_sd = float(vec2.std(ddof=1))
    v_cov = v_sd / (v_mean + eps) * 100.
    v_max = float(vec2.max())
    v_min = float(vec2.min())
    n_vox = vec.size

    # Output
    out_tab = pd.DataFrame({"VOI No." :  [voi_no],
                            "No. of voxels" : [n_vox],
                            "Mean" : [v_mean],
                            "SD" : [v_sd],
                            "CoV" : [v_cov],
                            "Max" : [v_max],
                            "Min" : [v_min]})

    return out_tab

def voi_analysis(img_file, voi_file, lut_file=None):
    """ Extract VOI values.
    It outputs Pandas DataFrame for VOI statistics.

    Inputs:
        img_file   :    Path for image to extract VOI values

        voi_file    :   Path for VOI map

        lut_file    :   Path for look-up table for VOI map.
                        If not None, look-up table is applied to output table.

    Output:
        out_tab     :   Pandas DataFrame for VOI statistics.
    """
    # Load image & VOI
    img_mat, img_aff = utils.loadImage(img_file)[:2]
    voi_mat = utils.loadImage(voi_file)[0].astype(np.int16)
    
    # Extract
    vno_list = np.unique(voi_mat)
    out_tab = pd.concat([_analysis(img_mat, voi_mat, v_no)
                            for v_no in vno_list])

    # Calculate volumes (unit: cm3)
    vol_per_vox = np.abs(np.prod(np.diag(img_aff[:3, :3])))
    out_tab.loc[:, "Volume"] = out_tab.loc[:, "No. of voxels"] / 1000.

    # Apply look-up table
    if lut_file is not None:
        lut = utils.loadLUT(lut_file)
        out_tab.loc[:, "VOI"] = out_tab.loc[:, "VOI No."].map(lut)

    # Image file name
    out_tab.loc[:, "Path"] = img_file

    return out_tab

