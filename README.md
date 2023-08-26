# SQLAlch-Currencies-2 README
This is the part 2: Create SQLAlchemy version of a currency app. It demonstrates the use of Python and the Click package to create a CLI for returning crypto currency investment info stored in a SQLite DB using SQLAlchemy. The currency, date and current price data are provided using an api from CoinGecko https://www.coingecko.com/ 

This app is based on an awesome Pluralsight tutorial by Douglas Starnes who pateiently explains, line by line, how the app works. https://www.pluralsight.com/

While the Part 1 (SQLAlch-Currencies) app used SQL statements to populate an SQLite DB, this part 2 app (SQLAlch-Currencies-2) uses the SQLAlchemy ORM and Core API to populates a separate SQLite DB. A comparison of the SQL and SQLAlchemy methods helps to demonstrate some of the pros and cons of each.


### SQLAlch-Currencies-2 Getting Started

After cloning the SQLAlch-Currencies-2 repo, cd to the folder, create a venv and install the requests, click and SQLAlchemy packages.

$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install requests SQLAlchemy click


The other imported packages are already part of the Python Standard Library

  click 
  sqlite3
  datetime


----------------------------------
CLI request examples: 

A simple test
Request the current price of the default crypto currency: bitcoin in usd  
(venv) $ python get_price.py

Request the current price of specific crypto currencies by specifying coin_id and currency
(venv) $ python main.py --coin_id=ethereum --currency=gbp

Add an investment to the db, specify coin_id, currency and amount
(venv) $ python main.py add-investment --coin_id=bitcoin --currency=usd --amount=1

Calculate the total value of a crypto currency you own (as listed in the db)
in the currency specified
(venv) $ python main.py get-investment-value --coin_id=bitcoin --currency=usd

Import multiple crypto currency investments into the db from a .csv file.
(venv) $ python main.py import-investments --csv_file investments.csv

----------------------------------

This CLI provides only a limited number of commands to demonstrate the use of SQL for populating an SQLite db.

The Part 2 app SQLAlch-Currencies-2 will demonstrate additional commands using SQLAlchemy


