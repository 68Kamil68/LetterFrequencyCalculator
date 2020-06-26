import matplotlib.pyplot as plt

consonants = {'b': 0, 'c': 0, 'ć': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0,
              'l': 0, 'ł': 0, 'm': 0, 'n': 0, 'p': 0, 'r': 0, 's': 0, 't': 0, 'w': 0, 'z': 0, 'ź': 0, 'ż': 0}

vowels = {'a': 0, 'ą': 0, 'e': 0, 'ę': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0, 'ó': 0}

with open("dictionary.txt") as f:
    for line in f:
        for letter in line.lower():
            if letter in consonants.keys():
                consonants[letter] += 1
            elif letter in vowels.keys():
                vowels[letter] += 1


sorted_consonants = dict(sorted(consonants.items(), key=lambda x: x[1]))
sorted_vowels = dict(sorted(vowels.items(), key=lambda x: x[1]))


plt.bar(sorted_consonants.keys(), sorted_consonants.values(), color='r')
plt.show()
plt.bar(sorted_vowels.keys(), sorted_vowels.values(), color='g')
plt.show()
plt.bar(['vowels', 'consonants'], [sum(sorted_vowels.values()), sum(sorted_consonants.values())])
plt.show()

