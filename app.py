def quiz_app():
    print("Welcome to Gamified Study Quest")
    questions = [
    {
        "question": "Which of the following is the correct way to output 'Hello, World!' to the screen in Python 3?",
        "choices": {
            "A": 'print "Hello, World!"',
            "B": 'console.log("Hello, World!")',
            "C": 'print("Hello, World!")',
            "D": 'printf("Hello, World!")'
        },
        "answer": "C",
        "explanation": "In Python 3, print() is a built-in function, so the text must be enclosed within parentheses."
    },
    {
        "question": "Which built-in data type would you use to store a logical value that can only be either True or False?",
        "choices": {
            "A": "bool",
            "B": "int",
            "C": "str",
            "D": "float"
        },
        "answer": "A",
        "explanation": "The bool (Boolean) data type represents logical states: True or False."
    },
    {
        "question": "What is the data type returned by the expression type(5.0) in Python?",
        "choices": {
            "A": "<class 'int'>",
            "B": "<class 'str'>",
            "C": "<class 'bool'>",
            "D": "<class 'float'>"
        },
        "answer": "D",
        "explanation": "Any number written with a decimal point (like 5.0) is treated as a floating-point number (float) in Python."
    },
    {
        "question": "How many times will the block of code inside the following loop execute?\nfor i in range(3):\n    print(i)",
        "choices": {
            "A": "2 times",
            "B": "3 times",
            "C": "4 times",
            "D": "Infinite times"
        },
        "answer": "B",
        "explanation": "range(3) generates numbers starting from 0 up to, but not including, 3 (0, 1, 2). This means the loop runs exactly 3 times."
    },
    {
        "question": "Which keyword is used to immediately exit or terminate out of a loop in Python?",
        "choices": {
            "A": "exit",
            "B": "stop",
            "C": "break",
            "D": "continue"
        },
        "answer": "C",
        "explanation": "The break statement terminates the current loop loop and resumes execution at the next statement."
    }
    ]
