with open('index.html', 'r') as f:
    html = f.read()

old = '''#stcm-wrapper {
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

new = '''#stcm-wrapper {
  --primaryColor: #c9a84c;
  --backgroundColor: rgba(20, 18, 12, 0.92);
  --textColor: rgba(240, 236, 228, 0.75);
  --iconColor: #c9a84c;
  --iconBackgroundColor: rgba(20, 18, 12, 0.92);
  --fontSize: 12px;
  --promptMaxWidth: 300px;
  --boxShadow: 0 2px 20px rgba(0,0,0,0.4);
  --borderRadius: 4px;
}
#stcm-wrapper .stcm-logo { display: none !important; }
#stcm-wrapper .stcm-credit { display: none !important; }
#stcm-prompt {
  border: 0.5px solid rgba(201, 168, 76, 0.2) !important;
  backdrop-filter: blur(8px) !important;
}'''

html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
