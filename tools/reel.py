#!/usr/bin/env python3
"""Reel 1080x1920 « étapes d'un chantier » (ex. PENDANT / APRÈS). Jamais « AVANT » sans vraie photo avant.
Usage : python3 tools/reel.py spec.json sortie.mp4
spec = {"steps":[{"photo":"photos_selection/...","tag":"PENDANT","cap":"Préparation et ratissage"},...],
        "end":{"theme":"marine","kick":"PENDANT / APRÈS","title":"...","sub":"...","foot":"..."}}"""
import sys, os, json, asyncio, subprocess, tempfile
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R, story as S
def step(c):
    T=R.TH['marine']; css=S.BASE.format(**T); im=S.img64(c['photo'])
    return f'''<style>{css}.bg{{position:absolute;inset:-60px;width:1200px;height:2040px;object-fit:cover;filter:blur(40px) brightness(.55)}}
.ph{{position:absolute;left:0;top:{c.get("top",300)}px;width:1080px;height:{c.get("h",1300)}px;object-fit:{c.get("fit","contain")};object-position:{c.get("pos","50% 50%")}}}
.lg{{position:absolute;left:80px;top:150px;width:330px;padding:20px 24px;background:#fff}}
.tag{{position:absolute;left:80px;top:1640px;background:#E31B0F;color:#fff;font-size:44px;font-weight:800;letter-spacing:6px;padding:16px 30px}}
.cap{{position:absolute;left:80px;top:1755px;font-size:38px;font-weight:600;color:#fff}}</style>
<body><img class="bg" src="{im}"><img class="ph" src="{im}"><img class="lg" src="{R.L}">
<div class="tag">{c["tag"]}</div><div class="cap">{S.nb(c.get("cap",""))}</div>'''
async def frames(spec,d):
    from playwright.async_api import async_playwright
    out=[]
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1920})
        items=[step(s) for s in spec['steps']]+[S.card(dict(spec['end']))]
        for i,h in enumerate(items):
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(500)
            f=os.path.join(d,f'f{i}.png'); await pg.screenshot(path=f); out.append(f)
        await b.close()
    return out
def build(spec,mp4,dur=3.0,fade=0.8):
    d=tempfile.mkdtemp(); fs=asyncio.run(frames(spec,d))
    cmd=['ffmpeg','-v','error','-y']
    for f in fs: cmd+=['-loop','1','-t',str(dur),'-i',f]
    cmd+=['-f','lavfi','-t',str(dur*len(fs)-fade*(len(fs)-1)),'-i','anullsrc=r=44100:cl=stereo']
    fc=[];prev='0:v'
    for i in range(1,len(fs)):
        o=f'v{i}'; fc.append(f'[{prev}][{i}:v]xfade=transition=fade:duration={fade}:offset={i*(dur-fade)}[{o}]'); prev=o
    cmd+=['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map',f'{len(fs)}:a','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-r','30','-c:a','aac','-shortest',mp4]
    subprocess.run(cmd,check=True); return fs
if __name__=="__main__":
    fs=build(json.load(open(sys.argv[1])),sys.argv[2]); print('\n'.join(fs))
