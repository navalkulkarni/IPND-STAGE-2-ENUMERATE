''' Code upto function choose_level contains strings for various levels and and their answers.'''

easy_level_string = "There are how many wonders in the world? There are __1__ wonders in the world.\n" \
                        "The 7th wonder of the world is __2__ .The 6th wonder of the world is __3__ .\n " \
                        "The 5th wonder of the world is __4__ ."

medium_level_string="Longest river in the world is __1__ . Second longest river in the world is __2__. " \
                    "Third longest river in the world is __3__. Fourth longest river in the world is __4__ "

difficult_level_string="Biggest country in the world is __1__ . Second biggest country in the world is __2__. " \
                    "Third biggest country in the world is __3__. Fourth biggest country in the world is __4__ "

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
        return level_blank(easy_level_string,level_answers)
    elif level_name=="medium":
        print medium_level_string
        level_answers=medium_level_answers
        return level_blank(medium_level_string,level_answers)
    else:
        print difficult_level_string
        level_answers=difficult_level_answers
        return level_blank(difficult_level_string,level_answers)

#this function gives the user 3 tries to guess the answer, if the user is correct, it replaces the blanks with correct answer
#And continues game until the answer list is empty. enumerate facilitates this easily. Thanks for the suggestion.

INDEX_START=1

def level_blank(level_string,level_answers):
    for index,answer in enumerate(level_answers,INDEX_START):
        number_of_tries = 2
        print "Enter in lower case only,check your CAPS LOCK key"
        user_input = raw_input("Type in your answer for the blank:")
        if user_input == answer:
            print "Correct !!!"
            level_string = level_string.replace(str(index), user_input)
            print level_string
        else:
            while number_of_tries > 0:
                print "You have " + str(number_of_tries) + " tries left"
                user_input = raw_input("Type in your answer for first blank:")
                if user_input == answer:
                    print "Correct !!!"
                    level_string = level_string.replace(str(index), user_input)
                    print level_string
                number_of_tries = number_of_tries - 1
            print "Sorry but you have lost the game."

choose_level()