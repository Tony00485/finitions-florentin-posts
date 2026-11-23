#!/usr/bin/env python3
"""Post duo (2 portraits) style render2 pierre, 1080x1350. Usage: python3 tools/duo_equipe.py $PWD/photos_selection/equipe/anthony.png $PWD/photos_selection/equipe/jordan.png $PWD/ig/equipe/duo.png"""
import sys, os, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
def b(f): return "data:image/png;base64,"+base64.b64encode(open(f,'rb').read()).decode()
def html(a,j):
    T=R.TH['pierre']
    return f'''<style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.p{{position:absolute;top:0;width:536px;height:830px;object-fit:cover;object-position:50% 22%}}
.g{{position:absolute;top:560px;width:536px;height:270px;background:linear-gradient(180deg,rgba(20,38,79,0),rgba(20,38,79,.35))}}
.lg{{position:absolute;left:44px;top:44px;width:250px;padding:16px 20px;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.2)}}
.n{{position:absolute;top:770px;width:440px;background:{R.N};color:#fff;padding:20px 28px 18px;border-top:6px solid #E31B0F;box-shadow:0 10px 26px rgba(20,38,79,.28)}}
.n b{{display:block;font-size:34px;font-weight:800;letter-spacing:-.5px;line-height:1.15}}.n small{{display:block;font-size:19px;font-weight:600;color:#9FD3F2;margin-top:6px;letter-spacing:.3px}}
.k{{position:absolute;left:80px;top:928px;font-size:24px;font-weight:700;letter-spacing:7px;color:{T["k"]}}}
.t{{position:absolute;left:80px;top:972px;width:940px;white-space:nowrap;font-size:58px;line-height:1.05;font-weight:800;letter-spacing:-1.5px}}
.rule{{position:absolute;left:80px;top:1056px;width:100px;height:6px;background:#E31B0F}}
.s{{position:absolute;left:80px;top:1094px;width:940px;white-space:nowrap;font-size:27px;line-height:1.35;font-weight:500;color:{T["v"]}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:130px;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 80px}}
.fl{{font-size:28px;font-weight:700;color:{T["fl"]}}}.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:30px;font-weight:800;padding:24px 48px}}</style>
<body><img class="p" style="left:0" src="{b(a)}"><img class="p" style="left:544px" src="{b(j)}"><div class="g" style="left:0"></div><div class="g" style="left:544px"></div>
<img class="lg" src="{R.L}">
<div class="n" style="left:44px"><b>Anthony D'Orazio</b><small>Gérant · Commercial et administratif</small></div>
<div class="n" style="left:588px"><b>Jordan D'Orazio</b><small>Gérant · Technique et coordination</small></div>
<div class="k">DEUX FRÈRES, UNE ENTREPRISE</div><div class="t">Enchantés, Anthony &amp; Jordan</div><div class="rule"></div>
<div class="s">Peinture · plâtrerie · isolation · carrelage · revêtements de sol</div>
<div class="foot"><div class="fl">Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
async def main(a,j,out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await br.new_page(viewport={"width":1080,"height":1350})
        await pg.set_content(f"<html>{html(a,j)}</html>"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out); await br.close()
asyncio.run(main(*sys.argv[1:4]))
