with open('index.html', 'r') as f:
    html = f.read()

html = html.replace(
    '.email-input::placeholder{color:#3a3530;}',
    '.email-input::placeholder{color:rgba(255,255,255,0.35);}'
)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
