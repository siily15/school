thislist = ["ploom","õun","pirn"]
print(thislist)
#listi esiene väärtus
print(thislist[1])
#lisa lõppus uus puuvili
thislist.append("kirss")
print(thislist)
#väljasta listi viimane väärtus
print(thislist[3])
#muuda ühe elemendi väärtus ja väljesta kogu list
thislist = ("ploom","õun","pirn","kirss")
thislist = "banan"
print(thislist)
#kas õun ekstiteerib
thislist = ("ploom","õun","pirn","kirss")
if "õun" in thislist:
    print("õun on jah, puuvili")
#listi pikkus
thislist = ("ploom","õun","pirn","kirss")
print(len(thislist))
#eemalda element
thislist = ["ploom","õun","pirn","kirss"]
thislist.remove("õun")
print(thislist)
#listi järjekord
thislist = ["ploom","õun","pirn","kirss"]
thislist.reverse()
print(thislist)
#listi sorteerimine
thislist = ["ploom","õun","pirn","kirss"]
thislist.sort()
print(thislist)