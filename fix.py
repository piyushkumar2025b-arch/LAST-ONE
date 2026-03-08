import re
content = open('app.py', encoding='utf-8').read()

# Remove both add_shape ellipse calls entirely
content = re.sub(
    r'\s*fig\.add_shape\(type="ellipse".*?\)\n',
    '\n',
    content,
    flags=re.DOTALL
)

print('FIXED' if 'add_shape' not in content else 'check manually')
open('app.py', 'w', encoding='utf-8').write(content)