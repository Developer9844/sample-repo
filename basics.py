a = "Hello World! H  "
c = "Hello, my name, is Taco, I am, programmer"

print(a[0])
print(len(a))
for x in a:
    print(x)

if "Hello" in a:
    print("yes, Hello is available")
else:
    print("None")

b = a.strip()
print(b, "and length is",len(b))

print(a.replace("H", "J"))

print(b.split(" "))
print(c.split(", "))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:

    if "a" in x:
        newlist.append(x.upper())

print("New list = ",newlist)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print(x)
    print(thisdict[x])

for x, y in thisdict.items():
    print(x,":", y)

adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

for x in adj:
    print(x)
    for y in fruits:
        print(y)
        print(x, y)

print("-"*5,"Classes and Objects", "-"*5)

class Employee:

    def __init__(self, fname, lname, department):
        self.fname = fname
        self.lname = lname
        self.department = department

    def details(self):
        print(f"Hello, My name is {self.fname} {self.lname}, and I work in {self.department} Department")

class Developer(Employee):
    def __init__(self, fname, lname, department):
        super().__init__(fname, lname, department)

x = Developer("Tom", "Python", "Hubspot")

x.details()

# c = "Hello, my name, is Taco, I am, programmer"

import re

t = re.sub("a", "-", c)

print(t)
# output = Hello, my n-me, is T-co, I -m, progr-mmer
# -----------------------------------------------------------------------------------------
import requests

def get_exchange_rates(api_key):
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

api_key = "fca_live_dx1pzRRe7M4n89i0Y4yDP6r2WZ2K6Zkiw09b8D1J"

exchange_rates = get_exchange_rates(api_key)

print(exchange_rates.values())



print("Available currencies:", ", ".join(exchange_rates.keys()))

enter_amount = int(input("Enter amount: "))

enter_from_currency = input("Enter currency: ").upper()
enter_to_currency = input("Enter conv currency: ").upper()


converted_amount = enter_amount * exchange_rates[enter_to_currency] / exchange_rates[enter_from_currency]

print(converted_amount)