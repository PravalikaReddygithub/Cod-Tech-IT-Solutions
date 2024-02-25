# Define question categories
categories = {
    "history": [
        {"question": "Who is the first person to walk on the moon?", "choices": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"], "answer": 1},
        {"question": "What year did World War II begin?", "choices": ["1945", "1941", "1939", "1945"], "answer": 3},
        {"question": "Who was the first president of the United States?", "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "answer": 1},
        {"question": "Which ancient civilization built the Great Pyramid of Giza?", "choices": ["Greeks", "Egyptians","Romans", "Persians"], "answer": 2}
    ],
    "science": [
        {"question": "What is the smallest unit of life?", "choices": [ "Atom", "Molecule", "Organelle","Cell"], "answer": 4},
        {"question": "What does DNA stand for?", "choices": ["Deoxyribonucleic acid", "Deoxyribose nucleic acid", "Deoxyribose nucleotide acid", "Deoxyribose nitrogenous acid"], "answer": 1},
        {"question": "Who developed the theory of relativity?", "choices": ["Isaac Newton", "Galileo Galilei","Albert Einstein",  "Stephen Hawking"], "answer": 3},
        {"question": "What is the chemical symbol for gold?", "choices": ["Ag", "Au", "Fe", "Cu"], "answer": 2}
    ],
    "geography": [
        {"question": "What is the capital of France?", "choices": [ "Rome", "Berlin", "Madrid","Paris"], "answer": 4},
        {"question": "Which continent is the largest by land area?", "choices": ["Asia", "Africa", "North America", "South America"], "answer": 1},
        {"question": "What is the longest river in the world?", "choices": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": 1},
        {"question": "Which country is known as the Land of the Rising Sun?", "choices": [ "China", "South Korea", "Japan","Vietnam"], "answer": 3}
    ],
    "literature": [
        {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": [ "J.K. Rowling", "George Orwell", "Harper Lee","Mark Twain"], "answer": 3},
        {"question": "Which Shakespeare play is the famous quote 'To be, or not to be' from?", "choices": ["Hamlet", "Macbeth", "Romeo and Juliet", "Othello"], "answer": 1},
        {"question": "Who is the author of '1984'?", "choices": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Philip K. Dick"], "answer": 1},
        {"question": "Which novel begins with the line, 'It was the best of times, it was the worst of times'?", "choices": [ "Pride and Prejudice", "Moby-Dick", "The Great Gatsby","A Tale of Two Cities"], "answer": 4}
    ],
    "maths": [
        {"question": "What is the result of 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": 2},
        {"question": "What is the square root of 25?", "choices": ["3", "4", "5", "6"], "answer": 3},
        {"question": "What is 8 multiplied by 8?", "choices": ["48", "56", "64", "72"], "answer": 3},
        {"question": "What is the value of pi (π) to two decimal places?", "choices": ["3.14", "3.16", "3.18", "3.20"], "answer": 1}
    ]
}

# Function to display question and choices
def display_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"], start=1):
        print(f"{i}. {choice}")

# Function to ask question and check answer
def ask_question(question):
    display_question(question)
    user_choice = input("Enter your choice : ").strip()
    try:
        user_choice = int(user_choice)
        if user_choice == question["answer"]:
            return True
        else:
            print("Incorrect choice.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

# Main program loop
score = 0
for category, questions in categories.items():
    print(f"\n** {category.upper()} Category:")
    for question in questions:
        if ask_question(question):
            score += 1

# Display final score and feedback
total_questions = sum(len(questions) for questions in categories.values())
print(f"\nYour final score is: {score}/{total_questions}")
if score == total_questions:
    print("Congratulations! You answered all questions correctly!")
elif score > total_questions / 2:
    print("Great job! You did well.")
else:
    print("Don't worry, keep practicing and you'll improve!")
