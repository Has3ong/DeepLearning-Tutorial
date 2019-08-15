## Deep Neural Networks 2


Data

<img width=600 src="https://user-images.githubusercontent.com/44635266/62998620-10ab7a00-bea7-11e9-9fea-74a53c10a894.png">

Data Classfication

<img width=600 src="https://user-images.githubusercontent.com/44635266/62998622-11441080-bea7-11e9-9b16-5598177df375.png">

Model

```

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 10)                30        
_________________________________________________________________
dense_2 (Dense)              (None, 10)                110       
_________________________________________________________________
dense_3 (Dense)              (None, 10)                110       
_________________________________________________________________
dense_4 (Dense)              (None, 10)                110       
_________________________________________________________________
dense_5 (Dense)              (None, 2)                 22        
=================================================================
Total params: 382
Trainable params: 382
Non-trainable params: 0
_________________________________________________________________
```

Result
```
Loss = 0.03705144514143467

a = [[1.0000000e+00 1.3668767e-08]

b = [1.3932752e-04 9.9986064e-01]]
```

<img width=600 src="https://user-images.githubusercontent.com/44635266/62999347-1dc96880-bea9-11e9-992a-3216df608c91.png">

Overfitting occurs when the number of learning exceeds 300.