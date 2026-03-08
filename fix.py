content = open('app.py', encoding='utf-8').read()

# Check what's actually at line 1452
lines = content.split('\n')
for i in range(1448, 1465):
    print(f"{i+1}: {repr(lines[i])}")