import back
import random

randWord=random.randint(0,len(back.word)-1)
randWordPos=random.randint(0,len(back.word[randWord])-1)
# print(randWordPos,randWord,back.word[randWord])
# print(back.word[randWord][randWordPos])
def showWord():
  keyWord=back.word[randWord]
  keyWordPos=keyWord.replace(back.word[randWord][randWordPos],'_')
  return keyWordPos
def gameStart():
  i=0
  flag=1
  print(f'''key word is ===>  {showWord()}''')
  userInput=input('entr the latter == ')
  while not back.word[randWord][randWordPos]==userInput and i<len(back.picture):
    
    print(back.picture[i])
    userInput=input('entr the latter == ')
    i+=1
  if back.word[randWord][randWordPos]==userInput:
    print('you are winner')
  else:
    print('you are loser')
# showWord()
print()
print('''++++++++++++++ Hello guys welcome to game ++++++++++++++''')
print()
print('                            ++++')
print()
print('                             😂')
print()
gameStart()