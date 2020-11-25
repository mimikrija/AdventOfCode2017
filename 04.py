def has_unique(words):
    return len(set(words)) == len(words)

def no_anagrams(words):
    temp = []
    for word in words:
        anagram = []
        for c in word:
            anagram.append(c)
        anagram.sort()
        anagram= (''.join(anagram))
        temp.append(anagram)
    return has_unique(temp)

solution_1 = 0
solution_2 = 0

for line in open('inputs/04','r'):
    pass_phrase = line.split()
    if has_unique(pass_phrase):
        solution_1 += 1
        if no_anagrams(pass_phrase):
            solution_2 += 1

print("There are ", solution_1, "unique pass phrases!")
# There are  451 unique pass phrases!

print("There are ", solution_2, "pass phrases with no anagrams!")
# There are  223 pass phrases with no anagrams!