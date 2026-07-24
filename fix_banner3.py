with open('index.html', 'r') as f:
    html = f.read()

old = '--backgroundColor: rgba(20, 18, 12, 0.92);'
new = '--backgroundColor: rgba(20, 18, 12, 0.65);'

html = html.replace(old, new)

old2 = '--iconBackgroundColor: rgba(20, 18, 12, 0.92);'
new2 = '--iconBackgroundColor: rgba(20, 18, 12, 0.65);'

html = html.replace(old2, new2)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
