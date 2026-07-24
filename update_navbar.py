import os
import glob
import re

def update_navbars():
    # Read index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Extract the header block
    header_pattern = re.compile(r'<!-- Start header -->.*?<!-- end of header -->', re.DOTALL)
    
    match = header_pattern.search(index_content)
    if not match:
        print("Could not find header block in index.html")
        # Try a more generic pattern
        header_pattern = re.compile(r'<header id="header".*?</header>', re.DOTALL)
        match = header_pattern.search(index_content)
        if not match:
            print("Could not find generic header block either. Aborting.")
            return

    new_header = match.group(0)
    print(f"Extracted header from index.html (length: {len(new_header)})")

    # Iterate through all html files
    html_files = glob.glob('*.html')
    updated_count = 0

    for file in html_files:
        if file == 'index.html':
            continue

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace header in the current file
        # We try to replace the block bounded by <!-- Start header --> and <!-- end of header -->
        # or just <header id="header"...>...</header>
        
        if '<!-- Start header -->' in content and '<!-- end of header -->' in content:
            new_content = re.sub(r'<!-- Start header -->.*?<!-- end of header -->', new_header, content, flags=re.DOTALL)
        else:
            new_content = re.sub(r'<header id="header".*?</header>', new_header, content, flags=re.DOTALL)

        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"Updated navbar in {file}")

    print(f"Done! Updated navbar in {updated_count} files.")

if __name__ == '__main__':
    update_navbars()
