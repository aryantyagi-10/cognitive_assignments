import re;
paragraph = """Technology has transformed the way we live, work, and communicate. 
From smartphones to artificial intelligence, innovation continues to shape our future. 
The internet connects people across the globe in an instant. 
Automation and machine learning are changing industries and creating new opportunities. 
While technology can sometimes feel overwhelming, it offers incredible tools for solving real-world problems.""";

words_more_than_5 = re.findall(r'\b[a-zA-Z]{6,}\b', paragraph);
print("All words with more than 5 letters are\n",words_more_than_5);
numbers = re.findall(r'\b\d+\b', paragraph);
print("\nAll numbers in text are\n",numbers);
capitalized_words = re.findall(r'\b[A-Z][a-z]+\b', paragraph);
print("\nAll capitalized words are\n",capitalized_words);

alpha_words = re.findall(r'\b[a-zA-Z]+\b', paragraph);
print("\nWords containing only alphabets (removing digits and special character)\n",alpha_words);
vowel_words = [word for word in alpha_words if word.lower().startswith(('a', 'e', 'i', 'o', 'u'))];
print("\nAll words starting with a vowel are\n",vowel_words);