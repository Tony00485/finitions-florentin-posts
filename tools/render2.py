#!/usr/bin/env python3
"""Cartes « magazine » : logo, accroche, contenu varié, bandeau de pied coloré avec bouton.
Usage : python3 tools/render2.py spec.json dossier_sortie
Spec : [{"out":"nom","theme":"marine|ciel|blanc|pierre|degrade","kind":"checks|numbers|tiles|stat|duo",
 "kick":"…","title":"…","intro":"…(option)","items":[...],"note":"…(option)","foot":"…","cta":"Devis gratuit","stat":"2005"}]
items : checks → ["texte",...] ; numbers/tiles → [["titre","texte"],...] ; stat → [["titre","texte"],...] ; duo → [["titre","texte"],["titre","texte"]]"""
import sys, os, json, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
R="#E31B0F"; B="#1E3B7D"; N="#14264F"
def b64(f): return "data:image/png;base64,"+base64.b64encode(open(f,'rb').read()).decode()
L=b64('logo_orig.png'); LW=b64('logo_white.png')
TH={
 "marine": dict(bg=f"linear-gradient(170deg,#2F6AB5 0%,{B} 40%,{N} 100%)",t="#FFFFFF",k="#FF6A5C",v="#C9D3EA",card="rgba(255,255,255,.09)",line="rgba(255,255,255,.25)",foot=N,fl="#8FD0F0",chip=True,dark=True,btn=R,btnt="#FFF"),
 "ciel":   dict(bg="#93CBEA",t=N,k=R,v="#27406E",card="rgba(255,255,255,.55)",line="rgba(20,38,79,.3)",foot=N,fl="#8FD0F0",chip=True,dark=False,btn="#FFFFFF",btnt=B),
 "blanc":  dict(bg="#FFFFFF",t=N,k=R,v="#4A5776",card="#F1F4FA",line="#D8DBE2",foot="#3A78B9",fl="#FFFFFF",chip=False,dark=False,btn=R,btnt="#FFF"),
 "pierre": dict(bg="#E8E4DD",t=N,k=R,v="#4A5776",card="#FFFFFF",line="rgba(20,38,79,.22)",foot=B,fl="#FFFFFF",chip=False,dark=False,btn=R,btnt="#FFF"),
 "degrade":dict(bg=f"linear-gradient(160deg,{B} 0%,{N} 100%)",t="#FFFFFF",k="#FF6A5C",v="#C9D3EA",card="rgba(255,255,255,.09)",line="rgba(255,255,255,.25)",foot="#0E1B3A",fl="#8FD0F0",chip=True,dark=True,btn=R,btnt="#FFF"),
}
def body(c,T):
    k=c['kind']; it=c.get('items',[])
    if k=='checks':
        rows="".join(f'<div class="row"><i class="ck">✓</i><span>{x}</span></div>' for x in it)
        return f'<div class="list">{rows}</div>'
    if k=='numbers':
        rows="".join(f'<div class="nrow"><b class="n">{i+1:02d}</b><div><div class="h">{a}</div><div class="p">{b}</div></div></div>' for i,(a,b) in enumerate(it))
        return f'<div class="list">{rows}</div>'
    if k=='tiles':
        t="".join(f'<div class="tile"><b class="n">{i+1:02d}</b><div class="h">{a}</div><div class="p">{b}</div></div>' for i,(a,b) in enumerate(it))
        return f'<div class="grid">{t}</div>'
    if k=='stat':
        t="".join(f'<div class="srow"><b>{a}</b><span>{b}</span></div>' for a,b in it)
        return f'<div class="big">{c["stat"]}</div><div class="list">{t}</div>'
    if k=='duo':
        t="".join(f'<div class="duo"><div class="h">{a}</div><div class="p">{b}</div></div>' for a,b in it)
        return f'<div class="duos">{t}</div>'
def html_photo(c):
    T=TH[c.get('theme','blanc')]
    ph="data:image/jpeg;base64,"+base64.b64encode(open(os.path.join(os.path.dirname(HERE),'photos',c['photo']),'rb').read()).decode()
    return f'''<style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:760px;object-fit:cover;object-position:{c.get("pos","50% 50%")}}}
.lg{{position:absolute;left:60px;top:60px;width:300px;padding:18px 22px;background:#fff}}
.k{{position:absolute;left:80px;top:810px;font-size:25px;font-weight:700;letter-spacing:7px;color:{T["k"]}}}
.t{{position:absolute;left:80px;top:856px;width:920px;font-size:64px;line-height:1.08;font-weight:800;letter-spacing:-1.5px}}
.s{{position:absolute;left:80px;top:1035px;width:920px;font-size:31px;line-height:1.4;font-weight:500;color:{T["v"]}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:170px;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:28px;font-weight:700;line-height:1.3;color:{T["fl"]}}}.fl small{{display:block;font-size:20px;font-weight:600;opacity:.85}}
.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:30px;font-weight:800;padding:26px 48px}}</style>
<body><img class="ph" src="{ph}"><img class="lg" src="{L}"><div class="k">{c["kick"]}</div><div class="t">{c["title"]}</div><div class="s">{c.get("sub","")}</div>
<div class="foot"><div class="fl">{c["foot"]}<small>{"Lyon et alentours" if c.get("nosite") else "finitionsflorentin.fr · Lyon"}</small></div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>'''
def html(c):
    c=dict(c)
    for k in ('title','kick','sub','note','intro','foot'):
        if c.get(k): c[k]=c[k].replace(' ?','&nbsp;?').replace(' :','&nbsp;:').replace(' !','&nbsp;!')
    if c['kind']=='photo': return html_photo(c)
    T=TH[c['theme']]
    logo=f'<img class="lg" src="{LW if T["dark"] else L}">'
    intro=f'<div class="intro">{c["intro"]}</div>' if c.get('intro') else ''
    note=f'<div class="note">{c["note"]}</div>' if c.get('note') else ''
    return f'''<style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.chip{{position:absolute;left:80px;top:80px;background:#fff;border-radius:0;padding:22px 30px;box-shadow:0 8px 24px rgba(0,0,0,.18)}}.chip img{{width:290px;display:block}}
.lg{{position:absolute;left:80px;top:90px;width:340px}}
.k{{position:absolute;left:80px;top:300px;font-size:25px;font-weight:700;letter-spacing:7px;color:{T["k"]}}}
.t{{position:absolute;left:80px;top:350px;width:920px;font-size:76px;line-height:1.05;font-weight:800;letter-spacing:-2px}}
.rule{{position:absolute;left:80px;width:120px;height:7px;background:{R}}}
.intro{{position:absolute;left:80px;width:920px;font-size:34px;line-height:1.4;font-weight:500;color:{T["v"]}}}
.body{{position:absolute;left:80px;width:920px}}
.row{{display:flex;gap:26px;align-items:center;font-size:40px;font-weight:600;margin-bottom:30px;line-height:1.25}}
.ck{{flex:none;width:52px;height:52px;border-radius:0;background:{R};color:#fff;font-style:normal;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center}}
.nrow{{display:flex;gap:28px;margin-bottom:34px}}.n{{color:{R if T["bg"].startswith("#") else "#F58A3D"};font-size:30px;font-weight:800;padding-top:4px;min-width:56px}}
.h{{font-size:38px;font-weight:700;line-height:1.2}}.p{{font-size:30px;line-height:1.35;font-weight:500;color:{T["v"]};margin-top:6px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}.tile{{background:{T["card"]};border:2px solid {T["line"]};border-radius:0;padding:30px 30px 34px;min-height:230px}}
.tile .n{{display:block;font-size:26px;margin-bottom:10px}}
.big{{font-size:230px;line-height:1;font-weight:800;letter-spacing:-8px;color:{R if not T["bg"].startswith("linear") else "#FFFFFF"};margin-bottom:10px}}
.srow{{display:flex;gap:26px;align-items:baseline;border-top:2px solid {T["line"]};padding:24px 0;font-size:34px}}.srow b{{min-width:200px;font-size:36px}}.srow span{{color:{T["v"]};font-weight:500}}
.duos{{display:flex;gap:28px}}.duo{{flex:1;background:{T["card"]};border:2px solid {T["line"]};border-radius:0;padding:34px}}
.note{{position:absolute;left:80px;width:920px;font-size:31px;line-height:1.4;font-weight:500;color:{T["v"]}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:170px;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:28px;font-weight:700;line-height:1.3;color:{T["fl"]}}}.fl small{{display:block;font-size:20px;font-weight:600;opacity:.85}}
.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:30px;font-weight:800;padding:26px 48px;border-radius:0}}</style>
<body>{logo}<div class="k">{c["kick"]}</div><div class="t">{c["title"]}</div>
<div class="rule" id="rule"></div>{intro}<div class="body" id="body">{body(c,T)}</div>{note}
<div class="foot"><div class="fl">{c["foot"]}<small>{"Lyon et alentours" if c.get("nosite") else "finitionsflorentin.fr · Lyon"}</small></div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>
<script>(function(){{
const t=document.querySelector('.t'),r=document.getElementById('rule'),b=document.getElementById('body'),i=document.querySelector('.intro'),n=document.querySelector('.note');
let y=t.offsetTop+t.offsetHeight+28; r.style.top=y+'px'; y+=7+34;
if(i){{i.style.top=y+'px'; y+=i.offsetHeight+34;}}
const end=1350-170-60; let h=b.offsetHeight+(n?24+n.offsetHeight:0); let sh=Math.max(0,(end-y-h)/2);
b.style.top=(y+sh)+'px'; y+=sh+b.offsetHeight+24; if(n) n.style.top=y+'px';
}})();</script>'''
async def main(spec,out):
    from playwright.async_api import async_playwright
    os.makedirs(out,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for c in spec:
            await pg.set_content(f"<html>{html(c)}</html>"); await pg.wait_for_timeout(600)
            await pg.screenshot(path=os.path.join(out,c['out']+'.png')); print('ok',c['out'])
        await b.close()
if __name__=="__main__": asyncio.run(main(json.load(open(sys.argv[1])),sys.argv[2]))
