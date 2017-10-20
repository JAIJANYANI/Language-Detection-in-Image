# Text-Language-Detection-in-Image
Detects and Recognizes text and font language in an image
## Description
Performed this analysis using The Tesseract OCR Engine.


The Project consist of following steps : 

1.) The first step is a connected component analysis in which outlines of the components are stored into Blobs<br />
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

* Simply Clone the repository and run this command from root directory.

```
python ocr_itt.py -i <image_path.jpg>

```

       
## Input 1
```$ python ocr_itt.py -i e.jpg``` <br/>
![e](https://user-images.githubusercontent.com/15799933/31809000-60ffe726-b593-11e7-95ab-e29f7c6d8153.jpg)

## Output
```
English
Confidence score is 78.6614583333
```
## Input 2
```$ python ocr_itt.py -i h.jpg``` <br/>
![h](https://user-images.githubusercontent.com/15799933/31809002-619ba3aa-b593-11e7-800f-8147d357b6e0.jpg)

## Output
```
Hindi
Confidence score is 84.2118644068
```
## Input 3
```$ python ocr_itt.py -i s.jpg``` <br/>
![s](https://user-images.githubusercontent.com/15799933/31809001-614bb534-b593-11e7-8c40-6cc07e5c6738.jpg)

## Output
```
Spanish
Confidence score is 69.7443609023
```

       
## Author

# Jai Janyani



