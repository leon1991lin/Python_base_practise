#剪刀 石頭 布¶
#使用者出拳，電腦隨機出拳，比較輸贏並輸出結果
 
from random import choice
 
dict1 = {"剪刀":1, "石頭":2, "布":3}
user_1 = input("請輸入你要出的拳:")
user_2 = choice(["剪刀", "石頭", "布"])
 
 
if (dict1[user_1] == 1 and dict1[user_2] == 2) or (dict1[user_1] == 2 and dict1[user_2] == 3) or (dict1[user_1] == 3 and dict1[user_2] == 1) :
   
    print("你出 {},電腦出 {},你輸了!".format(user_1, user_2 ))
    
elif (dict1[user_1] == 1 and dict1[user_2]  == 3) or (dict1[user_1] == 2 and dict1[user_2]  == 1) or (dict1[user_1] == 3 and dict1[user_2]  == 2):

    print("你出 {},電腦出 {},你贏了!".format(user_1, user_2 ))
    
else:    
    print("你出 {},電腦也出 {},本局平手!".format(user_1, user_2 ))
