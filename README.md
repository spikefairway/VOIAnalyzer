# VOIAnalyzer

**VOIAnalyzer** is a simple tool to extract statistics for image intensities on volume of interest (VOI), placed on medical image, e.g., MRI, CT, PET, SPECT, etc. This tool can be useful to extract statistics on VOIs drawn with some software packages such as FreeSurfer. VOIAnalyzer is only for research use and *NOT FOR CLINICAL USE*.

## Version

Current development status for VOIAnalyzer is beta. For stable use, PLEASE WAIT TILL RELEASE OF STABLE VERSION.

## Requirements

- Python (2.7 or 3.5)
- Numpy
- Pandas
- nipy
- nibabel
- wxPython

## Usage

VOIAnalyzer requires the following files to analyze:

- Image files to analyze
- VOI map file
- VOI look-up table file (optional)

Each voxel in VOI map has VOI No. as image intensity. VOIAnalyzer extracts statistics (mean, SD, max, min, etc.) for intensities on VOIs defined in VOI map, and outputs the statistics to CSV file. VOIAnalyzer expects images co-registered to VOI map. Image orientation, image size and voxel size for all image files must be same as VOI map file. Only [NIfTI-1 format](https://nifti.nimh.nih.gov/nifti-1) is supported as image files and VOI map file.


### VOI look-up table

You can define look-up table to translate VOI No. to VOI name with a text file. The look-up table file is a tab-separated text file as follows:

```
<VOI No.>   <VOI name>
```

For example,

```
1   GM
2   WM
3   CSF
```

means voxels with 1, 2 and 3 indicate gray matter (GM), white matter (WM) and cerebrospinal fluid (CSF). If you give look-up table file as an argument, you can see VOI name on outputed CSV file.

### Usage for CUI-based tool

```
$ python VOIAnalyzerCUI.py -h
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

### Usage for GUI-based tool

```
$ python VOIAnalyzerGUI
```

## License

VOIAnalyzer is licensed under the terms of the MIT license. Please see LICENSE file.

