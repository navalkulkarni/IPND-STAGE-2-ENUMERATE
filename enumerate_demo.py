easy_level_answers = ['7', 'eiffel tower', 'taj mahal','statue of liberty']
question_blanks=['__1__','__2__','__3__','__4__']
easy_level_string = "There are how many wonders in the world? There are __1__ wonders in the world.\n" \
                        "The 7th wonder of the world is __2__ .The 6th wonder of the world is __3__ .\n " \
                        "The 5th wonder of the world is __4__ ."
INDEX_START=1

for index,answer in enumerate(easy_level_answers,INDEX_START):
    number_of_tries = 2
    print "Enter in lower case only,check your CAPS LOCK key"
    user_input = raw_input("Type in your answer for first blank:")
    if user_input == answer:
        print "Correct !!!"
        #index=1
        easy_level_string = easy_level_string.replace(str(index), user_input)
        #return level_second_blank(first_blank_correct_string, level_answers)
        #index=index+1
        print easy_level_string
    else:
        while number_of_tries > 0:
            print "You have " + str(number_of_tries) + " tries left"
            user_input = raw_input("Type in your answer for first blank:")
            if user_input == answer:
                print "Correct !!!"
                #index=1
                easy_level_string = easy_level_string.replace(str(index), user_input)
                #return level_second_blank(first_blank_correct_string, level_answers)
                #index=index+1
                print easy_level_string
            number_of_tries = number_of_tries - 1
        print "Sorry but you have lost the game. Close the file and open it again to play again"

