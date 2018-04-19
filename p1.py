#####################################
#           A1035537賴煒勛          #
#           2018/3/5  lab_1_p1      #
#####################################

import random
answer =  random.randrange(1,100)
print (answer)


while True:
    #guess = int(input("input your answer plz:"))

    guess = input("Please input a number：")
    if  guess.isdigit():
        if 0<int(guess)<101:
            print("Number accept")
        else:
            print("Number is out off range 1~100")
            continue
    else:
        print("Plz input a int number")
        continue

    #print ('User guess ' + str(guess))
    if int(guess) > answer :
        print ('Answer is smaller')
    if int(guess) < answer :
        print ('Answer is larger')
    if int(guess) == answer :
        print ('Bingo! Right answer')
        break