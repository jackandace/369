import re

hero_css = open("youme/style.css").read()
if ".hero-collage" not in hero_css:
    with open("youme/style.css", "a") as f:
        f.write(open("hero_addon.css").read())

with open("youme/index.html", "r") as f:
    html = f.read()

new_hero = '''<section class="hero" id="hero">
  <div class="hero-text">
    <p class="eyebrow">Newborn Photo</p>
    <h1 class="hero-title">今しか撮れない。<br>この、<span>小さな小さな</span><br>ひとときを。</h1>
    <p class="hero-body">生まれたばかりの、ふわふわの重さ。<br>まだお腹の中の温もりを覚えているような、<br>あのひとときを、ずっと残しておきたいから。</p>
    <p class="hero-area">Gifu &amp; Aichi</p>
    <a href="https://lin.ee/pl6aaVW" class="hero-cta">料金・空き日程をLINEで確認する</a>
  </div>
  <div class="hero-collage">
    <div class="deco-text">The moment that will never come back again</div>
    <div class="deco-line"></div>
    <div class="photo photo-back"><img src="images/hero-blue.jpg" alt="ニューボーンフォト"></div>
    <div class="photo photo-main"><img src="images/hero-family.jpg" alt="ニューボーンフォト ファミリー"></div>
    <div class="photo photo-front"><img src="images/hero-feet.jpg" alt="ニューボーンフォト 小さな足"></div>
  </div>
</section>'''

html = re.sub(r'<section[^>]*id=["\']hero["\'].*?</section>', new_hero, html, flags=re.DOTALL)
open("youme/index.html", "w").write(html)
print("完了!")
