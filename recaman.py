import os                                                        #imports the os module so I can clear the terminal later

def recaman(num):                                                #defines the function "recaman" with one argument called "num"
    list = []                                                    #creates a list with no members
    for n in range(0, num):                                      #begins a for loop with the iterator "n" from the range of 0 to "num"
        if n == 0:                                               #checks if n is equal to 0, and if so...
            list.append(0)                                          #appends 0 to the end of list
        elif list[n-1] - n > 0 and not (list[n-1] - n in list):  #checks if the previous if statement didn't evaluate and if THAT is true
            list.append(list[n-1] - n)                              #appends (list[n-1] - n) to the end of list
        else:                                                    #check if both of the previous if statements didn't evaluate
            list.append(list[n-1] + n)                              #appends (list[n-1] + n) to the end of list
    return list                                                  #finally, it returns list back to wherever recaman(num) was called

os.system('clear')                                               #clears the terminal
print(recaman(100))                                                #prints the output of recaman(10) 
