with open('index.html', 'r') as f:
    html = f.read()

html = html.replace(
    '#stcm-preferences {\n  background-color: #0e0c09 !important;\n  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;\n  backdrop-filter: blur(12px) !important;\n}',
    '#stcm-preferences {\n  background-color: #0e0c09 !important;\n  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;\n  backdrop-filter: blur(12px) !important;\n}\n#stcm-preferences .stcm-credit-link,\n#stcm-preferences a[href*="silktide"] { display: none !important; }\n#stcm-preferences footer { background: #0e0c09 !important; border-top: 0.5px solid rgba(201,168,76,0.15) !important; }'
)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
