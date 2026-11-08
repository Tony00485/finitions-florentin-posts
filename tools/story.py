#!/usr/bin/env python3
"""Stories 1080x1920 dans le style render2. Usage : python3 tools/story.py spec.json dossier_sortie
kind : card | photo | split. Zones sûres : rien d'important au-dessus de y=220 ni sous y=1720.
"sticker": true laisse une zone vide (y 1080-1440 en card, centre de la photo en photo) pour coller le sticker à la main."""
import sys, os, json, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
ROOT=os.path.dirname(HERE)
def img64(p): return "data:image/jpeg;base64,"+base64.b64encode(open(os.path.join(ROOT,p),'rb').read()).decode()
def nb(s): return s.replace(' ?','&nbsp;?').replace(' :','&nbsp;:').replace(' !','&nbsp;!') if s else s
BASE="""*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{bg};color:{t}}}
.k{{font-size:30px;font-weight:700;letter-spacing:8px;color:{k}}}.t{{font-size:92px;line-height:1.05;font-weight:800;letter-spacing:-2px;margin-top:22px}}
.rule{{width:140px;height:8px;background:#E31B0F;margin:40px 0}}.s{{font-size:42px;line-height:1.35;font-weight:500;color:{v}}}
.band{{position:absolute;left:0;right:0;top:1540px;height:170px;background:{foot};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:32px;font-weight:700;color:{fl};line-height:1.25}}.btn{{background:{btn};color:{btnt};font-size:34px;font-weight:800;padding:28px 44px}}"""
def card(c):
    T=R.TH[c['theme']]; css=BASE.format(**T)
    logo=R.LW if T['dark'] else R.L
    return f'''<style>{css}.lg{{position:absolute;left:80px;top:240px;width:380px}}.box{{position:absolute;left:80px;top:470px;width:920px}}</style>
<body><img class="lg" src="{logo}"><div class="box"><div class="k">{nb(c["kick"])}</div><div class="t">{nb(c["title"])}</div><div class="rule"></div><div class="s">{nb(c.get("sub",""))}</div></div>
<div class="band"><div class="fl">{nb(c.get("foot",""))}</div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>'''
def photo(c):
    T=R.TH[c.get('theme','blanc')]; css=BASE.format(**T)
    return f'''<style>{css}.ph{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;object-position:{c.get("pos","50% 50%")}}}
.top{{position:absolute;left:0;right:0;top:0;height:520px;background:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,0))}}
.lg{{position:absolute;left:80px;top:240px;width:330px;padding:20px 24px;background:#fff}}
.panel{{position:absolute;left:0;right:0;top:{c.get("paneltop",1130)}px;bottom:0;background:{T["bg"]};padding:56px 80px}}.panel .t{{font-size:74px}}.panel .s{{font-size:38px;margin-top:20px}}</style>
<body><img class="ph" src="{img64(c["photo"])}"><div class="top"></div><img class="lg" src="{R.L}">
<div class="panel"><div class="k">{nb(c["kick"])}</div><div class="t">{nb(c["title"])}</div><div class="s">{nb(c.get("sub",""))}</div></div>
<div class="band"><div class="fl">{nb(c.get("foot",""))}</div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>'''
def split(c):
    T=R.TH[c.get('theme','marine')]; css=BASE.format(**T)
    return f'''<style>{css}.a,.b{{position:absolute;left:0;width:1080px;object-fit:cover}}.a{{top:0;height:760px;object-position:{c.get("posa","50% 40%")}}}.b{{top:760px;height:780px;object-position:{c.get("posb","50% 40%")}}}
.tag{{position:absolute;left:80px;background:#E31B0F;color:#fff;font-size:34px;font-weight:800;letter-spacing:6px;padding:14px 26px}}
.lg{{position:absolute;right:80px;top:240px;width:300px;padding:18px 22px;background:#fff}}
.mid{{position:absolute;left:0;right:0;top:700px;height:120px;background:{T["foot"]};display:flex;align-items:center;padding:0 80px;font-size:46px;font-weight:800;color:#fff}}</style>
<body><img class="a" src="{img64(c["avant"])}"><img class="b" src="{img64(c["apres"])}"><img class="lg" src="{R.L}">
<div class="tag" style="top:600px">AVANT</div><div class="mid">{nb(c["title"])}</div><div class="tag" style="top:860px">APRÈS</div>
<div class="band"><div class="fl">{nb(c.get("foot",""))}</div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>'''
async def main(spec,out):
    from playwright.async_api import async_playwright
    os.makedirs(out,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1920})
        for c in spec:
            h={'card':card,'photo':photo,'split':split}[c['kind']](c)
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(out,c['out']+'.png')); print('ok',c['out'])
        await b.close()
if __name__=="__main__":
    spec=json.load(open(sys.argv[1])); out=os.path.abspath(sys.argv[2]); asyncio.run(main(spec,out))
