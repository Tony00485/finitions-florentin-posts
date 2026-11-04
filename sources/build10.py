import asyncio, base64, re
src=open('build3.py').read()
head=src.split("c1=f'''")[0]
exec(head)
TH={
 "blanc": dict(bg="#FFFFFF",title=B,kick=R,lab=B,val="#5B6478",rule="#D8DBE2",logo=L,cont=B,cta=R,bars=[(R,700),(B,820),("#000000",560)],box="#F1F2F4",boxt=B,boxb=R,qkick=B),
 "bleu": dict(bg=B,title="#FFFFFF",kick="#FFFFFF",lab="#FFFFFF",val="#C9D3EA",rule="rgba(255,255,255,.25)",logo=LW,cont="#FFFFFF",cta="#FFFFFF",bars=[(R,700),("#FFFFFF",820),("#000000",560)],box="#FFFFFF",boxt=B,boxb=R,qkick="#FFFFFF"),
 "noir":  dict(bg="#121212",title="#FFFFFF",kick=R,lab="#FFFFFF",val="#C9CEDA",rule="rgba(255,255,255,.22)",logo=LW,cont="#FFFFFF",cta=R,bars=[(R,700),(B,820),("#FFFFFF",560)],box="#FFFFFF",boxt=B,boxb=R,qkick="#FFFFFF"),
 "rouge": dict(bg=R,title="#FFFFFF",kick="#FFFFFF",lab="#FFFFFF",val="rgba(255,255,255,.88)",rule="rgba(255,255,255,.35)",logo=LW,cont="#FFFFFF",cta="#FFFFFF",bars=[("#FFFFFF",700),(B,820),("#000000",560)],box="#FFFFFF",boxt=B,boxb=B,qkick="#FFFFFF"),
 "pierre":dict(bg="#E8E4DD",title=B,kick=R,lab=B,val="#5B6478",rule="rgba(30,59,125,.22)",logo=L,cont=B,cta=R,bars=[(R,700),(B,820),("#000000",560)],box="#FFFFFF",boxt=B,boxb=R,qkick=B),
 "ciel":  dict(bg="#DCE6F6",title=B,kick=R,lab=B,val="#4A5776",rule="rgba(30,59,125,.25)",logo=L,cont=B,cta=R,bars=[(R,700),(B,820),("#000000",560)],box="#FFFFFF",boxt=B,boxb=R,qkick=B),
}
def lst(t,kicker,title,rows,top=620):
    T=TH[t]
    r="".join(f'<div class="row" style="top:{top+i*90}px;{"border-bottom:2px solid "+T["rule"]+";" if i==len(rows)-1 else ""}"><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate(rows))
    return f'''<style>{BASE}
h1{{position:absolute;left:80px;top:300px;width:920px;font-size:100px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["title"]}}}
.row{{position:absolute;left:80px;right:80px;display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid {T["rule"]};padding:26px 0;font-size:30px}}
.row b{{font-weight:700;color:{T["lab"]}}}.row span{{color:{T["val"]};font-size:25px}}</style>
<body style="background:{T["bg"]}">
{bars(0,T["bars"])}
<img class="logo" src="{T["logo"]}" style="right:80px;top:120px">
<div class="abs" style="left:80px;top:230px;font-weight:600;letter-spacing:7px;font-size:25px;color:{T["kick"]}">{kicker}</div>
<h1>{title}</h1>{r}
<div class="contact" style="color:{T["cont"]}"><span>finitionsflorentin.fr · 07 87 85 93 06</span><em style="color:{T["cta"]}">Devis gratuit →</em></div></body>'''
def qa(t,kicker,q,label,ans):
    T=TH[t]
    return f'''<style>{BASE}
.q{{position:absolute;left:80px;top:300px;width:920px;font-size:88px;line-height:1.05;font-weight:800;letter-spacing:-2px;color:{T["title"]}}}
.ans{{position:absolute;left:80px;right:80px;top:700px;background:{T["box"]};color:{T["boxt"]};border-radius:8px;padding:50px 56px;border-left:16px solid {T["boxb"]}}}
.ans small{{display:block;font-size:24px;letter-spacing:6px;font-weight:700;color:{R};margin-bottom:18px}}
.ans p{{font-size:36px;line-height:1.35;font-weight:600}}</style>
<body style="background:{T["bg"]}">
<div class="abs" style="left:80px;top:100px;font-weight:600;letter-spacing:7px;font-size:25px;color:{T["qkick"]};opacity:.85">{kicker}</div>
<div class="q">{q}</div><div class="ans"><small>{label}</small><p>{ans}</p></div>
<img class="logo" src="{T["logo"]}" style="left:80px;bottom:70px">
<div class="abs" style="right:80px;bottom:92px;font-size:27px;font-weight:800;color:{T["cont"]}">Devis gratuit →</div>
{bars(0,[(T["bars"][2][0] if t=="rouge" else R,360)])}</body>'''
cards={
 "d_finition_blanc": lst("blanc","PEINTURE INTÉRIEURE","Quelle finition pour quelle surface ?",[("Mat","plafonds"),("Velours","murs et pièces de vie"),("Satin","boiseries, portes, plinthes"),("Pièces humides","peinture dédiée")],top=620),
 "d_protection_bleu": lst("bleu","CHANTIER","La protection, première étape du chantier.",[("Sols et parquets","bâche adaptée au support"),("Escaliers et meubles","couverts"),("Boiseries et prises","masquées"),("Poussière","ponçage avec aspiration")],top=700),
 "d_devis_ciel": lst("ciel","DEVIS","Un bon devis, c’est quoi ?",[("Travaux détaillés","pièce par pièce"),("Matériaux précisés","nature et qualité indiquées"),("Prix lisibles","HT, TVA et TTC"),("Délais et validité","annoncés clairement")],top=620),
 "d_parevapeur_bleu": qa("bleu","ISOLATION · LA QUESTION","À quoi sert le pare\u2011vapeur dans une isolation ?","SON RÔLE","Il limite le passage de l’humidité de la pièce vers l’isolant, qui perdrait sinon une partie de son efficacité."),
 "d_sikkens_pierre": lst("pierre","NOS PRODUITS · MURS","Sur vos murs : Sikkens Alpha Universal Velours.",[("Émissions","classe A+ dans l’air intérieur"),("COV","1 g/l maximum"),("Abrasion humide","classe 1 (NF EN 13300)"),("2 en 1","impression et finition")],top=700),
 "d_decennale_blanc": qa("blanc","ASSURANCE · LA QUESTION","Pourquoi demander l’attestation décennale ?","CE QU’ELLE PROTÈGE","Pendant 10 ans après la réception, elle couvre les dommages qui touchent la solidité de l’ouvrage, selon la nature des travaux. Demandez-la avant de signer : elle doit être jointe au devis."),
}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for n,h in cards.items():
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{n}.png")
        await b.close()
asyncio.run(main())
