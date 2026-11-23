#!/usr/bin/env python3
"""Post duo (2 portraits) style render2 pierre, 1080x1350. Usage: python3 tools/duo_equipe.py $PWD/photos_selection/equipe/anthony.png $PWD/photos_selection/equipe/jordan.png $PWD/ig/equipe/duo.png"""
import sys, os, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
def b(f): return "data:image/png;base64,"+base64.b64encode(open(f,'rb').read()).decode()
def html(a,j):
    T=R.TH['pierre']
    return f'''<style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.p{{position:absolute;top:0;width:540px;height:800px;object-fit:cover;object-position:50% 25%}}
.n{{position:absolute;top:690px;background:#fff;color:{R.N};font-size:28px;font-weight:800;padding:10px 24px;line-height:1.25}}.n small{{display:block;font-size:20px;font-weight:600;color:#4A5776}}
.lg{{position:absolute;left:40px;top:40px;width:230px;padding:14px 18px;background:#fff}}
.k{{position:absolute;left:80px;top:850px;font-size:25px;font-weight:700;letter-spacing:7px;color:{T["k"]}}}
.t{{position:absolute;left:80px;top:896px;width:920px;font-size:62px;line-height:1.08;font-weight:800;letter-spacing:-1.5px}}
.s{{position:absolute;left:80px;top:1010px;width:920px;font-size:31px;line-height:1.4;font-weight:500;color:{T["v"]}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:28px;font-weight:700;color:{T["fl"]}}}.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:30px;font-weight:800;padding:26px 48px}}</style>
<body><img class="p" style="left:0" src="{b(a)}"><img class="p" style="left:540px" src="{b(j)}">
<img class="lg" src="{R.L}"><div class="n" style="left:0">Anthony D'Orazio<small>Gérant · Commercial et administratif</small></div><div class="n" style="left:540px">Jordan D'Orazio<small>Gérant · Technique et coordination</small></div>
<div class="k">DEUX FRÈRES, UNE ENTREPRISE</div><div class="t">Anthony &amp; Jordan D'Orazio</div>
<div class="s">Entreprise lyonnaise fondée en 2005, dirigée par Anthony et Jordan depuis 2019.</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
async def main(a,j,out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await br.new_page(viewport={"width":1080,"height":1350})
        await pg.set_content(f"<html>{html(a,j)}</html>"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out); await br.close()
asyncio.run(main(*sys.argv[1:4]))
