#!/usr/bin/env python3
"""Rend des cartes 1080x1350 à partir d'un fichier JSON.
Usage : python3 tools/render.py spec.json dossier_sortie
Spec : liste d'objets {"out":"nom", "layout":"lst|qa|vf|frise|pastilles|geant|tuiles|coches|confiance|photo",
        "args":[...], "kwargs":{...}}
Voir README.md pour les arguments de chaque mise en page."""
import sys, os, re, json, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
os.chdir(HERE)
def head(fn,marker="cards={"): return open(fn).read().split(marker)[0]
A={}; exec(head('build13.py'),A)                # lst, qa, vf (thèmes blanc, bleu, ciel, pierre)
B={}; exec(head('build22.py'),B)                # frise, pastilles, geant, tuiles, coches
src23=open('build23.py').read()
conf=src23[src23.index("def confiance"):src23.index("cards={")]
exec(conf,B)
def photo(kick,title,sub,img,pos="50% 50%"):
    b64=B['b64']; L=B['L']; R=B['R']; Bl=B['B']
    ph="data:image/jpeg;base64,"+base64.b64encode(open(os.path.join(ROOT,'photos',img),'rb').read()).decode()
    css=f"""*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:#000}}
.ph{{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;object-position:{pos}}}
.card{{position:absolute;left:40px;right:40px;bottom:40px;height:380px;background:#fff;color:{Bl}}}
.bar{{position:absolute;left:0;height:10px}}
.k{{position:absolute;left:44px;top:62px;font-size:21px;font-weight:600;letter-spacing:6px;color:{R}}}
.t{{position:absolute;left:44px;top:102px;width:640px;font-size:52px;line-height:1.08;font-weight:800;letter-spacing:-1.5px}}
.s{{position:absolute;left:44px;top:226px;width:700px;font-size:24px;line-height:1.4;color:#4F586B;font-weight:500}}
.logo{{position:absolute;right:44px;top:66px;width:250px}}
.f{{position:absolute;left:44px;right:44px;bottom:30px;display:flex;justify-content:space-between;font-size:22px;font-weight:600}}
.f em{{font-style:normal;color:{R};font-weight:800}}"""
    return f'''<style>{css}</style><body><img class="ph" src="{ph}"><div class="card"><div class="bar" style="top:0;width:300px;background:{R}"></div><div class="bar" style="top:10px;width:380px;background:{Bl}"></div><div class="bar" style="top:20px;width:220px;background:#000"></div><div class="k">{kick}</div><div class="t">{title}</div><div class="s">{sub}</div><img class="logo" src="{L}"><div class="f"><span>finitionsflorentin.fr · Lyon</span><em>Devis gratuit →</em></div></div></body>'''
FN={'lst':A['lst'],'qa':A['qa'],'vf':A['vf'],'frise':B['frise'],'pastilles':B['pastilles'],'geant':B['geant'],'tuiles':B['tuiles'],'coches':B['coches'],'confiance':B['confiance'],'photo':photo}
async def main(spec,out):
    from playwright.async_api import async_playwright
    os.makedirs(out,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for c in spec:
            h=FN[c['layout']](*c.get('args',[]),**c.get('kwargs',{}))
            if c.get('nobars'): h=re.sub(r'<div class="abs" style="left:0;top:\d+px;width:\d+px;height:22px;background:[^"]*"></div>','',h)
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(out,c['out']+'.png'))
            print('ok',c['out'])
        await b.close()
if __name__=="__main__":
    asyncio.run(main(json.load(open(sys.argv[1])),sys.argv[2]))
