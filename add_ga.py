with open('index.html', 'r') as f:
    html = f.read()
tag = '<!-- Google tag (gtag.js) -->\n<script async src="https://www.googletagmanager.com/gtag/js?id=G-7J08B65J82"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag("js", new Date());\n  gtag("config", "G-7J08B65J82");\n</script>\n'
html = html.replace('<meta name="viewport"', tag + '<meta name="viewport"', 1)
with open('index.html', 'w') as f:
    f.write(html)
print('done')
