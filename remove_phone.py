import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove personal phone number and replace with placeholder
    content = content.replace('+91 900611274', '+91 XXXXXXXXXX')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Removed personal number.')
