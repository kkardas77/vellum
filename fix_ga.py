with open('index.html', 'r') as f:
    html = f.read()

ga_tag = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7J08B65J82"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-7J08B65J82');
</script>'''

html = html.replace('<title>Vellum Records</title>', '<title>Vellum Records</title>\n' + ga_tag)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
