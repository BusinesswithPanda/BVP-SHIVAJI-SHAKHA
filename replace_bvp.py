import glob, re

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # Case insensitive replacement, but preserve the original casing style if possible
        # Since usually it is 'BVP Moradabad' or 'BVP Moradabad'
        new_html = html.replace('BVP Moradabad', 'BVP Shivaji Shakha Moradabad')
        new_html = new_html.replace('BVP Moradabad', 'BVP SHIVAJI SHAKHA Moradabad')
        
        # Catch any lowercase or weird cases just in case
        new_html = re.sub(r'(?i)\bbvp Moradabad\b', 'BVP Shivaji Shakha Moradabad', new_html)
        
        if html != new_html:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_html)
            print(f'Updated text in {f}')
    except Exception as e:
        print(f'Error reading {f}')
print('Done!')
