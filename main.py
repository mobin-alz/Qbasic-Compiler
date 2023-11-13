def splitter(txt):
    word = ''
    state = 0
    res = []
    final = []
    
    for letter in txt:
        
        if (state == 0):  # Initial state
            if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                
                word += letter
                state = 1
            
            elif ((letter >= '0' and letter <= '9') or (letter == '.')):
                word += letter
                state = 2
            

            elif (letter == "<") : 
                word = letter 
                state = 3
                
            elif (letter == '='):
                
                word = letter
                state = 4
            
            elif (letter == '\"'):
                if word.strip():
                    res.append(word)
                word = ''
                word += letter
                state = 10
            
            elif (letter == ' '):
                word = ''
                state = 0
            
        elif (state == 1):  # Alphabets
            if ((letter >= '0' and letter <= '9') or (letter == '.')):
                res.append(word)
                word = letter
                state = 2
           
            elif ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                word += letter
           
            elif (letter == ' '):
                res.append(word)
                word = ''
                state = 0
           
            elif (letter == '('):
                res.append(word)
                state = 0
                word = ''
           
            elif (letter == '\"'):
                if word.strip():
                    res.append(word)
                word = ''
                word += letter
                state = 10
            
            elif letter == "=" : 
                res.append(word)
                word = ''
                state = 4

            elif letter == "<" : 
                res.append(word) 
                word = ""
                state = 3
      
        elif (state == 2):  # Numbers
            if ((letter >= '0' and letter <= '9') or (letter == '.')):
                word += letter
            else:
                res.append(word)
                word = ''
                state = 0
            if (letter == '\"'):
                if word.strip():
                    res.append(word)
                word = ''
                word += letter
                state = 10

            if letter == "=" : 
    
                word = letter 
                state = 4 

            if letter == "<" : 
                res.append(word) 
                word = ""
                state = 3

        elif (state == 3):  # Special characters (<)
            if (letter =='>'):
                res.append("un equal")
                word = letter
                state = 5
            elif ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                
                word = letter
                state = 1 
            elif ((letter >= '0' and letter <= '9') or (letter == '.')):
                word = letter
                state = 2
            
            elif (letter == ' '):
                word = ''
                state = 0
            
            
            
        elif (state == 4):  # Special characters (=)
            if (letter == "=" ):
                res.append("equal")
                word = ""
                state = 0

            else :     
                res.append("=")

                if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                    word = letter
                    state = 1 

                elif ((letter >= '0' and letter <= '9') or (letter == '.')):

                    word = letter
                    state = 2
                elif (letter == ' '):

                    word = ''
                    state = 0    
                else : 

                    word = ''
                    state = 0
            
        elif (state == 5):  # Special characters for > , ( , )

            if (letter in ['(', ')','>']):
                res.append(word)
                word = letter
            
            elif ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):    
                word = letter
                state = 1 
            
            elif ((letter >= '0' and letter <= '9') or (letter == '.')):
                word = letter
                state = 2
            
            elif (letter == ' '):
                word = ''
                state = 0    
        
        elif (state == 10):  # Double quotation
            if (letter == '\"'):
                word += letter
                res.append(word)
                word = ''
                state = 0
            else:
                word += letter
            state = 10
    
    for item in res : 
        if item :
            final.append(item)
    return final
            

with open("Codd1.txt" , "r") as file : 
    f = file.readlines()

data = {}
for a in f : 
    line = splitter(a)
    # print(line)
    for i,item in enumerate(line) :     
        
        if item == "Dim":
            
            if line[-1] == "integer" :
                data[line[i + 1]] = "int"

        if item == "=" :
            if line[i+1] != 'equal' :  
                data[line[i-1]] = line[i+1]


        if item == "if":
            a = data[line[i + 1]]
            equality = line[i + 2]
            b = data[line[i+3]]
            if equality == "equal" : 
                if int(a) == int(b) : 
                    print(line[-1])

            else : 
                if int(a) != int(b) : 
                    print(line[-1])









        
            
            
        
