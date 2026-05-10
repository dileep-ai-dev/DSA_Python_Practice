# Check Anagram
s = "listen"
t = "silent"

if sorted(s) == sorted(t):
    print("Anagram: True")
else:
    print("Anagram: False")


# First non-repeating character
word = "leetcode"

for ch in word:
    if word.count(ch) == 1:
        print("First non-repeating:", ch)
        break


# Palindrome check
p = "madam"
if p == p[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")


# Vowels and consonants count
text = "dileep"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)