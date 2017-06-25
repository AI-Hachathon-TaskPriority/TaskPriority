from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import date
import datetime

import os
import urllib

import numpy as np
import tensorflow as tf

dict_importance = {
	'0':'1.Low',
	'1':'2.Mid',
	'2':'3.High'
}
dict_assignor = {
	'Me':'1',
	'All subordinates':'2',
	'I':'1',
	'Boss':'3',
	'Client A':'4',
	'Client B':'5',
	'Father':'6',
	'HR':'7',
	'Subordinate C':'8',
	'Wife':'9',
	'Yamamoto-san':'10',
	'CEO':'11',
	'PR':'12',
	'Mr.X':'13',
	'General affairs':'14',
	'Takahashi-san':'15'
}

dict_assignee = {
	'Me':'1',
	'Yoko-san':'2',
	'Subordinate A':'1',
	'Subordinate B':'3',
	'Subordinate C':'4',
	'Subordinate D':'5',
	'Boss':'6',
	'All subordinate':'7',
	'Takashi-san':'8',
	'Watanabe-san':'9',
	'I':'1',
	'Subordinate E':'10'
}

dict_category = {
	'Job':'1',
	'Private':'2',
	'Both':'3'
}

# param: newTask (Dictionary)
# 	0: assignor
# 	1: assignee
# 	2: category
#	3: title
#	4: time
#	5: deadline
def inference(newTask):
	# each column values
	assignor = dict_assignor[newTask['Assignor']]
	assignee = dict_assignee[newTask['Assignee']]
	category = dict_category[newTask['Category']]
	title_r = newTask['Title']
	time = newTask['Time']
	deadline_r = newTask['Deadline']
	deadline = datetime.datetime(2017,int(deadline_r[:2]),int(deadline_r[3:5]),int(deadline_r[11:13]),int(deadline_r[14:])) - datetime.datetime(2017,06,24,20,00)
	deadline = deadline.days*24*60 + deadline.seconds/60
	inputList = [assignor,assignee,category,time,deadline]

	# Specify that all features have real-value data
	feature_columns = [tf.contrib.layers.real_valued_column("", dimension=5)]
	# Build 3 layer DNN with 10, 20, 10 units respectively.
	classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
		hidden_units=[10, 20, 10],
		n_classes=3,
		model_dir="./model")

	def new_samples():
	    return np.array([inputList],dtype=np.int)

	predictions = list(classifier.predict(input_fn=new_samples))
# 	importance result
	return dict_importance[str(predictions[0])]
# 	return predictions[0]

