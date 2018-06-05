# **ETAS - Efficient Traffic signal Assistance System**

This is a project aimed at helping traffic signals work in an efficient yet simple way to ensure road user safety while also reducing delays. It uses a deep learning model to do the same.

It considers 3 scenarios of the road traffic:
*More pedestrians and fewer vehicles
*More vehicles and fewer pedestrians
*Equal density of pedestrians and vehicles

The traffic signals are modelled to work in these three scenarios. The model can be deployed on processors like the Raspberry Pi, which can be placed at every signal to control it.

## **Software requirements for training**
*Python 
*TensorFlow
*TFLearn
*numpy

## **Datasets**
Road traffic data can be obtained from many government websites. The data obtained this way will have to be modelled such that only the fields required for the application are kept and the rest is ignored to remove the chances of over-fitting. If the data for the region you are training the model is not available, it will have to be obtained by placeing the necessary sensors and sampling the data.

Storing the data in .csv format will ensure readablity and ease in training process.

A sample dataset can be seen in [Sample dataset](https://github.com/AnjanaNiranjan/ETAS/blob/master/training/sample_dataset.csv).

## **Writing the network model**
This project uses the TFLearn framework. The number and kinds of layers in the network model can be determined only by trial and error. 

Check for efficiency and modify the model as per your requirements.

The model used in ETAS can be seen in [Model](https://github.com/AnjanaNiranjan/ETAS/blob/master/training/training.py).

The training can be done on a local machine or on a cloud platform. It can be saved for subsequent use.

## **Deploying the model on Raspberry Pi**
The saved model can be deployed on a processor like the Raspberry Pi and loaded in a program for use as shown in [code](https://github.com/AnjanaNiranjan/ETAS/blob/master/Raspberry%20Pi/trafficSignal.py).