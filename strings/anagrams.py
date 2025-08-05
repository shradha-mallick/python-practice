a= input("Enter the first string: ")
b= input("Enter the second string: ")
a=a.lower()
b=b.lower()

for x in a:
    if x.isalpha():
        if a.count(x)!=b.count(x):
            print("Not Anagrams")
            break
else:
    print('ANAGRAMS')