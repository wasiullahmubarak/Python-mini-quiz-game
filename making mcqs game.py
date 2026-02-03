import random
#making mcqs game
#delearing a dictionary in which my all variable exists
questions = [
    # ===== Islamic History (1-5 as example) =====
    {
        "question": "Who was the first caliph after Prophet Muhammad (PBUH)?",
        "a": "Umar ibn Khattab",
        "b": "Ali ibn Abi Talib",
        "c": "Abu Bakr Siddiq",
        "d": "Uthman ibn Affan",
        "answer": "c"
    },
    {
        "question": "Which battle was fought in 624 CE between the Muslims and the Quraysh?",
        "a": "Battle of Uhud",
        "b": "Battle of Badr",
        "c": "Battle of Khandaq",
        "d": "Battle of Tabuk",
        "answer": "b"
    },
    {
        "question": "Who compiled the Quran into a single book form?",
        "a": "Ali ibn Abi Talib",
        "b": "Umar ibn Khattab",
        "c": "Abu Bakr Siddiq",
        "d": "Uthman ibn Affan",
        "answer": "d"
    },
    {
        "question": "Which Prophet is known as the builder of the Kaaba?",
        "a": "Prophet Muhammad (PBUH)",
        "b": "Prophet Ibrahim (AS)",
        "c": "Prophet Musa (AS)",
        "d": "Prophet Isa (AS)",
        "answer": "b"
    },
    {
        "question": "What is the Hijri year of the migration (Hijrah) of Prophet Muhammad (PBUH)?",
        "a": "622 CE",
        "b": "610 CE",
        "c": "632 CE",
        "d": "624 CE",
        "answer": "a"
    },

    # ===== Philosophy (6-7 as example) =====
    {
        "question": "Who is known as the father of modern philosophy?",
        "a": "Plato",
        "b": "Descartes",
        "c": "Aristotle",
        "d": "Socrates",
        "answer": "b"
    },
    {
        "question": "Which philosopher wrote 'The Republic'?",
        "a": "Plato",
        "b": "Aristotle",
        "c": "Kant",
        "d": "Hume",
        "answer": "a"
    },

    # ===== English Grammar (8-9 as example) =====
    {
        "question": "Choose the correct sentence:",
        "a": "She go to school daily.",
        "b": "She goes to school daily.",
        "c": "She going to school daily.",
        "d": "She gone to school daily.",
        "answer": "b"
    },
    {
        "question": "Identify the adjective in the sentence: 'The sky is blue.'",
        "a": "sky",
        "b": "is",
        "c": "blue",
        "d": "The",
        "answer": "c"
    },

    # ===== Pakistan History (10-11 as example) =====
    {
        "question": "When did Pakistan gain independence?",
        "a": "1945",
        "b": "1947",
        "c": "1948",
        "d": "1950",
        "answer": "b"
    },
    {
        "question": "Who was the founder of Pakistan?",
        "a": "Liaquat Ali Khan",
        "b": "Allama Iqbal",
        "c": "Muhammad Ali Jinnah",
        "d": "Zulfiqar Ali Bhutto",
        "answer": "c"
    }
]

while True:
    print("welcome to mini quiz project")
    score = 0
    random.shuffle(questions)
    for q in questions:
        print(q["question"])
        print("a)", q["a"])
        print("b)", q["b"])
        print("c)", q["c"])
        print("d)", q["d"])
        user_ask = input("enter your answer : option : a/b/c/d")
        if user_ask == (q["answer"]):
            print("you are right")
            score += 1
        else:
            print("wrong answer")
    print("This is the end of the game")
    print("your score is :", score, "out of" ,len(questions))
    wants_to_play=input ("do you want to play again ? y/n")
    print("wants_to_play")
    if wants_to_play == "y":
     break

