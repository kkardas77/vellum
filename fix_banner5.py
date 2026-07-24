with open('index.html', 'r') as f:
    html = f.read()

old = '#stcm-prompt {\n  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;\n  backdrop-filter: blur(8px) !important;\n}'

new = '''#stcm-prompt {
  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;
  backdrop-filter: blur(8px) !important;
}
#stcm-preferences {
  background-color: rgba(20, 18, 12, 0.96) !important;
  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;
  backdrop-filter: blur(12px) !important;
}'''

html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
