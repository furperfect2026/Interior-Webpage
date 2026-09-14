import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the literal backticks and r n, and change 1 to 3
content = content.replace('data-val="1">0</h3>
                    <p', 'data-val="3">0</h3>\n                    <p')

# Update the JS
content = content.replace('target === 100 || target === 1', 'target === 100 || target === 3')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed.')
