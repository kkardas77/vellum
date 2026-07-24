with open('index.html', 'r') as f:
    html = f.read()

old = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7J08B65J82"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-7J08B65J82');
</script>"""

new = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7J08B65J82"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'region': ['EEA', 'GB']
  });
  gtag('js', new Date());
  gtag('config', 'G-7J08B65J82');
</script>"""

html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
