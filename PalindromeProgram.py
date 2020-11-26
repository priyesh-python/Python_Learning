#1. Palindrome check - "Palindrome"/"Not Palindrome"

def palindrome_check(str):
    #rev = ''.join(reversed(s))

    reversed_str_arr = []
    reversed_str = ""
    index = len(str)
    while index > 0:
        reversed_str_arr += str[index - 1]
        index = index - 1
    #print(reversed_str_arr)

    for i in reversed_str_arr:
        reversed_str += i
    #print(reversed_str)
    if (str == reversed_str):
        return True
    return False

s = input("Please Input a word: ")
ans = palindrome_check(s)
if (ans):
    print("It is Palindrome")
else:
    print("Not a palindrome")



# 3. Occurence of each character - malayalam - {"a": 4, "m": 2, "l": 2, "y": 1}

s_arr = list(s)
all_freq = {}

for i in s_arr:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(str(all_freq))



def subStrings(str, n):
    palindromes = []
    for l in range(n):
        for i in range(l, n):
                if palindrome_check(str[l:i+1]) and len(str[l:i+1])>1:
                    palindromes.append(str[l:i+1])
                #print(str[l:i+1])
    print(set(palindromes))


subStrings(s,len(s))



