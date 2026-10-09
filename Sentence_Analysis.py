sentence = input("Enter a sentence:")
sentence = " ".join(sentence.split())
sentence = sentence.lower()
words = sentence.split()
total_words = len(words)
python_count = words.count("python")

if words:
    longest_word = max(words, key=len)
else:
    longest_word = ""

print(sentence)
print("Total number of words:", total_words)
print('Number of times "python" appears:', python_count)
print(longest_word)