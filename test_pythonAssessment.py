from pythonAssessment import count_specific_word, most_common_word, average_word_length, count_paragraphs, count_sentences

def test_count_specific_word():
    text = "Hello world! This is a test. Hello again."
    word = "Hello"
    result = count_specific_word(text, word)
    assert result == 2

def test_count_specific_word_empty_string():
    text = "Hello world! This is a test. Hello again."
    word = ""
    result = count_specific_word(text, word)
    assert result == 0

def test_most_common_word():
    text = "Hello world! This is a test. Hello again."
    result = most_common_word(text)
    assert result == "Hello"

def test_average_word_length():
    text = "Hello world! This is a test."
    result = average_word_length(text)
    assert result == 3.5

def test_count_paragraphs():
    text = "Hello world!\n\nThis is a test.\n\nHello again."
    result = count_paragraphs(text)
    assert result == 3

def test_count_sentences():
    text = "Hello world! This is a test. Hello again?"
    result = count_sentences(text)
    assert result == 3
