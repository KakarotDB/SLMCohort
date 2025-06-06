import string
from collections import Counter
import os


def count_word_frequency(filepath):
    word_counts = Counter()

    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        return word_counts

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.split()
                word_counts.update(words)
    except Exception as e:
        print(f"An unexpected error occurred while processing the file '{filepath}': {e}")

    return word_counts


def print_top_n_words(word_counts, n=5):
    if not word_counts:
        print("No words were counted (file might be empty or contained only punctuation/whitespace).")
        return

    print(f"\n--- Top {n} Most Common Words ---")
    top_words = word_counts.most_common(n)

    if not top_words:
        print(f"Could not determine top {n} words (perhaps the file had fewer than {n} unique words).")
        return

    for word, count in top_words:
        print(f"'{word}': {count} times")


if __name__ == "__main__":
    print("--- Word Frequency Counter for a Text File ---")
    print("This program will count word frequencies and show the top 5 most common words.")

    test_file_name = "sample_text_for_word_count.txt"
    sample_content = """
    This is a sample text file created for testing purposes.
    It contains sample text, and more text, text everywhere.
    Text is good. Sample good sample, good.
    The quick brown fox jumps over the lazy dog.
    Dog, fox, cat, dog, mouse.
    Python is great, Python is fun.
    """
    try:
        with open(test_file_name, 'w', encoding='utf-8') as f:
            f.write(sample_content.strip())
        print(f"\nSuccessfully created a sample file: '{test_file_name}'")
        print("You can edit this file or specify another file for analysis.")
    except Exception as e:
        print(f"Could not create sample file '{test_file_name}': {e}")
        test_file_name = ""

    if not test_file_name or input("\nUse the created sample file? (yes/no): ").lower().strip() == 'no':
        test_file_name = input("Please enter the name (or full path) of the text file to analyze: ")

    print(f"\nAnalyzing file: '{test_file_name}'")
    word_frequencies = count_word_frequency(test_file_name)
    print_top_n_words(word_frequencies, 5)

    print("\n--- Program finished ---")
