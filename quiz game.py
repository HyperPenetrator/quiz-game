import random
import time

questions = [
    "Current Railway Minister of India is",
    "What is the capital of Australia?",
    "What does not grow on tree according to a popular Hindi saying?",
    "Which city is known as the Pink City of India?",
    "Who wrote India's National Anthem?",
    "How many major religions are there in India?",
    "What does HTML stand for?",
    "How many states are there in India?",
    "Where is India Gate located?",
    "Who wrote Vande Mataram?"
]

options = [
    ['Mamta Banarjee', 'Ram Vilash', 'Ashwini Vaishnaw', 'Piyush Goyal'],
    ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'],
    ['Money', 'Flowers', 'Leaves', 'Fruits'],
    ['Banglore', 'Maysore', 'Jaipur', 'Kochi'],
    ['Rabindranath Tagore', 'Lal Bahadur Shastri', 'Chetan Bhagat', 'RK Narayan'],
    [6, 7, 8, 9],
    ['Hyper Trainer Marking Language', 'HyperText Markup Language', 'HyperText Markdown Language', 'HighText Markup Language'],
    [28, 29, 31, 32],
    ['Agra', 'Punjab', 'Mumbai', 'New Delhi'],
    ['Sarat Chandra Chattopadhyay', 'Rabindranath Tagore', 'Bankim Chandra Chatterjee', 'Ishwar Chandra Vidyasagar']
]

answers = [
    'Ashwini Vaishnaw', 'Canberra', 'Money', 'Jaipur',
    'Rabindranath Tagore', 6, 'HyperText Markup Language', 28,
    'New Delhi', 'Bankim Chandra Chatterjee'
]

rewards = [0, 1000, 2500, 3000, 5000, 10000, 20500, 40000, 81000, 160000, 200000]

# Bundle the quiz content
quiz = list(zip(questions, options, answers))
random.shuffle(quiz)  # Shuffle questions

def display_question(q_data, q_number):
    question, opts, _ = q_data
    print(f"\nQ{q_number+1}: {question}")
    for idx, opt in enumerate(opts, start=1):
        print(f"{idx}. {opt}")
    print("⏳ You have 10 seconds to answer...")

def get_user_answer(q_data):
    _, opts, _ = q_data
    start_time = time.time()
    try:
        answer = input("Your answer (1-4 or type full answer): ").strip()
        if time.time() - start_time > 10:
            print("⌛ Time's up!")
            return None
    except:
        return None

    if answer.isdigit():
        idx = int(answer) - 1
        if 0 <= idx < 4:
            return str(opts[idx])
    return answer.title()

def run_quiz():
    score = 0
    for i, q_data in enumerate(quiz):
        display_question(q_data, i)
        user_ans = get_user_answer(q_data)
        correct_ans = str(q_data[2])

        if user_ans == correct_ans:
            score += 1
            print(f" Correct!  Current Reward: ₹{rewards[score]}")
        else:
            print(f" Incorrect or No Answer. Correct Answer: {correct_ans}")
            print(f" Final Reward: ₹{rewards[score]}")
            break  # Optional: End quiz on first wrong answer
    return score

def show_result(score):
    print("\n Quiz Over!")
    if score > 0:
        print(f" Total Correct: {score}")
        print(f" You won ₹{rewards[score]}!")
    else:
        print(" No correct answers. Better luck next time!")

# Run the game
if __name__ == "__main__":
    final_score = run_quiz()
    show_result(final_score)
