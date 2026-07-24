with open('index.html', 'r') as f:
    html = f.read()

# Zamiana hero video - Vimeo na natywne MP4
old_hero = '<iframe src="https://player.vimeo.com/video/1189411760?background=1&autoplay=1&loop=1&muted=1&quality=1080p" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>'
new_hero = '<video autoplay muted loop playsinline preload="auto" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;"><source src="hero.mp4" type="video/mp4"></video>'

# Zamiana promise video - Vimeo na natywne MP4
old_promise = '<iframe src="https://player.vimeo.com/video/1189679282?background=1&autoplay=1&loop=1&muted=1&quality=1080p" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>'
new_promise = '<video autoplay muted loop playsinline preload="auto" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;"><source src="promise.mp4" type="video/mp4"></video>'

html = html.replace(old_hero, new_hero)
html = html.replace(old_promise, new_promise)

with open('index.html', 'w') as f:
    f.write(html)
print('done')
