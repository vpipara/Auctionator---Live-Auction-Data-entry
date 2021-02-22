import pandas as pd
import mysql.connector as mc

# setting connection with SQL Server

def set_conn():
    conn = mc.connection.MySQLConnection(user='sql12392879', password='l2yUjsRdXL', host='sql12.freesqldatabase.com', database='sql12392879')
    return conn

def set_cur(conn):
    cur = conn.cursor()
    return cur

# get all registered users

def getLoginDet():
    cnction = set_conn()
    crsr = set_cur(cnction)
    crsr.execute("Select * from users")
    tb = crsr.fetchall()
    tb = pd.DataFrame(tb)
    return tb

# get all players data from players table

def getPlayerDet():
    cnction = set_conn()
    crsr = set_cur(cnction)
    crsr.execute("Select * from players")
    tb = crsr.fetchall()
    tb = pd.DataFrame(tb)
    return tb

# Checking if the username and password exist in database

def chkLogin(uname, pssw):
    all_users = getLoginDet()
    u_data = all_users[all_users[1]==uname]
    if(len(u_data)>0):
        if(pssw == u_data[2].iloc[0]):
            return 1
    return 0

# checking if player name exist in Database and return his attributes

def chkPlayer(player):
    all_players = getPlayerDet()
    our_player = all_players[all_players[1] == player]
    if(len(our_player)>0):
        n = player
        n = n.split()
        rn = ""
        for j in range(len(n)):
            rn += n[j][0].upper()+n[j][1:] + " "
        rn = rn[:-1]
        t = our_player.iloc[0][4]
        if(t=='batsman'):
            t='Batsman'
        elif(t=='bowler'):
            t='Bowler'
        elif(t=='all'):
            t='All Rounder'
        else:
            t='Wicketkeeper'
        c=our_player.iloc[0][2]
        b=our_player.iloc[0][3]
        i=our_player.iloc[0][0]
        return [i, rn, c, t, b]
    
    return [0]

# calcluating next bid based on current bid

def next_bid(curr_bid):
    if(curr_bid < 100):
        new_bid = curr_bid + 5
    elif((curr_bid>=100) & (curr_bid<200)):
        new_bid = curr_bid+10
    elif((curr_bid>=200) & (curr_bid<500)):
        new_bid = curr_bid + 20
    elif(curr_bid>=500):
        new_bid = curr_bid + 25
    return new_bid

# inserting bidding values in the database (all 3 tables: players, teams, auctionLive)

def update_mast_data(pl_id, bids, bid_amount, pl_country):
    cnction = set_conn()
    crsr = set_cur(cnction)
    if(len(bids) == 0):
        crsr.execute("insert into auctionLive(player_id, team_id, price) values(" + str(pl_id) + ", 0, 0)")
        crsr.execute("update players set final_price = 0 where id = " + str(pl_id))
        crsr.execute("update players set team_id = 0 where id = " + str(pl_id))
    else:
        crsr.execute("Select * from teams where id = " + str(bids[-1][0]))
        tb = crsr.fetchall()
        tb = pd.DataFrame(tb)
        purse_rem = tb.iloc[0][3]-bid_amount[-1]
        num_players = tb.iloc[0][6]+1
        if(pl_country == 1):
            num_fore = tb.iloc[0][5]+1
            crsr.execute("update teams set num_foreign = " + str(num_fore) + " where id = " + str(bids[-1][0]))
        for i in range(len(bids)):
            crsr.execute("insert into auctionLive(player_id, team_id, price) values(" + str(pl_id) + ", " + str(bids[i][0]) + ", " + str(bid_amount[i]) +")")
        crsr.execute("update players set team_id = " + str(bids[-1][0]) + " where id = " + str(pl_id))
        crsr.execute("update players set final_price = " + str(bid_amount[-1]) + " where id = " + str(pl_id))
        crsr.execute("update teams set purse = " + str(purse_rem) + " where id = " + str(bids[-1][0]))
        crsr.execute("update teams set total_players = " + str(num_players) + " where id = " + str(bids[-1][0]))
    cnction.commit()
    cnction.close()

# Getting list of purse remaining of each team

def getPurse():
    cnction= set_conn()
    crsr = set_cur(cnction)
    crsr.execute("Select * from teams order by id")
    tb = crsr.fetchall()
    tb = pd.DataFrame(tb)
    all_team_purse = tb[3].tolist()
    return all_team_purse

# getting total players and total foreign players in a team

def get_num_for_and_tot():
    cnction= set_conn()
    crsr = set_cur(cnction)
    crsr.execute("Select * from teams order by id")
    tb= crsr.fetchall()
    tb = pd.DataFrame(tb)
    num_for = tb[5].tolist()
    num_tot = tb[6].tolist()
    return [num_for, num_tot]



def get_comp_data():
    cnction = set_conn()
    crsr = set_cur(cnction)
    crsr.execute("Select * from players where team_id is not null;")
    df = crsr.fetchall()
    df = pd.DataFrame(df)
    return df

















