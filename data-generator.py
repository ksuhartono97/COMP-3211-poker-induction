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

output = raw_input("Output file name: ")
print("Creating more data for Flush")
suit_number = random.sample(suit_number_list, 1)
flush_dict = {}
for i in range(0, 1000):
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
for x in range(0, 1000):
    # same card number, but 2 different suit
    card_number1 = random.sample(card_number_list, 1)
    c1_s1 = random.sample(suit_number_list, 1)
    temp_suit_list = suit_number_list[:]
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
for x in range(0, 1000):
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
for i in range(0, 1000):
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

for i in range(0, 1000):
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
