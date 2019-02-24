import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import statsmodels
from statsmodels.sandbox.distributions.extras import pdf_mvsk
from scipy.stats import kurtosis, skew
from sklearn.model_selection import GridSearchCV
import random
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import random

import scipy.interpolate

def testNLP():
	names = ["AdaBoost"]
	classifiers = [AdaBoostClassifier(learning_rate=0.1,n_estimators=90)]

	csvfiles = ['sample/Hawke Bay.csv','sample/Tawatawa.csv', 'sample/Waimamaku.csv','sample/West Cape.csv']

	X = pd.DataFrame()
	y = pd.DataFrame()
							
	for i in range(len(csvfiles)):
		df = pd.read_csv(csvfiles[i], sep='\s*,\s*',header=0, encoding='ascii', engine='python')
		df2 = df.set_index(df.columns[0])
		del df2.index.name
		iX,iy = df2[df2.columns[:25]],df2[df2.columns[26]]
		X = pd.concat([X,iX])
		y = pd.concat([y,iy])

	doflist = []
	dof = pd.DataFrame()
	for i in range(100):	
		dof = dof.append(X.iloc[sorted(random.sample(range(len(X)), 100))[i]])[X.iloc[sorted(random.sample(range(len(X)), 100))].columns.tolist()]
		doflist.append(y.iloc[sorted(random.sample(range(len(X)), 100))[i]].values[0])
		dof['Label'] = doflist

	sX = pd.DataFrame()
	sy = pd.DataFrame()

	iX,iy = dof[dof.columns[:25]],dof[dof.columns[25]]
	sX = pd.concat([sX,iX])
	sy = pd.concat([sy,iy])

	output = []
	predictlist = []	
	for name, clf in zip(names, classifiers):
		clf.fit(X, y.values.ravel())
		score = clf.score(sX, sy.values.ravel())
		namescoredict = {'name':name,'score':score}
		predictlist.append(clf.predict(sX))
		pred1 = clf.predict(sX)
		confusion = confusion_matrix(sy,pred1)
		confusiondict = {'ul':int(confusion[0][0]),'ur':int(confusion[0][1]),'ll':int(confusion[1][0]),'lr':int(confusion[1][1])}
		classificationdict = {'end':classification_report(sy,pred1)}
		output.append(namescoredict)
		output.append(confusiondict)
		output.append(classificationdict)
		# print (namescoredict,confusiondict,classificationdict)
		
	dof.reset_index(inplace=True)
	dof['Prediction'] = predictlist[0]

	output.append(dof.values.tolist())

	dof.rename(columns={'index':'Depth'}, inplace=True)


	print(dof.keys())
	output.append(dof.columns.to_list())
	return output

