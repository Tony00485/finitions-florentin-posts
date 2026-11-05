import asyncio, base64, re
src=open('build3.py').read()
head=src.split("c1=f'''")[0]          # imports + helpers + constantes
exec(head)
def lst(kicker,title,rows,top=620):
    r="".join(f'<div class="row" style="top:{top+i*90}px;{"border-bottom:2px solid #D8DBE2;" if i==len(rows)-1 else ""}"><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate(rows))
    return f'''<style>{BASE}
h1{{position:absolute;left:80px;top:300px;width:920px;font-size:100px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{B}}}
.row{{position:absolute;left:80px;right:80px;display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid #D8DBE2;padding:26px 0;font-size:30px}}
.row b{{font-weight:700;color:{B}}}.row span{{color:#5B6478;font-size:25px}}</style>
<body style="background:#fff">
{bars(0,[(R,700),(B,820),("#000",560)])}
<img class="logo" src="{L}" style="right:80px;top:120px">
<div class="abs" style="left:80px;top:230px;font-weight:600;letter-spacing:7px;font-size:25px;color:{R}">{kicker}</div>
<h1>{title}</h1>{r}
<div class="contact" style="color:{B}"><span>finitionsflorentin.fr · Lyon</span><em style="color:{R}">Devis gratuit →</em></div></body>'''
def vf(kicker,statement,verdict,expl):
    return f'''<style>{BASE}
.vf{{position:absolute;left:80px;top:250px;font-size:30px;font-weight:700;letter-spacing:8px;color:{B}}}
.s{{position:absolute;left:80px;top:320px;width:920px;font-size:78px;line-height:1.08;font-weight:800;letter-spacing:-2px;color:#111}}
.faux{{position:absolute;left:80px;top:640px;font-size:250px;line-height:1;font-weight:800;letter-spacing:-8px;color:{R}}}
.exp{{position:absolute;left:80px;right:80px;top:930px;font-size:35px;line-height:1.4;font-weight:500;color:#2B3245;border-top:6px solid {B};padding-top:34px}}</style>
<body style="background:#F1F2F4">
<img class="logo" src="{L}" style="left:80px;top:80px">
<div class="vf">VRAI OU FAUX ?</div><div class="s">{statement}</div><div class="faux">{verdict}</div>
<div class="exp">{expl}</div>
<div class="contact" style="color:{B}"><span>{kicker}</span><em style="color:{R}">Devis gratuit →</em></div></body>'''
def qa(kicker,q,label,ans):
    return f'''<style>{BASE}
.q{{position:absolute;left:80px;top:300px;width:920px;font-size:88px;line-height:1.05;font-weight:800;letter-spacing:-2px;color:#fff}}
.ans{{position:absolute;left:80px;right:80px;top:790px;background:#fff;color:{B};border-radius:8px;padding:50px 56px;border-left:16px solid {R}}}
.ans small{{display:block;font-size:24px;letter-spacing:6px;font-weight:700;color:{R};margin-bottom:18px}}
.ans p{{font-size:36px;line-height:1.35;font-weight:600}}</style>
<body style="background:{B}">
<div class="abs" style="left:80px;top:100px;font-weight:600;letter-spacing:7px;font-size:25px;color:#fff;opacity:.85">{kicker}</div>
<div class="q">{q}</div><div class="ans"><small>{label}</small><p>{ans}</p></div>
<img class="logo" src="{LW}" style="left:80px;bottom:70px">
<div class="abs" style="right:80px;bottom:92px;font-size:27px;font-weight:800;color:#fff">Devis gratuit →</div>
{bars(0,[(R,360)])}</body>'''
cards={
 "finition": lst("PEINTURE INTÉRIEURE","Quelle finition pour quelle surface ?",[("Mat","plafonds"),("Velours","murs et pièces de vie"),("Satin","boiseries, portes, plinthes"),("Pièces humides","peinture dédiée")]),
 "souscouche": vf("Peinture intérieure","Une sous-couche, c’est facultatif.","FAUX.","Elle uniformise le fond et évite une teinte finale irrégulière. Sans elle, le support boit la peinture de façon inégale."),
 "parevapeur": qa("ISOLATION · LA QUESTION","À quoi sert le pare‑vapeur dans une isolation ?","SON RÔLE","Il limite le passage de l’humidité de la pièce vers l’isolant, qui perdrait sinon une partie de son efficacité."),
 "devis": lst("DEVIS","Un bon devis, c’est quoi ?",[("Travaux détaillés","pièce par pièce"),("Matériaux précisés","nature et qualité indiquées"),("Prix lisibles","HT, TVA et TTC"),("Délais et validité","annoncés clairement")]),
}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for n,h in cards.items():
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"v3_{n}.png")
        await b.close()
asyncio.run(main())
