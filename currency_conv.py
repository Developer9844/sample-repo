import requests
# import freecurrencyapi

# def get_exchange_rates(api_key):
#     url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"
#     response = requests.get(url)
#     data = response.json()
#     return data

# def convert_currency(amount, from_currency, to_currency, exchange_rates):
#     if from_currency not in exchange_rates or to_currency not in exchange_rates:
#         return None

#     converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
#     return converted_amount

# def main():
#     api_key = "fca_live_dx1pzRRe7M4n89i0Y4yDP6r2WZ2K6Zkiw09b8D1J"  # Replace with your actual API key
#     exchange_rates = get_exchange_rates(api_key)

#     print("Available currencies:", ", ".join(exchange_rates.keys()))

#     amount = float(input("Enter amount: "))
#     from_currency = input("Enter the source currency: ").upper()
#     to_currency = input("Enter the target currency: ").upper()

#     converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)

#     if converted_amount is not None:
#         print(f"{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
#     else:
#         print("Invalid currencies")

# if __name__ == "__main__":
#     main()----------------------------------------------------------------------

import csv

def csv_to_dict(csv_file):

    result_dict = {}

    with open(csv_file, 'r') as file:
        r = csv.reader(file)

        for row in r:
            key = row[0]
            value = row[1]

            result_dict[key] = value

    return result_dict

csv_file = "Index.csv"

p = csv_to_dict(csv_file)

print(p)

def get_exchange_rates():

    return p

def convert_currency(amount, from_currency, to_currency, p):
    if from_currency not in p or to_currency not in p:
        return None

    converted_amount = amount * p[to_currency] / p[from_currency]   # 100 INR * 1 USD/
    return converted_amount

def main():
    p = get_exchange_rates()

    print("Available currencies:", ", ".join(p.keys()))

    amount = float(input("Enter amount: "))
    from_currency = input("Enter the source currency: ").upper()
    to_currency = input("Enter the target currency: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency, p)

    if converted_amount is not None:
        print(f"{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currencies")

if __name__ == "__main__":
    main()