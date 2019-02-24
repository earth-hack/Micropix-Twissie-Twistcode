# Micropix-Twissie@Twistcode
This is a submission repository for European Association Of Geoscientist & Engineers (EAGE) Earth-Hack Hackathon 2019

## Description
### Rock properties detection from core images
We try to analyze and extract rock properties by classifying the rock properties and location corresponding to the core images using transfer learning.  

## Members
- Akmal
- Hasif
- Sidiq
- [Syuhada](https://github.com/kotakSempit) 

## Built With
Machine Learning Library
- [Pytorch](https://pytorch.org/) 
- [FastAI](https://www.fast.ai/)
- [Scikit-learn](https://scikit-learn.org/stable/)

## Application Setup
- Install all the library required
```
pip3 install flask torch torchvision fastai scikit-learn numpy scipy pandas
```
- Run the script to initialize the server
```
python3 server.py
```
- To access the application `http://localhost:5000`
- To access the API, send an image named 'file' as a multipart/form-data POST request to `http://localhost:5000/image`

## Demo
[Application Demo Link](http://13.67.66.80:5000/)

## License
The hack is governed by Creative Commons, CC BY. You can:
- Copy
- Adapt or Modify
- Redistribute (Publish, Display, Publicly Perform or Communicate the Work 
- License to others
