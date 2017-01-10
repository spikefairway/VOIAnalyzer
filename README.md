# VOIAnalyzer

**VOIAnalyzer** is a simple tool to extract statistics for image intensities on volume of interest (VOI), placed on medical image, e.g., MRI, CT, PET, SPECT, etc. This tool can be useful to extract statistics on VOIs drawn with some software packages such as FreeSurfer. VOIAnalyzer is only for research use and *NOT FOR CLINICAL USE*.

## Version

Current development status for VOIAnalyzer is pre-alpha. PLEASE WAIT TILL RELEASE OF BETA OR STABLE VERSION.

## Requirements

- Python 2.7 or 3.5
- Numpy
- Pandas
- nipy
- nibabel
- wxPython

## CUI-base usage

```
usage: VOIAnalyzerCUI.py [-h] -v VOI -o OUT [-l LUT] images [images ...]

Extract VOI statistics

positional arguments:
  images             Images to extract Statistics

  optional arguments:
    -h, --help         show this help message and exit
    -v VOI, --voi VOI  VOI map file
    -o OUT, --out OUT  Output file [CSV]
    -l LUT, --lut LUT  VOI look-up table file
```

## License

VOIAnalyzer is licensed under the terms of the MIT license. Please see LICENSE file.

