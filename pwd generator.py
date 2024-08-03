import random
import pyperclip
n=int(input("enter the number of times you need a random password:"))
for i in range(n):
  print("welcome to simple password generator")
  answer=input('Generator random password?(yes/no) :')
  if answer.lower()=='yes':
    print("wait....")
    print("------------------------------------")
    print("Here you have it!")
    print("------------------------------------")
    def shuffle(string):
      tempList = list(string)
      random.shuffle(tempList)
      return ''.join(tempList)
    uppercaseLetter1=chr(random.randint(65,90)) 
    uppercaseLetter2=chr(random.randint(65,90))
    uppercaseLetter3=chr(random.randint(65,90))
    uppercaseLetter4=chr(random.randint(65,90))
    lowercaseLetter5=chr(random.randint(97,122))
    Number6=chr(random.randint(48,57))
    lowercaseLetter7=chr(random.randint(97,122))
    Number8=chr(random.randint(48,57))
    Number9=chr(random.randint(48,57))
    symbol10=chr(random.randint(36,36))

    password = uppercaseLetter1 + uppercaseLetter2  + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter5 + Number6 + lowercaseLetter7 + Number8 + Number9 + symbol10
    password = shuffle(password)
    print(password)
    pyperclip.copy(password)
    spam = pyperclip.paste()
    print("------------------------------------")
    print("THE PASSWORD IS COPIED TO YOUR CLIPBOARD.")
    print("------------------------------------")
    print("JUST PASTE IT WHEREVER YOU WANT")
    print("------------------------------------")
    print("ThankYou!")
    print("...................................................")

    answer2=input("Are you satisfied?:")
    if answer2.lower()=='yes':
      print("Thank you")
      print(".................................................")
      
    elif answer2.lower()=="no":
      print("sorry for the inconvenience caused .. looking after the problems asap .. thanks!")
      print(".................................................")

    else:
      print("------------------------------------")
      print("I think there's a typo error")
      
  elif answer.lower()=="no":
    print('Okay!')
    print('Fun fact : There are more than 2000 computer languages in use')
    print(".......................................................................................")
    break
  
  else:
    print(" \nI hope you have wrongly typed .. please type the words correctly")
    print("...........................................................................")


    
    

  
        



  



