import numpy
import tflearn

from tflearn.data_utils import load_csv
data, labels = load_csv('ssl3.csv', target_column=0, categorical_labels=True, n_classes=3)

net = tflearn.input_data(shape=[None, 2])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 3, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net, tensorboard_verbose=3, tensorboard_dir="logs")
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=20, batch_size=16, show_metric=True)


model.save('my_model.tflearn')

