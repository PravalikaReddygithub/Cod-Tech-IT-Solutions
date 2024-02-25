# Define question categories
categories = {
    "history": [
        {"question": "Who is the first person to walk on the moon?", "choices": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"], "answer": "Neil Armstrong"},
        {"question": "What year did World War II begin?", "choices": ["1939", "1941", "1943", "1945"], "answer": "1939"},
        {"question": "Who was the first president of the United States?", "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "answer": "George Washington"},
        {"question": "Which ancient civilization built the Great Pyramid of Giza?", "choices": ["Egyptians", "Greeks", "Romans", "Persians"], "answer": "Egyptians"}
    ],
    "science": [
        {"question": "What is the smallest unit of life?", "choices": ["Cell", "Atom", "Molecule", "Organelle"], "answer": "Cell"},
        {"question": "What does DNA stand for?", "choices": ["Deoxyribonucleic acid", "Deoxyribose nucleic acid", "Deoxyribose nucleotide acid", "Deoxyribose nitrogenous acid"], "answer": "Deoxyribonucleic acid"},
        {"question": "Who developed the theory of relativity?", "choices": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Stephen Hawking"], "answer": "Albert Einstein"},
        {"question": "What is the chemical symbol for gold?", "choices": ["Au", "Ag", "Fe", "Cu"], "answer": "Au"}
    ],
    "geography": [
        {"question": "What is the capital of France?", "choices": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "Which continent is the largest by land area?", "choices": ["Asia", "Africa", "North America", "South America"], "answer": "Asia"},
        {"question": "What is the longest river in the world?", "choices": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": "Amazon"},
        {"question": "Which country is known as the Land of the Rising Sun?", "choices": ["Japan", "China", "South Korea", "Vietnam"], "answer": "Japan"}
    ],
    "literature": [
        {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": ["Harper Lee", "J.K. Rowling", "George Orwell", "Mark Twain"], "answer": "Harper Lee"},
        {"question": "Which Shakespeare play is the famous quote 'To be, or not to be' from?", "choices": ["Hamlet", "Macbeth", "Romeo and Juliet", "Othello"], "answer": "Hamlet"},
        {"question": "Who is the author of '1984'?", "choices": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Philip K. Dick"], "answer": "George Orwell"},
        {"question": "Which novel begins with the line, 'It was the best of times, it was the worst of times'?", "choices": ["A Tale of Two Cities", "Pride and Prejudice", "Moby-Dick", "The Great Gatsby"], "answer": "A Tale of Two Cities"}
    ],
    "maths": [
        {"question": "What is the result of 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "What is the square root of 25?", "choices": ["3", "4", "5", "6"], "answer": "5"},
        {"question": "What is 8 multiplied by 8?", "choices": ["48", "56", "64", "72"], "answer": "64"},
        {"question": "What is the value of pi (π) to two decimal places?", "choices": ["3.14", "3.16", "3.18", "3.20"], "answer": "3.14"}
    ]
}

# Function to display question and choices
def display_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i+1}. {choice}")

# Function to ask question and check answer
def ask_question(question):
    display_question(question)
    user_answer = input("Enter your answer: ").strip()
    if user_answer.lower() == question["answer"].lower():
        return True
    else:
        print("Incorrect answer.")
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
