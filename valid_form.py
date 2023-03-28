from forex_python.converter import CurrencyRates, CurrencyCodes

def find_currency_code(curr):
   cc = CurrencyCodes()
   for data in cc._currency_data:
            if curr in list(data.values()):
                  return data.pop('cc')
            
            

def isamount(amount):
      if type(amount) == float:
            return True
      return False
     