print('welcome')
Developer = input('do you want to Developer?')
if Developer.lower() != "yes":  
    quit()
print ('ok lets start')
score =0
question = input("If LTP is correct, is order execution always correct?")
if question.lower() =="no":
    print('correct')
    score +=1
else:
    print('incorrect')
    
question = input("If stop-loss is set, is loss always fixed?")
if question.lower() =="no":
    print('correct')
    score +=1
else:
    print('incorrect')

question = input("Is algo trading fully automated?")
if question.lower() =="yes":
    print('correct')
    score +=1
else:
    print('incorrect')

question = input("Does algo trading use predefined rules?")
if question.lower() =="yes":
    print('correct')
    score +=1
else:
    print('incorrect')

question = input("Who is the first Prime Minister of India?")
if question.lower()=="jawaharlal nehru":
    print('correct')
    score +=1
else:
    print('incorrect')
print ("your score "+ str(score))
                