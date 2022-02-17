#palindrome:if the first half of a string is same as the reverse of the second half of that string then it is a
#palindrome.Also if the reverse of the string is same as the original then it is palindrome. eg:radar

#symmetric:if the first half of the string is same as the second half then it is a symmetric string
#eg: salsal




def palindrome_method1(a):
    if a == a[::-1]:
        print("It is a palindrome")
    else:
        print("of course It is not a palindrome")

def palindrome_method2(b):
    l = len(b)
    for i in range(int(l/2)):
        if b[i] != b[l-(i+1)]:
            print("NOT PALINDROME")
            return
    print("PALINDROME")





palindrome_method1("adda")
palindrome_method2("RACECAR")
palindrome_method2("ADOGAPANICINAPAGODA")


print("                             symmertric strings                                                             ")

def symmetric_method1(s):
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:len(s)]
    for i in range(int(len(s)/2)):
        if s1[i] != s2[i]:
            print("IT IS NOT SYMMETRIC")
            return
    print("IT IS SYMMETRIC")

symmetric_method1("samhitha")
symmetric_method1("mama")
symmetric_method1("samosa")


print("           symmetrical or palindrome             ")








