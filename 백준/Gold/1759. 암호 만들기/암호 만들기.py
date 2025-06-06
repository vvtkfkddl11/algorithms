import sys
from itertools import combinations

vowels = []
consonants = []
temp = []
result = []

l, c = map(int, sys.stdin.readline().split())
alphas = map(str, sys.stdin.readline().split())

for i in alphas:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(i)
    else:
        consonants.append(i)

# 모음을 1개부터 (l-2)개까지 선택 가능 (자음이 최소 2개 필요하므로)
for vowel_count in range(1, min(len(vowels) + 1, l - 1)):
    consonant_count = l - vowel_count

    # 자음이 최소 2개 이상이어야 하고, 사용 가능한 자음 개수 이내여야 함
    if consonant_count >= 2 and consonant_count <= len(consonants):
        # 모음 조합들 생성
        vowel_combinations = list(combinations(vowels, vowel_count))

        # 자음 조합들 생성
        consonant_combinations = list(combinations(consonants, consonant_count))

        # 모음 조합과 자음 조합을 각각 합치기
        for vowel_combo in vowel_combinations:
            for consonant_combo in consonant_combinations:
                # 두 조합을 합치고 정렬
                password = sorted(list(vowel_combo) + list(consonant_combo))
                result.append(''.join(password))

result.sort()
for password in result:
    print(password)