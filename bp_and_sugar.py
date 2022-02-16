print("enter no. of patients")
n = int(input())

for i in range(n):
    print("enter test name")
    t = input()
    if t == "BP":
        print("ENTER bp1 VALUE")
        bp1 = int(input())
        print("ENTER bp2 VALUE")
        bp2 = int(input())
        if bp1 > 120 and bp2 < 80:
            print("HIGH BP")
        else:
            print("LOW BP")
    if t == "SUGAR":
        print("ENTER SUGAR VALUE")
        s = int(input())
        if s > 200:
         print("HIGH BLOOD SUGAR")
        else:
         print("LOW BLOOD SUGAR")
