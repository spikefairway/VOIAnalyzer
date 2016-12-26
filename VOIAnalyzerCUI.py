#!/usr/bin/env python
# coding : utf-8

"""
CUI interface for VOI analyzer.
"""

import pandas as pd
import argparse

from VOIAnalyzer.base import voi_analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract VOI statistics")
    parser.add_argument('images', help="Images to extract Statistics",
                        nargs='+', type=str)
    parser.add_argument('-v', '--voi', dest='voi',
                        help="VOI map file",
                        nargs=1, type=str, required=True)
    parser.add_argument('-o', '--out', dest='out',
                        help="Output file [CSV]",
                        nargs=1, type=str, required=True)
    parser.add_argument('-l', '--lut', dest='lut',
                        help="VOI look-up table file",
                        nargs=1, type=str,
                        default=[None])

    args = parser.parse_args()

    out_tab = pd.concat([voi_analysis(img, args.voi[0],
                                      lut_file=args.lut[0])
                        for img in args.images])
    out_tab.to_csv(args.out[0], index=False)

