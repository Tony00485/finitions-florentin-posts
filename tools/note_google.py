#!/usr/bin/env python3
"""Visuel « note Google » avec photo (style render2 pierre).
Usage : python3 tools/note_google.py NOTE NB_AVIS PHOTO_RELATIVE_PATH $PWD/sortie.png [ig|google]
ig = 1080x1350 ; google = 1200x900 (sans site/tel/email)."""
import sys, os, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
ROOT=os.path.dirname(HERE)
def b64(rel,mime):
    return f"data:{mime};base64,"+base64.b64encode(open(os.path.join(ROOT,rel),'rb').read()).decode()
GL=b64('photos_selection/logos/google_avis_clean.png','image/png')
def html(note,nb,photo,mode):
    T=R.TH['pierre']; ph=b64(photo,'image/jpeg')
    base=f'''*{{margin:0;box-sizing:border-box}}body{{position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.card{{position:absolute;background:#fff;box-shadow:0 14px 40px rgba(20,38,79,.22);border-top:6px solid #E31B0F}}
.num{{font-weight:800;letter-spacing:-6px;color:{R.N};line-height:.9}}.num small{{letter-spacing:0;color:#4A5776;font-weight:700}}
.avis{{font-weight:700;color:{R.N}}}.rule{{width:100px;height:6px;background:#E31B0F}}
.foot{{position:absolute;left:0;right:0;bottom:0;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:28px;font-weight:700;color:{T["fl"]}}}.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:30px;font-weight:800;padding:24px 48px}}'''
    if mode=='ig':
        return f'''<style>{base}body{{width:1080px;height:1350px}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:720px;object-fit:cover;object-position:50% 88%}}
.lg{{position:absolute;left:44px;top:44px;width:270px;padding:16px 20px;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.18)}}
.card{{left:70px;top:520px;width:940px;height:330px;display:flex;align-items:center;gap:40px;padding:0 40px}}
.num{{font-size:230px}}.num small{{font-size:76px}}.gl{{height:118px;display:block}}.avis{{font-size:30px;margin-top:4px;display:flex;align-items:baseline;gap:14px;white-space:nowrap}}.big{{font-size:92px;font-weight:800;color:#E31B0F;letter-spacing:-2px}}
.t{{position:absolute;left:80px;top:920px;width:920px;font-size:62px;line-height:1.05;font-weight:800;letter-spacing:-1.5px;white-space:nowrap}}
.rule{{position:absolute;left:80px;top:1010px}}.s{{position:absolute;left:80px;top:1042px;font-size:31px;font-weight:500;color:{T["v"]}}}
.foot{{height:150px}}</style>
<body><img class="ph" src="{ph}"><img class="lg" src="{R.L}">
<div class="card"><div class="num">{note}<small>/5</small></div><div><img class="gl" src="{GL}"><div class="avis"><b class="big">{nb}</b> avis clients</div></div></div>
<div class="t">Merci pour votre confiance</div><div class="rule"></div><div class="s">Merci à tous ceux qui ont laissé un avis.</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
    return f'''<style>{base}body{{width:1200px;height:900px}}
.ph{{position:absolute;left:0;top:0;width:520px;height:900px;object-fit:cover;object-position:62% 85%}}
.lg{{position:absolute;left:560px;top:50px;width:240px;padding:14px 18px;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.12)}}
.num{{position:absolute;left:556px;top:140px;font-size:200px}}.num small{{font-size:64px}}
.gl{{position:absolute;left:560px;top:340px;height:100px;box-shadow:0 6px 18px rgba(0,0,0,.12)}}.avis{{position:absolute;left:800px;top:350px;font-size:28px;line-height:1}}.big{{display:block;font-size:84px;font-weight:800;color:#E31B0F;letter-spacing:-2px;margin-bottom:2px}}
.t{{position:absolute;left:560px;top:530px;width:600px;font-size:44px;white-space:nowrap;line-height:1.1;font-weight:800;letter-spacing:-1px}}
.rule{{position:absolute;left:560px;top:630px}}.s{{position:absolute;left:560px;top:660px;width:600px;font-size:25px;font-weight:500;color:{T["v"]}}}
.foot{{height:120px;left:520px;padding:0 50px}}</style>
<body><img class="ph" src="{ph}"><img class="lg" src="{R.L}">
<div class="num">{note}<small>/5</small></div><img class="gl" src="{GL}"><div class="avis"><b class="big">{nb}</b> avis clients</div>
<div class="t">Merci pour votre confiance</div><div class="rule"></div><div class="s">Merci à tous ceux qui ont laissé un avis.</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn" style="font-size:24px;padding:20px 32px">Devis gratuit</div></div>'''
async def main(note,nb,photo,out,mode):
    from playwright.async_api import async_playwright
    W,H=(1080,1350) if mode=='ig' else (1200,900)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await br.new_page(viewport={"width":W,"height":H})
        await pg.set_content(f"<html>{html(note,nb,photo,mode)}</html>"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out); await br.close()
asyncio.run(main(*sys.argv[1:5],sys.argv[5] if len(sys.argv)>5 else 'ig'))
