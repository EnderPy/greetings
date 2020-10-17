import random
from random import randint;

#values
x = randint(1,2)
if x == 1:
     greetings1 = "Hi, "
else:
    greetings1 = "Hello, "
goodMood = ["good", "great", "amazing", "ok"]
badMood = ["bad", "horrible", "not good"]
neuMood = ["alright"]
moodtype = 0
#Chat
print("type your name:")
name = input()
print(greetings1 + name +".")

print("How was your day?")
mood = input()
if mood in goodMood:
    print("Thats Great,", name + ". What did you do?")
    moodtype == 0

if mood in badMood:
    print("Aww, Why was that?")
    moodtype == 1

activities = input()

if moodtype == 0:
    print("I love doing that!")
if moodtype == 1:
    print("That sounds awful.")

