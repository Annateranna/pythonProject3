example = input()
n = int(input())
vowels = 'ауоыиэяюёе'
example_vowels = [i for i, v in enumerate(example) if v in vowels]
for i in range(n):
    word = input()
    word_vowels = [j for j, v in enumerate(word) if v in vowels]
    if word_vowels == example_vowels:
        print(word)

