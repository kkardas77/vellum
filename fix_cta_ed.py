with open('index.html', 'r') as f:
    html = f.read()

html = html.replace(
    'color:#2e2a24;margin-bottom:48px;font-weight:400;',
    'color:rgba(255,255,255,0.45);margin-bottom:48px;font-weight:400;'
)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
