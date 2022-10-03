
temp=[]               # empty list
count=0               # set count to zero
while True:
    number=input("enter the number=")    # taking user input
    if number == "10":
        break
    else:
        temp.append(number)              # adding the numebr to the empty list until the user hit 10 for exit
user_choice=input("enter the number you want=")  # number to find the frequency of 
for i in  range(len(temp)):
    if temp[i]==user_choice:
        count+=1
    if count==0:
        print("no any repetation")
print(f"the count is{count}")            # printing the result

