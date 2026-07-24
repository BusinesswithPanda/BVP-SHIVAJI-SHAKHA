import glob, re

p = re.compile(r'(<div class="feature-card">.*?<h2>(?:Seva \(Service\)|Sanskar \(Values\)|Sahyog \(Cooperation\))</h2>.*?<div class="icon">\s*)<i class="[^"]+"></i>', re.DOTALL)

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        new_html = p.sub(r'\g<1><i class="flaticon-charity"></i>', html)
        
        if html != new_html:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_html)
            print(f'Updated icons in {f}')
    except Exception as e:
        print(f'Error reading {f}')
print('Done!')
