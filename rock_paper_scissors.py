import random
print("ROCK PAPER SCISSORS")
your_move=input("choose your move :(rock/papers/scissors)")
computers_moves=["rock","paper","scissor"]
length=len(computers_moves)
computers_random_moves=computers_moves[random.randrange(0,length-1)]

if computers_random_moves==your_move:
    print("The Match Draws!!")
elif computers_random_moves=="rock" and your_move=="paper":
    print("HURRAY!! YOU WON")
    print("GAME OVER")
elif computers_random_moves=="paper" and your_move=="rock":
    print("AWW!! COMPUTER WON")
    print("GAME OVER! BETTER LUCK NEXT TIME")
elif computers_random_moves=="scissors" and your_move=="paper":
    print("AWW!! COMPUTER WON ")
    print("GAME OVER , BETTER LUCK NEXT TIME")
elif computers_random_moves=="paper" and your_move=="scissor":
    print("HURRAY!! YOU WON")
    print("GAME OVER")
else:
    print("please enter valid choice")
