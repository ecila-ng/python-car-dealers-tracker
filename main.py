list1 = []  #contains data of all cars
list2 = []  #contains data of all manufacturers
list3 = []  #contains data of all dealers

def find_phone_number(key):  #This function returns dealer's number
      for i in range(0, len(list3)):
        index = list3[i].find(key)
        
        if (index != -1):
            index = i
            temp, temp2, num = list3[index].split(' ', 2)
            
            tempNumber = []
            #string to list conversion by iteration
            for x in num:     
                tempNumber.append(x)

            tempNumber.insert(0,"(")
            tempNumber.insert(4,")")
            tempNumber.insert(8,"-")
            num = ''.join(tempNumber)
            return num

def VIN_to_name(VIN): #This function returns car's brand based on its VIN
    for i in range(0,len(list2)):
        index = list2[i].find(VIN[0:3])
        if (index != -1):
            index = i
            
            code, name = list2[index].split(' ', 1)
            return name

#Program runs until made stop by command 'q'
while True:
    prompt = input() #Prompt user for input
    
    ###### QUIT COMMAND #####
    if (prompt == "q"):
        break;
        
    action, rest = prompt.split(' ', 1) #Split input by command and the rest

    ###### ADD COMMAND #####
    if (action == "a"):
        action2, rest = rest.split(' ', 1) #Split command and the rest

        if (action2 == "c"):
            list1.append(rest) #Store data into corresponding list

        if (action2 == "m"):
            list2.append(rest) #Store data into corresponding list

        if (action2 == "d"):
            list3.append(rest) #Store data into corresponding list

    ##### LIST COMMAND #####
    elif (action == "l"):    
        if (rest == "c"):  #Print list of cars if the command is 'c'
            print(*list1, sep = '\n')

        if (rest == "d"):  #Print list of cars if the command is 'd'
            for i in range(0, len(list3)):
                a, b = list3[i].split(' ', 1)
                print (a + " "*(20-len(a)) + b)
    
    ##### FIND COMMAND #####
    elif (action == "f"): 
        action2, needtofind = rest.split(' ', 1)
        if (action2 == "m"):            
            #Find corresponding code first
            for i in range(0,len(list2)):
                index = list2[i].find(needtofind)
                
                if (index != -1):
                    index = i
                    break
            
            code, needtofind = list2[index]. split(' ', 1)
                        
            #Now use code to find corresponding car
            for i in range(0, len(list1)):
                index = list1[i].find(code)
                if (index != -1):
                    index = i
                    #(list1[index]) <- found it
                    
                    #Format printing, have to split first
                    VIN, miles, dealer, price = list1[index].split(' ', 3)
                    print (needtofind + ":" + miles 
                           + " miles, $" + price + ": " 
                           + dealer + "[" + find_phone_number(dealer) + "]")
        
        if (action2 == "z"):
            namelist = []
            #Find corresponding dealer first
            for i in range(0,len(list3)):
                index = list3[i].find(needtofind)                
                if (index != -1):
                    index = i                     
                    name, temp = list3[index].split(' ', 1)
                    namelist.append(name)   
                        
            #Now use code to find corresponding car
            for x in range(0, len(list1)):
                for y in range(0, len(namelist)):
                    index = list1[x].find(namelist[y])
                    if (index != -1):
                        #Format printing, have to split first
                        VIN, miles, dealer, price = list1[x].split(' ', 3)
                        print (VIN_to_name(VIN)+ ":" + miles 
                               + " miles, $" + price + ": " + dealer 
                               + "[" + find_phone_number(dealer) + "]")
            
              