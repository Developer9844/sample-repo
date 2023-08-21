import json

x = { 
    "name":"John", 
    "age":30,
    "address":{
        "city":"New York",
        "street":"NY city road",
        "flat_no":420
    } 

}

y = json.dumps(x, indent=4)

print(y)
print(type(y))