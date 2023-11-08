with open("Codd1.txt", "r") as file_reader:
    f = file_reader.readlines()


def splitter(txt) : 
    word = ''
    state=0
    
    for letter in txt :

        if(state==0):
            
            if((letter>= 'a' and letter<='z') or (letter>='A' and letter<='Z')):
               word += letter
               state=1

            if((letter>='0' and letter<='9') or (letter=='.')):
               word += letter
               state=2

            if ((letter == ' ')):
                
                word =''
                state = 0

            if (letter == "(" or letter == ")" or letter == "<" or letter == ">" or letter == '=') :
                print(word)
                word = ''
                state = 3 

            if (letter == '\"') : 
                print(word)
                word = ''
                state = 10   

                 

            
        elif(state==1): # condition (a-z and A-Z)
            
            if((letter>='0' and letter<='9') or (letter=='.')):
               print(word)
               word = letter
               state = 2
            
            if((letter>='a' and letter<='z') or (letter>='A' and letter<='Z')):
               word += letter

            if ((letter == ' ')):
                
                word = ''
                state = 0
               
            if (letter == "(") :
                print(word)
                state = 0
                word = ''

            if (letter == '\"') :
                print(word)
                word = ''
                state = 10  



        elif(state==2): # condition(numbers)
            
            if((letter>='0' and letter<='9') or (letter=='.')):
               word+=letter

            if((letter >= 'a' and letter <= 'z') or (letter>='A' and letter<='Z')):
               print(word)
               word = ''
               state=1
            
            if ((letter == ' ')):
                print(word)
                word =''
                state = 0   
            
            if (letter == '\"') :
                print(word)
                word = ''
                state = 10



        elif(state==3):#   condition("==","<>","(",")")
            

            if((letter>='0' and letter<='9') or (letter=='.')):
               print(word)
               word = letter
               state = 2

            if((letter >= 'a' and letter <= 'z') or (letter>='A' and letter<='Z')):
               print(word)
               word = letter
               state=1  

            if ((letter == ' ')):
                word =''
                state = 0   
            
            if (letter == "") :
                state = 3
                

        
        
        elif(state == 10):
            
            if(letter=='\"'):
              
                print(w)
                w=""
                state=0

            w = w+letter
            state=10
            
            


