import json
jsonStr = '{ "first": "Steve", "last" : "Rogers"}'
parsedJson = json.loads(jsonStr)
print(parsedJson['first'])

d = {"first": "Bucky", "last" : "Barnes"}
jsonStr = json.dumps(d)
print(jsonStr)
parsedJson = json.loads(jsonStr)
print(parsedJson['first'])