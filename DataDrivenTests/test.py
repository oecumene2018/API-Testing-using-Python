import json

data = '{"K1": "val1", "K2": "val2}'

json_result = json.dumps(data)
print(type(json_result))