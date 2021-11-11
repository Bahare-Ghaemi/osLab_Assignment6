words = []

def load_data_from_file():
    with open("wordsDict.txt","r") as file:
        allWords = file.read()
        word = allWords.split("\n")
        for el in range(0,len(word),2):
            showResult={"english":word[el],"persian":word[el + 1]}
            words.append(showResult)


#----------English to Persian---------
def english_to_persian():
    value = ""
    word_input = input("enter your word : ")
    word_ = word_input.split(" ")
    
    for word in word_:
        for words_ in words:
            if words_["english"] == word:
                value += words_["persian"] + " "
                break
            else:
                print('INVALID word!')
                break
        else:
            value += word + " "

    print('\n-----------------------')
    print(' ',word_input,':',value)
    print('-------------------------')
#-------------------------------------

#----------Persian to English---------
def persian_to_english():
    value = ""
    word_input = input("enter your word : ")
    word_ = word_input.split(" ")
    
    for word in word_:
        for words_ in words:
            if words_["persian"] == word:
                value += words_["english"] + " "
                break
            else:
                print('INVALID word!')
                break
        else:
            value += word + " "

    print('\n-----------------------')
    print(' ',word_input,':',value)
    print('-------------------------')
#-------------------------------------


#----------Add New Word---------------
def new_word():
    englishW =input("enter english  word :")
    persianW =input("enter persian  word :")
    new_word = {"english":englishW, "persian":persianW}
    words.append(new_word)
    with open("wordsDict.txt","a") as file:
        file.write(englishW)
        file.write("\n")
        file.write(persianW)
        file.write("\n")
    print("new word added...")
#-------------------------------------


def Exit():
    print('you press EXIT...')
    #exit()
    return 0

#---------Show Menu----------
def show_menu():
    print("\n*** wellcom to my dictionary ***")
    print('1- English to persian')
    print('2- persian to English')
    print('3- Add new word')
    print('4- Save changes and Exit')
#----------------------------


load_data_from_file()

while True:
    show_menu()
    choice = int(input("Enter your choice : "))

    if choice==1:
        english_to_persian()
    elif choice==2:
        persian_to_english()
    elif choice==3:
        new_word()
    elif choice==4:
        Exit()
    else:
        print('invalid input! please try again...')
    


