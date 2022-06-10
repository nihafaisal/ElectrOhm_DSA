def ResistanceCombination(lst):
    R=[]
    TotalR=[]
    AllCombo=[]
    for i in lst:
        R.append([i, 1, 0 ])
        TotalR.append(i)
    #Single Series & Single Parallel
    RSS=[]
    RPP=[]
    CheckDuplicate=[]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][0]+R[j][0] not in CheckDuplicate:
                RSS.append([R[i][0]+R[j][0], R[i][1]+R[j][1], str(R[i][0])+' series with ' + str(R[j][0])])
                CheckDuplicate.append(R[i][0] + R[j][0])
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(R)):
            if round((R[i][0]**-1+R[j][0]**-1)**-1,2) not in CheckDuplicate:
                RPP.append([round((R[i][0]**-1+R[j][0]**-1)**-1,2), R[i][1]+R[j][1], str(R[i][0]) +' parallel with ' + str(R[j][0])])
                CheckDuplicate.append(round((R[i][0]**-1+R[j][0]**-1)**-1,2))
    #TRIPLE COMBO
    RPPS=[]
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RPP)):
            if R[i][0] + RPP[j][0] not in CheckDuplicate:
                RPPS.append([R[i][0] + RPP[j][0], R[i][1] + RPP[j][1], str(R[i][0]) + ' series with ' + str(RPP[j][2])])
                CheckDuplicate.append(R[i][0] + RPP[j][0])
    RPPP=[]
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RPP)):
            if round((R[i][0] ** -1 + RPP[j][0] ** -1) ** -1, 2) not in CheckDuplicate:
                RPPP.append([round((R[i][0] ** -1 + RPP[j][0] ** -1) ** -1, 2), R[i][1] + RPP[j][1],
                            str(R[i][0]) + ' parallel with ' + str(RPP[j][2])])
                CheckDuplicate.append(round((R[i][0] ** -1 + RPP[j][0] ** -1) ** -1, 2))
    RSSS=[]
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RSS)):
            if R[i][0] + RSS[j][0] not in CheckDuplicate:
                RSSS.append([R[i][0] + RSS[j][0], R[i][1] + RSS[j][1], str(R[i][0]) + ' series with ' + str(RSS[j][2])])
                CheckDuplicate.append(R[i][0] + RSS[j][0])
    RSSP=[]
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RSS)):
            if round((R[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2) not in CheckDuplicate:
                RSSP.append([round((R[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2), R[i][1] + RSS[j][1],
                             str(R[i][0]) + ' parallel with ' + str(RSS[j][2])])
                CheckDuplicate.append(round((R[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2))
    #QUAD COMBO
    RSPSS=[]
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RSSP)):
            if R[i][0] + RSSP[j][0] not in CheckDuplicate:
                RSPSS.append([R[i][0] + RSSP[j][0], R[i][1] + RSSP[j][1], str(R[i][0]) + ' series with ' + str(RSSP[j][2])])
                CheckDuplicate.append(R[i][0] + RSSP[j][0])
    RSPPP = []
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RPPP)):
            if R[i][0] + RPPP[j][0] not in CheckDuplicate:
                RSPPP.append(
                    [R[i][0] + RPPP[j][0], R[i][1] + RPPP[j][1], str(R[i][0]) + ' series with ' + str(RPPP[j][2])])
                CheckDuplicate.append(R[i][0] + RPPP[j][0])
    RPPSPP=[]
    CheckDuplicate = []
    for i in range(len(RPP)):
        for j in range(len(RPP)):
            if RPP[i][0] + RPP[j][0] not in CheckDuplicate:
                RPPSPP.append(
                    [RPP[i][0] + RPP[j][0], RPP[i][1] + RPP[j][1], str(RPP[i][2]) + ' series with ' + str(RPP[j][2])])
                CheckDuplicate.append(RPP[i][0] + RPP[j][0])
    RSSPSS = []
    CheckDuplicate = []
    for i in range(len(RSS)):
        for j in range(len(RSS)):
            if round((RSS[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2) not in CheckDuplicate:
                RSSPSS.append([round((RSS[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2), RSS[i][1] + RSS[j][1],
                             '(' + str(RSS[i][2]) + ') parallel with (' + str(RSS[j][2]) + ')' ])
                CheckDuplicate.append(round((RSS[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2))
    RPPSS=[]
    CheckDuplicate = []
    for i in range(len(RPP)):
        for j in range(len(RSS)):
            if RPP[i][0] + RSS[j][0] not in CheckDuplicate:
                RPPSS.append(
                    [RPP[i][0] + RSS[j][0], RPP[i][1] + RSS[j][1], str(RPP[i][2]) + ' series with ' + str(RSS[j][2])])
                CheckDuplicate.append(RPP[i][0] + RSS[j][0])
    RPPSS = []
    CheckDuplicate = []
    for i in range(len(RPP)):
        for j in range(len(RSS)):
            if round((RPP[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2) not in CheckDuplicate:
                RPPSS.append([round((RPP[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2), RPP[i][1] + RSS[j][1],
                               str(RPP[i][2]) + ' parallel with ' + str(RSS[j][2])])
                CheckDuplicate.append(round((RPP[i][0] ** -1 + RSS[j][0] ** -1) ** -1, 2))
    RSSSP = []
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RSSS)):
            if round((R[i][0] ** -1 + RSSS[j][0] ** -1) ** -1, 2) not in CheckDuplicate:
                RSSSP.append([round((R[i][0] ** -1 + RSSS[j][0] ** -1) ** -1, 2), R[i][1] + RSSS[j][1],
                              str(R[i][0]) + ' parallel with ' + str(RSSS[j][2])])
                CheckDuplicate.append(round((R[i][0] ** -1 + RSSS[j][0] ** -1) ** -1, 2))
    RPPPP=[]
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RPPP)):
            if round((R[i][0] ** -1 + RPPP[j][0] ** -1) ** -1, 2) not in CheckDuplicate:
                RSSSP.append([round((R[i][0] ** -1 + RPPP[j][0] ** -1) ** -1, 2), R[i][1] + RPPP[j][1],
                              str(R[i][0]) + ' parallel with ' + str(RPPP[j][2])])
                CheckDuplicate.append(round((R[i][0] ** -1 + RPPP[j][0] ** -1) ** -1, 2))
    RSSSS = []
    CheckDuplicate = []
    for i in range(len(R)):
        for j in range(len(RSSS)):
            if R[i][0] + RSSS[j][0] not in CheckDuplicate:
                RSSSS.append(
                    [R[i][0] + RSSS[j][0], R[i][1] + RSSS[j][1], str(R[i][0]) + ' series with ' + str(RSSS[j][2])])
                CheckDuplicate.append(R[i][0] + RSSS[j][0])

    AllCombo=R+RSS+RPP+RSSS+RPPP+RSSP+RPPS+RSPPP+RPPSS+RSPSS+RPPSPP+RSSSP+RPPPP+RSSSS+RSSPSS
    return(AllCombo)

def insert(BST, item):
	if BST == {}:
		BST["Resistance"] = item[0]
		BST["Resistors used"] = item[2]
		BST["No. of resistors"] = item[1]
		BST["left"] = {}
		BST["right"] = {}
	elif item[0] == BST["Resistance"]:
		if item[1] < BST["No. of resistors"]:
			BST["Resistance"] = item[0]
			BST["Resistors used"] = item[2]
			BST["No. of resistors"] = item[1]
			BST["left"] = {}
			BST["right"] = {}
	elif item[0] > BST["Resistance"]:
		insert(BST["right"], item)
	else:
		insert(BST["left"], item)

def readBST(file, BST):
	a = file.readline()
	if "\\" not in a:
		return BST
	else:
		a = a.split("\\")
		a[0], a[2] = eval(a[0]), int(a[2])
		BST["Resistance"], BST["Resistors used"], BST["No. of resistors"], BST["left"], BST["right"] = a[0], a[1], a[2], {}, {}
		BST["left"] = readBST(file, BST["left"])
		BST["right"] = readBST(file, BST["right"])
		return BST

def p_EnQueue(lst, item, value):
	flag = True
	for i in range(len(lst) -1 , -1, -1):
		#print(lst[i][2])
		if lst[i][2] < item[2]:
			lst.insert(i+1, item)
			flag = False
		if lst[i][2] == item[2]:
			if abs(lst[i][0]-value) < abs(item[0] - value):
				lst.insert(i+1, item)
				flag = False
		if not flag:
			break
	if flag:
		lst.insert(0, item)

def find(BST, value, final, error):
	if BST == {}:
		return final
	if abs((BST["Resistance"] - value)/value*100) <= error:
		if (BST["Resistance"], BST["Resistors used"], BST["No. of resistors"]) not in final:
			p_EnQueue(final, (BST["Resistance"], BST["Resistors used"], BST["No. of resistors"]), value)
		final = find(BST["left"], value, final, error)
		final = find(BST["right"], value, final, error)
	elif (BST["Resistance"] - value)/value*100 > error:
		final = find(BST["left"], value, final, error)
	elif (BST["Resistance"] - value)/value*100 < -error:
		final = find(BST["right"], value, final, error)
	return final

def bestR(R, B, error):
	final = find(B, R, [], error)
	if len(final) == 0:
		return ["Sorry, no combinations exist, please try some other value."]
	a, output, flag = final[0][2], [], True
	for i in final:
		if a == i[2]:
			for j in output:
				if abs(j[0] - R) < abs(i[0] -R):
					flag = False
			if flag:
				output.append(i)
			a += 1
		if a == 5:
			break
	return output


# file = open("bstAll.txt", "r")	
# bst = readBST(file, {})
# file.close()
error = 1

import turtle
def resistor(value):
    turtle.speed('fastest')
    turtle.down()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.up()
    turtle.backward(50)
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(15)
    turtle.up()
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    turtle.write(str(value) +' Ω')
    turtle.up()
    turtle.backward(30)
    turtle.right(90)
    turtle.backward(35)
    turtle.left(90)
    turtle.forward(110)

def series(lst):
    for i in lst:
        resistor(i)

def parallel(lst):
        p1 = len(lst)//2
        p2 = len(lst) - len(lst)//2
        turtle.down()
        turtle.forward(50)
        if len(lst) == 2:
                turtle.left(90)
                turtle.forward(50)
                turtle.right(90)
                resistor(lst[0])
                turtle.down()
                turtle.right(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.up()
                turtle.backward(160)
                turtle.down()
                turtle.right(90)
                turtle.forward(50)
                turtle.left(90)
                resistor(lst[1])
                turtle.down()
                turtle.left(90)
                turtle.forward(50)
                turtle.right(90)
                turtle.forward(50)
        else:
                for i in range(p1):
                        turtle.down()
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                        resistor(lst[i])
                        turtle.right(90)
                        turtle.down()
                        turtle.forward(50)
                        turtle.up()
                        turtle.backward(50)
                        turtle.left(90)
                        turtle.backward(160)
                turtle.right(90)
                turtle.forward(p1*50)
                turtle.left(90)
                turtle.down()
                resistor(lst[p1])
                turtle.backward(160)
                for i in range(p2-1):
                        turtle.down()
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                        resistor(lst[i+p1])
                        turtle.down()
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                        turtle.up()
                        turtle.backward(160)
                turtle.left(90)
                turtle.forward((p2-2)*50)
                turtle.right(90)
                turtle.up()
                turtle.forward(160)
                turtle.down()
                turtle.forward(50)

def c_4(lst):
        turtle.down()
        turtle.forward(50)
        for i in lst:
                turtle.down()
                if type(i) == list:
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                        series(i)
                        turtle.down()
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                else:
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                        turtle.forward(80)
                        resistor(i)
                        turtle.down()
                        turtle.forward(80)
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                turtle.up()
                turtle.backward(320)
        turtle.forward(320)
        turtle.down()
        turtle.forward(50)

def c_3(lst):
        for i in lst:
                if type(i) == list:
                        c_4(i)
                else:
                        turtle.down()
                        resistor(i)

def c_6(lst):
        turtle.down()
        turtle.forward(50)
        flag = False
        for i in lst:
                turtle.down()
                if type(i) == list:
                        print(1)
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                        series(i)
                        turtle.down()
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                else:
                        if flag ==  False:
                                flag = True
                                turtle.right(90)
                                turtle.forward(50)
                                turtle.left(90)
                                turtle.forward(80)
                                resistor(i)
                                turtle.down()
                                turtle.forward(80)
                                turtle.left(90)
                                turtle.forward(50)
                                turtle.right(90)
                        else:
                                break
                turtle.up()
                turtle.backward(320)
        turtle.down()
        turtle.forward(80)
        resistor(lst[2])
        turtle.down()
        turtle.forward(80)
        turtle.up()
        turtle.backward(320)
        turtle.forward(320)
        turtle.down()
        turtle.forward(50)

def c_9(lst):
        turtle.down()
        turtle.forward(50)
        flag = False
        for i in lst:
                turtle.down()
                if flag == False:
                        flag =  True
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                        series(i)
                        turtle.down()
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                else:
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                        series(i)
                        turtle.down()
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                turtle.up()
                turtle.backward(320)
        turtle.forward(320)
        turtle.down()
        turtle.forward(50)
                
def c_7(lst):
        for i in lst:
                parallel(i)

def c_5(lst):
        turtle.down()
        turtle.forward(50)
        for i in lst:
                turtle.down()
                if type(i) == list:
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                        series(i)
                        turtle.down()
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                else:
                        turtle.right(90)
                        turtle.forward(50)
                        turtle.left(90)
                        turtle.forward(160)
                        resistor(i)
                        turtle.down()
                        turtle.forward(160)
                        turtle.left(90)
                        turtle.forward(50)
                        turtle.right(90)
                turtle.up()
                turtle.backward(480)
        turtle.forward(480)
        turtle.down()
        turtle.forward(50)


def combinations(lst):
        if lst[0][0] ==  '(':
            lst.append('c_9')

        elif lst[1] == 'series':
                if len(lst) == 4:
                        lst.append('s_1')
                elif lst[4] == 'series':
                        if len(lst) == 7:
                                lst.append('s_1')
                        elif lst[7] == 'series':
                                if len(lst) == 10:
                                        lst.append('s_1')
                        else:
                                if len(lst) == 10:
                                        lst.append('c_1')
                else:
                        if len(lst) == 7:
                                lst.append('c_2')
                        
                        elif lst[7] == 'series':
                                if len(lst) == 10:
                                        lst.append('c_3')
                        else:
                                if len(lst) == 10:
                                        lst.append('c_8')
        elif lst[1] == 'parallel':
                if len(lst) == 4:
                        lst.append('p_1')
                elif lst[4] == 'parallel':
                        if len(lst) == 7:
                                lst.append('p_1')
                        elif lst[7] == 'parallel':
                                if len(lst) == 10:
                                        lst.append('p_1')
                        else:
                                if len(lst) == 10:
                                        lst.append('c_6')
                else:
                        if len(lst) == 7:
                                lst.append('c_4')
                        elif lst[7] == 'series':
                                if len(lst) == 10:
                                        lst.append('c_5')
                        else:
                                if len(lst) == 10:
                                        lst.append('c_7')

        return lst
                        
def lst_combinations(lst):
        turtle.speed('fastest')
        turtle.resetscreen()
        turtle.up()
        turtle.backward(600)
        orient = len(lst)//2
        orient2 = len(lst) - orient
        c = 0
        if lst[0] == "Sorry, no combinations exist, please try some other value." :
            return
        for i in lst:
                c += 1
                if c == 1:
                        turtle.up()
                        turtle.left(90)
                        turtle.forward(200)
                        turtle.right(90)
                elif c == 3:
                        turtle.up()
                        turtle.sety(0)
                        turtle.setx(0)
                        turtle.backward(600)
                        turtle.right(90)
                        turtle.forward(200)
                        turtle.left(90)

                if i[1] == '0':
                        resistor(i[0])
                else:
                        f_l = i[1].split()
                        p = combinations(f_l)
                        lst1 = []
                        lst2 = []
                        lst3 = []
                        turtle.up()
                        turtle.forward(30)
                        if p[-1] == 's_1' or p[-1] == 'p_1':
                                for j in range(len(p)-1):
                                        if j == 0 or j == 3 or j == 6 or j == 9:
                                                lst1.append(p[j])
                                if p[-1] == 's_1':
                                        series(lst1)
                                else:
                                       parallel(lst1)
                        elif p[-1] == 'c_1':
                                for j in range(len(p)-1):
                                        if j == 0 or j == 1:
                                                lst1.append(p[j])
                                        elif j == 3 or j == 6:
                                                lst2.append(p[j])
                                series(lst1)
                                parallel(lst2)
                        elif p[-1] == 'c_2':
                                for j in range(len(p)-1):
                                        if j == 0:
                                                lst1.append(p[j])
                                        elif j == 3 or j == 6:
                                                lst2.append(p[j])
                                series(lst1)
                                parallel(lst2)
                        elif p[-1] == 'c_3':
                                for j in range(len(p)-1):
                                        if j == 0:
                                                lst1.append(p[j])
                                        elif j == 3:
                                                lst2.append(p[j])
                                        elif j == 6 or j == 9:
                                                lst3.append(p[j])
                                lst2.append(lst3)
                                lst1.append(lst2)
                                c_3(lst1)
                        elif p[-1] == 'c_4' or p[-1] == 'c_5':
                                for j in range(len(p)-1):
                                        if j == 0:
                                                lst1.append(p[j])
                                        elif j == 3 or j == 6 or j == 9:
                                                lst2.append(p[j])
                                lst1.append(lst2)
                                if p[-1] == 'c_4':
                                        c_4(lst1)
                                else:
                                        c_5(lst1)
                        elif p[-1] == 'c_6':
                                for j in range(len(p)-1):
                                        if j == 0 and j == 3:
                                                lst1.append(p[j])
                                        elif j == 6 and j == 9:
                                                lst2.append(p[j])
                                lst3.append(lst2)
                                lst3.append(lst1)
                                c_6(lst3)
                        elif p[-1] == 'c_7':
                                for j in range(len(p)-1):
                                        if j == 0 or j == 3:
                                                lst1.append(p[j])
                                        elif j == 6 or j == 9:
                                                lst2.append(p[j])
                                lst3.append(lst1)
                                lst3.append(lst2)
                                c_7(lst3)
                        elif p[-1] == 'c_8':
                                for j in range(len(p)-1):
                                        if j == 0:
                                                lst1.append(p[j])
                                        elif j == 3 or j == 6 or j == 9:
                                                lst2.append(p[j])
                                series(lst1)
                                parallel(lst2)
                        else:
                                for j in range(len(p)-1):
                                        if j == 0 or j == 3:
                                                lst1.append(p[j])
                                        elif j == 6 or j == 9:
                                                lst2.append(p[j])
                                lst3.append(lst1)
                                lst3.append(lst2)
                                c_9(lst3)

from tkinter import *
window=Tk()
window.title("ElectrΩhm")
window.configure(background='white')

textentry1=Entry(window, width=40, bg='white')
textentry=Entry(window, width=40, bg='white')
textentry2=Entry(window, width=40, bg='white')

def click5():
    output=Text(window, width=70, height=6, wrap=WORD, background='white')
    output.grid(row=13, column=2, columnspan=2, sticky=W)
    output.delete(0.0, END)
    file = open("bstAll.txt", "r")  
    bst = readBST(file, {})
    file.close()
    error = 1
    a=float(textentry.get())
    lst=bestR(a, bst, error)
    Label (window, text='\n Here is the best possible Combination(s): \n', bg='white', fg='black', font='none 12 bold').grid(row=12, column=2, sticky=W)
    for i in lst:
        output.insert(END, str(i) + "\n")
    lst_combinations(lst)
        

def click4():
    output=Text(window, width=70, height=6, wrap=WORD, background='white')
    output.grid(row=13, column=2, columnspan=2, sticky=W)
    output.delete(0.0, END)
    a=float(textentry2.get())
    lst=bestR(a, bst, error)
    Label (window, text='\n Here is the best possible Combination(s): \n', bg='white', fg='black', font='none 12 bold').grid(row=12, column=2, sticky=W)
    for i in lst:
        output.insert(END, str(i) + "\n")
    lst_combinations(lst)

def click3():
    lst=textentry1.get()
    lst= lst.split()
    x = [int(i) for i in lst]
    resistances = ResistanceCombination(x)
    global error
    error = 5
    global bst
    bst = {}
    for i in resistances:
	    insert(bst, i)
    Label (window, text='Enter Desired Value of Resistance:', bg='white', fg='black', font='none 12 bold').grid(row=10, column=0, sticky=W)
    textentry2.grid(row=10, column=2, sticky=W)
    Button(window, text='Submit', width=10, command=click4).grid(row=10, column=3, sticky=W)
    
    
    
    
    
def click1():
    Label (window, text='\n\n\n You Chose Option 1! ', bg='white', fg='black', font='none 12 bold').grid(row=7, column=0, sticky=W)
    Label (window, text='Enter Desired Value of Resistance:', bg='white', fg='black', font='none 12 bold').grid(row=8, column=0, sticky=W)
    textentry.grid(row=8, column=2, sticky=W)
    Button(window, text='Submit', width=10, command=click5).grid(row=8, column=3, sticky=W)

def click2():
    Label (window, text='\n\n\n You Chose Option 2! \n\n', bg='white', fg='black', font='none 12 bold').grid(row=5, column=0, sticky=W)
    Label (window, text='Please Enter Resistor Values Separated by Spaces: ', bg='white', fg='black', font='none 12 bold').grid(row=6, column=0, sticky=W)
    textentry1.grid(row=6, column=2, sticky=W)
    Button(window, text='Submit List', width=10, command=click3).grid(row=6, column=3, sticky=W)
    

        

    

photo1=PhotoImage(file="Capture.PNG")
Label (window, image=photo1).grid(row=0, column=2, sticky=W)


Label (window, text='\n\n\nPlease any one Button to Continue:', bg='white', fg='black', font='none 12 bold').grid(row=2, column=0, sticky=W)


Button(window, text='Use E12 Standard Resistors', width=30, command=click1).grid(row=3, column=2, sticky=W)

Button(window, text='Use your own list of Resistors', width=30, command=click2).grid(row=4, column=2, sticky=W)


turtle.exitonclick()

window.mainloop()
 
