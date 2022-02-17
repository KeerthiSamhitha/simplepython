a = ["red", "yellow", "pink", "green", "black", "white"]
print(len(a))
for i in range(len(a)):
    if i == (len(a)-1):
        print(a[i], end=".")
#hiiiii
print()
i = 0
while i != len(a):
    if i == (len(a)-1):

        print(a[i], end="." )
    else:
        print(a[i], end=",")
    i = i+1





