with open('index.html', 'r') as f:
    html = f.read()

html = html.replace(
    'background-color: rgba(20, 18, 12, 0.96) !important;',
    'background-color: #0e0c09 !important;'
)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
