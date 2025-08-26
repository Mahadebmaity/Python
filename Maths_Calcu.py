from random import randint 
def Mathemeical_Quiz():
    score = Wrong_score = j= k = 0
    Wrong_Questions = {}
    Correct_Questions ={}
    def user_validation():
        user_input = input("How many times to play Quiz game?? (Not above 20)Defualt 10! =>> ").strip()
        
        if user_input == "":  
            return 10
        elif not user_input.isdigit():  
            print("Invalid input! Please enter a number.")
            return user_validation()
        else:
            user_input = int(user_input)
            if user_input > 20:
                print("Please choose 20 or below.")
                return user_validation()
            else:
                return user_input

    Choice = user_validation()
    for i in range(Choice):
        cc = randint(1,3)
        if cc == 1:
            a = randint(1, 15)
            b = randint(1, 10)
            answer = int(input(f"Qno{i+1}: What is {a} x {b} ?= "))
            if answer == a * b:
                print("Correct!")
                Correct_Questions.setdefault(j+1, []).append(f"Qno{i+1}: What is {a} x {b} ?={a * b} ")
                j+=1
                score += 1
            else:
                print("Wrong!")
                Wrong_Questions.setdefault(k+1, []).append(f"Qno{i+1}: What is {a} x {b} ?={a * b} ")
                k +=1
                Wrong_score += 1
        elif cc == 2:
            a = randint(1, 15)
            b = randint(1, 10)
            answer = int(input(f"Qno{i+1}: What is {a} + {b} ?= "))
            if answer == a + b:
                print("Correct!")
                Correct_Questions.setdefault(j+1, []).append(f"Qno{i+1}: What is {a} + {b} ?={a + b}")
                j +=1
                score += 1
            else:
                print("Wrong!")
                Wrong_Questions.setdefault(k+1, []).append(f"Qno{i+1}: What is {a} + {b} ?={a + b} ")
                k +=1
                Wrong_score += 1
        elif cc == 3:
            a = randint(1, 15)
            b = randint(1, 10)
            if a >= b:
                answer = int(input(f"Qno{i+1}: What is {a} - {b} ?= "))
                if answer == a - b:
                    print("Correct!")
                    Correct_Questions.setdefault(i+1, []).append(f"Qno{i+1}: What is {a} - {b} ?={a - b} ")
                    score += 1
                else:
                    print("Wrong!")
                    Wrong_Questions.setdefault(k+1, []).append(f"Qno{i+1}: What is {a} - {b} ?={a - b} ")
                    k +=1
                    Wrong_score += 1
            else:
                answer = int(input(f"Qno{i+1}: What is {b} - {a} ?= "))
                if answer == b - a:
                    print("Correct!")
                    Correct_Questions.setdefault(j+1, []).append(f"Qno{i+1}: What is {a} - {b} ?={a - b} ")
                    j +=1
                    score += 1
                else:
                    print("Wrong!")
                    Wrong_Questions.setdefault(k+1, []).append(f"Qno{i+1}: What is {a} - {b} ?={a - b} ")
                    k +=1
                    Wrong_score += 1

    def Greetings_Learner():
        if not Wrong_Questions:
            correct_str = ""
            for qlist in Correct_Questions.values():
                correct_str += "".join(qlist) + "\n"
            return f"Congratulations Nice!\nYou attempted all questions and answered all correctly, Good Job!\n\nAll correct answers:\n{correct_str}"
        
        # If there are wrong questions
        wrong_str = ""
        for qlist in Wrong_Questions.values():
            wrong_str += "".join(qlist) + "\n"
        
        correct_str = ""
        for qlist in Correct_Questions.values():
            correct_str += "".join(qlist) + "\n"
        return f"Here are your wrong questions with answers:\n{wrong_str}\nCorrect questions:\n{correct_str}\nNeed more practice!\nThank you! Practice again please!"

    print(f"Number of questions: {Choice}\nYour total score is: {score}\nWrong:{Wrong_score}\n{Greetings_Learner()}")

Mathemeical_Quiz()