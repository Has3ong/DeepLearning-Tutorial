## Regression analysis

* In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables. 
* It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors').
* More specifically, regression analysis helps one understand how the typical value of the dependent variable (or 'criterion variable') changes when any one of the independent variables is varied, while the other independent variables are held fixed.

<img width=500 src="https://user-images.githubusercontent.com/44635266/63090609-cb667580-bf96-11e9-868f-13cd84b3788b.png">

## Classfication analysis

* In machine learning and statistics, classification is the problem of identifying to which of a set of categories (sub-populations) a new observation belongs, on the basis of a training set of data containing observations (or instances) whose category membership is known.
* Examples are assigning a given email to the "spam" or "non-spam" class, and assigning a diagnosis to a given patient based on observed characteristics of the patient (sex, blood pressure, presence or absence of certain symptoms, etc.). 
* Classification is an example of pattern recognition. 

<img width=500 src="https://user-images.githubusercontent.com/44635266/63090738-2ef0a300-bf97-11e9-9739-01e383770d83.png">

## Activation Function

* In artificial neural networks, the activation function of a node defines the output of that node given an input or set of inputs.
* A standard computer chip circuit can be seen as a digital network of activation functions that can be "ON" (1) or "OFF" (0), depending on input.
* This is similar to the behavior of the linear perceptron in neural networks.
* However, only nonlinear activation functions allow such networks to compute nontrivial problems using only a small number of nodes.
* In artificial neural networks, this function is also called the transfer function.

<img width=500 src="https://user-images.githubusercontent.com/44635266/63090829-72e3a800-bf97-11e9-9ab8-f53c8591b5b3.png">

### Relu

<img width=500 src="https://user-images.githubusercontent.com/44635266/63090951-d7066c00-bf97-11e9-904d-832f63010919.png">


## MSE

* ***n*** statistics, the mean squared error (MSE) or mean squared deviation (MSD) of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value.
* MSE is a risk function, corresponding to the expected value of the squared error loss.
* The fact that MSE is almost always strictly positive (and not zero) is because of randomness or because the estimator does not account for information that could produce a more accurate estimate.


## Cross Entropy

* In information theory, the cross entropy between two probability distributions ***p*** and ***q*** over the same underlying set of events measures the average number of bits needed to identify an event drawn from the set if a coding scheme used for the set is optimized for an estimated probability distribution  ***q***, rather than the true distribution ***p***. 

## Back Propagation

* Backpropagation algorithms are a family of methods used to efficiently train artificial neural networks (ANNs) following a gradient descent approach that exploits the chain rule.
* The main feature of backpropagation is its iterative, recursive and efficient method for calculating the weights updates to improve the network until it is able to perform the task for which it is being trained.
* It is closely related to the Gauss–Newton algorithm.

##

* Backpropagation requires the derivatives of activation functions to be known at network design time.
* Automatic differentiation is a technique that can automatically and analytically provide the derivatives to the training algorithm. 
* In the context of learning, backpropagation is commonly used by the gradient descent optimization algorithm to adjust the weight of neurons by calculating the gradient of the loss function; backpropagation computes the gradient(s), whereas (stochastic) gradient descent uses the gradients for training the model (via optimization). 

<img width=500 src="https://user-images.githubusercontent.com/44635266/63091410-3a44ce00-bf99-11e9-8296-c928a90a3c36.png">