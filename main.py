#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz Game CLI - Main Program

A command-line quiz game where users answer multiple-choice questions.
"""

# Import utility functions from utils.py
from utils import get_questions, normalize_answer, get_user_answer

def ask_question(question_dict, question_number):
    """
    Display a question and get user answer
    """
    print(f"Question {question_number}: {question_dict['question']}")
    for option in question_dict['options']:
        print(option)

    user_answer = get_user_answer()
    is_correct = check_answer(user_answer, question_dict['answer'])
    return is_correct

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def show_feedback(is_correct, correct_answer, options):
    if is_correct:
        print("Correct!\n")
    else:
        correct_text = next(opt for opt in options if opt.startswith(correct_answer))
        print(f"Wrong! The correct answer is {correct_text}.\n")

def show_final_score(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"Final Score: {score}/{total_questions} ({percentage:.2f}%)")

def show_round_result(is_correct, correct_answer, options, score, question_number):
    show_feedback(is_correct, correct_answer, options)
    print(f"Current Score: {score}/{question_number}")

def main():
    questions = get_questions()
    score = 0

    for i, question in enumerate(questions, start=1):
        is_correct = ask_question(question, i)
        if is_correct:
            score += 1
        show_round_result(is_correct, question['answer'], question['options'], score, i)

    show_final_score(score, len(questions))

if __name__ == "__main__":
    main()

