import asyncio, base64
src=open('build3.py').read()
head=src.split("c1=f'''")[0]
exec(head)
TH={
 "blanc":dict(bg="#FFFFFF",t=B,k=R,tx="#5B6478",rule="#D8DBE2",logo=L,tile="#F1F2F4",dot=R),
 "bleu": dict(bg=B,t="#FFFFFF",k="#FFFFFF",tx="#C9D3EA",rule="rgba(255,255,255,.28)",logo=LW,tile="rgba(255,255,255,.10)",dot="#FFFFFF"),
 "ciel": dict(bg="#DCE6F6",t=B,k=R,tx="#4A5776",rule="rgba(30,59,125,.25)",logo=L,tile="rgba(255,255,255,.65)",dot=R),
 "pierre":dict(bg="#E8E4DD",t=B,k=R,tx="#5B6478",rule="rgba(30,59,125,.22)",logo=L,tile="rgba(255,255,255,.6)",dot=R),
}
def foot(T,cta=True):
    return f'<div class="contact" style="color:{T["t"]}"><span>finitionsflorentin.fr · 07 87 85 93 06</span><em style="color:{T["k"] if T["bg"]!=B else "#fff"}">Devis gratuit →</em></div>'
def top(T,kick,bar=True):
    bs=[(R,700),(B if T["bg"]!=B else "#FFFFFF",820),("#000",560)]
    return bars(0,bs)+f'<img class="logo" src="{T["logo"]}" style="right:80px;top:120px"><div class="abs" style="left:80px;top:230px;font-weight:600;letter-spacing:7px;font-size:25px;color:{T["k"]}">{kick}</div>'
# 1. frise chronologique
def frise(t,kick,title,items):
    T=TH[t]
    its="".join(f'<div class="abs" style="left:80px;top:{680+i*135}px;width:210px;font-size:32px;font-weight:800;color:{T["t"]}">{a}</div><div class="abs" style="left:330px;top:{684+i*135}px;width:670px;font-size:30px;line-height:1.3;font-weight:500;color:{T["tx"]}">{b}</div><div class="abs" style="left:298px;top:{694+i*135}px;width:18px;height:18px;border-radius:50%;background:{T["dot"]}"></div>' for i,(a,b) in enumerate(items))
    line=f'<div class="abs" style="left:306px;top:700px;width:2px;height:{(len(items)-1)*135}px;background:{T["rule"]}"></div>'
    return f'''<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:90px;line-height:1.02;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{line}{its}{foot(T)}</body>'''
# 2. liste numérotée en pastilles
def pastilles(t,kick,title,items,y0=610,step=120,fs=100):
    T=TH[t]
    its="".join(f'<div class="abs" style="left:80px;top:{y0+i*step}px;width:76px;height:76px;border-radius:50%;background:{R if t!="bleu" else "#fff"};color:{"#fff" if t!="bleu" else B};font-size:38px;font-weight:800;display:flex;align-items:center;justify-content:center">{i+1}</div><div class="abs" style="left:186px;top:{y0+8+i*step}px;width:810px;font-size:36px;font-weight:700;line-height:1.2;color:{T["t"]}">{a}<div style="font-size:25px;font-weight:500;color:{T["tx"]};margin-top:4px">{b}</div></div>' for i,(a,b) in enumerate(items))
    return f'''<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:{fs}px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{its}{foot(T)}</body>'''
# 3. énoncé géant
def geant(t,kick,big,small,sub):
    T=TH[t]
    return f'''<style>{BASE}.big{{position:absolute;left:80px;top:300px;width:920px;font-size:430px;line-height:.85;font-weight:800;letter-spacing:-10px;color:{T["t"]}}}.sm{{position:absolute;left:80px;top:790px;width:900px;font-size:66px;line-height:1.08;font-weight:800;letter-spacing:-2px;color:{T["t"]}}}.sub{{position:absolute;left:80px;top:1030px;width:900px;font-size:30px;line-height:1.4;font-weight:500;color:{T["tx"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<div class="big">{big}</div><div class="sm">{small}</div><div class="sub">{sub}</div>{foot(T)}</body>'''
# 4. grille de tuiles
def tuiles(t,kick,title,tiles):
    T=TH[t]
    out=""
    for i,(a,b) in enumerate(tiles):
        col=i%2; row=i//2
        w=440 if i<4 else 920
        x=80+col*480 if i<4 else 80
        y=600+row*200 if i<4 else 600+2*200
        out+=f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:180px;background:{T["tile"]};border-left:10px solid {R if t!="bleu" else "#fff"};padding:28px 36px"><div style="font-size:40px;font-weight:800;color:{T["t"]}">{a}</div><div style="font-size:24px;line-height:1.3;font-weight:500;color:{T["tx"]};margin-top:8px">{b}</div></div>'
    return f'''<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:100px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{out}{foot(T)}</body>'''
# 5. coches
def coches(t,kick,title,items):
    T=TH[t]
    its="".join(f'<div class="abs" style="left:80px;top:{640+i*150}px;width:60px;height:60px;border-radius:12px;background:{R if t!="bleu" else "#fff"};color:{"#fff" if t!="bleu" else B};font-size:40px;font-weight:800;display:flex;align-items:center;justify-content:center">✓</div><div class="abs" style="left:170px;top:{640+i*150}px;width:830px;font-size:34px;font-weight:700;line-height:1.2;color:{T["t"]}">{a}<div style="font-size:25px;font-weight:500;color:{T["tx"]};margin-top:4px">{b}</div></div>' for i,(a,b) in enumerate(items))
    return f'''<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:96px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>{its}{foot(T)}</body>'''

def confiance(t,kick,title,rows):
    T=TH[t]
    q=b64('logo_qualibat_rge.png')
    its="".join(f'<div style="margin-bottom:38px"><div style="font-size:34px;font-weight:800;line-height:1.15;color:{T["t"]}">{a}</div><div style="font-size:25px;font-weight:500;line-height:1.3;color:{T["tx"]};margin-top:6px">{b}</div></div>' for a,b in rows)
    return f'''<style>{BASE}h1{{position:absolute;left:80px;top:300px;width:920px;font-size:92px;line-height:1.0;font-weight:800;letter-spacing:-3px;color:{T["t"]}}}</style><body style="background:{T["bg"]}">{top(T,kick)}<h1>{title}</h1>
<div class="abs" style="left:80px;top:640px;width:400px;height:480px;background:#fff;display:flex;align-items:center;justify-content:center;border-top:10px solid {R}"><img src="{q}" style="height:380px;width:auto"></div>
<div class="abs" style="left:530px;top:640px;width:470px">{its}</div>{foot(T)}</body>'''
cards={"n_confiance":confiance("ciel","QUALIFICATIONS ET ASSURANCES","Des qualifications, des assurances.",[("Qualibat","peinture, ravalement, plaques de plâtre"),("Mention RGE","isolation thermique par l’intérieur"),("RC Pro et décennale","numéro de police indiqué sur chaque devis")])}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for n,h in cards.items():
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{n}.png")
        await b.close()
asyncio.run(main())
