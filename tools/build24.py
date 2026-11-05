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
<div class="contact" style="color:{T["cont"]}"><span>finitionsflorentin.fr · Lyon</span><em style="color:{T["cta"]}">Devis gratuit →</em></div></body>'''
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

def vf(t,kicker,statement,verdict,expl):
    T=TH[t]
    return f'''<style>{BASE}
.vf{{position:absolute;left:80px;top:250px;font-size:30px;font-weight:700;letter-spacing:8px;color:{T["lab"]}}}
.s{{position:absolute;left:80px;top:320px;width:920px;font-size:78px;line-height:1.08;font-weight:800;letter-spacing:-2px;color:{T["title"]}}}
.faux{{position:absolute;left:80px;top:640px;font-size:250px;line-height:1;font-weight:800;letter-spacing:-8px;color:{R if t!="bleu" else "#FFFFFF"}}}
.exp{{position:absolute;left:80px;right:80px;top:930px;font-size:35px;line-height:1.4;font-weight:500;color:{T["lab"]};border-top:6px solid {T["lab"]};padding-top:34px}}</style>
<body style="background:{T["bg"]}">
<img class="logo" src="{T["logo"]}" style="left:80px;top:80px">
<div class="vf">VRAI OU FAUX ?</div><div class="s">{statement}</div><div class="faux">{verdict}</div>
<div class="exp">{expl}</div>
<div class="contact" style="color:{T["cont"]}"><span>{kicker}</span><em style="color:{T["cta"]}">Devis gratuit →</em></div></body>'''

ns={}
exec(compile('\nsrc=open(\'build3.py\').read()\nhead=src.split("c1=f\'\'\'")[0]\nexec(head)\nTH={\n "blanc":dict(bg="#FFFFFF",t=B,k=R,tx="#5B6478",rule="#D8DBE2",logo=L,tile="#F1F2F4",dot=R),\n "bleu": dict(bg=B,t="#FFFFFF",k="#FFFFFF",tx="#C9D3EA",rule="rgba(255,255,255,.28)",logo=LW,tile="rgba(255,255,255,.10)",dot="#FFFFFF"),\n "ciel": dict(bg="#DCE6F6",t=B,k=R,tx="#4A5776",rule="rgba(30,59,125,.25)",logo=L,tile="rgba(255,255,255,.65)",dot=R),\n "pierre":dict(bg="#E8E4DD",t=B,k=R,tx="#5B6478",rule="rgba(30,59,125,.22)",logo=L,tile="rgba(255,255,255,.6)",dot=R),\n}\ndef foot(T,cta=True):\n    return f\'<div class="contact" style="color:{T["t"]}"><span>finitionsflorentin.fr · Lyon</span><em style="color:{T["k"] if T["bg"]!=B else "#fff"}">Devis gratuit →</em></div>\'\ndef top(T,kick,bar=True):\n    bs=[(R,700),(B if T["bg"]!=B else "#FFFFFF",820),("#000",560)]\n    return bars(0,bs)+f\'<img class="logo" src="{T["logo"]}" style="right:80px;top:120px"><div class="abs" style="left:80px;top:230px;font-weight:600;letter-spacing:7px;font-size:25px;color:{T["k"]}">{kick}</div>\'\n# 1. frise chronologique\ndef frise(t,kick,title,items):\n    T=TH[t]\n    its="".join(f\'<div class="abs" style="left:80px;top:{680+i*135}px;width:210px;font-size:32px;font-weight:800;color:{T["t"]}">{a}</div><div class="abs" style="left:330px;top:{684+i*135}px;width:670px;font-size:30px;line-height:1.3;font-weight:500;color:{T["tx"]}">{b}</div><div class="abs" style="left:298px;top:{694+i*135}px;width:18px;height:18px;border-radius:50%;background:{T["dot"]}"></div>\' for i,(a,b) in enumerate(items))\n    line=f\'<div class="abs" style="left:306px;top:700px;width:2px;height:{(len(items)-1)*135}px;background:{T["rule"]}"></div>\'\n    return f\'\'\'<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:90px;line-height:1.02;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{line}{its}{foot(T)}</body>\'\'\'\n# 2. liste numérotée en pastilles\ndef pastilles(t,kick,title,items,y0=610,step=120,fs=100):\n    T=TH[t]\n    its="".join(f\'<div class="abs" style="left:80px;top:{y0+i*step}px;width:76px;height:76px;border-radius:50%;background:{R if t!="bleu" else "#fff"};color:{"#fff" if t!="bleu" else B};font-size:38px;font-weight:800;display:flex;align-items:center;justify-content:center">{i+1}</div><div class="abs" style="left:186px;top:{y0+8+i*step}px;width:810px;font-size:36px;font-weight:700;line-height:1.2;color:{T["t"]}">{a}<div style="font-size:25px;font-weight:500;color:{T["tx"]};margin-top:4px">{b}</div></div>\' for i,(a,b) in enumerate(items))\n    return f\'\'\'<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:{fs}px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{its}{foot(T)}</body>\'\'\'\n# 3. énoncé géant\ndef geant(t,kick,big,small,sub):\n    T=TH[t]\n    return f\'\'\'<style>{BASE}.big{{position:absolute;left:80px;top:300px;width:920px;font-size:430px;line-height:.85;font-weight:800;letter-spacing:-10px;color:{T["t"]}}}.sm{{position:absolute;left:80px;top:790px;width:900px;font-size:66px;line-height:1.08;font-weight:800;letter-spacing:-2px;color:{T["t"]}}}.sub{{position:absolute;left:80px;top:1030px;width:900px;font-size:30px;line-height:1.4;font-weight:500;color:{T["tx"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<div class="big">{big}</div><div class="sm">{small}</div><div class="sub">{sub}</div>{foot(T)}</body>\'\'\'\n# 4. grille de tuiles\ndef tuiles(t,kick,title,tiles):\n    T=TH[t]\n    out=""\n    for i,(a,b) in enumerate(tiles):\n        col=i%2; row=i//2\n        w=440 if i<4 else 920\n        x=80+col*480 if i<4 else 80\n        y=600+row*200 if i<4 else 600+2*200\n        out+=f\'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:180px;background:{T["tile"]};border-left:10px solid {R if t!="bleu" else "#fff"};padding:28px 36px"><div style="font-size:40px;font-weight:800;color:{T["t"]}">{a}</div><div style="font-size:24px;line-height:1.3;font-weight:500;color:{T["tx"]};margin-top:8px">{b}</div></div>\'\n    return f\'\'\'<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:100px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{out}{foot(T)}</body>\'\'\'\n# 5. coches\ndef coches(t,kick,title,items):\n    T=TH[t]\n    its="".join(f\'<div class="abs" style="left:80px;top:{640+i*150}px;width:60px;height:60px;border-radius:12px;background:{R if t!="bleu" else "#fff"};color:{"#fff" if t!="bleu" else B};font-size:40px;font-weight:800;display:flex;align-items:center;justify-content:center">✓</div><div class="abs" style="left:170px;top:{640+i*150}px;width:830px;font-size:34px;font-weight:700;line-height:1.2;color:{T["t"]}">{a}<div style="font-size:25px;font-weight:500;color:{T["tx"]};margin-top:4px">{b}</div></div>\' for i,(a,b) in enumerate(items))\n    return f\'\'\'<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:96px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{its}{foot(T)}</body>\'\'\'\n','b22','exec'),ns)
tuiles=ns['tuiles']

cards={
 "n_placo_usages": lst("ciel","PLÂTRERIE","Quelle plaque de plâtre pour quelle pièce ?",[("Standard","pièces sèches"),("Hydrofuge","pièces humides"),("Feu","protection incendie"),("Phonique","chambres, séparations"),("Haute densité","renfort, charges lourdes")],top=690),
 "n_placo_hydro": vf("pierre","Devis gratuit sur finitionsflorentin.fr","Une plaque hydrofuge rend une douche étanche.","FAUX.","Elle résiste mieux à l’humidité, mais en zone de douche, un système d’étanchéité adapté reste nécessaire."),
 "n_isolants": tuiles("blanc","ISOLATION","Trois isolants, trois atouts.",[("Laine de verre","incombustible, pose simple"),("Laine de roche","incombustible, dense"),("Laine de bois","origine végétale, confort d’été"),("Le bon choix","selon le support et la pièce")]),
 "n_dephasage": qa("bleu","ISOLATION · LA QUESTION","L’isolant sert aussi en été&nbsp;?","LE DÉPHASAGE","Un isolant à fort déphasage ralentit l’arrivée de la chaleur dans la pièce. La laine de bois y est réputée performante."),
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
