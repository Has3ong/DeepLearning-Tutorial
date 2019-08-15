## Deep Neural Networks 5

#### UCI Machine Learning Repository

* https://archive.ics.uci.edu/ml/index.php


### Concrete Compressive Strength Data Set 

#### Attribute Information:

Attribute Information:

* Given are the variable name, variable type, the measurement unit and a brief description.
* The concrete compressive strength is the regression problem.
* The order of this listing corresponds to the order of numerals along the rows of the database. 

Name -- Data Type -- Measurement -- Description 

* Cement (component 1) -- quantitative -- kg in a m3 mixture -- Input Variable 
* Blast Furnace Slag (component 2) -- quantitative -- kg in a m3 mixture -- Input Variable 
* Fly Ash (component 3) -- quantitative -- kg in a m3 mixture -- Input Variable 
* Water (component 4) -- quantitative -- kg in a m3 mixture -- Input Variable 
* Superplasticizer (component 5) -- quantitative -- kg in a m3 mixture -- Input Variable 
* Coarse Aggregate (component 6) -- quantitative -- kg in a m3 mixture -- Input Variable 
* Fine Aggregate (component 7)	-- quantitative -- kg in a m3 mixture -- Input Variable 
* Age -- quantitative -- Day (1~365) -- Input Variable 
* Concrete compressive strength -- quantitative -- MPa -- Output Variable 


Model

```

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 512)               4608      
_________________________________________________________________
dense_2 (Dense)              (None, 256)               131328    
_________________________________________________________________
dense_3 (Dense)              (None, 128)               32896     
_________________________________________________________________
dense_4 (Dense)              (None, 32)                4128      
_________________________________________________________________
dense_5 (Dense)              (None, 1)                 33        
=================================================================
Total params: 172,993
Trainable params: 172,993
Non-trainable params: 0
_________________________________________________________________
```

Result

<img width=600 src="https://user-images.githubusercontent.com/44635266/63077943-ee802d80-bf74-11e9-97c1-599712f2e4f1.png">
