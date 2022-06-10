lst=[10,18,22,27,30,47,56,68,150,180,220,270,330,390,470,1000,1200,1500,2200,3300,4700,5600,6800,7500,8200,10000,20000,22000,33000,47000,100000,680000,820000,100000,2200000]
print(len(lst))
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
                             str(RSS[i][2]) + ' parallel with ' + str(RSS[j][2])])
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
                    [R[i][0] + RSSS[j][0], R[i][1] + RSSS[j][1], str(R[i][2]) + ' series with ' + str(RSSS[j][2])])
                CheckDuplicate.append(R[i][0] + RSSS[j][0])

    AllCombo = R + RSS + RPP + RSSS + RPPP + RSSP + RPPS + RSPPP + RPPSS + RSPSS + RPPSPP + RSSSP + RPPPP + RSSSS + RSSPSS
    return(AllCombo)
Final = ResistanceCombination(lst)
R = open("resistors2.txt", "w")
for i in Final:
    a = str(i[0])
    b = str(i[1])
    R.write(a)
    R.write("\\")
    R.write(b)
    R.write("\\")
    R.write(str(i[2]))
    R.write("\n")
R.close()