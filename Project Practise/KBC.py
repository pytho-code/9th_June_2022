


intro="""

                WELCOME TO KBC
"""
kbc={
    1:{ 
        "question":"In a row of boys Akash is fifth from the left and Nikhil is eleventh from the right. If Akash is twenty-fifth from the right then how many boys are there between Akash and Nikhil?",
        "A":14,
        "B":13,
        "C":12,
        "D":15,
        "Ans":"A"
        },
    2:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    3:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    4:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    5:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    6:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    7:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    8:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    9:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },
    10:
    {
        "question" : "How many times in a day, are the hands of a clock in straight line but opposite in direction?",
        "A":22,
        "B":23,
        "C":24,
        "D":48,
        "Ans":"B"
    },

}

status=True
print(intro)
score=0
while status:
    for q in kbc:
        print(kbc[q]["question"])
        print("A.",kbc[q]["A"])
        print("B.",kbc[q]["B"])
        print("C.",kbc[q]["C"])
        print("D.",kbc[q]["D"])
        Answer=input("Enter your Answer: ")
        if kbc[q]["Ans"].lower()==Answer.lower():
            print(kbc[q]["Ans"])
            score=score+50
            print("Correct Answer")
            print("Score:",score)
            #print(" ")
        else:
            score=score-50
            print("Wrong Answer")
            print("Score:",score)
            break
            

    print(f"Your final score is {score}!\n\n")

    choice=input("Would you like to play again?: (y/n) ")
    if choice=="n" or choice=="no":
         status=False
    else:
            status=True


    
        


