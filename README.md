# Master-Thesis
This repository is linked to the master's thesis : How close an NLP model can be to a numerical data input machine learning model ?
The goal of this thesis is to quantify the loss of accuracy when switching from structured to unstructured data for a wine variety prediction task. This repository is then composed of all codes used in our analysis. There is a first foler concerning our dataset creation, a second one concerning the analysis of our datasets and a third one concerning the implementation of our models.

As soon as you see a zip file, you can run the following code to extract the file :
Just replace 'Master-Thesis-main.zip' by the file name.
```python
import zipfile as zf
files = zf.ZipFile("Master-Thesis-main.zip", 'r')
files.extractall()
files.close()


