import asyncio, base64
from playwright.async_api import async_playwright
def b64(p): return "data:image/png;base64,"+base64.b64encode(open(p,'rb').read()).decode()
L=b64('logo_orig.png'); LW=b64('logo_white.png')
R="#E31B0F"; B="#1E3B7D"
BASE="""*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Poppins,sans-serif;position:relative;overflow:hidden}
.logo{position:absolute;width:330px}.abs{position:absolute}
.contact{position:absolute;left:80px;right:80px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-size:27px;font-weight:600}
.contact em{font-style:normal;font-weight:800}"""
def bars(top,cols):
    return "".join(f'<div class="abs" style="left:0;top:{top+i*34}px;width:{w}px;height:22px;background:{c}"></div>' for i,(c,w) in enumerate(cols))
c1=f'''<style>{BASE}
h1{{position:absolute;left:80px;top:300px;width:920px;font-size:104px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{B}}}
.row{{position:absolute;left:80px;right:80px;display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid #D8DBE2;padding:26px 0;font-size:30px}}
.row b{{font-weight:700;color:{B}}}.row span{{color:#5B6478;font-size:25px}}</style>
<body style="background:#fff">
{bars(0,[(R,700),(B,820),("#000",560)])}
<img class="logo" src="{L}" style="right:80px;top:120px">
<div class="abs" style="left:80px;top:230px;font-weight:600;letter-spacing:7px;font-size:25px;color:{R}">PEINTURE INTÉRIEURE</div>
<h1>La peinture se joue avant le rouleau.</h1>
<div class="row" style="top:760px"><b>Lessiver</b><span>un support propre accroche mieux</span></div>
<div class="row" style="top:850px"><b>Reboucher et poncer</b><span>on rattrape trous et fissures</span></div>
<div class="row" style="top:940px"><b>Sous-couche</b><span>elle uniformise le fond</span></div>
<div class="row" style="top:1030px;border-bottom:2px solid #D8DBE2"><b>Deux couches</b><span>pour une teinte régulière</span></div>
<div class="contact" style="color:{B}"><span>finitionsflorentin.fr · Lyon</span><em style="color:{R}">Devis gratuit →</em></div></body>'''
c2=f'''<style>{BASE}
.q{{position:absolute;left:80px;top:330px;width:920px;font-size:92px;line-height:1.05;font-weight:800;letter-spacing:-2px;color:#fff}}
.ans{{position:absolute;left:80px;right:80px;top:780px;background:#fff;color:{B};border-radius:8px;padding:50px 56px;border-left:16px solid {R}}}
.ans small{{display:block;font-size:24px;letter-spacing:6px;font-weight:700;color:{R};margin-bottom:18px}}
.ans p{{font-size:36px;line-height:1.35;font-weight:600}}</style>
<body style="background:{B}">
<div class="abs" style="left:80px;top:100px;font-weight:600;letter-spacing:7px;font-size:25px;color:#fff;opacity:.85">PLÂTRERIE · LA QUESTION</div>
<div class="q">Pourquoi un joint de placo finit par fissurer ?</div>
<div class="ans"><small>LES CAUSES FRÉQUENTES</small><p>Pas de bande à joints, une couche d’enduit trop épaisse, ou un séchage trop rapide entre deux passes.</p></div>
<img class="logo" src="{LW}" style="left:80px;bottom:70px">
<div class="abs" style="right:80px;bottom:92px;font-size:27px;font-weight:800;color:#fff">Devis gratuit →</div>
{bars(0,[(R,360)])}</body>'''
c3=f'''<style>{BASE}
.vf{{position:absolute;left:80px;top:250px;font-size:30px;font-weight:700;letter-spacing:8px;color:{B}}}
.s{{position:absolute;left:80px;top:320px;width:920px;font-size:78px;line-height:1.08;font-weight:800;letter-spacing:-2px;color:#111}}
.faux{{position:absolute;left:80px;top:640px;font-size:250px;line-height:1;font-weight:800;letter-spacing:-8px;color:{R}}}
.exp{{position:absolute;left:80px;right:80px;top:930px;font-size:35px;line-height:1.4;font-weight:500;color:#2B3245;border-top:6px solid {B};padding-top:34px}}</style>
<body style="background:#F1F2F4">
<img class="logo" src="{L}" style="left:80px;top:80px">
<div class="vf">VRAI OU FAUX ?</div>
<div class="s">On peut carreler sur n’importe quel mur.</div>
<div class="faux">FAUX.</div>
<div class="exp">Le support doit être plan, propre, sec et stable. Sinon le carrelage se décolle.</div>
<div class="contact" style="color:{B}"><span>Carrelage et revêtements</span><em style="color:{R}">Devis gratuit →</em></div></body>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for n,h in (("peinture",c1),("placo",c2),("carrelage",c3)):
            await pg.set_content(f"<html><head>{h}</head>" if False else f"<html>{h}</html>"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"v3_{n}.png")
        await b.close()
asyncio.run(main())
