from collections import Counter
import string

# Sample text
text = """
Data science is amazing. It involves data, science, and creativity.
The more data, the better insights. Science and data go hand in hand.
"""

# Clean and tokenize text
words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()

# Count word frequency
word_counts = Counter(words)

# Display the top 5 most common words
print("Top 5 Most Frequent Words:")
for word, count in word_counts.most_common(5):
    print(f"{word}: {count}")
