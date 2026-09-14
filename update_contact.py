import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update Phone
    content = content.replace('+91 98765 43210', '+91 900611274')
    
    # Update Address in contact.html
    if f == 'contact.html':
        content = re.sub(r'123 Industrial Estate, Phase 4<br>Mumbai, Maharashtra 400001', 'Dhanori<br>Pune, Maharashtra 411047', content)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Updated contact details.')
