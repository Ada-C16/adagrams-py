import pytest

from adagrams.game import word_in_english_dictionary


def test_word_in_english_dictionary_valid_word_returns_true():
    # Arrange
    word = "banana"

    # ACT
    is_valid = word_in_english_dictionary(word)
    
    # Assert
    assert is_valid == True



def test_word_in_english_dictionary_invalid_word_returns_false():
    # Arrange
    word = "xlkdfa;elkfjl"
    
    # Act 
    is_valid = word_in_english_dictionary(word)

    # Assert
    assert is_valid == False