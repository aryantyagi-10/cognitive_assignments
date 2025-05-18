import re;

text = """Technology has transformed the way we live, work, and communicate.
From smartphones to artificial intelligence, innovation continues to shape our future.
The internet connects people across the globe in an instant.
Automation and machine learning are changing industries and creating new opportunities.
While technology can sometimes feel overwhelming, it offers incredible tools for solving real-world problems.
Contact us at support@example.com or visit https://www.tech-news.com. 
You can also call us at 123-456-7890 or +91 9876543210.""";

def custom_tokenize(text):
    pattern = r"""
        (?:[a-zA-Z]+(?:['’][a-zA-Z]+)?)     
        |(?:\d+\.\d+)                        
        |(?:\d+)                            
        |(?:[a-zA-Z]+(?:-[a-zA-Z]+)+)       
""";
    tokens = re.findall(pattern, text, re.VERBOSE);
    return tokens;

def clean_text(text):
    text = re.sub(r'\b[\w.-]+?@\w+?\.\w+?\b', '<EMAIL>', text);
    text = re.sub(r'https?://\S+|www\.\S+', '<URL>', text);
    text = re.sub(r'\b(?:\+91\s?)?\d{10}\b', '<PHONE>', text);
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', '<PHONE>', text);
    return text;

cleaned_text = clean_text(text);
print("Cleaned Text:\n", cleaned_text);

tokens = custom_tokenize(cleaned_text);
print("\nCustom Tokens:",tokens);
