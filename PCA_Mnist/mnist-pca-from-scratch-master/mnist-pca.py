import numpy as np
from mnist import MNIST
import matplotlib.pyplot as plt

def calc_pca(data, samples, classes=None):
	exit = []
	previous = []
	mean = np.mean(data, axis = 0)
	mean_sub = data - mean
	cov = np.cov(mean_sub, rowvar = 0)
	eigen_values, eigen_vectors = np.linalg.eig(np.mat(cov))
	eigen_values_sorted = np.argsort(-eigen_values)
	for num_eigen in samples:
		eigen_values_filtered = eigen_values_sorted[:num_eigen]
		eigen_vectors_filtered = eigen_vectors[:,eigen_values_filtered]
		data_matrix = mean_sub * eigen_vectors_filtered		
		reconstructed = (data_matrix * eigen_vectors_filtered.T) + mean
		exit.append((num_eigen, reconstructed.real, eigen_vectors_filtered.T.real))
		if classes is not None:
			for i in classes:
				mean_class = np.mean(classes[i], axis = 0)
				mean_sub_class = classes[i] - mean_class
				data_matrix_class = mean_sub_class * eigen_vectors_filtered
				reconstructed_class = (data_matrix_class * eigen_vectors_filtered.T) + mean_class
				exit.append((num_eigen, reconstructed_class.real, None))
	return exit

def print_pca(data):
	for row in data:
		for j in range(row[0]):
			plt.subplot(5,4,j+1)
			reshaped = np.array(row[1][j]).reshape(28,28)
			plt.imshow(reshaped, cmap='gray')
			plt.axis('off')
		plt.show()
		if row[2] is not None:
			for j in range(row[0]):
				plt.subplot(5,4,j+1)
				reshaped = np.array(row[2][j]).reshape(28,28)
				plt.imshow(reshaped, cmap='gray')
				plt.axis('off')
			plt.show()

mndata = MNIST('../dataset/MNIST')
train_images, train_labels = mndata.load_training()
test_images,  test_labels  = mndata.load_testing()
num_classes = 10
samples = [2, 5, 10, 20]
classes = {}
for i in range(num_classes):
	classes[i] = []
for i, image in enumerate(test_images):
	classes[test_labels[i]].append(image)
for i in range(num_classes):
	values = calc_pca(classes[i], samples)
	print_pca(values)
values = calc_pca(test_images, samples, classes)
print_pca(values)
#one_of_each = {}
#for i in classes:
#	one_of_each[i] = [classes[i][0]]
#values = calc_pca(train_images, samples, one_of_each)
#print_pca(values)