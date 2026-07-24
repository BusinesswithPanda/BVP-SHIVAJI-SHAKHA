import os
import glob
import re

# Read contact.html to get the exact footer
with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the footer block
match = re.search(r'(<!-- start footer -->.*?<!-- end footer -->)', content, re.DOTALL | re.IGNORECASE)
if not match:
    print('Could not find footer in contact.html')
    exit(1)

new_footer = match.group(1)

html_files = glob.glob('*.html')
updated = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Check if this file has a footer
    if '<!-- start footer -->' in file_content and '<!-- end footer -->' in file_content:
        # Replace the footer block
        new_content = re.sub(r'<!-- start footer -->.*?<!-- end footer -->', lambda m: new_footer, file_content, flags=re.DOTALL | re.IGNORECASE)
        if file_content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1

print(f'Updated footer in {updated} HTML files.')
