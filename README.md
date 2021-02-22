# Auctionator---Live-Auction-Data-entry

## Creating the database

Create a mysql database on any server of your choice\
Then create 4 tables in it namely:\
a) users (columns - id(int), username(varchar), password(varchar))\
b) players (columns - id(int), name(varchar), country(varchar), base_price(int), final_price(int), team_id(int))\
c) teams (columns - id(int), name(varchar), sname(varchar), purse(int), num_indian(int), num_foreign(int), total_players(int))\
d) auctionLive (columns - player_id(int), team_id(int), price(int))

## Connecting Database using python

import mysql.connector as mc\
cnx = mc.connection.MySQLConnection(user='sql12392879', password='l2yUjsRdXL', host='sql12.freesqldatabase.com', database='sql12392879')\
cur = cnx.cursor()

In the above code, change the details of the SQL server present here with yours.\
Also, after running the above code, run >> cur.execute(query_to_be_executed)\
Then run >> conn.commit() to commit the changes on actual dataset.\
(without >> sign)

## Inserting values in database

Insert the values in all tables using INSERT function of SQL.\
Things to keep in mind when inserting values:\
-> in players table, add the complete name in lowercase without any special symbol (.,/;:><())\
-> in players table, add the player type as 'all' for all rounder and 'wkt' for wicketkeeper, batsman and bowler remains as it is.

## Connecting Database with application
Open the all_func.py and in function set_conn give all the details of your server by changing existing values that exist in file

## Opening the file
Save all three files (UI_comp.py, all_func.py, IPL_Logo) in same directory, and run UI_comp.py.
