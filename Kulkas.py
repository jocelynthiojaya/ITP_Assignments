#Kulkas
endprogram = False
topshelf = {}
midshelf = {}
botshelf = {}
fridge = [topshelf, midshelf, botshelf]

topspace = 20
midspace = 20
botspace = 20

class foodItems():
    
    name: str
    volume: int



    def __init__(self, name = '', volume = 0):
        self.name = name  
        self.volume = volume
    
    def setName(self):
        self.name = input('What do you want to put in?')
    
    def setVolume(self):
        self.volume += int(input('How much do you want to put?'))
    

while endprogram == False:
    answer = input('Do you want to use the fridge? (Yes/No)')
    answer = answer.strip() 
    answer = answer.lower()

    if  answer == 'yes':
        answer = input('Choose an action! (Put/Take/View)')
        answer = answer.strip() 
        answer = answer.lower()
        
        #PUT
        if answer == 'put':
            answer = input('Pick a shelf! (Top/Middle/Bottom)')
            answer = answer.strip() 
            answer = answer.lower()

    
            if answer == 'top':
                item = foodItems()
                item.setName()
                item.setVolume()
                if item.name in topshelf:
                    volume = topshelf[item.name]
                    topshelf[item.name] = volume + item.volume
                    topspace = topspace - item.volume
                    print('Available space in top shelf is: ' + str(topspace))
                else: 
                    topshelf[item.name] = item.volume
                    print(item.name.title() + ' is in the fridge!')
                    if (topspace - item.volume) >= 0:        
                        topspace = topspace - item.volume
                        print('Available space in top shelf is: ' + str(topspace))
                    else:
                        print('not enough space!')
                

            elif answer == 'middle':
                item = foodItems()
                item.setName()
                item.setVolume()
                if item.name in midshelf:
                    volume = midshelf[item.name]
                    midshelf[item.name] = volume + item.volume
                    midspace = midspace - item.volume
                    print('Available space in top shelf is: ' + str(midspace))
                else:                   
                    midshelf[item.name] = item.volume
                    print(item.name.title() + ' is in the fridge!')
                    if (midspace - item.volume) >= 0:
                        midspace = midspace - item.volume
                        print('Available space in middle shelf is: ' + str(midspace))
                    else:
                        print('not enough space!')
    
            elif answer == 'bottom':
                item = foodItems()
                item.setName()
                item.setVolume()
                if item.name in botshelf:
                    volume = botshelf[item.name]
                    botshelf[item.name] = volume + item.volume
                    botspace = botspace - item.volume
                    print('Available space in top shelf is: ' + str(botspace))
                else:   
                    botshelf[item.name] = item.volume
                    print(item.name.title() + ' is in the fridge!')
                    if (botspace - item.volume) >= 0:
                        botspace = botspace - item.volume
                        print('Available space in bottom shelf is: ' + str(botspace))
                    else:
                        print('not enough space!')
            else:
                print('Invalid answer')
       
        #TAKE
        elif answer == 'take':
            answer = input('Pick a shelf! (Top/Middle/Bottom)')
            answer = answer.strip() 
            answer = answer.lower()

            if answer == 'top':
                itemtake = input('What do you want to take?')
                takevolume = int(input('How much do you want to take?'))
                #for i in topshelf:
                if takevolume > topshelf[itemtake]:
                    print('That amount of ' + itemtake + ' is not available.')
                else:
                    if itemtake in topshelf:
                        volume = topshelf[itemtake]
                        topshelf[itemtake] = volume - takevolume
                        topspace = topspace + takevolume
                        print('Available space in top shelf is: ' + str(topspace))
                    else:
                        print('The item you wanted to take is not in the fridge.')
                        #doesnt work if take is the first request
            elif answer == 'middle':
                itemtake = input('What do you want to take?')
                takevolume = int(input('How much do you want to take?'))
                if takevolume > midyesshelf[itemtake]:
                    print('That amount of ' + itemtake + ' is not available.')
                else:
                    if itemtake in midshelf:
                        volume = midshelf[itemtake]
                        midshelf[itemtake] = volume - takevolume
                        midspace = midspace + takevolume
                        print('Available space in middle shelf is: ' + str(midspace))
                    else:
                        print('The item you wanted to take is not in the fridge.')
            elif answer == 'bottom':
                itemtake = input('What do you want to take?')
                takevolume = int(input('How much do you want to take?'))
                if takevolume > botshelf[itemtake]:
                    print('That amount of ' + itemtake + ' is not available.')
                else:
                    if itemtake in botshelf:
                        volume = botshelf[itemtake]
                        botshelf[itemtake] = volume - takevolume
                        botspace = botspace + takevolume
                        print('Available space in top shelf is: ' + str(botspace))
                    else:
                        print('The item you wanted to take is not in the fridge.')
            else:
                print('Invalid answer') 
        
        #VIEW
        elif answer == 'view':
            print('--------------------')
            print('--------------------')
            for i in topshelf:
                print(i +': ' + str(topshelf[i]))
            print('--------------------')
            for i in midshelf:
                print(i +': ' + str(midshelf[i]))
            print('--------------------')
            for i in botshelf:
                print(i +': ' + str(botshelf[i]))
            print('--------------------')
            print('--------------------')
        
        #INVALID ANSWER
        else:
            print('Invalid answer')

    elif answer == 'no':
        print('Ok, Goodbye!')
        endprogram = True
    else:
        print('Invalid answer')