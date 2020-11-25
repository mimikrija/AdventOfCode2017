def unique(words):
    if len(set(words)) == len(words):
        return 1
    else:
        return 0

def no_anagrams(words):
    temp = []
    for word in words:
        anagram = "".join(sorted(word))
        temp.append(anagram)
    return unique(temp)

solution_1 = 0
solution_2 = 0

for line in open('inputs/04','r'):
    pass_phrase = line.split()
    solution_1 += unique(pass_phrase)
    solution_2 += no_anagrams(pass_phrase)

print("There are ", solution_1, "unique pass phrases!")
# There are  451 unique pass phrases!

print("There are ", solution_2, "pass phrases with no anagrams!")
# There are  223 pass phrases with no anagrams!