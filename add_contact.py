with open('index.html', 'r') as f:
    html = f.read()

# 1. Zmień linki "Get in touch" z showCS() na scroll do sekcji
html = html.replace(
    'onclick="showCS()">Get in touch</a></li>',
    'href="#contact">Get in touch</a></li>'
)
html = html.replace(
    'onclick="toggleMenu();showCS()">Get in touch</a>',
    'href="#contact" onclick="toggleMenu()">Get in touch</a>'
)

# 2. Dodaj sekcję contact przed zamknięciem </main> lub przed stopką
contact_section = '''
<!-- GET IN TOUCH -->
<section id="contact" style="position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="contact-bg.jpg" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center;filter:brightness(0.35);">
    <div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(11,9,6,0.5) 0%,rgba(11,9,6,0.2) 50%,rgba(11,9,6,0.7) 100%);"></div>
  </div>
  <div style="position:relative;z-index:1;text-align:center;padding:48px 24px;max-width:480px;margin:0 auto;">
    <p style="font-size:10px;letter-spacing:0.42em;text-transform:uppercase;color:rgba(201,168,76,0.7);margin-bottom:32px;font-family:'DM Sans',sans-serif;">Get in touch</p>
    <a href="mailto:hello@vellumrecords.com" style="display:block;font-size:18px;font-weight:300;color:#e8e2d9;text-decoration:none;letter-spacing:0.08em;margin-bottom:48px;font-family:'DM Sans',sans-serif;transition:color 0.3s;" onmouseover="this.style.color='#c9a84c'" onmouseout="this.style.color='#e8e2d9'">hello@vellumrecords.com</a>
    <div style="display:flex;gap:32px;justify-content:center;align-items:center;">
      <a href="https://www.instagram.com/vellum.records" target="_blank" rel="noopener" aria-label="Instagram" style="color:rgba(240,236,228,0.5);text-decoration:none;transition:color 0.3s;" onmouseover="this.style.color='#c9a84c'" onmouseout="this.style.color='rgba(240,236,228,0.5)'">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>
      </a>
      <a href="https://www.tiktok.com/@vellumrecords" target="_blank" rel="noopener" aria-label="TikTok" style="color:rgba(240,236,228,0.5);text-decoration:none;transition:color 0.3s;" onmouseover="this.style.color='#c9a84c'" onmouseout="this.style.color='rgba(240,236,228,0.5)'">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.18 8.18 0 004.78 1.52V6.76a4.85 4.85 0 01-1.01-.07z"/></svg>
      </a>
    </div>
    <p style="margin-top:48px;font-size:10px;letter-spacing:0.2em;color:rgba(240,236,228,0.25);font-family:'DM Sans',sans-serif;text-transform:uppercase;">Warsaw, Poland</p>
  </div>
</section>
'''

# Wstaw przed stopką
html = html.replace(
    '<footer',
    contact_section + '<footer'
)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
