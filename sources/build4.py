import asyncio, base64
from playwright.async_api import async_playwright
def b64(p): return "data:image/png;base64,"+base64.b64encode(open(p,'rb').read()).decode()
L=b64('logo_orig.png'); LW=b64('logo_white.png')
R="#E31B0F"; B="#1E3B7D"; INK="#12151C"; PAPER="#F7F5F0"; NAVY="#16295C"
BASE=f"""*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Inter,sans-serif}}
.abs{{position:absolute}}.frame{{position:absolute;left:40px;top:40px;right:40px;bottom:40px;border:1.5px solid}}
.serif{{font-family:Lora,serif}}.cap{{position:absolute;left:100px;font-size:22px;font-weight:600;letter-spacing:6px}}
.foot{{position:absolute;left:100px;right:100px;bottom:90px;display:flex;justify-content:space-between;align-items:flex-end;font-size:24px;font-weight:500}}
.foot img{{width:250px}}.line{{position:absolute;left:100px;width:90px;height:4px}}"""
def card(bg,fg,fr,body,logo): return f'<html><style>{BASE}</style><body style="background:{bg};color:{fg}"><div class="frame" style="border-color:{fr}"></div>{body}<div class="foot"><img src="{logo}"><div style="text-align:right;line-height:1.6">finitionsflorentin.fr<br>07 87 85 93 06</div></div></body></html>'
rows="".join(f'<div class="abs" style="left:100px;right:100px;top:{y}px;border-top:1.5px solid #D9D5CB;padding-top:24px;display:flex;gap:36px;align-items:baseline"><span style="font-size:22px;font-weight:600;letter-spacing:3px;color:{R};min-width:44px">{n}</span><span class="serif" style="font-size:38px;font-weight:600;color:{B};min-width:370px">{t}</span><span style="font-size:25px;color:#5A6070">{s}</span></div>' for n,t,s,y in [("01","Lessiver","un fond propre accroche mieux",620),("02","Reboucher, poncer","on rattrape trous et fissures",720),("03","Sous-couche","elle uniformise le fond",820),("04","Deux couches","pour une teinte régulière",920)])
c1=card(PAPER,INK,"#CFCABD",f'''<div class="cap" style="top:130px;color:{R}">PEINTURE INTÉRIEURE</div>
<div class="abs serif" style="left:100px;top:190px;width:880px;font-size:98px;line-height:1.08;font-weight:600;color:{B};letter-spacing:-2px">La peinture se joue avant le rouleau.</div>
<div class="line" style="top:540px;background:{R}"></div>{rows}''',L).replace('bottom:90px','bottom:90px;opacity:0').replace('<div class="foot"','<div class="foot" ',1)
# peinture: footer collides with rows -> use compact footer
c1=c1.replace('bottom:90px;opacity:0','bottom:90px')
c2=card(NAVY,"#F7F5F0","#5C6C98",f'''<div class="cap" style="top:130px;color:#FF6B5E">PLÂTRERIE · LA QUESTION</div>
<div class="abs serif" style="left:100px;top:250px;width:880px;font-size:94px;line-height:1.1;font-weight:600;letter-spacing:-2px">Pourquoi un joint de placo finit-il par fissurer ?</div>
<div class="line" style="top:800px;background:{R}"></div>
<div class="abs" style="left:100px;top:840px;width:820px;font-size:24px;letter-spacing:6px;font-weight:600;color:#FF6B5E">LES CAUSES FRÉQUENTES</div>
<div class="abs serif" style="left:100px;top:900px;width:860px;font-size:38px;line-height:1.45;font-weight:400">Pas de bande à joints, une couche d’enduit trop épaisse, ou un séchage trop rapide entre deux passes.</div>''',LW)
c3=card(PAPER,INK,"#CFCABD",f'''<div class="cap" style="top:130px;color:{B}">VRAI OU FAUX ?</div>
<div class="abs serif" style="left:100px;top:190px;width:880px;font-size:80px;line-height:1.1;font-weight:600;color:{INK};letter-spacing:-1.5px">On peut carreler sur n’importe quel mur.</div>
<div class="abs serif" style="left:92px;top:520px;font-size:300px;line-height:1;font-style:italic;font-weight:600;color:{R};letter-spacing:-8px">Faux.</div>
<div class="line" style="top:900px;background:{B}"></div>
<div class="abs serif" style="left:100px;top:950px;width:860px;font-size:38px;line-height:1.45;color:#2B3245">Le support doit être plan, propre, sec et stable. Sinon le carrelage se décolle.</div>''',L)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for n,h in (("peinture",c1),("placo",c2),("carrelage",c3)):
            await pg.set_content(h); await pg.wait_for_timeout(500); await pg.screenshot(path=f"v4_{n}.png")
        await b.close()
asyncio.run(main())
