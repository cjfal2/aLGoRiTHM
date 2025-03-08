import sys
input = sys.stdin.readline

def generate_feedback(secret, guess):
    feedback = ["X"] * 5
    secret_list = list(secret)
    
    for i in range(5):
        if guess[i] == secret_list[i]:
            feedback[i] = "*"
            secret_list[i] = None
    
    for i in range(5):
        if feedback[i] == "X" and guess[i] in secret_list:
            feedback[i] = "!"
            secret_list[secret_list.index(guess[i])] = None
    
    return "".join(feedback)

def count_possible_words(dictionary, secret, feedback):
    count = 0
    for word in dictionary:
        if generate_feedback(secret, word) == feedback:
            count += 1
    return count


N = int(input().strip())
dictionary = [input().strip() for _ in range(N)]
secret = dictionary[0]
G = int(input().strip())
feedbacks = [input().strip() for _ in range(G)]


for feedback in feedbacks:
    print(count_possible_words(dictionary, secret, feedback))
