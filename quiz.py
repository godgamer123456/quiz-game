import random
import time

def line():
    print("=" * 45)

def welcome():
    line()
    print("           THE QUIZ CHALLENGE")
    line()
    print("Answer questions, earn points, and beat")
    print("your high score!")
    line()

def choose_difficulty():
    print("\nChoose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Mixed")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        elif choice == "4":
            return "Mixed"
        else:
            print("Please enter a number from 1 to 4.")

def get_questions():
    questions = {
        "Easy": [
            ("What is 7 + 8?", ["A. 14", "B. 15", "C. 16", "D. 17"], "B"),
            ("How many days are in a week?", ["A. 5", "B. 6", "C. 7", "D. 8"], "C"),
            ("What color do you get by mixing red and blue?", ["A. Green", "B. Orange", "C. Yellow", "D. Purple"], "D"),
            ("Which animal barks?", ["A. Cat", "B. Dog", "C. Horse", "D. Fish"], "B"),
            ("How many legs does a spider have?", ["A. 6", "B. 8", "C. 10", "D. 4"], "B"),
            ("What is 20 divided by 4?", ["A. 4", "B. 5", "C. 6", "D. 8"], "B"),
            ("Which season comes after spring?", ["A. Winter", "B. Autumn", "C. Summer", "D. Spring"], "C"),
            ("How many months are in a year?", ["A. 10", "B. 11", "C. 12", "D. 13"], "C"),
            ("What is the opposite of tall?", ["A. Short", "B. Wide", "C. Long", "D. Big"], "A"),
            ("Which animal is known as man's best friend?", ["A. Cat", "B. Dog", "C. Rabbit", "D. Bird"], "B"),
            ("How many wheels does a bicycle have?", ["A. 1", "B. 2", "C. 3", "D. 4"], "B"),
            ("What is 9 x 3?", ["A. 18", "B. 21", "C. 27", "D. 30"], "C"),
            ("Which of these is a fruit?", ["A. Carrot", "B. Potato", "C. Apple", "D. Lettuce"], "C"),
            ("What do bees make?", ["A. Milk", "B. Honey", "C. Bread", "D. Juice"], "B"),
            ("How many hours are in a day?", ["A. 12", "B. 18", "C. 24", "D. 30"], "C")
        ],
        "Medium": [
            ("What is the capital of Japan?", ["A. Seoul", "B. Tokyo", "C. Beijing", "D. Bangkok"], "B"),
            ("What is 12 x 12?", ["A. 124", "B. 132", "C. 144", "D. 154"], "C"),
            ("Which planet is closest to the Sun?", ["A. Venus", "B. Earth", "C. Mars", "D. Mercury"], "D"),
            ("How many sides does an octagon have?", ["A. 6", "B. 7", "C. 8", "D. 9"], "C"),
            ("What is the largest ocean?", ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"], "B"),
            ("Who wrote Romeo and Juliet?", ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. J.K. Rowling"], "C"),
            ("What is the square root of 81?", ["A. 7", "B. 8", "C. 9", "D. 10"], "C"),
            ("Which gas do plants absorb?", ["A. Oxygen", "B. Carbon dioxide", "C. Hydrogen", "D. Helium"], "B"),
            ("How many continents are there?", ["A. 5", "B. 6", "C. 7", "D. 8"], "C"),
            ("What is the largest mammal?", ["A. Elephant", "B. Giraffe", "C. Blue whale", "D. Shark"], "C"),
            ("Which country is famous for the pyramids of Giza?", ["A. Greece", "B. Egypt", "C. Italy", "D. India"], "B"),
            ("What is 15% of 200?", ["A. 15", "B. 20", "C. 30", "D. 40"], "C"),
            ("Which organ pumps blood around the body?", ["A. Brain", "B. Liver", "C. Heart", "D. Lung"], "C"),
            ("What is the freezing point of water in Celsius?", ["A. 0", "B. 10", "C. 32", "D. 100"], "A"),
            ("Which language is mainly spoken in Brazil?", ["A. Spanish", "B. Portuguese", "C. French", "D. English"], "B")
        ],
        "Hard": [
            ("What is the chemical symbol for gold?", ["A. Go", "B. Ag", "C. Au", "D. Gd"], "C"),
            ("What is the smallest prime number?", ["A. 0", "B. 1", "C. 2", "D. 3"], "C"),
            ("Which planet has the most prominent ring system?", ["A. Mars", "B. Saturn", "C. Venus", "D. Mercury"], "B"),
            ("What is the capital of Canada?", ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"], "C"),
            ("How many bones are in the adult human body?", ["A. 186", "B. 196", "C. 206", "D. 216"], "C"),
            ("What is the hardest natural substance?", ["A. Iron", "B. Diamond", "C. Quartz", "D. Granite"], "B"),
            ("Which scientist developed the theory of relativity?", ["A. Isaac Newton", "B. Galileo Galilei", "C. Albert Einstein", "D. Nikola Tesla"], "C"),
            ("What is the chemical formula for water?", ["A. CO2", "B. H2O", "C. O2", "D. NaCl"], "B"),
            ("Which country invented paper?", ["A. India", "B. Egypt", "C. China", "D. Greece"], "C"),
            ("What is 17 squared?", ["A. 279", "B. 289", "C. 299", "D. 309"], "B"),
            ("Which blood cells help fight infections?", ["A. Red blood cells", "B. Platelets", "C. White blood cells", "D. Plasma"], "C"),
            ("What is the largest desert in the world?", ["A. Sahara", "B. Gobi", "C. Antarctic Desert", "D. Arabian Desert"], "C"),
            ("Which element has the atomic number 1?", ["A. Helium", "B. Hydrogen", "C. Oxygen", "D. Carbon"], "B"),
            ("What is the capital of New Zealand?", ["A. Auckland", "B. Christchurch", "C. Wellington", "D. Hamilton"], "C"),
            ("How many degrees are in a triangle's angles combined?", ["A. 90", "B. 180", "C. 270", "D. 360"], "B")
        ]
    }

    return questions

def ask_question(question, number, total, points, streak):
    print()
    line()
    print("Question", number, "of", total)
    print("Current points:", points)
    print("Correct streak:", streak)
    line()
    print(question[0])

    for option in question[1]:
        print(option)

    while True:
        answer = input("Your answer: ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Enter A, B, C, or D.")

def play_quiz():
    all_questions = get_questions()
    difficulty = choose_difficulty()

    if difficulty == "Mixed":
        questions = []

        for category in all_questions.values():
            questions.extend(category)

        random.shuffle(questions)
    else:
        questions = all_questions[difficulty].copy()
        random.shuffle(questions)

    while True:
        try:
            amount = int(input("\nHow many questions do you want? (5-15): "))

            if 5 <= amount <= 15:
                break
            else:
                print("Choose a number between 5 and 15.")
        except ValueError:
            print("Please enter a valid number.")

    questions = questions[:amount]

    score = 0
    correct = 0
    wrong = 0
    streak = 0
    best_streak = 0
    results = []

    start_time = time.time()

    print("\nGet ready!")
    time.sleep(1)

    for number, question in enumerate(questions, 1):
        answer = ask_question(
            question, number, len(questions), score, streak
        )

        if answer == question[2]:
            print("\nCorrect!")
            correct += 1
            streak += 1
            points = 10

            if streak >= 3:
                points += 5
                print("Streak bonus! +5 points")

            score += points
            print("You earned", points, "points!")

            if streak > best_streak:
                best_streak = streak
        else:
            print("\nWrong answer!")
            print("Correct answer:", question[2])
            wrong += 1
            streak = 0

        results.append((question[0], answer, question[2]))
        time.sleep(0.5)

    elapsed = round(time.time() - start_time, 1)
    percentage = correct / len(questions) * 100

    line()
    print("              FINAL RESULTS")
    line()
    print("Difficulty:", difficulty)
    print("Questions answered:", len(questions))
    print("Correct answers:", correct)
    print("Wrong answers:", wrong)
    print("Accuracy:", round(percentage, 1), "%")
    print("Points earned:", score)
    print("Best streak:", best_streak)
    print("Time taken:", elapsed, "seconds")

    if percentage == 100:
        print("\nPerfect score! You got every question right!")
    elif percentage >= 80:
        print("\nAmazing job! You really know your stuff.")
    elif percentage >= 60:
        print("\nGood work! You did pretty well.")
    elif percentage >= 40:
        print("\nNot bad. A little more practice will help.")
    else:
        print("\nKeep practicing and see if you can do better!")

    print("\nWould you like to review your answers?")
    review = input("Enter yes or no: ").strip().lower()

    if review in ["yes", "y"]:
        for question, answer, correct_answer in results:
            print("\n" + question)
            print("Your answer:", answer)
            print("Correct answer:", correct_answer)

    return score, correct, len(questions), elapsed

def show_statistics(games, total_correct, total_questions, best_score):
    line()
    print("             GAME STATISTICS")
    line()

    print("Games played:", games)
    print("Total correct answers:", total_correct)
    print("Total questions answered:", total_questions)
    print("Highest points in one game:", best_score)

    if total_questions > 0:
        accuracy = total_correct / total_questions * 100
        print("Overall accuracy:", round(accuracy, 1), "%")
    else:
        print("Play a game to start your statistics!")

    line()

def main():
    games = 0
    total_correct = 0
    total_questions = 0
    best_score = 0

    welcome()

    while True:
        print("\nMAIN MENU")
        print("1. Play Quiz")
        print("2. View Statistics")
        print("3. How to Play")
        print("4. Quit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            score, correct, total, elapsed = play_quiz()

            games += 1
            total_correct += correct
            total_questions += total

            if score > best_score:
                best_score = score

            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            show_statistics(
                games, total_correct, total_questions, best_score
            )
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            line()
            print("HOW TO PLAY")
            line()
            print("Choose a difficulty and number of questions.")
            print("Answer each question with A, B, C, or D.")
            print("Correct answers earn 10 points.")
            print("Three or more correct answers in a row")
            print("give you 5 bonus points per correct answer.")
            print("Try to get the highest score possible!")
            line()
            input("\nPress Enter to return to the menu...")

        elif choice == "4":
            print("\nThanks for playing the Quiz Challenge!")

            if games > 0:
                print("You played", games, "game(s).")
                print("Your best score was", best_score, "points.")

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
