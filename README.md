# ipotekabank
i've put together 2 little scipts that read from json files (i actually creates random json file using randomizer.py), do some transformation and output in excel and jpeg formats.

## transactions.py
this file uses publicly available unconfirmed_transactions.json file downloaded from https://blockchain.info/unconfirmed-transactions?format=json.
it aggrigates the data by calculating these valuese
- total_fee
- total_transactions
- total_inputs
- total_outputs
lastly it saves the data in .xlsx

## usd_rate.py
this little script opens a json file created by randomizer.py and performs following transformations over it
- calculates volatily by calculating standard deviation of each currency
- finds top 3 currencies with highest volatility namely AWG, ANG, and AZN
- because the data was random. the graph also is pretty normally distributed, which will not be the case in real life


