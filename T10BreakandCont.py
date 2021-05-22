#i = 0

#while(True):
    #if i+1<5:
     #   i = i + 1
    #continue
    #print(i + 1, end=" ")
    #if (i==44):

    #    break   #Stop the loop
   # i = i + 1

# Program


while(True):
    inp = int(input("Enter the Number\n"))
    if inp>100:
        print("Congrates you are eligible\n")
        break
    else:
        print("Failed, try again\n")
        continue