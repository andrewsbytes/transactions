import datetime
from json import loads
from pprint import pprint

def date_range(date1, date2):
  start = datetime.datetime.strptime(date1, '%Y-%m-%d')
  end = datetime.datetime.strptime(date2, '%Y-%m-%d')
  step = datetime.timedelta(days=1)
  datelist= []
  while start <= end:
    datelist.append(start.date())
    start += step
  return datelist

def to_date(date):
  return datetime.datetime.strptime(date, '%Y-%m-%d').date()

def main():

  balance = 700

  with open('recurring.json') as f:
    recurring = loads(f.read())

  dates = date_range('2018-08-20', '2018-12-31')
  transactions = dict()

  for date in dates:
    debits = dict()

    for k, v in recurring['monthly'].items():
      if v['day'] == date.day:
        debits[k] = v

    for k, v in recurring['yearly'].items():
      if v['month'] == date.month and v['day'] == date.day:
        debits[k] = v

    for k, v in recurring['amex'].items():
      if to_date(k) == date:
        debits['amex'] = dict(amount = v)

    transactions[date] = dict()
    transactions[date]['debits']= debits

    amount = 0

    for k, v in transactions[date]['debits'].items():
      amount += v['amount']
    
    balance -= amount
    
    if date.day in recurring['facebook']['days']:
      balance += recurring['facebook']['amount']
    
    transactions[date]['amount'] = amount
    transactions[date]['balance'] = balance
    
  # pprint(transactions)

  for k, v in sorted(transactions.items()):
    print k, v['balance'], v['amount'] # , v['debits']

if __name__ == '__main__':
  main()
