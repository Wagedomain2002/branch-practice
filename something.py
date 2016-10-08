from random import randint
print ('Ghost game')
feeling_brave = True;
score = 0;

while feeling_brave:
    ghost_door = randint(1,3)
    print('Three doors ahead..')
    print('A Ghost behind one of them')
    print('Which door do you open?')
    door = input('1,2, or 3?')
    door_number = int(door)
    if door_number > 3:
        print('Good buy. You are scared, and you left the house.')
        feeling_brave = False
    else:
        if door_number == ghost_door:
            print('BUSTED!')
            feeling_brave = False
        else:
            print ('No ghost')
            print ('You enter the next door')
            score = score + 1
        print('Game over! You scored', score)
    
