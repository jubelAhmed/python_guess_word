
# word guessing games
import random
from random_word import RandomWords
r = RandomWords()

# print(r.get_random_word())
# print(r.get_random_words())
# print(r.word_of_the_day())

# print(r.get_random_word(includePartOfSpeech="noun,verb", minLength=3, maxLength=6))

print("----------------------------------------------")
print("This Is The Word  Guessing Games From 5 Words")
print("----------------------------------------------")
print("----------------------------------------------")

#get random words in list

all_words = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family', 'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr', 'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right', 'room', 'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']
lists = []
count = 0
turn  = 5

while turn>0 :
    for i in range(4):
        lists.append(random.choice(all_words))


    # while (1):
    #     try:
    #         word = r.get_random_word()
    #         if word:
    #             count = count+1
    #             lists.append(word)
    #         if count==5:
    #             break
    #     except: continue
    #
    # print(lists)

    print('Chose the word  \n')
    j=1
    for list in lists:
        print( str(j) + ' : '+list+'\n')
        j = j+1

    guess_no = input("Chose the number : ")

    guess_word = random.choice(lists)

    guess_word_position = lists.index(guess_word)
    point = 0
    if (int(guess_no) == (guess_word_position+1) ) :
        print("guess correct\nGuess word is : "+guess_word)
        point = point +10
    else:
        print("guess wrong\nguess word is : "+guess_word)
    lists = []
    turn = turn-1
    print("\nYou have "+str(turn)+" turn")

print('Your Point is : ' + str(point))























