import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update email domain to .co
    content = content.replace('razaenterprises.com', 'razaenterprises.co')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Updated email addresses.')
