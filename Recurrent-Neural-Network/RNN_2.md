## Recurrent Neural Networks 1

#### UCI Machine Learning Repository

* https://archive.ics.uci.edu/ml/index.php


### Ozone Level Detection Data Set 

#### Attribute Information:

The following are specifications for several most important attributes that are highly valued by Texas Commission on Environmental Quality (TCEQ). More details can be found in the two relevant papers. 

* O 3 - Local ozone peak prediction 
* Upwind - Upwind ozone background level 
* EmFactor - Precursor emissions related factor 
* Tmax - Maximum temperature in degrees F 
* Tb - Base temperature where net ozone production begins (50 F) 
* SRd - Solar radiation total for the day 
* WSa - Wind speed near sunrise (using 09-12 UTC forecast mode) 
* WSp - Wind speed mid-day (using 15-21 UTC forecast mode) 

Please refer to those two .names files.


models
```_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_1 (LSTM)                (None, 10, 128)           102912    
_________________________________________________________________
lstm_2 (LSTM)                (None, 10, 256)           394240    
_________________________________________________________________
dense_1 (Dense)              (None, 10, 2)             514       
=================================================================
Total params: 497,666
Trainable params: 497,666
Non-trainable params: 0
_________________________________________________________________
```

result
```
[0.12089240550994873, 0.9800000190734863]
```


