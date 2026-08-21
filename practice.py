import random 

words = ["ironman","thor","hawkeye","wanda","vision"]

word = random.choice(words)
print(word)

jumble = "".join(random.sample(word,len(word)))
#print(jumble)

chance = 3

print("-"*30)
print("---Avengers jumble bumble---")
print("-"*30)


while chance!=0:
    print("the word is",jumble)

    guess = input("enetr your guessed word:").lower()
    if guess == word:
        print("correct guess!!")
        print("you won!")
        print()
        break
    else:
        chance -= 1
        print("incorrect guess!!")
        print("Remaning chances are:",chance)
        print()
else:
    print("all you chance are exhausted")
    print("you lose")
    print("the correct word is",word)


print("thank you for playing")