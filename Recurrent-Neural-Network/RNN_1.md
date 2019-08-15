## Recurrent Neural Networks 1

https://poloniex.com/support/api/

data

```
{"date":1424304000,"high":244,"low":225,"open":225,"close":244,"volume":46.27631267,"quoteVolume":0.19311748,"weightedAverage":239.62777823},
{"date":1424390400,"high":245,"low":240.25,"open":240.25011809,"close":240.25,"volume":55.894897,"quoteVolume":0.23042935,"weightedAverage":242.56847926},
{"date":1424476800,"high":245,"low":245,"open":245,"close":245,"volume":14.72223865,"quoteVolume":0.06009077,"weightedAverage":245},
```

model

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_1 (LSTM)                (None, 128)               66560     
_________________________________________________________________
dropout_1 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 129       
=================================================================
Total params: 66,689
Trainable params: 66,689
Non-trainable params: 0
_________________________________________________________________
```

result

<img width=600 src="https://user-images.githubusercontent.com/44635266/63088267-66f3e800-bf8f-11e9-9c33-b191ca5be9a7.png">
