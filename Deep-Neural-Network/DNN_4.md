## Deep Neural Networks 4

#### UCI Machine Learning Repository

* https://archive.ics.uci.edu/ml/index.php

### Iris Data Set

#### Attribute Information:

Listing of attributes: 
 

1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica

model

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 512)               2560      
_________________________________________________________________
dense_2 (Dense)              (None, 256)               131328    
_________________________________________________________________
dense_3 (Dense)              (None, 128)               32896     
_________________________________________________________________
dense_4 (Dense)              (None, 32)                4128      
_________________________________________________________________
dense_5 (Dense)              (None, 3)                 99        
=================================================================
Total params: 171,011
Trainable params: 171,011
Non-trainable params: 0
_________________________________________________________________
```

result

<img width=600 src="https://user-images.githubusercontent.com/44635266/63076685-0655b280-bf71-11e9-843f-d48e97287933.png">