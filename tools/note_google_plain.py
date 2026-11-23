#!/usr/bin/env python3
"""Visuel « note Google » sans photo : bloc marine de la charte + note en blanc.
Usage : python3 tools/note_google_plain.py NOTE NB_AVIS $PWD/sortie.png [ig|google]"""
import sys, os, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
ROOT=os.path.dirname(HERE)
GL="data:image/png;base64,"+base64.b64encode(open(os.path.join(ROOT,'photos_selection/logos/google_avis_clean.png'),'rb').read()).decode()
MAR=R.TH['marine']; T=R.TH['pierre']
base=f'''*{{margin:0;box-sizing:border-box}}body{{position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.blk{{position:absolute;background:{MAR["bg"]}}}.lg{{position:absolute;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.25)}}
.gl{{position:absolute;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.25)}}
.num{{position:absolute;font-weight:800;letter-spacing:-8px;color:#fff;line-height:.9}}.num small{{letter-spacing:0;color:#C9D3EA;font-weight:700}}
.avis{{position:absolute;color:#fff;font-weight:700;display:flex;align-items:baseline;gap:14px;white-space:nowrap}}.big{{font-weight:800;color:#FF6A5C;letter-spacing:-2px}}
.t{{position:absolute;font-weight:800;letter-spacing:-1.5px;white-space:nowrap}}.rule{{position:absolute;width:100px;height:6px;background:#E31B0F}}.s{{position:absolute;font-weight:500;color:{T["v"]}}}
.foot{{position:absolute;bottom:0;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center}}
.fl{{font-size:28px;font-weight:700;color:{T["fl"]}}}.btn{{background:{T["btn"]};color:{T["btnt"]};font-weight:800}}'''
def html(note,nb,mode):
    if mode=='ig':
        return f'''<style>{base}body{{width:1080px;height:1350px}}
.blk{{left:0;top:0;width:1080px;height:800px}}.lg{{left:60px;top:55px;width:270px;padding:16px 20px}}
.gl{{left:60px;top:200px;height:130px;}}.num{{left:70px;top:355px;font-size:320px}}.num small{{font-size:100px}}
.avis{{left:80px;top:665px;font-size:42px}}.big{{font-size:100px}}
.t{{left:80px;top:880px;font-size:64px}}.rule{{left:80px;top:992px}}.s{{left:80px;top:1026px;font-size:31px}}
.foot{{left:0;right:0;height:150px;padding:0 80px}}.btn{{font-size:30px;padding:24px 48px}}</style>
<body><div class="blk"></div><img class="lg" src="{R.L}"><img class="gl" src="{GL}">
<div class="num">{note}<small>/5</small></div><div class="avis"><span class="big">{nb}</span> avis clients</div>
<div class="t">Merci pour votre confiance</div><div class="rule"></div><div class="s">Merci à tous ceux qui ont laissé un avis.</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
    return f'''<style>{base}body{{width:1200px;height:900px}}
.blk{{left:0;top:0;width:620px;height:900px}}.gl{{left:60px;top:70px;height:120px}}
.num{{left:50px;top:230px;font-size:260px}}.num small{{font-size:80px}}.avis{{left:60px;top:560px;font-size:34px}}.big{{font-size:110px}}
.lg{{left:680px;top:60px;width:250px;padding:14px 18px}}.t{{left:680px;top:300px;font-size:46px;white-space:normal;width:480px;line-height:1.1}}
.rule{{left:680px;top:450px}}.s{{left:680px;top:486px;width:470px;font-size:27px;line-height:1.35}}
.foot{{left:620px;right:0;height:120px;padding:0 40px}}.btn{{font-size:24px;padding:20px 28px}}</style>
<body><div class="blk"></div><img class="gl" src="{GL}"><div class="num">{note}<small>/5</small></div>
<div class="avis"><span class="big">{nb}</span> avis clients</div><img class="lg" src="{R.L}">
<div class="t">Merci pour votre confiance</div><div class="rule"></div><div class="s">Merci à tous ceux qui ont laissé un avis.</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
async def main(note,nb,out,mode):
    from playwright.async_api import async_playwright
    W,H=(1080,1350) if mode=='ig' else (1200,900)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await br.new_page(viewport={"width":W,"height":H})
        await pg.set_content(f"<html>{html(note,nb,mode)}</html>"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out); await br.close()
asyncio.run(main(*sys.argv[1:4],sys.argv[4] if len(sys.argv)>4 else 'ig'))
