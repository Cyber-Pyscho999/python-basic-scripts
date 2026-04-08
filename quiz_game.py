
def start():

    guesses = []
    correct_guesses = 0

    for key in questions:
        print("----------------------")
        print(key)
        guess = input("")
        guess = guess.capitalize()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)


    display_score(correct_guesses,guesses)

def check_answer(answer,guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        print("Correct Answer: "+answer)
        return 0
def answer():
    pass
def display_score(correct_guesses,guesses):
    print("----------------")
    print("Results: ",end="")
    print("Your score is "+str(correct_guesses)+"/7")
questions = {" 1.what walled area in the city of Manila is home\nto Santiago and Manila Cathedral?: ": "Intramuros",
             "2.One of the most famous dishes from the Philippines is what sweet and savory stew,  \n commonly featuring chicken or another meat, marinated in soy, vinegar, garlic,  \n and a blend of herbs and spices?: ":"Adobo",
"3.Panay, Negros, and Cebu are the most populated islands of  \n which of the three major island group of the Philippines?":"Visayas","4.Although it doesn't have legal  \n status as such, which domesticated swamp-type water buffalo is considered the national animal of  \n the Philippines?":"Carabao","5.White Beach and Puka Shell Beach are just  \n two of the dozen beaches on which little island in the central Philippines?":"Boracay",
             "6.Which city that starts with 'M' is the financial heart of the Philippines, with more  \n than 62,000 registered businesses as of 2012?":"Makati","7.The mascot of which Filipino fast-food company  \n was chosen by founder Tony Tan to reflect Filipino optimism and industriousness?":"Jollibee"}
start()

