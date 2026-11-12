#!/usr/bin/env python3
"""Visuels Google Business Profile au format recommandé 4:3 (1200x900).
Usage : python3 tools/google43.py spec.json dossier_sortie   (chemins ABSOLUS : render2 fait un chdir)
Même spec que render2 (kind photo | checks | stat ...), sans site ni téléphone (Google).
Tout le texte reste dans une zone centrale sûre (marges 60 px) pour éviter tout recadrage."""
import sys, os, json, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
ROOT=os.path.dirname(HERE)
def nb(s): return s.replace(' ?','&nbsp;?').replace(' :','&nbsp;:').replace(' !','&nbsp;!') if s else s
CSS="""*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:900px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{bg};color:{t}}}
.k{{font-size:20px;font-weight:700;letter-spacing:6px;color:{k}}}.t{{font-size:54px;line-height:1.06;font-weight:800;letter-spacing:-1.5px;margin-top:16px}}
.rule{{width:100px;height:6px;background:#E31B0F;margin:26px 0}}.s{{font-size:28px;line-height:1.35;font-weight:500;color:{v}}}
.foot{{position:absolute;bottom:0;height:120px;background:{foot};display:flex;justify-content:space-between;align-items:center;padding:0 50px}}
.fl{{font-size:22px;font-weight:700;line-height:1.3;color:{fl}}}.btn{{white-space:nowrap;background:{btn};color:{btnt};font-size:24px;font-weight:800;padding:20px 32px}}"""
def photo(c):
    T=R.TH[c.get('theme','blanc')]; css=CSS.format(**T)
    ph="data:image/jpeg;base64,"+base64.b64encode(open(os.path.join(ROOT,c['photo']),'rb').read()).decode()
    return f'''<style>{css}.ph{{position:absolute;left:0;top:0;width:640px;height:900px;object-fit:cover;object-position:{c.get("pos","50% 50%")}}}
.pan{{position:absolute;left:640px;top:0;width:560px;height:900px}}.lg{{position:absolute;left:50px;top:60px;width:250px}}
.box{{position:absolute;left:50px;top:190px;width:460px}}.foot{{left:640px;right:0}}</style>
<body><img class="ph" src="{ph}"><div class="pan"><img class="lg" src="{R.LW if T["dark"] else R.L}">
<div class="box"><div class="k">{nb(c["kick"])}</div><div class="t">{nb(c["title"])}</div><div class="rule"></div><div class="s">{nb(c.get("sub",""))}</div></div></div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>'''
def card(c):
    T=R.TH[c.get('theme','marine')]; css=CSS.format(**T)
    items=c.get('items',[])
    lines="".join(f'<div class="s" style="margin-top:16px;font-size:34px">✓ {nb(x if isinstance(x,str) else " ".join(x))}</div>' for x in items)
    return f'''<style>{css}.lg{{position:absolute;left:80px;top:70px;width:290px}}.box{{position:absolute;left:80px;top:220px;width:1040px}}.t{{font-size:72px}}.foot{{left:0;right:0}}</style>
<body><img class="lg" src="{R.LW if T["dark"] else R.L}"><div class="box"><div class="k">{nb(c["kick"])}</div><div class="t">{nb(c["title"])}</div><div class="rule"></div>{lines}</div>
<div class="foot"><div class="fl">{nb(c.get("foot",""))}<br><small style="font-size:17px;opacity:.85">Lyon et alentours</small></div><div class="btn">{c.get("cta","Devis gratuit")}</div></div>'''
async def main(spec,out):
    from playwright.async_api import async_playwright
    os.makedirs(out,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1200,"height":900})
        for c in spec:
            h=photo(c) if c['kind']=='photo' else card(c)
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(out,c['out']+'.png')); print('ok',c['out'])
        await b.close()
if __name__=="__main__": asyncio.run(main(json.load(open(sys.argv[1])),sys.argv[2]))
