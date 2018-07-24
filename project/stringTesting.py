# stringTesting.py
# Shows how to use split, etc.
# 02/01/2016
__author__  = "Mr. Cochran's Birthday is 02/22/2016"

# this method will check the parameter phrase to see if it
# contains any punctuation mark
import string
def contains_punctuation(phrase):
    phrase = "".join(l for l in phrase if l not in string.punctuation)
    return phrase
# this method shows how the split method works on a string
def split_example(split_phrase):
    phrase = split_phrase.split(" ")
    return(phrase)

# this method looks to see if user input exists inside a list
# right now it only works with a single word
# it needs to be updated to work with phrases
def input_in_list(rank):
    word=""
    users_pet = raw_input("What type of pet do you have? ")
    users_pet = contains_punctuation(users_pet)
    phrase=split_example(users_pet)
    pets = ['dog','cat','fish','bird','hamster','guinea pig','iguana','snake','horse','pig']
    counter=0
    tempPhrase=[]
    tempword=""
    for word in phrase:

        for i in range(0,len(pets)):
            if pets[i] == word:
                rank = int(i)
                print('A ' + word + ' is a very common pet to have. ')
                print('In the US, a ' + word + ' ranks #' + str(rank+1) + ' in the list of the 10 most common household pets.')
            else:
                counter +=1
    if counter==len(phrase):
        print('I don\'t have any information to share with you about your pet. Sorry.')

if __name__ == "__main__":
    rank=0
    choice = int(raw_input("1 to show split example 2 to show list indexing 3 to show punctuation search: "))
    if choice == 1:
        split_example()
    elif choice == 2:
        input_in_list(rank)
    else:   # choice == 3; do I need to code this specifically?
        phrase = raw_input("Enter a phrase of your choice: ")
        if contains_punctuation(phrase):
            print("I found a punctuation mark in that phrase.")
            #TODO: Figure out a way to remove punctuation from phrase
        else:
            print("That phrase doesn't contain any punctuation marks.")


                    """del tempPhrase[:]
        if word[len(word)-1]=="s":
            tempword = word
            for i in range (0,len(tempword1):
                tempPhrase.append(tempword[i])
            for i in range (0,len(tempPhrase)):
                word = word+tempPhrase[i]"""