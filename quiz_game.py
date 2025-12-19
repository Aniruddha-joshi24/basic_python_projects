print("Welcome to my computer quiz!") 

playing = input("Do you want to play?(yes/no) ")

if playing.lower() != "yes":
    quit()
print("Okay let the games begin! :) ")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("YOU GOT THAT RIGHT")
    score += 1
else:
    print("Incorrect!")


answer = input("what does GPU stand for? ")
if answer.lower()== "graphic processing unit":
    print("YOU GOT THAT RIGHT")
    score += 1
else:
    print("Incorrect!")


answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("YOU GOT THAT RIGHT")
    score += 1
else:
    print("Incorrect!")


answer = input("what does psu stand for? ")
if answer.lower() == "power supply unit":
    print("YOU GOT THAT RIGHT")
    score += 1
else:
    print("Incorrect!")

print("You got " +str(score) + "question correct!")
percentage = (score / 4) * 100
print(f"You got {percentage}% incorrect")
