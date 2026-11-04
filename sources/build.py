import asyncio
from playwright.async_api import async_playwright
CSS="""
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Poppins,sans-serif;position:relative;overflow:hidden}
.logo{position:absolute;left:80px;top:80px;font-weight:700;letter-spacing:5px;font-size:24px;line-height:1.3}
.logo small{display:block;font-weight:500;letter-spacing:7px;font-size:15px;opacity:.7}
.kick{position:absolute;left:80px;top:250px;font-weight:600;letter-spacing:7px;font-size:26px}
h1{position:absolute;left:80px;top:305px;width:920px;font-weight:800;font-size:86px;line-height:1.05;letter-spacing:-2px}
.bar{position:absolute;left:80px;width:110px;height:8px;border-radius:4px}
ul{position:absolute;left:80px;width:920px;list-style:none}
li{display:flex;gap:28px;margin-bottom:34px;align-items:flex-start}
.n{font-weight:700;font-size:28px;min-width:60px;height:60px;border-radius:30px;display:flex;align-items:center;justify-content:center}
li b{display:block;font-size:34px;font-weight:600;line-height:1.2}li span{display:block;font-size:26px;line-height:1.35;opacity:.8;margin-top:4px}
.foot{position:absolute;left:0;bottom:0;width:100%;height:190px;display:flex;align-items:center;justify-content:space-between;padding:0 80px}
.foot p{font-size:30px;font-weight:600;line-height:1.3}.btn{font-weight:700;font-size:32px;padding:26px 48px;border-radius:60px}
"""
cards=[
("peinture","#1F3A34","#F4EFE6","#D9825B","#FFFFFF","#1F3A34","PEINTURE INTÉRIEURE","Avant de peindre,<br>on prépare.",
 [("Lessiver","Une paroi propre accroche mieux la peinture."),("Reboucher et poncer","Trous, fissures, relief : on rattrape tout."),("Appliquer une sous-couche","Elle uniformise le support."),("Peindre en deux couches","Pour une teinte régulière, sans reprise.")],
 "Peinture et décoration","Demander un devis"),
("placo","#F4EFE6","#1F3A34","#C8643C","#1F3A34","#F4EFE6","PLÂTRERIE","Des joints invisibles,<br>ça se travaille.",
 [("Bande à joints posée dans l’enduit","Elle évite les fissures aux jonctions."),("Plusieurs passes fines","Mieux qu’une seule couche épaisse."),("Séchage entre chaque passe","On ne brûle pas les étapes."),("Ponçage soigné","C’est lui qui rend la cloison lisse sous la peinture.")],
 "Cloisons et plâtrerie","Demander un devis"),
("carrelage","#C8643C","#FFFFFF","#1F3A34","#1F3A34","#F4EFE6","CARRELAGE","Ce qu’on vérifie<br>avant de poser.",
 [("Un support plan","On rattrape les creux avant la colle."),("Propre, sec et stable","Sinon le carrelage se décolle."),("Un calepinage","On prévoit les coupes avant de coller."),("Des joints de dilatation","Là où le sol doit pouvoir travailler.")],
 "Carrelage et revêtements","Demander un devis"),
]
def html(c):
    k,bg,fg,acc,btnbg,footbg,kick,h,items,foot,cta=c
    footc = "#F4EFE6" if footbg=="#F4EFE6" else "#fff"
    li="".join(f'<li><div class="n" style="background:{acc};color:#fff">{i+1}</div><div><b>{t}</b><span>{s}</span></div></li>' for i,(t,s) in enumerate(items))
    btncol = "#fff" if btnbg!="#FFFFFF" else bg
    btncol2 = bg if btnbg in ("#FFFFFF",) else "#F4EFE6"
    footfg = "#1F3A34" if footbg=="#F4EFE6" else "#fff"
    return f'''<html><head><style>{CSS}</style></head><body style="background:{bg};color:{fg}">
<div class="logo">FINITIONS<br>FLORENTIN<small>RÉNOVATION · LYON</small></div>
<div class="kick" style="color:{acc}">{kick}</div><h1>{h}</h1>
<div class="bar" style="background:{acc};top:585px"></div>
<ul style="top:660px">{li}</ul>
<div class="foot" style="background:{footbg};color:{footfg}"><p>{foot}</p><div class="btn" style="background:{acc};color:#fff">{cta}</div></div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for c in cards:
            await pg.set_content(html(c)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"carte_{c[0]}.png")
        await b.close()
asyncio.run(main())
