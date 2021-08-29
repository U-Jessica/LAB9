fname=input("enter file name")
try_count=3
with open(fname) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
while(try_count):
    line_no=int(input("Enter line number to read "))
    try:
        print(lines[line_no-1])
        try_count=0
    except:
        print('Line number exceeded length of file')
        try_count-=1
freq={}
for i in lines:
    words=i.split(" ")
    for word in words:
        if (word in freq):
            freq[word]+=1
        else:
            freq[word]=1
going=True
while(going):
    check=input("Enter word to see frequency ")
    try:
        print(freq[check])
        going=False
    except:
        print("Word in not available in file")
    finally:
        still_going="Y"
        if(going):
            still_going=input("Do you want to continue irrespective of the error? Y/N? ")
        if(still_going=="N"):
            going=False
        

