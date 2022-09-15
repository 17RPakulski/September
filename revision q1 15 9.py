compnum = 50

user = int(input('enter a number: '))

count = 1

while user != compnum: 
    print('wrong')
    if user < compnum:
        print('too low')
        count += 1
    elif user > compnum:
        print('too high')
        count += 1
    else:
        break
        
    user = int(input('enter a number: '))
    
print('correct')
print('took you', count,'guesses')    