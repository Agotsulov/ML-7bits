import numpy as np
from random import shuffle


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_examples = X.shape[0]
                  
    grad = np.zeros((num_examples, W.shape[1]), dtype=np.float)
    
    for i in range(num_examples):
        exp_f = np.exp(X[i, :].dot(W))

        p = exp_f / np.sum(exp_f)
        
        grad[i] = p
        grad[i, y[i]] -= 1
        
        loss += -np.log(p[y[i]])

    loss = loss / num_examples + 0.5 * reg * np.sum(W ** 2)
    
    grad /= num_examples
    dW = np.dot(X.T, grad)
    dW += reg * W
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_examples = X.shape[0]

    exp_f = np.exp(np.dot(X, W))
    p = exp_f / np.sum(exp_f, axis=1, keepdims=True)
    L_i = -np.log(p[range(num_examples), y])

    loss = np.sum(L_i) / num_examples + 0.5 * reg * np.sum(W * W)

    grad = p
    grad[range(num_examples), y] -= 1
    grad /= num_examples

    dW = np.dot(X.T, grad)
    dW += reg * W
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW
