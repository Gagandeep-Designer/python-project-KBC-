# Create a program capable of displaying questions to the user like KBC
# use list data type to store the questions and their correct answers
# Display the final amount the person is taking home after playing the game

import tkinter as  tk

p=tk.Tk()
p.title("************WELCOME IN THE KON BNE GA KOORPATI GAME*********** 👍")
my_label=tk.Label(p,text="*******\U0001F91D KON BNE GA \nKROOORPATI******👍",font=("Arial bold",70),background=("pink"))
my_label.grid(column=0,row=0)
p.mainloop()
print("****WELCOME IN THE KON BNE GA KOORPATI GAME****")
print(" ")
question_list=[
    "1.What is the capital of India",
    "2.What is the currency of japan",
    "3.Who is the Best Leader of India",
    "4.Which is following Prime number a)4 b)9 c)11 d)15"
    ]

prices=[
    1000,
    20000,
    40000,
    80000
]
print(" ")
while True:
     print("Your Question list:\n",question_list)
     print("Your Prices List:\n",prices)
            
         
        #using function to check if answer is correct
     user_choice=int(input("Enter your Question:="))
     if user_choice==1:
                print("What is Capital of India ?")
                print("1.New Delhi \n2.Delhi\n3.Maharastera...")
                # if user_choice==1:
                answer=input("Enter your answer......")
                if answer=='1' or answer=='new delhi':
                    print("CORRECT ANSWER.....\U0001f44f \n")
                    print("You are win the Game And collect the 1000 RS.\n" )
                else:
                    print("Sorry You are wrong.....!\n")
                    print("You lossing 1000 RS...Otherwise Well Done app Bhout Asha khele.....\n")
            
     elif user_choice==2:
                print("2.What is the currency of japan ?")
                print("1.Dollar \n2.Yen\n3.Rupee....")
                # if user_choice==2:
                answer=input("Enter your answer......")
                if answer=='2' or answer=='yen':
                    print("CORRECT ANSWER.....\U0001f44f\n")
                    print("You are win the Game And collect the 20,000 RS.\n" )
                else:
                    print("Sorry You are wrong.....!\n")
                    print("You lossing 20,000 RS...Otherwise Well Done app Bhout Asha khele.....\n")
            
     elif user_choice==3:
                print("3.Who is the Best Leader of India ?")
                print("1.Mahatma Gandhi Ji \n2.DR. Br Ambedkar\n3.Nrinder Modi Ji....")
                # if user_choice==2:
                answer=input("Enter your answer......")
                if answer=='2' or answer=='dr.br ambedkar':
                    print("CORRECT ANSWER.....\U0001f44f\n")
                    print("You are win the Game And collect the 40,000 RS.\n" )
                else:
                    print("Sorry You are wrong.....!\n")
                    print("You lossing 40,000 RS...Otherwise Well Done app Bhout Asha khele.....\n")

     elif user_choice==4:
                print("4.Which is following Prime number?")
                print("1.a)4 \n2.b)9\n3.c)11....")
                # if user_choice==3:
                answer=input("Enter your answer......")
                if answer=='3' or answer=='11':
                    print("CORRECT ANSWER.....\U0001f44f\n")
                    print("You are win the Game And collect the 80,000 RS.\n" )
                else:
                    print("Sorry You are wrong.....!\n")
                    print("You lossing 80,000 RS...Otherwise Well Done app Bhout Asha khele.....\n")
     else:
            print("you are lost the Game KON BNE GA KROORPATI......\n")             

