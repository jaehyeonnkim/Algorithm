from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

result = 0
for card in combinations(card_list,3):
    total = sum(card)
    if total <= M:
        result = max(result, total)
print(result)
