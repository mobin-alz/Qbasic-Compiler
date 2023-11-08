with open("Codd1.txt", "r") as file_reader:
    f = file_reader.readlines()


def splitter(txt) : 
    word = ''
    
    for letter in txt : 
        if letter == ' ' : 
            if word == '' :
                pass
            else : 
                print(word)
            word = ''
        
        elif letter == '=' :
            if word == '' :
                pass
            else : 
                print(word)
            print("=")
            word = ''
        else : 
            word += letter    
    if word == '' or word == ' ':
        pass
    else : 
        print(word)


for item in f:
      
    if item != '\n':
        
        splitter(item)