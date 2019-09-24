import requests

def getQuotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    print(response)
    return response