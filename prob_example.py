from itertools import *
from sympy.stats import given, density, Die
import random

# 1. factorial
def fac(n):
    return n * fac(n-1) if n > 0 else 1

print("factorial 4 is",fac(4))


# 2. 6명 수강생 중 2명에게 순위별 상품을 주는 경우의 수
gift = ["가","나","다","라","마","바"]

# 2-1. permutation
rank_per = list(permutations(gift,2))
rank_per_num = len(rank_per)
print("gift permutation:",rank_per_num)


# 2-2. combination
rank_com = list(combinations(gift,2))
rank_com_num = len(rank_com)
print("gift combinations:",rank_com_num)


# 2-3. permutations
re_per = list(product(gift, repeat=3))
re_per_num = len(re_per)
print("gift permutations:",re_per_num)


# 2-4. combinations with replacement
re_com = list(combinations_with_replacement(gift, 3))
re_per_com = len(re_com)
print("gift combinations with replacement:",re_per_com)


# 3. conditional probability and independence
answer_Q1andQ2 = 0
answer_Q2 = 0
answer_Q1orQ2 = 0
random.seed(4)

def random_answer():
    return random.choice(["A","B"])

# 30명의 응답 결과
for i in range(30):
    Q1 = random_answer()
    Q2 = random_answer()
    if Q2 == "A":
        answer_Q2 += 1
    if Q2 == "A" and Q1 == "A":
        answer_Q1andQ2 += 1
    if Q2 == "A" or Q1 == "A":
        answer_Q1orQ2 += 1


print( "P(B|A):", answer_Q1andQ2/answer_Q2)
print( "P(B|O):", answer_Q1andQ2/answer_Q1orQ2)


# 4. Random variable
# 4-1. making Die with 6 dimensions
Die6 = Die('Die6', 6)
Die6_dict = density(Die6).dict
print("Die6_dict:",Die6_dict)

# 4-2. making Die with over three dimensions
condi = given(Die6, Die6 > 3)
condi_dict = density(condi).dict
print("condi_dict",condi_dict)




