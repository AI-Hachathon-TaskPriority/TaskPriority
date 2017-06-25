from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np
import tensorflow as tf

# Data sets
TRAINING = "train.csv"
TEST = "test.csv"

def main():

  # Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
      filename=TRAINING,
      target_dtype=np.int,
      features_dtype=np.int)
  test_set = tf.contrib.learn.datasets.base.load_csv_without_header(
      filename=TEST,
      target_dtype=np.int,
      features_dtype=np.int)

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=5)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[10, 10, 5],
                                              n_classes=3,
                                              model_dir="./tmp/model")
  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)

    return x, y

  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=2000)

  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(test_set.data)
    y = tf.constant(test_set.target)

    return x, y

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                       steps=1)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # Classify two new flower samples.
  def new_samples():
    return np.array(
      [[1,1,3,90,53280],
       [1,1,3,600,97920],
       [1,1,3,25,53280]],
       dtype=np.int)

  predictions = list(classifier.predict(input_fn=new_samples))

  print(
      "New Samples, Class Predictions:    {}\n"
      .format(predictions))

if __name__ == "__main__":
    main()