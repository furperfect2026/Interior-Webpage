import os
import glob

files = glob.glob('*.html')

nav_links = '''<nav class="hidden md:flex gap-8 text-white font-medium">
                <a href="index.html" class="hover:text-primary transition-colors">Home</a>
                <a href="about.html" class="hover:text-primary transition-colors">About Us</a>
                <a href="portfolio.html" class="hover:text-primary transition-colors">Portfolio</a>
                <a href="faq.html" class="hover:text-primary transition-colors">FAQ</a>
                <a href="contact.html" class="hover:text-primary transition-colors">Contact</a>
            </nav>'''

seo_tags = '''<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Raza Enterprises provides the best interior design services in Pune, Dhanori, and surrounding areas. We specialize in luxury residential, commercial, and turnkey interior projects with our in-house factory.">
    <meta name="keywords" content="Interiors Near me, Best Interiors In Pune, Best Interiors In Dhanori, Interior Designers in Pune, Luxury Home Interiors, Commercial Interior Design, Turnkey Interior Projects, Raza Enterprises, Home Decor, Best Interior Decorators, Interior Design Company, 2 BHK interior design cost in Pune, factory made furniture Pune, turnkey contractors Dhanori">
    <meta name="author" content="Raza Enterprises">'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    import re
    # Replace nav
    content = re.sub(r'<nav class="hidden md:flex gap-8 text-white font-medium">.*?</nav>', nav_links, content, flags=re.DOTALL)
    
    # Replace SEO
    content = re.sub(r'<meta name="viewport" content="width=device-width, initial-scale=1.0">.*?</title>', seo_tags + '\n    <title>' , content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Updated files')
