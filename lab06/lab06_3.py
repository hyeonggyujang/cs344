import numpy as np
from keras.datasets import boston_housing

(train_examples, train_labels), (test_examples, test_labels) = boston_housing.load_data()

print('train_examples (size: {}; axes: {}; shape: {}; type: {};)\n\n'.format(len(train_examples), train_examples.ndim, train_examples.shape, train_examples.dtype))
print('train_labels (size: {}; axes: {}; shape: {}; type: {};)\n\n'.format(len(train_labels), train_labels.ndim, train_labels.shape, train_labels.dtype))
print('test_examples (size: {}; axes: {}; shape: {}; type: {};)\n\n'.format(len(test_examples), test_examples.ndim, test_examples.shape, test_examples.dtype))
print('test_labels (size: {}; axes: {}; shape: {}; type: {};)\n\n'.format(len(test_labels), test_labels.ndim, test_labels.shape, test_labels.dtype))
