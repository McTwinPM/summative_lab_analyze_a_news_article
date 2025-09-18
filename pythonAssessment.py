import re
from collections import Counter
from pathlib import Path
import string

def main():
    # Read the article from the file
    file_path = Path('newsArticleForPythonAssessment.txt')
    article = read_article(file_path)
    while True:
        print("\n--- News Article Analysis Menu ---")
        print("1. Count occurrences of a specific word")
        print("2. Find the most common word")
        print("3. Calculate average word length")
        print("4. Count number of paragraphs")
        print("5. Count number of sentences")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        match choice:
            case '1':
                word = input("Enter the word to count: ")
                count_specific_word(article, word)
            case '2':
                identify_most_common_word(article)
            case '3':
                calculate_average_word_length(article)
            case '4':
                count_paragraphs(article)
            case '5':
                count_sentences(article)
            case '6':
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")

    
# Function to read the article
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Count occurrences of a specific word
def count_specific_word(article, word):
    count = 0
    words = [w.strip(string.punctuation).lower() for w in article.split()]
    if word == "":
        print("Please type a valid word.")
        return 0
    for w in words:
        if w == word:
            count += 1
    print(f'The word "{word}" appears {count} times in the article.')
    return count

# Most common word in the article
def identify_most_common_word(article):
    words = article.split()
    word_count = Counter(words)
    most_common = word_count.most_common(1)
    if most_common:
        print(f'The most common word is "{most_common[0][0]}" which appears {most_common[0][1]} times.')
        return most_common[0][0]

    else:
        print('No words found in the article.')
        return None
    
# Average word length
def calculate_average_word_length(article):
    words = article.split()
    words = [w.strip(string.punctuation) for w in words]
    total_length = sum(len(w) for w in words)
    average_length = total_length / len(words) if words else 0
    print(f'The average word length in the article is {average_length:.2f} characters.')
    return average_length

# Count number of paragraphs
def count_paragraphs(article):
    paragraphs = article.split('\n\n')
    print(f'The article contains {len(paragraphs)} paragraphs.')
    return len(paragraphs)

# Count number of sentences
def count_sentences(article):
    sentences = re.split(r'[.!?]+', article)
    # sentences = [s for s in sentences if s.strip()]
    print(f'The article contains {len(sentences)} sentences.')
    return len(sentences)

if __name__ == "__main__":
    main()