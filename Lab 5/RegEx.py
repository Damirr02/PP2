import re
with open('row.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Ex 1
pattern = r'ab*'
matches = re.findall(pattern, content)
print("Matches found:")
for match in matches:
    print(match)
    
# Ex 2
pattern = r'ab{2,3}'
matches = re.findall(pattern, content)
print("Matches found:")
for match in matches:
    print(match)
    
# Ex 3
pattern = r'\b[a-z]+_[a-z]+\b'
matches = re.findall(pattern, content)
print("Matches found:")
for match in matches:
    print(match)

# Ex 4
pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, content)
print("Matches found:")
for match in matches:
    print(match)

# Ex 5
pattern = r'a.*b$'
matches = re.findall(pattern, content)
print("Matches found:")
for match in matches:
    print(match)
    
# Ex 6
pattern = r'(,) | (.) | ( )'
modified_content = re.sub(pattern, ':', content)
print("Modified content:")
print(modified_content)

# Ex 7
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = ''.join(word.capitalize() for word in words[:1] + [word.capitalize() for word in words[1:]])
    return camel_case
snake_case_string = content.strip()  # Strip any leading/trailing whitespace
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case string:", camel_case_string)

# Ex 8
pattern = r'(?=[A-Z])'
parts = re.split(pattern, content)
print("Resulting parts:")
for part in parts:
    print(part)
    
# Ex 9
def insert_spaces(text):
    modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return modified_text

modified_content = insert_spaces(content)
print("Modified content:")
print(modified_content)

# Ex 10
def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper() and snake_case:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

camel_case_string = content.strip()
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case string:", snake_case_string)