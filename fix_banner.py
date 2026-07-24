with open('index.html', 'r') as f:
    html = f.read()

old = '#stcm-wrapper {\n  --primaryColor: #C9A84C;\n  --backgroundColor: #111009;\n  --textColor: #f0ece4;\n  --iconColor: #c9a84c;\n  --iconBackgroundColor: #111009;\n}'

new = '''#stcm-wrapper {
  --primaryColor: #C9A84C;
  --backgroundColor: #111009;
  --textColor: #f0ece4;
  --iconColor: #c9a84c;
  --iconBackgroundColor: #111009;
  --fontSize: 13px;
  --promptMaxWidth: 320px;
}
#stcm-wrapper .stcm-logo { display: none !important; }
#stcm-wrapper .stcm-credit { display: none !important; }'''

html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
