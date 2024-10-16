
import json
import pandas as pd

file="unconfirmed_transactions.json"
with open (file, 'r') as f:
    data = json.load(f)

total_fee = 0
total_transactions = 0
total_inputs = 0
total_outputs = 0
addresses = set()

for tx in data['txs']:
    total_transactions += 1
    total_fee += tx['fee']

    for input in tx['inputs']:
        total_inputs += input['prev_out']['value']
        addresses.add(input['prev_out']['addr'])
    
    for output in tx['out']:
        total_outputs += output['value']
        if 'addr' in output:
            addresses.add(output['addr'])
    
insights = {
    "Total Transactions": total_transactions,
    "Total Fees (satoshis)": total_fee,
    "Total Inputs Value (satoshis)": total_inputs,
    "Total Outputs Value (satoshis)": total_outputs,
    "Unique Addresses Involved": len(addresses)
    # "Addresses": ', '.join(addresses)
}

df = pd.DataFrame(insights.items(), columns=['Metric', 'Value'])
df.to_excel('output.xlsx', index=False)