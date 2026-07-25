import os
import glob

search_text = '<li><a href="sports.html">Sports</a></li>'
replace_text = '''<li class="menu-item-has-children"><a href="sports.html">Sports</a>
                          <ul class="sub-menu">
                            <li><a href="yoga-day.html">Yoga Day</a></li>
                            <li><a href="badminton-day.html">Badminton Day</a></li>
                            <li><a href="cricket-day.html">Cricket Day</a></li>
                            <li><a href="plant-day.html">Plant Day</a></li>
                          </ul>
                        </li>'''

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_text in content:
        content = content.replace(search_text, replace_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filepath}')
