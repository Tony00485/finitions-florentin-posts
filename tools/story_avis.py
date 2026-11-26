#!/usr/bin/env python3
"""Stories « Avis clients » 1080x1920 (charte render2). Texte des avis repris tel quel (coupes signalées par …), clients anonymisés.
Usage : python3 tools/story_avis.py $PWD/ig/stories/avis"""
import sys, os, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import render2 as R
ROOT=os.path.dirname(HERE)
GL="data:image/png;base64,"+base64.b64encode(open(os.path.join(ROOT,'photos_selection/logos/google_avis_clean.png'),'rb').read()).decode()
T=R.TH['pierre']; M=R.TH['marine']
AVIS=[
("Je ne peux que vous recommander cette entreprise pour vos travaux d'isolation et création de cloison. Les délais ont été tenus, les finitions sont soignées et les échanges rapides. Je suis très satisfaite du travail et du résultat !","Client · isolation et création de cloison"),
("Nous avons choisi cette entreprise pour une rénovation complète d'une vieille maison et nous en sommes ravis. Très bon accueil par Anthony, devis clair, détaillé. … Le suivi du chantier a été très bien fait, les délais respectés. … C'est un plaisir de travailler avec une entreprise comme celle-ci.","Client · rénovation complète d'une maison"),
("Je suis satisfait de l'entreprise … bon contact, devis clair, planning d'intervention respecté, travail satisfaisant, Mr D'Orazio a été disponible. Je recommande cette entreprise.","Client · réfection des peintures d'un F3"),
("Le chantier a été rapide, bien préparé au préalable, et les travaux très bien effectués. Le suivi client a également été très satisfaisant. Je recommande donc cette entreprise que je remercie par ailleurs pour son professionnalisme.","Client · rénovation d'un appartement"),
("Monsieur D'Orazio et son équipe sont intervenus avec une contrainte, de mon côté, de travaux à réaliser au plus vite. Les délais ont été respectés et la qualité était au rendez-vous ! Je recommande grandement Finitions Florentin et son équipe. Un grand merci pour leur professionnalisme !","Client · travaux à réaliser au plus vite"),
("Nous avons fait appel à la société Finitions Florentin pour refaire notre salle de bains et notre wc (murs, plafond, carrelage, peinture et sol). Travail soigné, employé efficace et les patrons … sont facilement joignables et à l'écoute.","Client · salle de bains et WC"),
("Nous avons été comblés par les services de finitions florentin. Un accueil sympathique et un devis clair nous ont inspiré confiance … Nous avons beaucoup apprécié le travail de finition effectué, le respect de l'engagement pris et la sympathie de l'équipe …","Client · préparation d'une nouvelle cuisine"),
("Réactivité, sérieux, disponibilité, gentillesse, efficacité, clarté dans les devis … Leurs équipes sont efficaces, le travail est bien fait ! En résumé, Bravo Messieurs !","Client · rénovation à Lyon"),
]
BASE=f'''*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{T["bg"]};color:{T["t"]}}}
.lg{{position:absolute;left:60px;top:110px;width:260px;padding:16px 20px;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,.18)}}
.gl{{position:absolute;right:60px;top:110px;height:94px;box-shadow:0 8px 24px rgba(0,0,0,.18)}}
.band{{position:absolute;left:0;width:1080px;height:150px;background:{T["foot"]};display:flex;justify-content:space-between;align-items:center;padding:0 70px}}
.fl{{margin-top:32px;font-size:28px;font-weight:700;color:{T["fl"]}}}.btn{{background:{T["btn"]};color:{T["btnt"]};font-size:32px;font-weight:800;padding:24px 44px}}'''
def avis(i,txt,who):
    n=len(txt); fs=58 if n<190 else 50 if n<250 else 45
    return f'''<style>{BASE}
.stars{{position:absolute;left:70px;top:330px;font-size:96px;letter-spacing:10px;color:#FFC21A;line-height:1}}
.q{{position:absolute;left:62px;top:400px;font-size:230px;line-height:1;font-weight:800;color:#E31B0F;font-family:Georgia,serif}}
.t{{position:absolute;left:70px;top:600px;width:940px;font-size:{fs}px;line-height:1.28;font-weight:600;color:{R.N}}}
.rule{{position:absolute;left:70px;top:1380px;width:100px;height:6px;background:#E31B0F}}
.w{{position:absolute;left:70px;top:1410px;font-size:32px;font-weight:700;color:{T["v"]}}}
.band{{top:1560px;height:360px;align-items:flex-start;padding-top:50px}}</style>
<body><img class="lg" src="{R.L}"><img class="gl" src="{GL}"><div class="stars">★★★★★</div><div class="q">“</div>
<div class="t">{txt}</div><div class="rule"></div><div class="w">{who}</div>
<div class="band"><div class="fl">Avis Google · Lyon et alentours</div><div class="btn">Devis gratuit</div></div>'''
def intro():
    return f'''<style>{BASE}body{{background:{M["bg"]}}}.lg{{top:110px}}
.k{{position:absolute;left:70px;top:420px;font-size:34px;font-weight:700;letter-spacing:8px;color:#FF8A7C}}
.stars{{position:absolute;left:70px;top:500px;font-size:124px;letter-spacing:12px;color:#FFC21A;line-height:1}}
.n{{position:absolute;left:64px;top:640px;font-size:400px;font-weight:800;letter-spacing:-10px;color:#fff;line-height:.9}}.n small{{font-size:120px;letter-spacing:0;color:#C9D3EA}}
.rb{{position:absolute;left:0;top:1090px;width:1080px;height:170px;background:#E31B0F;display:flex;align-items:center;padding:0 70px;gap:24px;color:#fff}}.rb b{{font-size:130px;font-weight:800;letter-spacing:-3px;line-height:1}}.rb span{{font-size:56px;font-weight:700}}
.t{{position:absolute;left:70px;top:1330px;font-size:60px;font-weight:800;color:#fff;letter-spacing:-1px}}.s{{position:absolute;left:70px;top:1420px;font-size:34px;color:#C9D3EA;font-weight:500}}</style>
<body><img class="lg" src="{R.L}"><img class="gl" src="{GL}"><div class="k">AVIS CLIENTS</div><div class="stars">★★★★★</div><div class="n">4,9<small>/5</small></div>
<div class="rb"><b>220</b><span>avis clients</span></div><div class="t">Ce que disent nos clients</div><div class="s">Glissez pour lire leurs avis →</div>'''
def outro():
    return f'''<style>{BASE}body{{background:{M["bg"]}}}
.t{{position:absolute;left:70px;top:620px;width:940px;font-size:96px;line-height:1.05;font-weight:800;color:#fff;letter-spacing:-2px}}
.rule{{position:absolute;left:70px;top:960px;width:100px;height:6px;background:#E31B0F}}
.s{{position:absolute;left:70px;top:1000px;width:940px;font-size:46px;line-height:1.35;font-weight:500;color:#C9D3EA}}
.btn2{{position:absolute;left:70px;top:1330px;background:{T["btn"]};color:#fff;font-size:44px;font-weight:800;padding:34px 60px}}</style>
<body><img class="lg" src="{R.L}"><div class="t">Merci pour votre confiance</div><div class="rule"></div>
<div class="s">Un projet à Lyon et alentours ? Écrivez-nous en message privé.</div><div class="btn2">Devis gratuit</div>'''
async def main(out):
    from playwright.async_api import async_playwright
    os.makedirs(out,exist_ok=True)
    pages=[("avis_0_intro",intro())]+[(f"avis_{i}",avis(i,t,w)) for i,(t,w) in enumerate(AVIS,1)]+[("avis_9_merci",outro())]
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await br.new_page(viewport={"width":1080,"height":1920})
        for name,h in pages:
            await pg.set_content(f"<html>{h}</html>"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out,name+'.png')); print('ok',name)
        await br.close()
asyncio.run(main(sys.argv[1]))
