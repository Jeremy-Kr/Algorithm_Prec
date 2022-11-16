# 다시 풀기

# t, target_num = map(int,input().split())
# card_list = list(map(int,input().split()))
# sum_cards = []
# sum_card = 0
# temp_sum = 0
# sum_card_idx = 0
# if t == 3:
#     print(sum(card_list))

# for i in range(len(card_list)):
#     for j in range(len(card_list)):
#         for k in range(len(card_list)):
#             sum_cards.append(card_list[i]+card_list[j]+card_list[k])

# new_card_list = sorted(set(sum_cards))

# if len(new_card_list) > 3:
#     while (sum_card <= target_num):
#         sum_card = new_card_list[sum_card_idx]
#         sum_card_idx += 1

#     print(new_card_list[sum_card_idx-2])
# else: sum(card_list)