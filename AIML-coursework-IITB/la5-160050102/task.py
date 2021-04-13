import numpy as np
from utils import *

def preprocess(X, Y):
	''' TASK 0
	X = input feature matrix [N X D] 
	Y = output values [N X 1]
	Convert data X, Y obtained from read_data() to a usable format by gradient descent function
	Return the processed X, Y that can be directly passed to grad_descent function
	NOTE: X has first column denote index of data point. Ignore that column 
	and add constant 1 instead (for bias part of feature set)
	'''
	X_new = np.ones(Y.shape)
	for i in range(1,X.shape[1]):
		if(isinstance(X[0,i],str)):
			X_new1 = one_hot_encode(X[:,i],np.unique(X[:,i]))
			X_new = np.append(X_new,X_new1,axis=1)
		else:
			arr = [[X[:,i][j]] for j in range(len(X[:,i]))]
			arr = np.array(arr)
			arr = (arr - arr.mean(0))/arr.std(0)
			X_new = np.append(X_new,arr,axis=1)

	X_new = X_new.astype(float)
	Y = Y.astype(float)

	return X_new,Y


def grad_ridge(W, X, Y, _lambda):
	'''  TASK 2
	W = weight vector [D X 1]
	X = input feature matrix [N X D]
	Y = output values [N X 1]
	_lambda = scalar parameter lambda
	Return the gradient of ridge objective function (||Y - X W||^2  + lambda*||w||^2 )
	'''
	return -2*(np.matmul(np.transpose(X),(Y - np.matmul(X,W)))) + 2*_lambda*W

def ridge_grad_descent(X, Y, _lambda, max_iter=30000, lr=0.00001, epsilon = 1e-4):
	''' TASK 2
	X 			= input feature matrix [N X D]
	Y 			= output values [N X 1]
	_lambda 	= scalar parameter lambda
	max_iter 	= maximum number of iterations of gradient descent to run in case of no convergence
	lr 			= learning rate
	epsilon 	= gradient norm below which we can say that the algorithm has converged 
	Return the trained weight vector [D X 1] after performing gradient descent using Ridge Loss Function 
	NOTE: You may precompure some values to make computation faster
	'''
	W = np.zeros((X.shape[1],1))
	W_new = W - lr*grad_ridge(W,X,Y,_lambda)
	for i in range(max_iter):
		W = W_new.copy()
		W_new = W - lr*grad_ridge(W,X,Y,_lambda)
		if(np.linalg.norm(W - W_new) < epsilon):
			break
	return W_new

def k_fold_cross_validation(X, Y, k, lambdas, algo):
	''' TASK 3
	X 			= input feature matrix [N X D]
	Y 			= output values [N X 1]
	k 			= number of splits to perform while doing kfold cross validation
	lambdas 	= list of scalar parameter lambda
	algo 		= one of {coord_grad_descent, ridge_grad_descent}
	Return a list of average SSE values (on validation set) across various datasets obtained from k equal splits in X, Y 
	on each of the lambdas given 
	'''
	X_size = X.shape[0]
	part_len = int(X_size/k)
	avg_sse = []
	for i in range(len(lambdas)):
		# print(i)
		lambda_itr = lambdas[i]
		sum_itr= 0
		for j in range(k):
			X_itr = np.append(X[0:j*part_len],X[(j+1)*part_len:],axis = 0)
			Y_itr = np.append(Y[0:j*part_len],Y[(j+1)*part_len:],axis = 0)
			W = algo(X_itr,Y_itr,lambda_itr)
			sse_itr = sse(X[j*part_len:(j+1)*part_len],Y[j*part_len:(j+1)*part_len],W)
			sum_itr += sse_itr
		sum_itr /= k
		avg_sse.append(sum_itr)
	return avg_sse

def coord_grad_descent(X, Y, _lambda, max_iter=2000):
	''' TASK 4
	X 			= input feature matrix [N X D]
	Y 			= output values [N X 1]
	_lambda 	= scalar parameter lambda
	max_iter 	= maximum number of iterations of gradient descent to run in case of no convergence
	Return the trained weight vector [D X 1] after performing gradient descent using Ridge Loss Function 
	'''
	W = np.zeros((X.shape[1],1))
	cona = np.zeros((X.shape[1],1))
	
	for i in range(X.shape[1]):
		cona[i] = np.linalg.norm(X[:,i])**2

	conb1 = np.matmul(np.transpose(X),Y)
	conb2 = np.matmul(np.transpose(X),X)

	for i in range(max_iter):
		for j in range(X.shape[1]):
			cona_itr = cona[j]
			W[j] = 0
			conb_itr = -2*(conb1[j] - (np.matmul(conb2[j],W))[0])
			if(conb_itr + _lambda > 0 and conb_itr - _lambda < 0):
				W[j] = 0
			if(conb_itr + _lambda > 0 and conb_itr - _lambda > 0):
				W[j] = (_lambda - conb_itr)/(2*cona_itr)
			if(conb_itr + _lambda < 0 and conb_itr - _lambda < 0):
				W[j] = -(_lambda + conb_itr)/(2*cona_itr)
	return W


if __name__ == "__main__":
	# Do your testing for Kfold Cross Validation in by experimenting with the code below 
	X, Y = read_data("./dataset/train.csv")
	X, Y = preprocess(X, Y)
	trainX, trainY, testX, testY = separate_data(X, Y)
	
	lambdas = [i*1000 for i in range(230,540)] # Assign a suitable list Task 5 need best SSE on test data so tune lambda accordingly
	scores = k_fold_cross_validation(trainX, trainY, 6,lambdas,coord_grad_descent)
	# error = sse(testX,testY,scores)
	# print(error)
	plot_kfold(lambdas, scores)
