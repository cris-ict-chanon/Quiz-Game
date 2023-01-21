print("Lady&Gentle men welcome to my fitness quiz")
playing = input("Type yes to proceed with the quiz: ")

if playing.lower() != "yes":
    quit()

print("shall we start!")
score = 0
answer = input("1.What is the monomer of proteins? ").lower()
if answer == "amino acids":
    print("Good Job!")
    score += 1
else:
    print("Nice try")

answer = input("2.What does kJ stand for? ").lower()
if answer == "kilojoules":
    print("Good Job!")
    score += 1
else:
    print("Nice try")

answer = input("3.which macronutrient helps with building muscles? ").lower()
if answer == "proteins":
    print("Good Job!")
    score += 1
else:
    print("Nice try")

answer = input("4.who is the current classic physique champion? ").lower()
if answer == "christ bumstead":
    print("Good Job!")
    score += 1
else:
    print("Nice try")

answer = input("5.what does PPL stand for? ").lower()
if answer == "push pull leg":
    print("Good Job!")
    score += 1
else:
    print("Nice try")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5)* 100)+ "%.")