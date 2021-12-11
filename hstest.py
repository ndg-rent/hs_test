from flask import Flask, render_template,request,redirect,url_for,flash
from data.py import *
from datetime import datetime as dt
import operator as op


app=Flask(__name__)
app.config['SECRET_KEY']='c2b672d1550107311eec35d885f742729a108ca79156494e'




#*****************

#*****************
act_cust_id = 0
act_acct_id = 0

#list of customers
@app.route('/',methods=('GET', 'POST'))
def index():
    act_cust_id = request.form.get('cust_id')
    return render_template('index.html',customers=get_customers())

#list of accounts for selected customer
@app.route('/accounts',methods=('GET', 'POST'))
def accounts():
    act_acct_id = request.form.get('acct_id')
    return render_template('accounts.html',accounts=get_accounts(selection=act_cust_id))

#new account
@app.route('/account',methods=('GET', 'POST'))
def account():
    #act_acct_id = request.form.get('acct_id')
    return render_template('account.html')

#list of transfers
@app.route('/transfers',methods=('GET', 'POST'))
def index():
#    act_cust_id = request.form.get('cust_id')
    return render_template('transfers.html',customers=get_transfers())

#new transfer
@app.route('/transfer')
def transfer():
    return render_template('transfer.html')

#@app.route('/process',methods=['POST'])
#def process():
#    accountTo = request.form['accountTo']
#    amount = request.form['amount']
#    return redirect(url_for('account.html'))

@app.route('/message')
def message():
    return render_template('message.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
