import numpy as np
import pandas as pd

#Global variable
suit = {'S1', 'S2', 'S3', 'S4', 'S5'}
rank = {'C1', 'C2', 'C3', 'C4', 'C5'}

#A function that is given a list it would count the number of n dupilciates of a rank. Used in one pair, three of a kind and four of a kind
def count_duplicate(l,n):
    for i in range (1, 14):
        if(l.count(i) == n):
            return True
    return False

#Given a ranks list l and uses the function count_duplicate to see if there is a pair
def is_one_pair(l):
    if(count_duplicate(l, 2)):
        return True
    return False

#Given a ranks list l and uses simular function as count_duplicate but this time has a counter that counts the number of times a rank is duplicated twice
def is_two_pair(l):
    count = 0;
    for i in range (1, 14):
        if(l.count(i) == 2):
            count = count + 1;
    if(count == 2):
        return True
    return False

#Given a ranks list l and uses the function count_duplicate to see if there is three of a kind.
def is_three_kind(l):
    if(count_duplicate(l, 3)):
        return True
    return False

#Sorts rank list l and then check if l is consecutive and considers a special case of card ranks with 10, 11, 12, 13, 1
def is_straight(l):
    l.sort()
    skip = False
    for i in range(1, len(l)):
        if(l[i-1] + 1 != l[i]):
            if(l[0] == 1 and l[1]== 10 and skip == False):
                skip= True
            else:
                return False
    return True;

#Loop through the suit list and check if all suits are the same
def is_flush(l):
    for i in range (1, 5):
        if(l[0] != l[i]):
            return False
    return True

#Puts the rank list into is_one_pair and is_three_kind to see if it is a full house
def is_full_house(l):
    if(is_one_pair(l) and is_three_kind(l)):
        return True
    return False

#Given a ranks list l and uses the function count_duplicate to see if there is four of the same rank
def is_four_kind(l):
    if(count_duplicate(l, 4)):
        return True
    return False

#Uses a ranks list l1 and put it in is_straight flush and a suit list l2 in is_flush to the function is_flush to see if it is straight flush
def is_straight_flush(l1, l2):
    if(is_straight(l1) and is_flush(l2)):
        return True
    return False

#checks if it is a royal flush through passing a suit list l2 into is_flush then using rank list l1 to determine if the ranks are 10, 11, 12, 13, 1
def is_royal_flush(l1, l2):
    if(is_flush(l2)):
        temp = {'1':0,'10':0,'11':0,'12':0,'13':0}
        temp[str(1)]= l1.count(1)
        for i in range (10, 14):
            temp[str(i)]= l1.count(i)
        for i in range (0, 4):
            if (temp[str(10+i)] == 0):
                break
            if(i == 3 and temp['1'] != 0):
                return True
    return False

def main():
    #Importing file to dataframe
    file_name = raw_input("Please insert file name: ")
    df = pd.read_csv(str(file_name))
    df = df.drop(['id'], axis = 1)
    df_rank = df.drop(suit, axis=1)
    df_suit = df.copy().drop(rank, axis=1)
    #A hand list to note down each hand's rank
    hand=[]
    for i in range (0, len(df)):
        if(is_royal_flush(df_rank.iloc[i].values.tolist(), df_suit.iloc[i].values.tolist())):
            print(str(i) + ": ROYAL FLUSH!")
            hand.append(9)
        
        elif (is_straight_flush(df_rank.iloc[i].values.tolist(), df_suit.iloc[i].values.tolist())):
            print(str(i) + ": STRAIGHT FLUSH!")
            hand.append(8)
        
        elif(is_four_kind(df_rank.iloc[i].values.tolist())):
            print(str(i) + ": FOUR OF A KIND!!")
            hand.append(7)
        
        elif(is_full_house(df_rank.iloc[i].values.tolist())):
            print(str(i) + ": FULL HOUSE!!")
            hand.append(6)

        elif(is_flush(df_suit.iloc[i].values.tolist())):
            print(str(i) + ": It's a FLUSH!")
            hand.append(5)
        
        elif(is_straight(df_rank.iloc[i].values.tolist())):
            print(str(i) + ": It's a STRAIGHT!")
            hand.append(4)

        elif(is_three_kind(df_rank.iloc[i].values.tolist())):
            print(str(i) + ": THREE OF A KIND!")
            hand.append(3)

        elif(is_two_pair(df_rank.iloc[i].values.tolist())):
            print(str(i) + ": TWO PAIR!")
            hand.append(2)

        elif(is_one_pair(df_rank.iloc[i].values.tolist())):
            print(str(i) + ": ONE PAIR!")
            hand.append(1)

        else:
            print(str(i) + ": Others")
            hand.append(0)
                
    output = raw_input("Please insert output file name: ")
    output_df = pd.DataFrame()
    #Inserting the hand list into dataframe
    output_df['hand'] = hand
    #Adding the id column back to the dataframe
    #NOTE: please edit the file and add the title 'id' manually
    output_df.index = np.arange(1,len(output_df)+1)
    output_df.to_csv(str(output))

main()
    
