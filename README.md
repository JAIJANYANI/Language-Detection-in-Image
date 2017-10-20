# Language-Detection-in-Image
Detects and Recognize text and font language in an image
## Description
Performed this analysis using The Tesseract OCR Engine.


The Project consist of following steps : 

1.)The first step is a connected component analysis in which outlines of the components are stored into Blobs<br />
2.) Blobs are organized into text lines and broken into words<br />
3.) Recognize every word in a two-pass process<br />
4.) A final phase resolves fuzzy spaces, and finalize text<br />


## Prerequisites

# Software
* libtesseract (>=3.04)
* libleptonica (>=1.71)
* Cython
* Pillow
* tesserocr
* Python 2.7.0 |Anaconda 4.3.0 (64-bit)|<br />

Tested on Ubuntu 16.04 LTS amd64 xenial image built on 2017-09-19 8-core CPU


## Installation

```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install python-dev python-pip
sudo apt-get install tesseract-ocr-all libtesseract-dev libleptonica-dev
pip install Cython
pip install Pillow
pip install tesserocr
```


## Running

* Simply run this command from root directory.

```
python ocr.py -i image_path.jpg

```

       

## Screenshots






## Output
```


```


       
## Author

# Jai Janyani



