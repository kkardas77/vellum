with open('index.html', 'r') as f:
    html = f.read()

# Dodaj JS który wymusza tło po otwarciu modalu
js_fix = """
<script>
// Fix modal background
document.addEventListener('DOMContentLoaded', function() {
  const observer = new MutationObserver(function() {
    const modal = document.querySelector('#stcm-modal');
    if (modal) {
      modal.style.setProperty('background-color', '#0e0c09', 'important');
      modal.style.setProperty('backdrop-filter', 'none', 'important');
    }
  });
  observer.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['style', 'class'] });
});
</script>"""

html = html.replace('</style>\n<script src="https://cdn.jsdelivr.net/gh/silktide', js_fix + '\n</style>\n<script src="https://cdn.jsdelivr.net/gh/silktide')

with open('index.html', 'w') as f:
    f.write(html)
print('done')
