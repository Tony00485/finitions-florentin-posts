#!/usr/bin/env python3
"""Visuel « note Google » (render2 pierre). Usage : python3 tools/note_google.py NOTE NB_AVIS $PWD/ig/note_google.png [ig|google]
ig = 1080x1350 ; google = 1200x900 (sans site/tel/email)."""
import sys, os, asyncio
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R, base64
GL='data:image/png;base64,'+base64.b64encode(open(os.path.join(os.path.dirname(HERE),'photos_selection/logos/google_avis_clean.png'),'rb').read()).decode()
def html(note,nb,mode):
    T=R.TH['pierre']; W,H=(1080,1350) if mode=='ig' else (1200,900)
    if mode=='ig': big,lg,top,fh,ts,ss=380,300,260,170,66,32
    else: big,lg,top,fh,ts,ss=230,250,178,120,50,27
    return f'''<style>*{{margin:0;box-sizing:border-box}}body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.lg{{position:absolute;left:60px;top:55px;width:{lg}px;padding:16px 20px;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.15)}}
.k{{position:absolute;left:80px;top:{top}px;font-size:25px;font-weight:700;letter-spacing:7px;color:{T["k"]}}}
.n{{position:absolute;left:70px;top:{top-10}px;font-size:{big}px;line-height:1;font-weight:800;letter-spacing:-8px;color:{R.N}}}.n small{{font-size:{big//3}px;letter-spacing:0;color:#4A5776;font-weight:700}}
.st{{position:absolute;left:80px;top:{top-10+big+20}px;display:flex;align-items:center;gap:28px}}.st img{{height:{int(big*0.42)}px;box-shadow:0 6px 18px rgba(0,0,0,.12)}}.st span{{font-size:{big//9}px;color:{R.N};font-weight:700}}
.t{{position:absolute;left:80px;top:{top-10+big+20+int(big*0.42)+60}px;width:{W-160}px;font-size:{ts}px;line-height:1.08;font-weight:800;letter-spacing:-1.5px}}
.rule{{position:absolute;left:80px;top:{top-10+big+20+int(big*0.42)+60+int(ts*1.15)+34}px;width:100px;height:6px;background:#E31B0F}}
.s{{position:absolute;left:80px;top:{top-10+big+20+int(big*0.42)+60+int(ts*1.15)+68}px;width:{W-160}px;font-size:{ss}px;line-height:1.35;font-weight:500;color:{T["v"]}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:{fh}px;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:28px;font-weight:700;color:{T["fl"]}}}.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:30px;font-weight:800;padding:24px 48px}}</style>
<body><img class="lg" src="{R.L}"><div class="n">{note}<small>/5</small></div>
<div class="st"><img src="{GL}"><span>{nb} avis clients</span></div>
<div class="t">Merci pour votre confiance</div><div class="rule"></div>
<div class="s">Merci à tous ceux qui ont laissé un avis.</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
async def main(note,nb,out,mode):
    from playwright.async_api import async_playwright
    W,H=(1080,1350) if mode=='ig' else (1200,900)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await br.new_page(viewport={"width":W,"height":H})
        await pg.set_content(f"<html>{html(note,nb,mode)}</html>"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out); await br.close()
asyncio.run(main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4] if len(sys.argv)>4 else 'ig'))
