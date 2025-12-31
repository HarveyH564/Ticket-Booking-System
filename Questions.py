def create_event_map():
    return

def create_question():
    return

def delete_question():
    return

def respond_to_question():
    return


import json
from datetime import datetime


def create_question(user, question):
# New question
    try:
        with open("questions.json", "r") as f:
            questions = json.load(f)
    except:
        questions = []

    new_question = {
        "id": len(questions) + 1,
        "user": user,
        "question": question,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "answered": False
    }

    questions.append(new_question)

    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    return new_question


def get_user_questions(username):
# Questions from specific user
    try:
        with open("questions.json", "r") as f:
            all_questions = json.load(f)
    except:
        return []

    user_questions = [q for q in all_questions if q["user"] == username]
    return user_questions


def get_unanswered_questions():
# Unanswered questions (Admin function)
    try:
        with open("questions.json", "r") as f:
            all_questions = json.load(f)
    except:
        return []

    unanswered = [q for q in all_questions if not q["answered"]]
    return unanswered


def respond_to_question(question_id, answer):
# Answer question (Admin function)
    try:
        with open("questions.json", "r") as f:
            questions = json.load(f)
    except:
        return False

    for question in questions:
        if question["id"] == question_id:
            question["answered"] = True
            question["answer"] = answer
            question["answered_time"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            break

    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    return True


def delete_question(question_id):
# Delete question (Admin function)
    try:
        with open("questions.json", "r") as f:
            questions = json.load(f)
    except:
        return False

    questions = [q for q in questions if q["id"] != question_id]

    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    return True