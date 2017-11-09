import numpy as np
import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

suit_number_list = list(range(1, 5))
card_number_list = list(range(1, 14))

file = raw_input("Indicate file name that you would like to add: ")
print("Reading training file")
df = pd.read_csv(str(file))
counts = df['hand'].value_counts().to_dict()
print(counts)
one = raw_input("Indicate how much more 1 you would like to add: ")
two = raw_input("Indicate how much more 2 you would like to add: ")
three = raw_input("Indicate how much more 3 you would like to add: ") 
four = raw_input("Indicate how much more 4 you would like to add: ")
five = raw_input("Indicate how much more 5 you would like to add ")
six = raw_input("Indicate how much more 6 you would like to add: ")
seven = raw_input("Indicate how much more 7 you would like to add: ")
eight = raw_input("Indicate how much more 8 you would like to add: ")
nine = raw_input("Indicate how much more 9 you would like to add: ")

output = raw_input("Output file name: ")

print("Creating more data for one pair")
for i in range(0, int(one)):
    temp_num_list = card_number_list[:]
    num1 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num1[0])
    num3 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num3[0])
    num4 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num4[0])
    num5 = random.sample(temp_num_list, 1)
    temp_suit_list = suit_number_list[:]
    suit1 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(suit1[0])
    suit2 = random.sample(temp_suit_list, 1)
    one_pair_dict = {1 :(num1, suit1),
                     2 :(num1, suit2),
                     3 :(num3, random.sample(suit_number_list, 1)),
                     4 :(num4, random.sample(suit_number_list, 1)),
                     5 :(num5, random.sample(suit_number_list, 1))}
    
    cards = list(range(1, 6))
    df_one_pair_dict ={}

    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_one_pair_dict['S1'] = one_pair_dict[c1[0]][1]
    df_one_pair_dict['C1'] = one_pair_dict[c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_one_pair_dict['S2'] = one_pair_dict[c2[0]][1]
    df_one_pair_dict['C2'] = one_pair_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_one_pair_dict['S3'] = one_pair_dict[c3[0]][1]
    df_one_pair_dict['C3'] = one_pair_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_one_pair_dict['S4'] = one_pair_dict[c4[0]][1]
    df_one_pair_dict['C4'] = one_pair_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_one_pair_dict['S5'] = one_pair_dict[c5[0]][1]
    df_one_pair_dict['C5'] = one_pair_dict[c5[0]][0]

    df_one_pair_dict['hand'] = 1
    one_pair= pd.DataFrame.from_dict(df_one_pair_dict)
    one_pair = one_pair[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new one pair data:")
    print(one_pair)
    df= df.append(one_pair)

print("Creating more data for Two Pair")
for i in range(0, int(two)):
    temp_num_list = card_number_list[:]
    num1to2 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num1to2[0])
    num3to4 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num3to4[0])
    num5 = random.sample(temp_num_list, 1)

    temp_suit_list = suit_number_list[:]
    suit1 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(suit1[0])
    suit2 = random.sample(temp_suit_list, 1)

    temp_suit_list = suit_number_list[:]
    suit3 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(suit3[0])
    suit4 = random.sample(temp_suit_list, 1)
    
    two_pair_dict = {1 :(num1to2, suit1),
                     2 :(num1to2, suit2),
                     3 :(num3to4, suit3),
                     4 :(num3to4, suit4),
                     5 :(num5, random.sample(suit_number_list, 1))}
    
    cards = list(range(1, 6))
    df_two_pair_dict ={}

    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_two_pair_dict['S1'] = two_pair_dict[c1[0]][1]
    df_two_pair_dict['C1'] = two_pair_dict[c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_two_pair_dict['S2'] = two_pair_dict[c2[0]][1]
    df_two_pair_dict['C2'] = two_pair_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_two_pair_dict['S3'] = two_pair_dict[c3[0]][1]
    df_two_pair_dict['C3'] = two_pair_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_two_pair_dict['S4'] = two_pair_dict[c4[0]][1]
    df_two_pair_dict['C4'] = two_pair_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_two_pair_dict['S5'] = two_pair_dict[c5[0]][1]
    df_two_pair_dict['C5'] = two_pair_dict[c5[0]][0]

    df_two_pair_dict['hand'] = 2
    two_pair= pd.DataFrame.from_dict(df_two_pair_dict)
    two_pair = two_pair[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new two pairs data:")
    print(two_pair)
    df= df.append(two_pair)


print("Creating more data for Three of a kind")
for i in range(0, int(three)):
    temp_num_list = card_number_list[:]
    num1to2to3 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num1to2to3[0])
    num4 = random.sample(temp_num_list, 1)
    temp_num_list.remove(num4[0])
    num5 = random.sample(temp_num_list, 1)

    temp_suit_list = suit_number_list[:]
    suit1 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(suit1[0])
    suit2 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(suit2[0])
    suit3 = random.sample(temp_suit_list, 1)

    three_kind_dict = {1 :(num1to2to3, suit1),
                     2 :(num1to2to3, suit2),
                     3 :(num1to2to3, suit3),
                     4 :(num4, random.sample(suit_number_list, 1)),
                     5 :(num5, random.sample(suit_number_list, 1))}
    
    cards = list(range(1, 6))
    df_three_kind_dict ={}

    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_three_kind_dict['S1'] = three_kind_dict[c1[0]][1]
    df_three_kind_dict['C1'] = three_kind_dict[c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_three_kind_dict['S2'] = three_kind_dict[c2[0]][1]
    df_three_kind_dict['C2'] = three_kind_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_three_kind_dict['S3'] = three_kind_dict[c3[0]][1]
    df_three_kind_dict['C3'] = three_kind_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_three_kind_dict['S4'] = three_kind_dict[c4[0]][1]
    df_three_kind_dict['C4'] = three_kind_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_three_kind_dict['S5'] = three_kind_dict[c5[0]][1]
    df_three_kind_dict['C5'] = three_kind_dict[c5[0]][0]

    df_three_kind_dict['hand'] = 3
    three_kind= pd.DataFrame.from_dict(df_three_kind_dict)
    three_kind = three_kind[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new three of a kind data:")
    print(three_kind)
    df= df.append(three_kind)

print("Creating data for Straight")
for i in range(0, int(four)):
    temp_suit_list = suit_number_list[:]
    suit1 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(suit1[0])

    c_num = list(range(1, 10))
    c = random.sample(c_num, 1)
    kind = random.sample(suit_number_list, 1)
    straight_dict = {1 :(c[0], suit1),
                     2 :(c[0]+1, random.sample(suit_number_list, 1)),
                     3 :(c[0]+2, random.sample(suit_number_list, 1)),
                     4 :(c[0]+3, random.sample(suit_number_list, 1)),
                     5 :(c[0]+4, random.sample(suit_number_list, 1))}

    cards = list(range(1, 6))
    df_straight_dict ={}

    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_straight_dict['S1'] = straight_dict[c1[0]][1]
    df_straight_dict['C1'] = straight_dict[c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_straight_dict['S2'] = straight_dict[c2[0]][1]
    df_straight_dict['C2'] = straight_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_straight_dict['S3'] = straight_dict[c3[0]][1]
    df_straight_dict['C3'] = straight_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_straight_dict['S4'] = straight_dict[c4[0]][1]
    df_straight_dict['C4'] = straight_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_straight_dict['S5'] = straight_dict[c5[0]][1]
    df_straight_dict['C5'] = straight_dict[c5[0]][0]

    df_straight_dict['hand'] = 4
    straight= pd.DataFrame.from_dict(df_straight_dict)
    straight = straight[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new straight data:")
    print(straight)
    df= df.append(straight)

print("Creating more data for Flush")
flush_dict = {}
for i in range(0, int(five)):
    suit_number = random.sample(suit_number_list, 1)
    flush_dict['S1'] = suit_number
    flush_dict['S2'] = suit_number
    flush_dict['S3'] = suit_number
    flush_dict['S4'] = suit_number
    flush_dict['S5'] = suit_number

    temp_card_number = card_number_list[:]
    card = random.sample(temp_card_number, 1)
    temp_card_number.remove(card[0])
    flush_dict['C1'] = card
    card = random.sample(temp_card_number, 1)
    temp_card_number.remove(card[0])
    flush_dict['C2'] = card
    card = random.sample(temp_card_number, 1)
    temp_card_number.remove(card[0])
    flush_dict['C3'] = card
    card = random.sample(temp_card_number, 1)
    temp_card_number.remove(card[0])
    flush_dict['C4'] = card
    card = random.sample(temp_card_number, 1)
    temp_card_number.remove(card[0])
    flush_dict['C5'] = card
    flush_dict['hand'] = 5
    flush = pd.DataFrame.from_dict(flush_dict)
    
    flush = flush[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new flush data:")
    print(flush)
    df= df.append(flush)
    
print("\nCreating more data for Full house")
for x in range(0, int(six)):
    # same card number, but 2 different suit
    card_number1 = random.sample(card_number_list, 1)
    temp_suit_list =  suit_number_list[:]
    c1_s1 = random.sample(suit_number_list, 1)
    temp_suit_list.remove(c1_s1[0])
    c1_s2 = random.sample(temp_suit_list, 1)

    # different card number as above, but 3 different suit
    temp_card_number = card_number_list[:]  
    temp_card_number.remove(card_number1[0])
    card_number2 = random.sample(temp_card_number, 1)

    c2_s1 = random.sample(suit_number, 1)
    temp_suit_list = suit_number_list[:]
    temp_suit_list.remove(c2_s1[0])
    c2_s2 = random.sample(temp_suit_list, 1)
    temp_suit_list.remove(c2_s2[0])
    c2_s3 = random.sample(temp_suit_list, 1)

    full_house_dict = {1 :(card_number1, c1_s1),
                       2 :(card_number1, c1_s2),
                       3 :(card_number2, c2_s1),
                       4 :(card_number2, c2_s2),
                       5 :(card_number2, c2_s3)}

    cards = list(range(1, 6))
    df_full_house_dict ={}

    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_full_house_dict['S1'] = full_house_dict[c1[0]][1]
    df_full_house_dict['C1'] = full_house_dict[c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_full_house_dict['S2'] = full_house_dict[c2[0]][1]
    df_full_house_dict['C2'] = full_house_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_full_house_dict['S3'] = full_house_dict[c3[0]][1]
    df_full_house_dict['C3'] = full_house_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_full_house_dict['S4'] = full_house_dict[c4[0]][1]
    df_full_house_dict['C4'] = full_house_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_full_house_dict['S5'] = full_house_dict[c5[0]][1]
    df_full_house_dict['C5'] = full_house_dict[c5[0]][0]

    df_full_house_dict['hand'] = 6
    full_house = pd.DataFrame.from_dict(df_full_house_dict)
    full_house = full_house[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new full house data:")
    print(full_house)
    df= df.append(full_house)

print("\nCreating more data for Four of a kind")
for x in range(0, int(seven)):
    # get card number 1 and 2
    four_kind_dict = {}
    df_four_kind_dict = {}
    temp_card_number_list = card_number_list[:]
    c1 = random.sample(temp_card_number_list, 1)
    temp_card_number_list.remove(c1[0])
    c2 = random.sample(temp_card_number_list, 1)
    temp_card_number_list.remove(c2[0])

    # randomly choose card number 1 and 2 for four of a kind
    card_range= range(1, 6)
    card_num = random.sample(card_range, 1)

    temp_suit_number_list = suit_number_list[:]
    for i in range(1, 6):
        if(i == card_num[0]):
            four_kind_dict[i] = c2, random.sample(suit_number_list, 1)
        else:
            suit_number = random.sample(temp_suit_number_list, 1)
            temp_suit_number_list.remove(suit_number[0])
            four_kind_dict[i] = c1, suit_number

    df_four_kind_dict['S1'] = four_kind_dict[1][1]
    df_four_kind_dict['C1'] = four_kind_dict[1][0]
    df_four_kind_dict['S2'] = four_kind_dict[2][1]
    df_four_kind_dict['C2'] = four_kind_dict[2][0]
    df_four_kind_dict['S3'] = four_kind_dict[3][1]
    df_four_kind_dict['C3'] = four_kind_dict[3][0]
    df_four_kind_dict['S4'] = four_kind_dict[4][1]
    df_four_kind_dict['C4'] = four_kind_dict[4][0]
    df_four_kind_dict['S5'] = four_kind_dict[5][1]
    df_four_kind_dict['C5'] = four_kind_dict[5][0]
    df_four_kind_dict['hand'] = 7
    four_kind = pd.DataFrame.from_dict(df_four_kind_dict)
    four_kind = four_kind[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new four of a kind:")
    print(four_kind)
    df= df.append(four_kind)
    
print("\nCreating more data for Straight Flush")
for i in range(0, int(eight)):
    c_num = list(range(1, 9))
    c = random.sample(c_num, 1)
    kind = random.sample(suit_number_list, 1)
    straight_flush_dict = {1 :(c[0], kind),
                           2 :(c[0]+1, kind),
                           3 :(c[0]+2, kind),
                           4 :(c[0]+3, kind),
                           5 :(c[0]+4, kind)}

    cards = list(range(1, 6))
    df_straight_flush_dict ={}

    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_straight_flush_dict['S1'] = straight_flush_dict[c1[0]][1]
    df_straight_flush_dict['C1'] = straight_flush_dict[c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_straight_flush_dict['S2'] = straight_flush_dict[c2[0]][1]
    df_straight_flush_dict['C2'] = straight_flush_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_straight_flush_dict['S3'] = straight_flush_dict[c3[0]][1]
    df_straight_flush_dict['C3'] = straight_flush_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_straight_flush_dict['S4'] = straight_flush_dict[c4[0]][1]
    df_straight_flush_dict['C4'] = straight_flush_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_straight_flush_dict['S5'] = straight_flush_dict[c5[0]][1]
    df_straight_flush_dict['C5'] = straight_flush_dict[c5[0]][0]

    df_straight_flush_dict['hand'] = 8
    straight_flush = pd.DataFrame.from_dict(df_straight_flush_dict)
    straight_flush = straight_flush[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new straight flush data:")
    print(straight_flush)
    df= df.append(straight_flush)

print("\nCreating Royal Flush")

for i in range(0, int(nine)):
    #generate a random suit
    suit = random.sample(suit_number_list, 1)
    royal_flush_dict = {1 :([10], suit[0]),
                        2 :([11], suit[0]),
                        3 :([12], suit[0]),
                        4 :([13], suit[0]),
                        5 :([1], suit[0])}
    cards = list(range(1, 6))
    df_royal_flush_dict  ={}
    c1 = random.sample(cards, 1)
    cards.remove(c1[0])
    df_royal_flush_dict['S1'] = royal_flush_dict [c1[0]][1]
    df_royal_flush_dict['C1'] = royal_flush_dict [c1[0]][0]

    c2 = random.sample(cards, 1)
    cards.remove(c2[0])
    df_royal_flush_dict['S2'] = royal_flush_dict[c2[0]][1]
    df_royal_flush_dict['C2'] = royal_flush_dict[c2[0]][0]

    c3 = random.sample(cards, 1)
    cards.remove(c3[0])
    df_royal_flush_dict['S3'] = royal_flush_dict[c3[0]][1]
    df_royal_flush_dict['C3'] = royal_flush_dict[c3[0]][0]

    c4 = random.sample(cards, 1)
    cards.remove(c4[0])
    df_royal_flush_dict['S4'] = royal_flush_dict[c4[0]][1]
    df_royal_flush_dict['C4'] = royal_flush_dict[c4[0]][0]

    c5 = random.sample(cards, 1)
    cards.remove(c5[0])
    df_royal_flush_dict['S5'] = royal_flush_dict[c5[0]][1]
    df_royal_flush_dict['C5'] = royal_flush_dict[c5[0]][0]
    df_royal_flush_dict['hand'] = 9
    royal_flush = pd.DataFrame.from_dict(df_royal_flush_dict)
    royal_flush = royal_flush[['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand']]
    print("Inserting new royal flush:")
    print(royal_flush)
    df= df.append(royal_flush)

print("\nProducing csv file of train with predict result:")
df.to_csv(str(output),mode = 'w', index=False)
print(str(output) + ' is made')
counts = df['hand'].value_counts().to_dict()
print(counts)
