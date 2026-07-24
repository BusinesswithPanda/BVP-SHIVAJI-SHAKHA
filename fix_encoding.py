import glob

replacements = {
    'Ã¢â‚¬Å“': '\"',    # Left double quote
    'Ã¢â‚¬Â': '\"',     # Right double quote
    'Ã¢â‚¬â„¢': '\'',    # Apostrophe / right single quote
    'Ã¢â‚¬â€œ': '-',     # En dash
    'Ã¢â‚¬â€': '--',    # Em dash
    'Ã¢â‚¬Ëœ': '\'',    # Left single quote
    'Ã‚Â': ' ',         # Non-breaking space
    'Ã¢â‚¬Â ': '\" ',   # Sometimes trailing spaces map weird
}

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        new_html = html
        for broken, fixed in replacements.items():
            new_html = new_html.replace(broken, fixed)
            
        if html != new_html:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_html)
            print(f'Fixed encoding characters in {f}')
    except Exception as e:
        print(f'Error reading {f}')
print('Done!')
