from datetime import datetime as dt
import operator as op

customers =[
  {
    "id": 1,
    "name": "Arisha Barron"
  },
  {
    "id": 2,
    "name": "Branden Gibson"
  },
  {
    "id": 3,
    "name": "Rhonda Church"
  },
  {
    "id": 4,
    "name": "Georgina Hazel"
  }
]

accounts = [] # {'id': ,'cust_id':, 'name':,'dt_stamp':, 'amount':}
transfers = [] # {'id':, 'dt_stamp':, 'acc_from':, 'acc_to':,'amount':}

account = {'id': 0,'cust_id':0, 'name':'','dt_stamp':dt.now(), 'amount':0}
transfer = {'id': 0, 'dt_stamp':dt.now(), 'acc_from':0, 'acc_to':0,'amount':0}


def get_customers():
    return customers

def get_accounts(selection):
    if selection == 0:
        return accounts
    else :
        return [ sub for sub in accounts if sub['cust_id']==selection ]

def get_transfers(acc_id):
    sub_list = [ sub for sub in transfers if sub['acc_from']==acc_id or sub['acc_to']==acc_id ]
    su_list.sort(key=op.itemgetter('dt_stamp'),reverse=True)
    return sub_list

# appending the transfers list
def append_transfers(transfer):
    transfers.append(transfer)
    for account in accounts:
        if account['id']== transfer['acc_from']:
            account[amount]-=transfer['amount']
        elif account['id']== transfer['acc_from']:
            account[amount]+=transfer['amount']

# appending the accounts list
def append_accounts(account):
    if not accounts:
        account['id'] = 2543001
    else :
        account['id'] = accounts[len(accounts)-1]['id']
    accounts.append(account)
    if not transfers:
        new_transfer_id = 1
    else :
        new_transfer_id = transfers[len(transfers)-1]['id']+1
    transfers.append({'id':new_transfer_id,'dt_stamp':account['dt_stamp'],'acc_from':0,'acc_to':account['id'],'amount':account['amount']})
