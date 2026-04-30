# ============================================================
# 			QUIZ NIGHT HOST
# ============================================================

# Import modules
import requests      # Used to call the free Open Trivia Database API
import html          # Used to convert HTML entities into normal text as there are a lot of html codes in the API
import random        # Used to shuffle answer options randomly

# Base URL for the trivia API
API_BASE_URL = "https://opentdb.com/api.php"

# Categories dictionary: menu number -> (category name, API ID)
# Used to display choices and fetch questions from the API
# Used the link to get the category numbers
CATEGORIES = {
    "1": ("General Knowledge", 9),
    "2": ("Science & Nature", 17), 	
    "3": ("History", 23),
    "4": ("Geography", 22),
    "5": ("Sports", 21),
    "6": ("Music", 12),
    "7": ("Movies", 11),
    "8": ("Video Games", 15),
}

# Difficulty levels available for the quiz
DIFFICULTIES = ["easy", "medium", "hard"]

# Base score per difficulty: easy = 5, medium = 10, hard = 15
BASE_SCORES = {"easy": 5, "medium": 10, "hard": 15}


# ============================================================
# 			API FUNCTIONS
# ============================================================

def fetch_questions(amount, category_id, difficulty):
    """
    Fetch multiple-choice questions from the Open Trivia Database API.
    
    API usage explanation:
    - Endpoint: https://opentdb.com/api.php
    - Parameters:
        amount     : number of questions to fetch
        category   : numeric ID from CATEGORIES
        difficulty : "easy", "medium", or "hard"
        type       : "multiple" for multiple-choice only
    - No API key is required; completely free and open.
    - Returns a list of question dictionaries in JSON format
      or None if an error occurs.
    """
    # Prepare parameters for API call
    params = {
        "amount": amount,
        "category": category_id,
        "difficulty": difficulty,
        "type": "multiple"
    }

    try:
        # Send GET request to API
        response = requests.get(API_BASE_URL, params=params, timeout=8)
        response.raise_for_status()      # Raises error if HTTP status is bad
        data = response.json()          # Convert JSON string to Python dict

        # Check if API returned valid results
        if data["response_code"] == 0:
            return data["results"]       # Return list of question dicts
        else:
            print("No questions found for that category/difficulty.")
            return None

    except requests.exceptions.RequestException:
        # Catch network errors or timeouts
        print("Error connecting to API.")
        return None


def decode_question(raw):
    """
    Decode a raw question from the API.
    
    - Converts HTML stuff to normal characters
    - Returns a cleaned dictionary with:
      question, correct answer, incorrect answers, difficulty, category
    """
    return {
        "question": html.unescape(raw["question"]),           # Decode question text
        "correct": html.unescape(raw["correct_answer"]),     # Decode correct answer
        "incorrect": [html.unescape(x) for x in raw["incorrect_answers"]],  # Decode incorrect options
        "difficulty": raw["difficulty"],                     # Difficulty level
        "category": raw["category"],                         # Category name
    }


# ============================================================
# 			GAME LOGIC FUNCTIONS
# ============================================================

def shuffle_answers(correct, incorrect):
    """
    Combine correct and incorrect answers, shuffle randomly.
    Returns:
        answers -> shuffled list
        correct_index -> index of the correct answer in the shuffled list
    """
    answers = incorrect + [correct]      # Combine into single list
    random.shuffle(answers)              # Random the order
    correct_index = answers.index(correct)  # Find where correct answer ended up
    return answers, correct_index


def calculate_points(difficulty):
    """
    Return points based on question difficulty.
    Easy = 5 pts, Medium = 10 pts, Hard = 15 pts
    """
    return BASE_SCORES[difficulty]


# ============================================================
# 		USER INPUT FUNCTIONS
# ============================================================

def prompt_name():
    """
    Ask the player to enter their name.
    Ensures name has at least 2 characters.
    Provides default if input not available.
    """
    while True:
        try:
            name = input("Enter your name: ").strip()   # Remove extra spaces
        except:
            # Fallback if input() fails 
            print("Input not available. Using default name.")
            return "Player"

        if len(name) >= 2:
            return name     # Return valid name
        print("Name must be at least 2 characters.")


def prompt_category():
    """
    Show category menu and let player choose.
    Returns a tuple: (category_name, category_id)
    """
    print("\nChoose a category:")
    for key, (name, _) in CATEGORIES.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Your choice: ").strip()
        if choice in CATEGORIES:
            return CATEGORIES[choice]    # Return selected category
        print("Invalid choice. Enter a number from the menu.") # error checking


def prompt_difficulty():
    """
    Show difficulty menu and let player choose.
    Returns the chosen difficulty as a string.
    """
    print("\nChoose difficulty:")
    # in enumerate lets you loop through interable and have access to both index and element itself
    for i, d in enumerate(DIFFICULTIES, 1):
        print(f"{i}. {d}")

    while True:
        choice = input("Your choice: ").strip()
        if choice in ("1", "2", "3"):
            return DIFFICULTIES[int(choice) - 1]
        print("Invalid choice. Enter 1, 2, or 3.")


def prompt_count():
    """
    Ask player how many questions they want.
    Only allows 5, 10, or 15.
    """
    while True:
        num = input("How many questions (5/10/15): ").strip()
        if num in ("5", "10", "15"):
            return int(num)
        print("Invalid choice. Enter 5, 10, or 15.")


# ============================================================
# 			QUIZ LOOP FUNCTION
# ============================================================

def run_quiz(questions):
    """
    Main gameplay loop:
    - Presents each question
    - Shuffles answers
    - Checks player's choice
    - Updates score
    Returns total score.
    """
    score = 0                         # Initialize score
    for i, raw in enumerate(questions, 1):  # Loop through questions
        q = decode_question(raw)      # Decode HTML characters

        answers, correct_idx = shuffle_answers(q["correct"], q["incorrect"])  # Mix answers

        # Display question number and text
        print(f"\nQ{i}: {q['question']}")

        # Display all options with letter labels
        labels = ["A", "B", "C", "D"]
        for label, ans in zip(labels, answers):
            print(f"{label}. {ans}")

        # Input validation loop
        while True:
            choice = input("Your answer: ").strip().upper()  # Convert to uppercase
            if choice in labels:
                player_idx = labels.index(choice)             # Map letter to index
                break
            print("Enter A, B, C, or D.")

        # Check if player chose the correct answer
        if player_idx == correct_idx:
            points = calculate_points(q["difficulty"])      # Get points for difficulty
            score += points                                 # Add to total score
            print(f"Correct! +{points} points")
        else:
            print(f"Wrong! The correct answer was: {q['correct']}")

    return score   # Return total score after all questions


# ============================================================
# 		SAVE RESULTS FUNCTION
# ============================================================

def save_results(name, score, total):
    """
    Save final results to a plain text file.
    - Filename: playername_results.txt
    - Contents: player name, score, total questions
    """
    filename = f"{name}_results.txt"     # Simple, safe filename
    with open(filename, "w") as f:       # Open file for writing
        f.write(f"Player: {name}\n")
        f.write(f"Score: {score}\n")
        f.write(f"Questions: {total}\n")
    print(f"Results saved to {filename}")


# ============================================================
# 			MAIN FUNCTION
# ============================================================

def main():
    """
    Main program:
    - Greet player
    - Get name, category, difficulty, question count
    - Fetch questions from API
    - Run the quiz
    - Display and save results
    """
    print("QUIZ NIGHT HOST")

    # Get player info
    name = prompt_name()
    category_name, category_id = prompt_category()
    difficulty = prompt_difficulty()
    count = prompt_count()

    # Fetch questions from the API
    print("Loading questions...")
    questions = fetch_questions(count, category_id, difficulty)

    if not questions:   # Stop if API failed
        print("Could not fetch questions. Exiting.")
        return

    # Run the quiz and get final score
    score = run_quiz(questions)

    # Show score
    print(f"\nFinal Score: {score}")

    # Save results to file
    save_results(name, score, count)
    
    # Ask if the user wants to play again
    while True:
        play_again = input("Do you want to play again (y/n)").strip().lower()
        if play_again == "y":
            main()
            break 
        elif play_again == "n":
            print (f"Thanks for playing {name}! See you next time!")
            break
        else:
            play_again = input("Please enter either y or n")


# ============================================================
# 			START THE GAME
# ============================================================

if __name__ == "__main__":
    main()