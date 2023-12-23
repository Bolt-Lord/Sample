from question_model import Question


question_data = {
    "response_code": 0,
    "results": [
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The Great Wall of China is visible from the moon.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "French is an official language in Canada.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "&quot;Ananas&quot; is mostly used as the word for Pineapple in other languages.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The Sun rises from the North.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "On average, at least 1 person is killed by a drunk driver in the United States every hour.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "In 2010, Twitter and the United States Library of Congress partnered together to archive every tweet by American citizens.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Adolf Hitler was born in Australia. ",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Jingle Bells was originally meant for Thanksgiving",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        }
    ]
}


def question_bank_list():
    question_bank = []
    for question in question_data['results']:
        new_question = Question(
            question['question'], question['correct_answer'])
        question_bank.append(new_question)
    return question_bank
