#Efren Aguirre
#7/6/2022
#This program gets an order from a user and calculates the order tax, sub
#total and total, then it prints out the receipt


def main():
    #Initialize variable to be able to enter the first while loop
    endProgram = 'no'

    #loop to run the program more than once if needed
    while endProgram == 'no':
        #reset variables back to zero to prevent calculation errors. 
        totalBurger = 0 
        totalFry = 0
        totalSoda = 0
        total = 0 
        #initialize to no to be able to enter the second loop 
        endOrder = 'no'
        #this loop will allow the user to enter their order 
        while endOrder== 'no':
            print('Enter 1 for Yum Yum Burger')
            print('Enter 2 for Grease Yum Fries')
            print('Enter 3 for Soda Yum')
            option = int(input('Enter here:'))
            #this will decide what option the user entered
            if option == 1:
                totalBurger = getBurger(totalBurger)
            elif option == 2:
                totalFry = getFry(totalFry)
            elif option == 3:
                totalSoda = getSoda(totalSoda)
                #Prompts the user if their order is finished
            endOrder = input('Do you want to end your order? (yes/no):')
           
        total = calcTotal(totalBurger, totalFry, totalSoda)
        
        printReceipt(total)

        endProgram = input('Do you want to end the program? (yes/no):')


#this will determine the value of the total of the burgers ordered
def getBurger(totalBurger):
    burgerCount = int(input('Enter the number of burgers you want:'))
    totalBurger = totalBurger + (burgerCount * .99)
    return totalBurger
#this will determine the value of the total of the fries ordered
def getFry (totalFry):
    fryCount = int(input('Enter the number of fries you want:'))
    totalFry = totalFry + (fryCount * .79)
    return totalFry
 #this will determine the value of the total of the sodas ordered   
def getSoda(totalSoda):
    sodaCount = int(input('Enter how many sodas you want:'))
    totalSoda = totalSoda + (sodaCount * 1.09)
    return totalSoda
#calculates the total value of the order
def calcTotal(totalBurger, totalFry, totalSoda):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * .06
    total = subtotal + tax
    return total
#prints out the receipt of the order
def printReceipt (total):
    print('Your total is $', total)

main()












