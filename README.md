# GUI Tool for uploading & downloading structural data


UD v1.0 for uploading & downloading structural data, based on python.


-----

This repository contains:

# 1. GUI tool

**Step:**
1) [Python environment](https://www.python.org/)
2) install [PyQt5](https://pypi.org/project/PyQt5/) & [pyppeteer](https://github.com/pyppeteer/pyppeteer)
* you can just type the following command in your terminal or cmd
```
pip install -U PyQt5
pip install -U pyppeteer
```
* or, use our [requirements.txt](UploadDownloadTool/requirements.txt):
```
pip install -r [requirements.txt]
```
3) run GUI
```
python run.py
```
4) GUI manual
* This tool is divided into Uploader & Downloader
```
Uploader: 

* Compulsory：
            - Data Folder: (Full path to your structural data. Noth that you have to put all data in one folder.)
            - Account File: (Two-column file (recommed *.csv) that is seperated by commas (,). First column is account id; the second is password.)
* Optional:
            - Subject infomation: (Two-column file that is seperated by commas.Set the first row as columns names ['age','sex'].)
              But I suggest that you can just leave it empty ˃͜˂

```
```
Downloader: 

* You MUST use the same Data path that you used in the uploader!

```

# Reference:
Manjón, J. V., & Coupé, P. (2016). volBrain: an online MRI brain volumetry system. Frontiers in neuroinformatics, 10, 30.
-------

**Do not hesitate to contact me if you have any further questions**

**Have fun :)**
