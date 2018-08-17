

ger_eng={"red":"rot","green":"grun","blue":"balu","yellow":"gelb"}
print(ger_eng)
print(ger_eng["red"])
der_fr={"rot":"rouge","grun":"vert","balu":"bleu","gelb":"jaune"}
print("French word for red from german word is :"+"" +der_fr[ger_eng["red"]])
dictionaries={"english":ger_eng,"french":der_fr}
print(dictionaries)
print(dictionaries["french"])
print(dictionaries["english"]["green"])
print(ger_eng.items())
#dictionary values to list : sperating key value pair
print(ger_eng.keys())
print(ger_eng.values())
#ways to iterarte over dictionary : printinh key, value, key-value pair
for key in ger_eng:
    print("{}:{}".format(key,ger_eng[key]))
    print(ger_eng[key])
    print(key)
for value in der_fr.values():
    print(value)
for key,value in ger_eng.items():
    print("{}:{}".format(key,value))
print(len(ger_eng))
print(len(der_fr))
if "red" in ger_eng:print(ger_eng["red"])
#.copy() to copy dictionary
german=ger_eng.copy()
print(german)

a={1:"a",2:"b",3:"c"}
b={4:"d",5:"r",6:"g"}
a.update(b) # merging two dictionaries
c={1:1,6:8,0:6,9:67}
lst=[]
for key in c:
    print(lst.append(c[key]))
#combining two lists and then converting it to dictionary    
dishes=["pizza","noodles","upma","coffee","icecream"]
cost=[200,89,90,87,199]
menu=zip(dishes,cost)
final=dict(menu)
print(final)    