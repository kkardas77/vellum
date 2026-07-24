with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('rgba(20, 18, 12, 0.65)', 'rgba(20, 18, 12, 0.35)')

with open('index.html', 'w') as f:
    f.write(html)
print('done')
