import json

# json str -(json.loads)-> python dic
x = '{"name":"Bill", "age":63, "city":"Sea"}'
y = json.loads(x)
print(y["age"])
print(y["city"])

# python dic -(json.dumps)-> json str
x = {
    "name": "Bill",
    "age": 66,
    "city": "Sea"
}
y = json.dumps(x)
print(x["name"])
print(y)

# dic list tuple string int float True False None -(json.dumps)-> json str
print(json.dumps({"name": "Bill", "age": 66}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello的s", ensure_ascii=False))
print(json.dumps(55))
print(json.dumps(33.44))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}
print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))

