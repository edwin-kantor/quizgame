#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz Game CLI - Main Program

A command-line quiz game where users answer multiple-choice questions.
"""

# TODO 🇺🇸: Import utility functions from utils.py
# TODO 🇷🇴: Importă funcțiile utilitare din utils.py


def ask_question(question_dict, question_number):
    """
    Display a question and get user answer
    
    Args:
        question_dict: Dictionary containing question, options, and answer
        question_number: Current question number (1-based)
    
    Returns:
        True if answer is correct, False otherwise
    """
    # TODO 🇺🇸: Display question with number, display all options,
    #          get user input, normalize answer, check if correct,
    #          return True if correct, False otherwise
    # TODO 🇷🇴: Afișează întrebarea cu numărul, afișează toate
    #          opțiunile, obține input de la utilizator, normalizează
    #          răspunsul, verifică dacă este corect, returnează True
    #          dacă este corect, False altfel

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    pass


def check_answer(user_answer, correct_answer):
    """
    Check if user answer matches correct answer
    
    Args:
        user_answer: Normalized user answer
        correct_answer: Correct answer
    
    Returns:
        True if answer is correct, False otherwise
    """
    # TODO 🇺🇸: Compare user_answer with correct_answer and
    #          return True if they match, False otherwise
    # TODO 🇷🇴: Compară user_answer cu correct_answer și
    #          returnează True dacă se potrivesc, False altfel

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    pass


def show_feedback(is_correct, correct_answer, options):
    """
    Display feedback for user's answer
    
    Args:
        is_correct: True if answer is correct, False otherwise
        correct_answer: Correct answer letter
        options: List of option strings
    """
    # TODO 🇺🇸: Print formatted feedback message showing
    #          if answer is correct or incorrect, and display
    #          the correct answer with full option text
    # TODO 🇷🇴: Afișează mesaj de feedback formatat arătând
    #          dacă răspunsul este corect sau incorect, și afișează
    #          răspunsul corect cu textul complet al opțiunii

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    pass


def show_final_score(score, total_questions):
    """
    Display final quiz results
    
    Args:
        score: Final score (number of correct answers)
        total_questions: Total number of questions
    """
    # TODO 🇺🇸: Print formatted final score display showing
    #          score, total questions, and percentage
    # TODO 🇷🇴: Afișează scorul final formatat arătând
    #          scorul, numărul total de întrebări și procentul

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    pass


def main():
    """
    Main program loop
    """
    # TODO 🇺🇸: Get questions list, initialize score to 0,
    #          loop through all questions, ask each question,
    #          update score if answer is correct, display feedback
    #          after each question, show current score, and display
    #          final score at the end
    # TODO 🇷🇴: Obține lista de întrebări, inițializează scorul la 0,
    #          iterează prin toate întrebările, întreabă fiecare
    #          întrebare, actualizează scorul dacă răspunsul este corect,
    #          afișează feedback după fiecare întrebare, arată scorul
    #          actual și afișează scorul final la sfârșit

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    pass


if __name__ == "__main__":
    main()
