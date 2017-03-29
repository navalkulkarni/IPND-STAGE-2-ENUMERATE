''' Code upto function choose_level contains strings for various levels and and their answers.'''

easy_level_string = "There are how many wonders in the world? There are __1__ wonders in the world.\n" \
                        "The 7th wonder of the world is __2__ .The 6th wonder of the world is __3__ .\n " \
                        "The 5th wonder of the world is __4__ ."

medium_level_string="Longest river in the world is __1__ . 2nd longest river in the world is __2__. " \
                    "3rd longest river in the world is __3__. 4th longest river in the world is __4__ "

difficult_level_string="Biggest country in the world is __1__ . 2nd biggest country in the world is __2__. " \
                    "3rd biggest country in the world is __3__. 4th biggest country in the world is __4__ "

easy_level_answers = ['7', 'eiffel tower', 'taj mahal','statue of liberty']
medium_level_answers=['nile', 'amazon', 'yangtze','mississippi']
difficult_level_answers=['russia', 'canada', 'united states','china']

#This function helps user to choose a level between easy,medium and hard, and, if user enters any other input then it
# prompts the user to input again. further, it passes the name to function get_level
def choose_level():
    print "Please Select a Difficulty Level for the game!!!"
    level_name = raw_input("Type in easy,medium or difficult\n")
    print "Enter in lower case only,check your CAPS LOCK key"
    if level_name=="easy":
        print get_level(level_name)
    elif level_name=="medium":
        get_level(level_name)
    elif level_name=="difficult":
        get_level(level_name)
    else:
        print "Wrong Input"
        return choose_level()

#this function takes level_name as an argument and prints the corresponding level's string and passes that string and
#list of answers to function level_first_blank

def get_level(level_name):
    if level_name=="easy":
        print easy_level_string
        level_answers=easy_level_answers
        return level_first_blank(easy_level_string,level_answers)
    elif level_name=="medium":
        print medium_level_string
        level_answers=medium_level_answers
        return level_first_blank(medium_level_string,level_answers)
    else:
        print difficult_level_string
        level_answers=difficult_level_answers
        return level_first_blank(difficult_level_string,level_answers)

#this function gives the user 3 tries to guess the answer, if the user is correct, it replaces __1__ with correct answer
#And passes on this replaced string to the next function.

def level_first_blank(level_string,level_answers):
    number_of_tries=2
    print "Enter in lower case only,check your CAPS LOCK key"
    user_input=raw_input("Type in your answer for first blank:")
    if user_input==level_answers[0]:
        print "Correct !!!"
        first_blank_correct_string=level_string.replace('__1__',user_input)
        return level_second_blank(first_blank_correct_string,level_answers)
    else:
        while number_of_tries>0:
            print "You have "+str(number_of_tries)+ " tries left"
            user_input = raw_input("Type in your answer for first blank:")
            if user_input == level_answers[0]:
                print "Correct !!!"
                first_blank_correct_string = level_string.replace('__1__', user_input)
                return level_second_blank(first_blank_correct_string,level_answers)
            number_of_tries=number_of_tries-1
        print "Sorry but you have lost the game. Close the file and open it again to play again"

#this function gives the user 3 tries to guess the answer, if the user is correct, it replaces __2__ with correct answer
#And passes on this replaced string to the next function.


def level_second_blank(first_blank_correct_string,level_answers):
    print first_blank_correct_string
    number_of_tries = 2
    user_input = raw_input("Type in your answer for second blank:")
    if user_input == level_answers[1]:
        print "Correct !!!"
        second_blank_correct_string = first_blank_correct_string.replace('__2__', user_input)
        return level_third_blank(second_blank_correct_string,level_answers)
    else:
        while number_of_tries > 0:
            print "You have " + str(number_of_tries) + "  tries left"
            user_input = raw_input("Type in your answer for second blank:")
            if user_input == level_answers[1]:
                print "Correct !!!"
                second_blank_correct_string = first_blank_correct_string.replace('__2__', user_input)
                return level_third_blank(second_blank_correct_string,level_answers)
            number_of_tries = number_of_tries - 1
        print "Sorry but you have lost the game. Close the file and open it again to play again"

#this function gives the user 3 tries to guess the answer, if the user is correct, it replaces __3__ with correct answer
#And passes on this replaced string to the next function.


def level_third_blank(second_blank_correct_string,level_answers):
    print second_blank_correct_string
    #easy_level_answers = ['7', 'eiffel tower', 'taj mahal']
    number_of_tries = 2
    user_input = raw_input("Type in your answer for third blank:")
    if user_input == level_answers[2]:
        print "Correct !!!"
        third_blank_correct_string = second_blank_correct_string.replace('__3__', user_input)
        return level_fourth_blank(third_blank_correct_string,level_answers)
    else:
        while number_of_tries > 0:
            print "You have " + str(number_of_tries) + " tries left"
            user_input = raw_input("Type in your answer for third blank:")
            if user_input == level_answers[2]:
                print "Correct !!!"
                third_blank_correct_string = second_blank_correct_string.replace('__3__', user_input)
                return level_fourth_blank(third_blank_correct_string,level_answers)
            number_of_tries = number_of_tries - 1
        print "Sorry but you have lost the game. Close the file and open it again to play again"

#this function gives the user 3 tries to guess the answer, if the user is correct, it replaces __4__ with correct answer
#And passes on this replaced string to the next function.


def level_fourth_blank(third_blank_correct_string,level_answers):
    print third_blank_correct_string
    number_of_tries = 2
    user_input = raw_input("Type in your answer for fourth blank:")
    if user_input == level_answers[3]:
        print "Correct !!!"
        fourth_blank_correct_string = third_blank_correct_string.replace('__4__', user_input)
        return level_correct_string(fourth_blank_correct_string)
    else:
        while number_of_tries > 0:
            print "You have " + str(number_of_tries) + " tries left"
            user_input = raw_input("Type in your answer for fourth blank:")
            if user_input == level_answers[3]:
                print "Correct !!!"
                fourth_blank_correct_string = third_blank_correct_string.replace('__4__', user_input)
                return level_correct_string(fourth_blank_correct_string)
            number_of_tries = number_of_tries - 1
        print "Sorry but you have lost the game. Close the file and open it again to play again"

#and,finally, this function level_correct_string prints the final fully answered string

def level_correct_string(fourth_blank_correct_string):
    print "Congratulations!!! You have finished the game"
    print fourth_blank_correct_string


choose_level()





