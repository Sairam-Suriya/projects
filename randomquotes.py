import random
ch=['1','2','3','4','5']
name=input("enter your name:").title()
Motivation=['When you have a dream, you have got to grab it and never let go','Nothing is impossible. The word itself says I am possible!','There is nothing impossible to they who will try']
Life=["The purpose of our lives is to be happy.","Life is what happens when you're busy making other plans.","Many of life’s failures are people who did not realize how close they were to success when they gave up."]
Success=["Without continual growth and progress, such words as improvement, achievement, and success have no meaning.","Try not to become a man of success, but rather try to become a man of value.","Success is a lousy teacher. It seduces smart people into thinking they can't lose."]
Love=["I am who I am because of you. You are every reason, every hope, and every dream I’ve ever had." , "Take my hand, take my whole life too. For I can’t help falling in love with you.", "I will never stop trying. Because when you find the one... you never give up." ]
Wisdom=["The fool doth think he is wise, but the wise man knows himself to be a fool.","Whenever you find yourself on the side of the majority, it is time to reform (or pause and reflect).","It is better to remain silent at the risk of being thought a fool, than to talk and remove all doubt of it."]
i = input("enter your choice: \n1.Motivation\n2.Life \n3.Success \n4.Love \n5.Wisdom \n")
if i not in ch:
     input("enter your choice")
if i=='1':
     print(name +" -> "+random.choice(Motivation))
elif i=='2':
     print(name +" -> "+random.choice(Life))
elif i=='3':
     print(name +" -> "+random.choice(Success))
elif i=='4':
     print(name +" -> "+random.choice(Love))
elif i=='5':
     print(name +" -> "+random.choice(Wisdom))
