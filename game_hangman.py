import random

# Hangman stages (same as you provided)
stages = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     // \\
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     // 
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """,
]

print("🎉 LET'S PLAY HANGMAN! 🎉")


words = ["apple", "banana", "cherry", "falcon", "grape", "horizon", "island", "jungle"]
random_word = random.choice(words)


display = ["_" for _ in random_word]
lives = len(stages) - 1


game_over = False
while not game_over:
    print("\n" + " ".join(display))
    user_choice = input("GUESS A LETTER: ").lower()

    if user_choice in display:
        print(f"You already guessed '{user_choice}'. Try again!")
        continue


    if user_choice in random_word:
        for position in range(len(random_word)):
            if random_word[position] == user_choice:
                display[position] = user_choice
    else:
        lives -= 1
        print(f"Wrong guess! You lost a life. Lives left: {lives}")


    if "_" not in display:
        game_over = True
        print("\n🎉 YOU WIN! The word was:", random_word)


    if lives == 0:
        game_over = True
        print(stages[0])
        print("\n😢 YOU LOSE! The word was:", random_word)
    else:
        print(stages[lives])
