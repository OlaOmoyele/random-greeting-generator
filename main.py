import random

word_choices: list = ['hello', 'goodbye', 'ni hao', 'ohayo', 'shalom']

greeting: str = random.choice(word_choices)

if __name__ == '__main__':
    print(greeting)
