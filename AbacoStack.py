#----------------------------------------------------
# Assignment 3: AlbacoStack.py
#
# Author: Khanh Bui
# Collaborators/references: Discord help to understand the idea of tasks
#----------------------------------------------------
import random # Importing random for random generator
# Task 1: This task create card class
# Input: colours_num and depth
# Ouput: N/A 
class Card: # done # replace method
    def __init__(self,colours_num,depth):
        self.__beads = []
        self.colours_num = colours_num
        self.depth = depth
        self.colours = ["A","B","C","D","E","F"]
        self.chosen_colours = self.colours[:colours_num]
        for i in range(self.colours_num):
            for j in range(self.depth):
                self.__beads.append(self.colours[0])
            self.colours.pop(0)
    # function shuffle the card in the deck
    # Input: N/A
    # Ouput: N/A           
    def reset(self):
        random.shuffle(self.__beads) 
    # function show the card
    # Input: N/A
    # Ouput: N/A      
    def show(self): # done
        show_list = []      
        for i in range(self.colours_num):
            show_list.append(self.stack(i + 1))
        if self.colours_num > 1:
            for i in range(self.colours_num):
                print("|", end = "")
                for j in range(self.depth):
                    if j // self.depth == 0:
                        print(show_list[j][i], end = "")
                    else:
                        print(show_list[j][i], end = " ")
                print("|", end = "")
                print()
        elif self.colours_num == 1:
            for i in self.__beads:
                print("|", end = "")
                print(i, end = "")
                print("|", end = "")
                print()


    # function return the column of the card
    # Input: number
    # Ouput: the column of the card 
    def stack(self,number): # done
        if number > self.colours_num or number == 0:
            raise Exception("the input Number is not with in the card's size, 0 is excluded")
        else:
            card_list = []
            count = 0
            for i in range(self.colours_num):
                temp_list = []
                for j in range(self.depth):
                    temp_list.append(self.__beads[count])
                    count = count + 1
                card_list.append(temp_list)

            return card_list[number - 1]

                
    # function replace the current card by the input file and n would be the line from the file going to inputted
    # Input: file_name, n
    # Ouput: string of Card            
    def replace(self,file_name,n): # Done
        item_list = [] 
        with open(file_name, 'r') as fp:
            x = len(fp.readlines())
        if n > x - 1 or n < 0:
            raise Exception(" n is invalid in the txt file")      
        with open(file_name, 'r') as fp:
            items = fp.readlines()[n]
            item_list = list(items.split(" "))
        word_repitition = []
        item_list = list(map(lambda s: s.strip(), item_list))
        for word in item_list:       
            if word not in word_repitition:
                word_repitition.append(word)
        self.colours_num = len(word_repitition)
        self.depth = len(item_list) // len(word_repitition)
        self.__beads = item_list
        
    # function return string of card when it is being called
    # Input: N/A
    # Ouput: string of Card
    def __str__(self): # done
        string = ""
        array_list = []
        beads_list = []
        for i in self.__beads:
            beads_list.append(i)
        for i in range(self.depth ):
            temp_list = []
            for j in range(self.colours_num):          
                temp_list.append(beads_list[0])
                beads_list.remove(beads_list[0])
            array_list.append(temp_list)
        for i in array_list:
            for j in i:
                string += j
        string = str(array_list)
        string = string[1:-1]
        string = string.replace("[", "|")
        string = string.replace("]","|")
        string = string.replace("'","")
        string = string.replace(",","")
        return string

# Task 2: This task create bounded stack
# Input: capacity
# Ouput: N/A  
# implementing stack with limited capacity
class Bstack: 
    def __init__(self,capacity): # Done
        self.capacity = capacity
        self.items = []
    def push(self, item): # fix # done # tested
        if len(self.items) != self.capacity: 
            self.items.append(item)
        else:
            raise Exception("Error: The stack have reached maximum capacity")
    def pop(self): # tested
        if len(self.items) == 0:
            raise Exception("Error: AN EMPTY STACK detected")
        return self.items.pop()
    def peek(self): # fix # done # tested
        if len(self.items) == 0:
            raise Exception("Error: AN EMPTY STACK detected")
        #elif len(self.items) == self.capacity:
            #raise Exception("Error: The stack have reached maximum capacity, cannot proceed peek method")
        return self.items[len(self.items)-1] 
    def isEmpty(self): # tested
        return self.items == []
    def size(self): # tested
        return len(self.items)
    def checkBottom(self):
        return self.items[0]
    def clear(self):
        self.items.clear()
    def show(self):
        print(self.items)
    def __str__(self):
        return str(self.items) 
    def __rep__(self):
        return str(self.items)          
    def isFull(self):
        if len(self.items) == self.capacity:
            return True
        else: 
            return False
# Task 3: class AbacoStack, This stack class responsible for mostly game action 
# Input: depth, stack_num
# Ouput: N/A 
class AbacoStack:
    def __init__(self,stack_num, depth): # Done
        self.depth = depth
        self.stack_num = stack_num
        self.a_list = [None] * (self.stack_num + 2)
        self.moves = 0
        self.stack_list = [] #
        self.colours = ["A","B","C","D","E","F"]
        self.pop_colours = []
        # making list size
        for index in range(self.stack_num + 2):
            self.a_list[index] = "."

        for stack in range(stack_num):
            b_stack = Bstack(self.depth)    
            for j in range(self.depth):
                b_stack.push(self.colours[0])
            pop = self.colours.pop(0)
            self.stack_list.append(b_stack)      
            self.pop_colours.append(pop)

    # The function responsible for all the move make in the game
    # Input: move
    # Ouput: N/A 
    def moveBead(self, move): # Worked          
        if type(move) != str or len(move) > 2:
            raise Exception("--Invalid input--")
        else:      
            self.valid = False
            command_list = []
            for character in move:
                command_list.append(character) # printout correct
            if command_list[0].isdigit() != True:
                raise Exception (" the first character should be an int")
        # upward move # Done # involve a_list and stack list
            if (command_list[1]).lower() ==  "u" and int(command_list[0]) != 0 and int(command_list[0]) != len(self.a_list) and self.a_list[int(command_list[0])] == ".": # pass
                for index in range(len(self.stack_list)):
                    if index + 1 == int(command_list[0]) and self.a_list[index + 1] == ".":
                        # pop first time
                        if self.stack_list[index].peek() != ".":
                            temp_item = (self.stack_list[index]).pop()
                            self.stack_list[index].push(self.a_list[index + 1])
                            self.a_list[index + 1] = temp_item
                            
                        else: # experiment
                            temp_list = []
                            empty_count = 0
                            for i in range(self.depth):
                                temp_item = (self.stack_list[index]).pop()
                                temp_list.append(temp_item)
                                if temp_item == ".":
                                    empty_count = empty_count + 1
                            for i in range(len(temp_list)):
                                if i == empty_count:
                                    temp = temp_list[i]
                                    self.a_list[index + 1] = temp
                                    temp_list[i] = "."
                            for i in reversed(temp_list):
                                self.stack_list[index].push(i)
                        self.valid == True
                        
                self.moves = self.moves + 1

        # downward move # Done # involve a_list and stack list 
            elif (command_list[1]).lower() ==  "d" and command_list[0] != 0 and command_list[0] != len(self.a_list) - 1 and self.stack_list[int(command_list[0]) - 1].peek() == ".":
                for index in range(len(self.stack_list)):
                    if index + 1 == int(command_list[0]): # find the index in the stack list  
                        temp_list = []
                        empty_count = 0
                        for i in range(self.depth):
                            temp_item = (self.stack_list[index]).pop()
                            temp_list.append(temp_item)                        
                            if temp_item == ".":
                                empty_count = empty_count + 1
                        for i in reversed(temp_list):
                            self.stack_list[index].push(i) 
                        #self.stack_list[index].show()

                        if empty_count == 1:
                            #print("pass1")
                            temp_item = self.stack_list[index].pop()
                            self.stack_list[index].push(self.a_list[index + 1])
                            self.a_list[index + 1] = temp_item
                            
                            
                        else:
                            # Fixed
                            temp_list = []
                            for i in range(empty_count):
                                pop = self.stack_list[index].pop()
                                temp_list.append(pop)

                            temp_item = self.a_list[index + 1] 
                            self.a_list[index + 1] = "."
                            temp_list[0] = temp_item
                            #self.stack_list[index].show()

                            for i in (temp_list):              
                                self.stack_list[index].push(i)
                        self.valid == True
                self.moves = self.moves + 1                        



        # right move #  Done  # involve a_list only
            elif (command_list[1]).lower() ==  "r" and int(command_list[0]) != len(self.a_list) - 1 and self.a_list[int(command_list[0]) + 1] == ".":

                for index in range(len(self.a_list)):
                    if index == int(command_list[0]) : #or index != len(self.a_list - 1):

                        temp = self.a_list[index]
                        self.a_list[index] = self.a_list[index + 1]
                        self.a_list[index + 1] = temp
                        self.moves = self.moves + 1 

                        self.valid == True

                
        #left move # Not Done # involve a_list only
            elif (command_list[1]).lower() == "l" and int(command_list[0]) != 0 and self.a_list[int(command_list[0]) - 1] == "." :

                for index in range(len(self.a_list)):
                    if index == int(command_list[0]):

                        temp = self.a_list[index]
                        self.a_list[index] = self.a_list[index-1]
                        self.a_list[index - 1] = temp
                        self.moves = self.moves + 1 

                        self.valid == True
            else:
                raise Exception("Error: invalid move")   
    # FUnction used to check whether game win
    # Input: card
    # Ouput: N/A                            
    # 
    def isSolved(self, card): #  Take card object from main # Done  # niceee su
        win = False
        card_stack_list = []
        for i in range(self.stack_num):
            card_stack_list.append(card.stack(i + 1))        
        self.compare_list = []

        for i in range(self.stack_num):
            temp_list = []
            for j in range(self.depth):
                pop = self.stack_list[i].pop()
                temp_list.append(pop)

            self.compare_list.append(temp_list)

        for i in self.compare_list:
            i.reverse()

        if self.compare_list == card_stack_list:

            win = True       
        else:
            win = False
        
        for i in self.compare_list:
            i.reverse()        
        for i in range(self.stack_num):
            temp_list = []            
            for j in range(self.depth):
                pop = self.compare_list[i].pop()
                self.stack_list[i].push(pop)
        
        return win
    # Function to reset game status
    # Input: N/A
    # Ouput: N/A     
    # 
    def reset(self): # Done
        self.stack_list = []
        self.moves = 0 # reset the moves
        
        for index in range(self.stack_num + 2):
            self.a_list[index] = "."    

        for stack in range(self.stack_num):
            b_stack = Bstack(self.depth)    
            for j in range(self.depth):
                b_stack.push(self.pop_colours[0])
            pop = self.pop_colours.pop(0)
            self.stack_list.append(b_stack)      
            self.pop_colours.append(pop)        
    
    # Function used to show the 2 game board status
    # Input: card(optional)
    # Ouput: N/A         
    # 
    def show(self,card = None): 
        # print number on the top
        for colour in range(self.stack_num + 2):
            print(colour, end =" ")
        print()
        # print the upper list
        for item in self.a_list:
            print(item,end = " ")
        card_len = len(self.a_list) + 6
        #if card is not None:
        #    self.card = card
        if card != None:
            print(" " * card_len, end = "")
            print("Card")       
        else:
            print()     

        # Above correct
        temp_stack_list = [] # duplicate temp_stack_lsit
        count = 0
        for i in range(len(self.stack_list)): # in range of colours
            b_stack = Bstack(self.depth) # temp bstack
            temp_list = []
            for item in range(self.depth):        
                temp_pop = self.stack_list[i].pop()
                temp_list.append(temp_pop)
            temp_list.reverse()
            for item in temp_list:
                self.stack_list[count].push(item)
                b_stack.push(item)
            temp_stack_list.append(b_stack)
            count = count + 1
        
        display = []
        
        for i in range(len(temp_stack_list)):
            temp_list = [] 
            for index in range(self.depth):      
                pop_item = temp_stack_list[i].pop()
                temp_list.append(pop_item)
            display.append(temp_list)
        # Create card list 
        if card != None:
            card_list = str(card).replace("|", "")
            card_list = card_list.split(" ")
            card_list = [card_list[i:i + self.depth] for i in range(0, len(card_list), self.depth)]  
        #   Display

        for item in range(self.depth):
            print("|", end =" ")# later
            for i in range(self.stack_num):
                print(display[i][item], end = " ")      
            print("|", end ="")
            if card != None:
                print("%12s" % "|", end =" ")
                for i in range(len(card_list)):                  
                    print(card_list[i][item], end = " ")      
                print("|", end ="")
            print() 

 
        print("+",end = "")
        for index in range(len(self.a_list) * 2 - 3):
            print("-",end ="")
        print("+", end = "")
        print(" " * 20, end = "")
        print( "moves: " + str(self.moves) )


    # reutrn a string if Abaco Stack being called
    # Input: N/A
    # Ouput: N/A                                
    def __str__(self):
        return str(self.stack_list)

# Main function: Used to run program and also to test 
# Input: N/A   
# Ouput: N/A         
def main():
    
    # Test Card class
    # Create card object in main
    #card = Card(3,3)
    # Test reset method in class object
    #card.reset() 
    # Test show method in card object
    #card.show()
    #print("after")
    # Test stack function in class object
    #print(card.stack(1))
    #card.replace("testFile.txt", 6)
    #print("show card")
    #card.show()
    #print("print card")
    #print(card)
    '''
    # Test Bstack class
    # create new Bstack 
    stack = Bstack(5)
    # Test push method
    print("1. Test push method")
    stack.push("puppy")
    stack.show()
    # Test pop method
    print("2. Test pop method")
    stack.pop()
    stack.show()
    # Test peek and size method
    print("3. Test peek and size method")
    stack.push("husky")
    stack.push("cat")
    stack.push("hmmm")
    print(stack.peek())
    print(stack.size())
    # Test is EMpty method
    print("4. Test is EMpty method")
    print(stack.isEmpty())
    # test clear
    print("5. Test clear method")
    stack.clear()
    print(stack.size())
    # Test __str__()
    print("6. test __str__ method")
    stack.push("hello")
    print(stack)
    # Test isFull()
    print("7. test isFull method")
    stack.push("husky")
    stack.push("cat")
    stack.push("hmmm")    
    stack.push("hi")
    print(stack)
    print(stack.isFull())
'''
    # Abaco stack Test
    # This is the small game simulation to test
    a_stack = AbacoStack(2,2)
    a_card = Card(2,2)
    a_card.reset()
    while a_stack.isSolved(a_card) == False:
        a_stack.show(a_card)           
        hey = input(": ")
        if hey == "r":
            a_stack.reset()
        else: 
            a_stack.moveBead(hey)
    print("@@ good job, you win @@")
        
if __name__ == "__main__":  
    main()    