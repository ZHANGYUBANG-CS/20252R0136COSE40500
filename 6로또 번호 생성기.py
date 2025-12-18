import random

lotto = random.sample(range(1, 46), 6)
lotto.sort() # 오름차순 정렬
print(f"이번 주 추천 로또 번호: {lotto}")