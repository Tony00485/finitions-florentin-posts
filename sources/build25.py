import asyncio, base64
from playwright.async_api import async_playwright
def b64(p,m): return f"data:{m};base64,"+base64.b64encode(open(p,'rb').read()).decode()
L=b64('logo_orig.png','image/png')
R="#E31B0F"; B="#1E3B7D"
CSS=f"""*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:#000}}
.ph{{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;object-position:62% 50%}}
.card{{position:absolute;left:40px;right:40px;bottom:40px;height:380px;background:#fff;color:{B}}}
.bar{{position:absolute;left:0;height:10px}}
.k{{position:absolute;left:44px;top:52px;font-size:21px;font-weight:600;letter-spacing:6px;color:{R}}}
.t{{position:absolute;left:44px;top:92px;width:640px;font-size:52px;line-height:1.08;font-weight:800;letter-spacing:-1.5px}}
.s{{position:absolute;left:44px;top:212px;width:700px;font-size:24px;line-height:1.4;color:#4F586B;font-weight:500}}
.logo{{position:absolute;right:44px;top:56px;width:250px}}
.f{{position:absolute;left:44px;right:44px;bottom:30px;display:flex;justify-content:space-between;font-size:22px;font-weight:600}}
.f em{{font-style:normal;color:{R};font-weight:800}}"""
S="Réalisé par Finitions Florentin."
cards=[("cuisine","RÉALISATION","Une cuisine<br>aux finitions soignées.",S),("courbe","PLÂTRERIE · PEINTURE","Une courbe au plafond,<br>des finitions nettes.",S),("terracotta","RÉALISATION","Des teintes chaudes,<br>des lignes nettes.",S),("feuillage","PAPIER PEINT","Un papier peint feuillage,<br>posé avec précision.",S)]
def html(k,kick,t,s):
    ph=b64(f'p_{k}.jpg','image/jpeg')
    return f'''<html><style>{CSS}</style><body><img class="ph" src="{ph}">
<div class="card"><div class="bar" style="top:0;width:300px;background:{R}"></div><div class="bar" style="top:10px;width:380px;background:{B}"></div><div class="bar" style="top:20px;width:220px;background:#000"></div>
<div class="k" style="top:62px">{kick}</div><div class="t" style="top:102px">{t}</div><div class="s" style="top:226px">{s}</div>
<img class="logo" src="{L}" style="top:66px"><div class="f"><span>finitionsflorentin.fr · 07 87 85 93 06</span><em>Devis gratuit →</em></div></div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for c in cards:
            await pg.set_content(html(*c)); await pg.wait_for_timeout(500); await pg.screenshot(path=f"ph_{c[0]}.png")
        await b.close()
asyncio.run(main())
