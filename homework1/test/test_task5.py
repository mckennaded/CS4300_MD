import pytest
from src.task5 import favorite_books, first_three_books, student_database

def test_first_three_books():
    assert first_three_books() == favorite_books[:3]

def test_student_database():
    assert student_database["Alice"] == 1001
    assert student_database.get("David") is None
