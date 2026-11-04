import asyncio, base64
from playwright.async_api import async_playwright
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
LOGO="data:image/png;base64,"+b64('logo_orig.png'); LOGOW="data:image/png;base64,"+b64('logo_white.png')
RED="#E31B0F"; BLUE="#1E3B7D"
CSS="""
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Poppins,sans-serif;position:relative;overflow:hidden}
.logo{position:absolute;width:360px}
.kick{position:absolute;left:80px;top:250px;font-weight:600;letter-spacing:7px;font-size:26px}
h1{position:absolute;left:80px;top:305px;width:920px;font-weight:800;font-size:86px;line-height:1.05;letter-spacing:-2px}
.bar{position:absolute;left:80px;top:585px;width:110px;height:8px;border-radius:4px}
ul{position:absolute;left:80px;top:660px;width:920px;list-style:none}
li{display:flex;gap:28px;margin-bottom:34px;align-items:flex-start}
.n{font-weight:700;font-size:28px;min-width:60px;height:60px;border-radius:30px;display:flex;align-items:center;justify-content:center;color:#fff}
li b{display:block;font-size:34px;font-weight:600;line-height:1.2}li span{display:block;font-size:26px;line-height:1.35;opacity:.75;margin-top:4px}
.foot{position:absolute;left:0;bottom:0;width:100%;height:190px;display:flex;align-items:center;justify-content:space-between;padding:0 80px}
.foot p{font-size:30px;font-weight:600;line-height:1.3}.btn{font-weight:700;font-size:32px;padding:26px 48px;border-radius:60px;color:#fff}
"""
C=[
 dict(k="peinture",bg="#FFFFFF",fg=BLUE,kc=RED,acc=RED,logo=LOGO,pos="left:80px;top:80px",foot="#F1F2F4",ff=BLUE,btn=BLUE,fp="Peinture et décoration",
  kick="PEINTURE INTÉRIEURE",h="Avant de peindre,<br>on prépare.",
  items=[("Lessiver","Une paroi propre accroche mieux la peinture."),("Reboucher et poncer","Trous, fissures, relief : on rattrape tout."),("Appliquer une sous-couche","Elle uniformise le support."),("Peindre en deux couches","Pour une teinte régulière, sans reprise.")]),
 dict(k="placo",bg="#14161A",fg="#FFFFFF",kc="#FF5A4D",acc=RED,logo=LOGOW,pos="right:80px;top:80px",foot="#1E2127",ff="#FFFFFF",btn=RED,fp="Cloisons et plâtrerie",
  kick="PLÂTRERIE",h="Des joints invisibles,<br>ça se travaille.",
  items=[("Bande à joints posée dans l’enduit","Elle évite les fissures aux jonctions."),("Plusieurs passes fines","Mieux qu’une seule couche épaisse."),("Séchage entre chaque passe","On ne brûle pas les étapes."),("Ponçage soigné","C’est lui qui rend la cloison lisse sous la peinture.")]),
 dict(k="carrelage",bg="#F1F2F4",fg=BLUE,kc=RED,acc=BLUE,logo=LOGO,pos="left:80px;top:80px",foot="#FFFFFF",ff=BLUE,btn=RED,fp="Carrelage et revêtements",
  kick="CARRELAGE",h="Ce qu’on vérifie<br>avant de poser.",
  items=[("Un support plan","On rattrape les creux avant la colle."),("Propre, sec et stable","Sinon le carrelage se décolle."),("Un calepinage","On prévoit les coupes avant de coller."),("Des joints de dilatation","Là où le sol doit pouvoir travailler.")]),
]
def html(c):
    li="".join(f'<li><div class="n" style="background:{c["acc"]}">{i+1}</div><div><b>{t}</b><span>{s}</span></div></li>' for i,(t,s) in enumerate(c["items"]))
    return f'''<html><head><style>{CSS}</style></head><body style="background:{c["bg"]};color:{c["fg"]}">
<img class="logo" src="{c["logo"]}" style="{c["pos"]}">
<div class="kick" style="color:{c["kc"]}">{c["kick"]}</div><h1>{c["h"]}</h1><div class="bar" style="background:{c["acc"]}"></div>
<ul>{li}</ul>
<div class="foot" style="background:{c["foot"]};color:{c["ff"]}"><p>{c["fp"]}</p><div class="btn" style="background:{c["btn"]}">Devis gratuit</div></div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for c in C:
            await pg.set_content(html(c)); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"v2_{c['k']}.png")
        await b.close()
asyncio.run(main())
