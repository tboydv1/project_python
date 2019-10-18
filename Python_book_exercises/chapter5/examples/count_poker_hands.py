# counut poker hands
#1. open the poker data file for reading
file_str = input("Enter a file name: ")

while True:
    try:
        poker_file = open(file_str, 'r')
        break
    except FileNotFoundError:
        print("Error opening file:", file_str)
        file_str = input("Enter a file name: ")

# all counts are ints, so count as a suffix is enough
total_count = 0
nothing_count = 0
pair_count = 0
two_pair_count = 0
three_of_a_kind_count = 0
straight_count = 0
flush_count = 0
full_house_count = 0
four_of_a_kind_count = 0
straight_flush_count = 0
royal_flush_count = 0


# Loop through each line of file
for line_str in poker_file:
    total_count = total_count + 1
    fields = line_str.split(',')
    hand_rank_str = fields[-1]

    try:
        hand_rank_int = int(hand_rank_str)
    except ValueError:
        continue

    if hand_rank_int == 1:
        pair_count  = pair_count + 1
    elif hand_rank_int == 2:
        two_pair_count = two_pair_count + 1
    elif hand_rank_int == 3:
        three_of_a_kind_count = three_of_a_kind_count + 1
    elif hand_rank_int == 4:
        straight_count = straight_count + 1
    elif hand_rank_int == 5:
        flush_count += 1
    elif hand_rank_int == 6:
        full_house_count += 1
    elif hand_rank_int == 7:
        four_of_a_kind_count += 1
    elif hand_rank_int == 8:
        straight_flush_count += 1
    elif hand_rank_int == 9:
        royal_flush_count += 1
    else:
        nothing_count += 1



print("Total hands in file: ", total_count)
print("Hands counts by rank number: ", nothing_count, pair_count,
      two_pair_count,\
      three_of_a_kind_count, straight_count, flush_count, full_house_count, \
      four_of_a_kind_count, straight_flush_count, royal_flush_count)

print("Probability:")
print(" {:20} {:>15.4%}".format("of a nothing:",nothing_count/total_count))
print(" {:20} {:>15.4%}".format("of one pair:",pair_count/total_count))
print(" {:20} {:>15.4%}".format("of two pairs:",two_pair_count/total_count))
print(" {:20} {:>15.4%}".format("of three of a kind:",three_of_a_kind_count/total_count))
print(" {:20} {:>15.4%}".format("of a straight:",straight_count/total_count))
print(" {:20} {:>15.4%}".format("of a flush:",flush_count/total_count))
print(" {:20} {:>15.4%}".format("of a full house:",full_house_count/total_count))
print(" {:20} {:>15.4%}".format("of four of a kind:",four_of_a_kind_count/total_count))
print(" {:20} {:>15.4%}".format("of a royal flush:",royal_flush_count/total_count))
