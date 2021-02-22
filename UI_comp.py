import tkinter as tk
from PIL import Image, ImageTk
import all_func as af
import os
import sys

pl_data = []
bids = []
bid_amount = []
all_purse = []
f = []
t=[]

# Login Click in first window

def LoginClk():
    u_name = name.get()
    pssw = password.get()
    crrct = af.chkLogin(u_name, pssw)
    if(crrct==0):
        error.grid(row=8, column=0, columnspan=4)
    else:
        show_win2()
        
# Search click in second window

def srchClk():
    player = name_ent.get()
    pl_ex = af.chkPlayer(player)
    if(len(pl_ex) != 1):
        err_msg.grid_remove()
        player_name_sub.grid(row=9, column=2, sticky="W")
        player_name_clear.grid(row=9, column=3, sticky="W")
        td1.grid(row=8, column=0, sticky="N")
        td1.config(text = pl_ex[1])
        td2.grid(row=8, column=1, sticky="N")
        td2.config(text = pl_ex[2])
        td3.grid(row=8, column=2, sticky="N")
        td3.config(text = pl_ex[3])
        td4.grid(row=8, column=3, sticky="N")
        td4.config(text = pl_ex[4])
        hd1.grid(row=7, column=0, sticky="N")
        hd2.grid(row=7, column=1, sticky="N")
        hd3.grid(row=7, column=2, sticky="N")
        hd4.grid(row=7, column=3, sticky="N")
        global pl_data
        pl_data = pl_ex
    else:
        err_msg.grid(row=7, column=0, columnspan=4)

# Start Auction click in second window

def strtAuctionClk():
    global bids
    bids = []
    global bid_amount
    bid_amount = []
    show_win3()
    hide_win2()
    hide_win1()
    statement = pl_data[2] + ", " + pl_data[3] + ", Base Price: " + str(pl_data[4])
    lbl_player_data.config(text=statement)
    lbl_player_name.config(text=pl_data[1])
    all_btn()
    global all_purse
    all_purse = af.getPurse()
    updatesAuc()
    updatePurses()
    forAndTotChk()
    
# Updating live auction details in the third window (bottom)

def updatesAuc():
    if(len(bids) == 0):
        latest_update1.config(text = "")
        latest_update2.config(text = "No bids till now")
    elif(len(bids) == 1):
        latest_update1.config(text = "No bids till now")
        latest_update2.config(text = bids[-1][1] + " - " + str(bid_amount[-1]))
    else:
        latest_update2.config(text = bids[-1][1] + " - " + str(bid_amount[-1]))
        latest_update1.config(text = bids[-2][1] + " - " + str(bid_amount[-2]))

# If next bid is found to be greater than purse value, then disable that team's button

def updatePurses():
    if(len(bids)!=0):
        next_bid = af.next_bid(bid_amount[-1])
    else:
        next_bid = pl_data[4]
    if(all_purse[0] < next_bid):
        btn_csk.config(state=tk.DISABLED)
    if(all_purse[1] < next_bid):
        btn_dc.config(state=tk.DISABLED)
    if(all_purse[2] < next_bid):
        btn_kxip.config(state=tk.DISABLED)
    if(all_purse[3] < next_bid):
        btn_kkr.config(state=tk.DISABLED)
    if(all_purse[4] < next_bid):
        btn_mi.config(state=tk.DISABLED)
    if(all_purse[5] < next_bid):
        btn_rr.config(state=tk.DISABLED)
    if(all_purse[6] < next_bid):
        btn_rcb.config(state=tk.DISABLED)
    if(all_purse[7] < next_bid):
        btn_srh.config(state=tk.DISABLED)

# undo button's visibility (window 3)

def undo_vis():
    if(len(bids) > 0):
        btn_undo.grid(row=7, column=3)
    else:
        btn_undo.grid_remove()

# if teams button is clicked in window 3

def cskClk():
    bids.append([1, 'Chennai Super Kings'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(0)
    updatesAuc()
    updatePurses()
    undo_vis()

def dcClk():
    bids.append([2, 'Delhi Capitals'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(1)
    updatesAuc()
    updatePurses()
    undo_vis()
        
def kxipClk():
    bids.append([3, 'Kings XI Punjab'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(2)
    updatesAuc()
    updatePurses()
    undo_vis()
    
def kkrClk():
    bids.append([4, 'Kolkata Knight Riders'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(3)
    updatesAuc()
    updatePurses()
    undo_vis()

def miClk():
    bids.append([5, 'Mumbai Indians'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(4)
    updatesAuc()
    updatePurses()
    undo_vis()
    
def rrClk():
    bids.append([6, 'Rajasthan Royals'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(5)
    updatesAuc()
    updatePurses()
    undo_vis()
    
def rcbClk():
    bids.append([7, 'Royal Challengers Bangalore'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(6)
    updatesAuc()
    updatePurses()
    undo_vis()
    
def srhClk():
    bids.append([8, 'Sunrisers Hyderabad'])
    if(len(bid_amount) == 0):
        bid_amount.append(pl_data[4])
    else:
        curr_bid = bid_amount[-1]
        bid_amount.append(af.next_bid(curr_bid))
    #btn_dis(7)
    updatesAuc()
    updatePurses()
    undo_vis()

# When undo button is clicked

def undoClk():
    bids.pop()
    bid_amount.pop()
    """if(len(bids)>0):
        btn_dis(bids[-1][0]-1)
    else:
        all_btn()"""
    undo_vis()
    updatesAuc()
    updatePurses()

# Activate all buttons

def all_btn():
    btns = [btn_csk, btn_dc, btn_kxip, btn_kkr, btn_mi, btn_rr, btn_rcb, btn_srh]
    for i in range(8):
        btns[i].config(state=tk.NORMAL)

# disable all buttons

def all_btn_dis():
    btns = [btn_csk, btn_dc, btn_kxip, btn_kkr, btn_mi, btn_rr, btn_rcb, btn_srh]
    for i in range(8):
        btns[i].config(state=tk.DISABLED)

# Finish Auction clicked on window 3

def fnshAucClk():
    if(pl_data[2] == 'India'):
        pl_country=0
    else:
        pl_country=1
    af.update_mast_data(pl_data[0], bids, bid_amount, pl_country)
    if(len(bids)==0):
        final_res.config(text="UNSOLD!!", fg = "red", font=('Roboto', 15, 'bold'))
    else:
        text_dis = "SOLD TO " + bids[-1][1] + " at " + str(bid_amount[-1]) + " Lacs."
        final_res.config(text=text_dis, fg="green", font=('Roboto', 15, 'bold'))
    latest_update1.grid_remove()
    latest_update2.grid_remove()
    btn_undo.grid_remove()
    fin_auc.grid_remove()
    all_btn_dis()
    final_res.grid(row=7, column=0, rowspan=2, columnspan=4)
    move_win2.grid(row=9, column=0, columnspan=4)

def win2Clk():
    hide_win3()
    hide_win1()
    show_win2()

# Show all the contents of window 1

def show_win1():
    lbl_heading.grid(row=2, column=0, columnspan=4)
    lbl_cred.grid(row=4, column=0, columnspan=4, sticky="S")
    lbl_name.grid(row=6, column=0, sticky="E", padx=20)
    name.grid(row=6, column=1, columnspan=3, sticky="W", padx=25, ipady=5)
    lbl_password.grid(row=7, column=0, sticky="E", padx=20)
    password.grid(row=7, column=1, columnspan=3, sticky="W", padx=25, ipady=5)
    login.grid(row=9, column=1)
    reset_pass.grid(row=9, column=2)

# Show all contents of window 2

def show_win2():
    hide_win2()
    hide_win1()
    hide_win3()
    lbl_player.grid(row=2, column=0, columnspan=4)
    name_ent.grid(row=3, column=0, columnspan=4, ipady=7)
    name_ent.delete(0,tk.END)
    name_ent.insert(0,"")
    play_name_sub.grid(row=4, column=0, columnspan=4)

# Show all contents of window 3
    
def show_win3():
    hide_win2()
    hide_win1()
    lbl_player_name.grid(row=2, column=1, columnspan=2, sticky="N")
    lbl_player_data.grid(row=3, column=1, columnspan=2, sticky="N")
    btn_csk.grid(row=4, column=0)
    btn_dc.grid(row=4, column=1)
    btn_kkr.grid(row=4, column=3)
    btn_kxip.grid(row=4, column=2)
    btn_mi.grid(row=5, column=0)
    btn_srh.grid(row=5, column=3)
    btn_rcb.grid(row=5, column=2)
    btn_rr.grid(row=5, column=1)
    fin_auc.grid(row = 7, column=0, columnspan=4)
    latest_update1.grid(row=9, column=0, columnspan=4)
    latest_update2.grid(row=10, column=0, columnspan=4)

# Hide all contents of window 1

def hide_win1():
    lbl_heading.grid_remove()
    lbl_name.grid_remove()
    name.grid_remove()
    lbl_password.grid_remove()
    password.grid_remove()
    login.grid_remove()
    reset_pass.grid_remove()
    lbl_cred.grid_remove()
    error.grid_remove()

# Hide all contents of window 2

def hide_win2():
    lbl_player.grid_remove()
    name_ent.grid_remove()
    play_name_sub.grid_remove()
    player_name_sub.grid_remove()
    player_name_clear.grid_remove()
    td1.grid_remove()
    td2.grid_remove()
    td3.grid_remove()
    td4.grid_remove()
    hd1.grid_remove()
    hd2.grid_remove()
    hd3.grid_remove()
    hd4.grid_remove()
    err_msg.grid_remove()

# Hide all contents of window 3

def hide_win3():
    lbl_player_name.grid_remove()
    lbl_player_data.grid_remove()
    btn_csk.grid_remove()
    btn_dc.grid_remove()
    btn_kkr.grid_remove()
    btn_kxip.grid_remove()
    btn_mi.grid_remove()
    btn_srh.grid_remove()
    btn_rcb.grid_remove()
    btn_rr.grid_remove()
    fin_auc.grid_remove()
    latest_update1.grid_remove()
    latest_update2.grid_remove()
    final_res.grid_remove()
    move_win2.grid_remove()

# Disable the corresponding button (window 3)

def btn_dis(team_i):
    btns = [btn_csk, btn_dc, btn_kxip, btn_kkr, btn_mi, btn_rr, btn_rcb, btn_srh]
    for i in range(8):
        if(f[i] == 0 & t[i] == 0):
            if(i==team_i):
                btns[i].config(state=tk.DISABLED)
            else:
                btns[i].config(state=tk.NORMAL)

# check for total number of foreign and total players in a team

def forAndTotChk():
    btns = [btn_csk, btn_dc, btn_kxip, btn_kkr, btn_mi, btn_rr, btn_rcb, btn_srh]
    both = af.get_num_for_and_tot()
    global f
    f = both[0]
    global t
    t = both[1]
    for i in range(len(f)):
        if(f[i] >= 8):
            if(pl_data[2] != 'India'):
                btns[i].config(state=tk.DISABLED)
                f[i] = 1
            else:
                f[i] = 0
        else:
            f[i] = 0
        if(t[i]>=25):
            btns[i].config(state=tk.DISABLED)
            t[i] = 1
        else:
            t[i] = 0

main_win = tk.Tk()
main_win.geometry("550x550")
main_win.title("AUCTIONATOR")
for i in range(11):
    main_win.rowconfigure(i, weight=1)
for i in range(4):
    main_win.columnconfigure(i, weight=1)

# Logo
path = os.path.join(sys.path[0] + '\\Cricspoint41-03.png')
img = Image.open('IPL-Logo-PNG.png')
img = img.resize((140,140))
img2 = ImageTk.PhotoImage(img)
label1 = tk.Label(image=img2)
label1.image = img2
label1.grid(row=0, column=0, columnspan=4, rowspan=2)

# window 1
lbl_heading = tk.Label(main_win, text="AUCTIONATOR", font=("Roboto", 30, "bold"))
lbl_cred = tk.Label(main_win, text="Enter credentials", font=("Roboto", 15))
lbl_name = tk.Label(main_win, text="Username", font=("Roboto", 11))
name = tk.Entry(main_win, width=55)
lbl_password = tk.Label(main_win, text="Password", font=("Roboto", 11))
password = tk.Entry(main_win, width=55, show="*")
login = tk.Button(main_win, text="Log In", command=LoginClk, height=2, width=12, bg="#A0CC3A", font=("Roboto", 12, "bold"))
reset_pass = tk.Button(main_win, text="Sign Up", height=2, width=12, bg="#2F90CE", font=("Roboto", 12, "bold"))
error = tk.Label(main_win, text="Wrong credentials, try again!!", fg="red")

#window 2
lbl_player = tk.Label(main_win, text="Enter Player's Full Name:", font=("Roboto", 15))
name_ent = tk.Entry(main_win, width = 70)
play_name_sub = tk.Button(main_win, text="Search", width=15, bg="#804D9E", fg="white", command=srchClk)
hd1 = tk.Label(main_win, text="Name", font=("Roboto", 10, "bold"))
hd2 = tk.Label(main_win, text="Country", font=("Roboto", 10, "bold"))
hd3 = tk.Label(main_win, text="Type", font=("Roboto", 10, "bold"))
hd4 = tk.Label(main_win, text="Base Price(Lacs)", font=("Roboto", 10, "bold"))
td1 = tk.Label(main_win, width=20, text="Vaibhav Pipara", font=("Roboto", 10))
td2 = tk.Label(main_win, width=20, text="India", font=("Roboto", 10))
td3 = tk.Label(main_win, width=20, text="Batsman", font=("Roboto", 10))
td4 = tk.Label(main_win, width=20, text="Inf", font=("Roboto", 10))
player_name_sub = tk.Button(main_win, text="Start Auction", command=strtAuctionClk, width=12, height=2, bg="#A0CC3A", font=("Roboto", 12, "bold"))
player_name_clear = tk.Button(main_win, text="Reset", width=10, height=2, bg="#2F90CE", font=("Roboto", 12, "bold"), command=show_win2)
err_msg = tk.Label(main_win, text="Name not found, TRY AGAIN!!!", fg="red")

# window 3
lbl_player_name = tk.Label(main_win, text="Vaibhav Pipara", font=("Roboto", 20, "bold"))
lbl_player_data = tk.Label(main_win, text="India, Batsman, Base Price = inf", font=("Roboto", 12))
btn_csk = tk.Button(main_win, text="CSK", height=2, width=10, fg="black", bg="#F0CE15", command=cskClk)
btn_dc = tk.Button(main_win, text="DC", height=2, width=10, fg="white", bg="#0A69A8", command=dcClk)
btn_kkr = tk.Button(main_win, text="KKR", height=2, width=10, fg="white", bg="#3A2563", command=kkrClk)
btn_kxip = tk.Button(main_win, text="KXIP", height=2, width=10, fg="white", bg="#EE363E", command=kxipClk)
btn_mi = tk.Button(main_win, text="MI", height=2, width=10, fg="white", bg="#0F4B9B", command=miClk)
btn_srh = tk.Button(main_win, text="SRH", height=2, width=10, fg="white", bg="#DF4925", command=srhClk)
btn_rcb = tk.Button(main_win, text="RCB", height=2, width=10, fg="white", bg="#B4353D", command=rcbClk)
btn_rr = tk.Button(main_win, text="RR", height=2, width=10, fg="white", bg="#DA6498", command=rrClk)
fin_auc = tk.Button(main_win, text="Finish", height=2, width=20, fg="black", bg="#A0CC3A", font=("Roboto", 12, "bold"), command=fnshAucClk)
btn_undo = tk.Button(main_win, text="Undo", width=10, command=undoClk, fg="white", bg="blue")
latest_update1 = tk.Label(main_win, text="UP 1")
latest_update2 = tk.Label(main_win, text="UP 2")
final_res = tk.Label(main_win, text = "final")
move_win2 = tk.Button(main_win, text="Move to Next Player", command=win2Clk, height=2, width=20, fg="black", bg="#A0CC3A", font=("Roboto", 12, "bold"))

show_win1()

main_win.mainloop()