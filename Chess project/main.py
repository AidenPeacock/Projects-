import tkinter as tk
win = tk.Tk()
from functools import partial
Piecedict = {"00":"BlackRook.png", "01": "BlackKnight.png", "02" : "BlackBishop.png", "03":"BlackQueen.png",
             "04":"BlackKing.png", "05":"BlackBishop.png", "06":"BlackKnight.png", "07":"BlackRook.png",
             "70":"WhiteRook.png", "71": "WhiteKnight.png", "72" : "WhiteBishop.png", "73":"WhiteQueen.png",
             "74":"WhiteKing.png", "75":"WhiteBishop.png", "76":"WhiteKnight.png", "77":"WhiteRook.png", "99":"16x16.png"}
Boardstate = [0]*64
Decimal2octal = {}
for i in range(8):
    for j in range(8):
        strink = ("{}{}".format(i, j))
        if strink[0] == "1":
            Piecedict[strink] = "BlackPawn.png"
        if strink[0] == "6":
            Piecedict[strink] = "WhitePawn.png"
        try:
            Boardstate[i*8+j] = Piecedict[strink]
        except KeyError:
            Boardstate[i*8+j] = "TkDefaultFont"
        Decimal2octal[i*8+j] = strink
print(Decimal2octal)
Ptruthval = {}
for k in range(8):
    Ptruthval["1{}".format(k)] = True
for a in range(8):
    Ptruthval["6{}".format(a)] = True
v= 0
def interact(c):
    bname = Button_ID[c]
    movestore.append(bname)

    def makemove():
        global v
        v += 1
        if (info1["row"] + info1["column"]) % 2 == 0:
            movestore[1].config(bg="#FFBEB0", image=Boarddict["99"], height=60, width=60, font="TkDefaultFont")
        else:
            movestore[1].config(bg="#A64A36", image=Boarddict["99"], height=60, width=60, font="TkDefaultFont")

        if (info2["row"] + info2["column"]) % 2 == 0:
            movestore[0].config(bg="#FFBEB0")
        else:
            movestore[0].config(bg="#A64A36")
        a = info1["row"]*8 + info1["column"]
        b = info2["row"]*8 + info2["column"]
        Boardstate[a], Boardstate[b] = Boardstate[b], Boardstate[a]
        if "png" in Boardstate[a] and Boardstate[b]:
            Boardstate[a] = "TkDefaultFont"
        movestore[0].grid(row=info2["row"], column=info2["column"])
        movestore[1].grid(row=info1["row"], column=info1["column"])



        print(Boardstate)
        movestore.clear()

    def validmoves(Piece, row, column):
        legalsquare = []
        if "Black" in Piece:
            c = "White"
        else:
            c = "Black"
        if "Bishop" in Piece or "Queen" in Piece:
            incr = 0
            check1 = check2 = check3 = check4 = False
            while not (check1 and check2 and check3 and check4):
                incr += 1
                if not check1:
                    try:
                        x = Boardstate[(row + incr) * 8 + column + incr]
                        if "Tk" in x:
                            legalsquare.append((row + incr) * 8 + column + incr)
                        elif c in x:
                            legalsquare.append((row + incr) * 8 + column + incr)
                            check1 = True
                        else:
                            check1 = True
                    except IndexError:
                        check1 = True
                else:
                    check1 = True
                if (row - incr >= 0) and not check2:
                    try:
                        x = Boardstate[(row - incr) * 8 + column + incr]
                        if "Tk" in x:
                            legalsquare.append((row - incr) * 8 + column + incr)
                        elif c in x:
                            legalsquare.append((row - incr) * 8 + column + incr)
                            check2 = True
                        else:
                            check2 = True
                    except IndexError:
                        check2 = True
                else:
                    check2 = True
                if (column - incr >= 0) and not check3:
                    try:
                        x = Boardstate[(row + incr)*8 + column - incr]
                        if "Tk" in x:
                            legalsquare.append((row + incr) * 8 + column - incr)
                        elif c in x:
                            legalsquare.append((row + incr) * 8 + column - incr)
                            check3 = True
                        else:
                            check3 = True
                    except IndexError:
                        check3 = True
                else:
                    check3 = True
                if (column - incr >= 0) and (row - incr >= 0) and check4 == False:
                    try:
                        x = Boardstate[(row - incr) * 8 + column - incr]
                        if "Tk" in x:
                            legalsquare.append((row - incr) * 8 + column - incr)
                        elif c in x:
                            legalsquare.append((row - incr) * 8 + column - incr)
                            check4 = True
                        else:
                            check4 = True
                    except IndexError:
                        check4 = True
                else:
                    check4 = True
        if "Rook" in Piece or "Queen" in Piece:
            incr = 0
            check1 = check2 = check3 = check4 = False
            if "Black" in Piece:
                c = "White"
            else:
                c = "Black"
            while not (check1 and check2 and check3 and check4):
                incr += 1
                if not check1:
                    try:
                        x = Boardstate[(row + incr) * 8 + column]
                        if "Tk" in x:
                            legalsquare.append((row + incr) * 8 + column)
                        elif c in x:
                            legalsquare.append((row + incr) * 8 + column)
                            check1 = True
                        else:
                            check1 = True
                    except IndexError:
                        check1 = True
                else:
                    check1 = True
                if not check2:
                    try:
                        x = Boardstate[(row) * 8 + column + incr]
                        if "Tk" in x:
                            legalsquare.append((row) * 8 + column + incr)
                        elif c in x:
                            legalsquare.append((row) * 8 + column + incr)
                            check2 = True
                        else:
                            check2 = True
                    except IndexError:
                        check2 = True
                else:
                    check2 = True
                if (column - incr >= 0) and not check3:
                    try:
                        x = Boardstate[(row) * 8 + column - incr]
                        if "Tk" in x:
                            legalsquare.append((row) * 8 + column - incr)
                        elif c in x:
                            legalsquare.append((row) * 8 + column - incr)
                            check3 = True
                        else:
                            check3 = True
                    except IndexError:
                        check3 = True
                else:
                    check3 = True
                if (row - incr >= 0) and not check4:
                    try:
                        x = Boardstate[(row - incr) * 8 + column]
                        if "Tk" in x:
                            legalsquare.append((row - incr) * 8 + column)
                        elif c in x:
                            legalsquare.append((row - incr) * 8 + column)
                            check4 = True
                        else:
                            check4 = True
                    except IndexError:
                        check4 = True
                else:
                    check4 = True

        if "Pawn" in Piece:
            Blackhopcheck = row+1
            Whitehopcheck = row-1
            if Boardstate[Blackhopcheck*8+column] != "TkDefaultFont" and "Black" in Piece:
                return []
            elif Boardstate[Whitehopcheck*8+column] != "TkDefaultFont" and "White" in Piece:
                return []
            elif "Black" in Piece:
                return[row+1, row+2]
            elif "White" in Piece:
                return[row-1, row-2]
        if "Knight" in Piece:
            pass




        return legalsquare





    if len(movestore) == 2:
        #SWAPS THE BUTTONS WHEN CLICKED TWICE
        info1 = movestore[0].grid_info()
        info2 = movestore[1].grid_info()
        movingPiece = movestore[0]["font"]
        attackedPiece = movestore[1]["font"]
        print(movingPiece)
        print(attackedPiece)
        mademove = False
        if v % 2 == 1 and "White" in movingPiece:
            movestore.clear()
        elif v % 2 == 0 and "Black" in movingPiece:
            movestore.clear()
        elif movingPiece == "TkDefaultFont":
            movestore.clear()
        elif "King" in str(attackedPiece):
            movestore.clear()
        elif "King" in movingPiece and (abs(info2["row"] - info1["row"]) > 1 or abs(info2["column"] - info1["column"]) > 1):
            movestore.clear()
        elif "Bishop" in movingPiece:
            legalsquare = validmoves(movingPiece, info1["row"], info1["column"])
            if info2["row"]*8 + info2["column"] in legalsquare:
                makemove()
            else:
                movestore.clear()

        elif "Rook" in movingPiece:
            legalsquare = validmoves(movingPiece, info1["row"], info1["column"])
            if info2["row"]*8 + info2["column"] in legalsquare:
                makemove()
            else:
                movestore.clear()
        elif "Queen" in movingPiece:
            legalsquare = validmoves(movingPiece, info1["row"], info1["column"])
            if info2["row"] * 8 + info2["column"] in legalsquare:
                makemove()
            else:
                movestore.clear()
        elif "Knight" in movingPiece and (abs(info1["row"]-info2["row"]) + abs(info1["column"]-info2["column"]) != 3):
            movestore.clear()
        elif "White" in movingPiece and "White" in str(attackedPiece):
            movestore.clear()
        elif "Black" in movingPiece and "Black" in str(attackedPiece):
            movestore.clear()
        elif "Pawn" in movingPiece:
            if "BlackPawn" in movingPiece:
                if attackedPiece != "TkDefaultFont":
                    if (info2["row"] == info1["row"] + 1) and abs(info1["column"] - info2["column"]) == 1:
                        makemove()
                        mademove = True
                    else:
                        movestore.clear()
                if info2["row"] - info1["row"] >2 or info1["row"] - info2["row"] > 0 or info1["column"] != info2["column"]:
                    movestore.clear()
                elif not mademove:
                    try:
                        x = Ptruthval["{}{}".format(info1["row"], info2["column"])]
                        legalsquares = validmoves(movingPiece, info1["row"], info1["column"])
                        if legalsquares == []:
                            movestore.clear()
                        else:
                            makemove()
                    except KeyError:
                        if info2["row"] - info1["row"] >1:
                            movestore.clear()
                        elif attackedPiece == "TkDefaultFont":
                            makemove()

            elif "WhitePawn" in movingPiece:
                if attackedPiece != "TkDefaultFont":
                    if (info1["row"] == info2["row"] + 1) and abs(info1["column"] - info2["column"]) == 1:
                        makemove()
                        mademove = True
                    else:
                        movestore.clear()
                if info1["row"] - info2["row"] > 2 or info2["row"] - info1["row"] > 0 or info1["column"] != info2["column"]:
                    movestore.clear()
                elif not mademove:
                    try:
                        x = Ptruthval["{}{}".format(info1["row"], info2["column"])]
                        legalsquares = validmoves(movingPiece, info1["row"], info1["column"])
                        if legalsquares == []:
                            movestore.clear()
                        else:
                            makemove()
                    except KeyError:
                        if info1["row"] - info2["row"] >1:
                            movestore.clear()
                        elif attackedPiece == "TkDefaultFont":
                            makemove()

        else:
            makemove()



movestore = []
Boarddict = {}
Button_ID = []
c = 0
for i in range(8):
    for j in range(8):
        if (i+j)% 2 == 0:
            iscolor = "#FFBEB0"
        else:
            iscolor = "#A64A36"
        strink = ("{}{}".format(i, j))
        try:
            Boarddict[strink] = tk.PhotoImage(file=r"{}".format(Piecedict[strink]))
            win.B = tk.Button(bg=iscolor, activebackground="lawn green", image=Boarddict[strink],
                              command=partial(interact, c), font=Piecedict[strink])
            win.B.grid(row=i, column=j)
            Button_ID.append(win.B)
        except KeyError:
            Boarddict[strink] = tk.PhotoImage(file=r"")
            win.B = tk.Button(bg=iscolor, activebackground="lawn green", image=Boarddict[strink], height=60, width=60,
                              command=partial(interact, c), font="TkDefaultFont")
            win.B.grid(row=i, column=j)
            Button_ID.append(win.B)

        c += 1


Boarddict["99"] = tk.PhotoImage(file=r"{}".format(Piecedict["99"]))
win.mainloop()
