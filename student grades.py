print("                                     GRADE OF A SINGLE STUDENT                                          ")
print("ENTER MARKS OF A STUDENT")
x = int(input())
if x > 90 and x < 100:
    print("excellent _ 'O' grade")
elif x > 80 and x < 90:
    print("very good _ 'A' grade")
elif x > 70 and x < 80:
    print("good_'B' grade")
elif x > 60 and x < 70:
    print("average _ 'B' grade")
elif x < 60:
    print("bad_ 'C' grade")

print("                                   ENTERING N NUMBER OF STUDENTS                                       ")
print("ENTER THE NUMBER OF STUDENTS")
nStu = int(input())
print("ENTER NUMBER OF SUBJECTS")
nSub = int(input())
for i in range(nStu):
    for j in range(nSub):
        print("Enter marks of subject " + str(j) + " of student " + str(i))
        m = int(input())
        if m >= 90 and m <= 100:
            print("excellent _ 'O' grade")
        elif m >= 80 and m < 90:
           print("very good _ 'A' grade")
        elif m >= 70 and m < 80:
            print("good_'B' grade")
        elif m >= 60 and m < 70:
            print("average _ 'B' grade")
        elif m < 60:
            print("bad_ 'C' grade")
        else:
            print("wrong marks")




