with open('index.html', 'r') as f:
    html = f.read()

old = '#stcm-preferences {\n  background-color: #0e0c09 !important;\n  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;\n  backdrop-filter: blur(12px) !important;\n}'

new = '#stcm-preferences {\n  background-color: #0e0c09 !important;\n  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;\n  backdrop-filter: blur(12px) !important;\n}\n#stcm-modal {\n  background-color: #0e0c09 !important;\n  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;\n}'

html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
