with open('index.html', 'r') as f:
    html = f.read()

# hero-sub - podnosimy opacity z 0.28 na 0.55
html = html.replace(
    'color:rgba(255,255,255,0.28);margin-bottom:56px;font-weight:400;',
    'color:rgba(255,255,255,0.55);margin-bottom:56px;font-weight:400;'
)

# spf-coda - podnosimy opacity z 0.28 na 0.65 i font-size z 14px na 17px
html = html.replace(
    'font-size:14px;font-weight:300;\n  color:rgba(240,236,228,0.28);',
    'font-size:17px;font-weight:300;\n  color:rgba(240,236,228,0.65);'
)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
