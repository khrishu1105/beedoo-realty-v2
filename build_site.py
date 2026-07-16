#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""以共用頁首頁尾＋新設計語言（明體/墨藍金/斜切形狀）產生貝多不動產全站頁面。"""
import re
from pathlib import Path

ROOT = Path("/Users/khrishu/My_AI_Agent/beedoo_site/redesign")

# ---- 1) 讀取基礎 CSS（css/base.css），與子頁 EXTRA 合併寫入 site.css ----
base_css = (ROOT / "css" / "base.css").read_text(encoding="utf-8")

CSS_EXTRA = r"""
/* ===== 子頁共用 ===== */
.page-hero{position:relative;background:linear-gradient(150deg,var(--ink-2) 0%,var(--navy) 100%);color:#e8e2d5;padding:118px 0 92px;overflow:hidden;clip-path:polygon(0 0,100% 0,100% calc(100% - 46px),0 100%)}
.page-hero::after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 82% 26%,rgba(201,166,99,.26),transparent 48%);pointer-events:none}
.page-hero .wrap{position:relative;z-index:2}
.crumb{font-family:var(--disp);font-style:italic;letter-spacing:.1em;font-size:.95rem;color:var(--gold-lt);margin-bottom:18px}
.crumb a{color:#b9c3cf}.crumb a:hover{color:var(--gold-lt)}.crumb span{margin:0 10px;opacity:.5}
.page-hero h1{font-size:clamp(2rem,4.6vw,3.1rem);color:#fbf7ee;font-weight:600;letter-spacing:.03em;margin:0 0 16px}
.page-hero .ph-sub{max-width:640px;font-weight:300;color:#cdd6df;font-size:clamp(1.02rem,2vw,1.18rem);margin:0}
.prose{max-width:820px;margin:0 auto}
.prose .meta{font-weight:300;color:var(--muted);font-size:.94rem;border-left:2px solid var(--gold);padding-left:16px;margin-bottom:30px}
.prose h2{font-family:var(--serif);font-size:1.4rem;font-weight:600;color:var(--heading);margin:38px 0 14px}
.prose h3{font-family:var(--serif);font-size:1.14rem;font-weight:600;margin:24px 0 10px}
.prose p{font-weight:300;color:#3f4852}
.prose ul{padding-left:20px;margin:0 0 1.2em}
.prose li{font-weight:300;color:#3f4852;margin:7px 0}
.prose strong{font-weight:500;color:var(--heading)}
.prose a{color:var(--gold-dp);border-bottom:1px solid var(--line-gold)}
.faq{max-width:860px;margin:0 auto;border-top:1px solid var(--line-gold)}
.faq details{border-bottom:1px solid var(--paper-line)}
.faq summary{cursor:pointer;font-family:var(--serif);font-size:1.14rem;font-weight:600;color:var(--heading);padding:22px 46px 22px 2px;position:relative;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:8px;top:18px;font-family:var(--disp);font-size:1.6rem;color:var(--gold);font-weight:400}
.faq details[open] summary::after{content:"–"}
.faq details .fa{padding:0 46px 24px 2px;margin:0;font-weight:300;color:var(--muted)}
.faq details .fa a{color:var(--gold-dp);border-bottom:1px solid var(--line-gold)}
.faq-note{text-align:center;color:var(--muted);font-weight:300;font-size:.9rem;margin-top:26px}
.vals{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line-gold)}
.val{padding:38px 34px;border-left:1px solid var(--paper-line)}
.val:first-child{border-left:0;padding-left:0}
.val .rn{font-family:var(--disp);font-style:italic;font-size:1.7rem;color:var(--gold);line-height:1}
.val h3{font-family:var(--serif);font-size:1.24rem;font-weight:600;margin:14px 0 8px;letter-spacing:.03em}
.val p{font-weight:300;color:var(--muted);margin:0}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:58px;align-items:start}
.info-card{border-top:1px solid var(--line-gold);margin-top:22px}
.info-row{display:flex;gap:16px;padding:18px 2px;border-bottom:1px solid var(--paper-line);align-items:center}
.info-row .ic{flex-shrink:0;width:44px;height:44px;display:flex;align-items:center;justify-content:center;background:var(--paper-2);transform:skewX(-11deg)}
.info-row .ic svg{width:20px;height:20px;stroke:var(--gold-dp);fill:none;stroke-width:1.6;transform:skewX(11deg)}
.info-row .lbl{font-weight:300;color:var(--muted);font-size:.85rem;letter-spacing:.05em}
.info-row .val2{font-family:var(--serif);color:var(--heading);font-size:1.02rem}
.info-row .val2 a{color:var(--heading)}.info-row .val2 a:hover{color:var(--gold-dp)}
.map-wrap{margin-top:26px;line-height:0;border:1px solid var(--paper-line);overflow:hidden}
.map-wrap iframe{width:100%;height:300px;border:0;filter:grayscale(.2)}
.cform{margin-top:22px}
.cform .row{margin-bottom:16px}
.cform label{display:block;font-weight:400;color:#3f4852;font-size:.92rem;letter-spacing:.03em}
.cform input,.cform textarea{width:100%;margin-top:7px;padding:12px 14px;border:1px solid var(--paper-line);background:#fff;font:inherit;font-weight:300;font-size:1rem;color:var(--text)}
.cform input:focus,.cform textarea:focus{outline:none;border-color:var(--gold);box-shadow:0 0 0 3px rgba(201,166,99,.16)}
.cform .form-submit{border:0;cursor:pointer;font-family:var(--sans);font-weight:400;letter-spacing:.06em;color:var(--paper);padding:15px 30px;background:var(--ink);clip-path:polygon(12px 0,100% 0,calc(100% - 12px) 100%,0 100%)}
.cform .form-submit:hover{background:var(--navy)}
.cform .form-result{margin-top:16px;font-weight:300;color:var(--gold-dp)}
@media(max-width:900px){.vals{grid-template-columns:1fr;border-top:0}.val{border-left:0;padding:26px 0;border-bottom:1px solid var(--paper-line)}.val:first-child{padding-top:0}.contact-grid{grid-template-columns:1fr;gap:40px}}
@media(max-width:760px){.page-hero{clip-path:polygon(0 0,100% 0,100% calc(100% - 30px),0 100%);padding:92px 0 66px}}
/* 首頁 hero 旋轉品牌章（方案B：logo 正立，金環＋金點自轉） */
.hero-emblem{position:absolute;z-index:2;top:50%;right:7%;transform:translateY(-50%);width:400px;height:400px;display:flex;align-items:center;justify-content:center;pointer-events:none}
.hero-emblem .he-ring{position:absolute;inset:0;border:1px solid rgba(232,209,153,.4);border-radius:50%;animation:spin 30s linear infinite}
.hero-emblem .he-ring::before{content:"";position:absolute;top:-5px;left:50%;width:9px;height:9px;margin-left:-4.5px;background:var(--gold-lt);border-radius:50%;box-shadow:0 0 12px rgba(232,209,153,.95)}
.hero-emblem .he-ring2{position:absolute;inset:30px;border:1px solid rgba(201,166,99,.16);border-radius:50%}
.hero-emblem img{width:150px;height:150px;opacity:.95}
@keyframes spin{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){.hero-emblem .he-ring{animation:none}}
@media(max-width:1040px){.hero-emblem{display:none}}
"""
(ROOT / "css").mkdir(exist_ok=True)
(ROOT / "css" / "site.css").write_text(base_css + "\n" + CSS_EXTRA, encoding="utf-8")

# ---- 2) 共用區塊 ----
NAV = [("index.html","首頁"),("about.html","關於我們"),("services.html","服務項目"),
       ("urban-renewal.html","都市更新・危老"),("projects.html","服務個案")]

def header(active):
    items = ""
    for href,label in NAV:
        cur = ' aria-current="page"' if href==active else ""
        items += f'<li><a href="{href}"{cur}>{label}</a></li>\n    '
    cta_cur = ' aria-current="page"' if active=="contact.html" else ""
    return f'''<header class="top"><div class="wrap nav">
  <a class="brand" href="index.html" aria-label="貝多不動產 首頁">
    <img src="assets/logo-mark-dark.svg" alt="貝多不動產標誌" width="42" height="42">
    <span><span class="tw">貝多不動產</span><span class="en">BEEDOO REALTY</span></span>
  </a>
  <button class="burger" aria-label="開啟選單" aria-expanded="false" aria-controls="menu"><span></span></button>
  <ul class="menu" id="menu">
    {items}<li><a class="cta" href="contact.html"{cta_cur}>免費諮詢</a></li>
  </ul>
</div></header>'''

FOOTER = '''<footer class="foot"><div class="wrap">
  <div class="foot-top">
    <div class="foot-brand">
      <a class="brand" href="index.html"><img src="assets/logo-mark-light.svg" alt="貝多不動產標誌" width="42" height="42">
        <span><span class="tw">貝多不動產</span><span class="en">BEEDOO REALTY</span></span></a>
      <p>貝多行銷有限公司 — 深耕不動產代銷二十年，提供土地開發、工業廠房、都市更新、危老重建與不動產行銷顧問服務。</p>
      <p style="margin-top:8px">統一編號：82864762</p>
    </div>
    <div><h4>服務項目</h4><ul>
      <li><a href="services.html#development">土地開發</a></li><li><a href="services.html#industrial">工業廠房</a></li>
      <li><a href="urban-renewal.html">都市更新</a></li><li><a href="urban-renewal.html#weilao">危老重建</a></li>
      <li><a href="services.html#consulting">不動產行銷顧問</a></li></ul></div>
    <div><h4>聯絡資訊</h4><ul>
      <li>新北市林口區文化三路一段468號</li>
      <li><a href="tel:+886226005619">電話：02-2600-5619</a></li>
      <li><a href="tel:+886919935618">胡銍芃：0919-935-618</a></li>
      <li><a href="mailto:alechu2628@gmail.com">alechu2628@gmail.com</a></li></ul></div>
  </div>
  <div class="foot-bot">
    <div><a href="privacy.html">隱私權政策</a><a href="terms.html">服務條款</a><a href="accessibility.html">無障礙聲明</a></div>
    <div>© 2026 貝多行銷有限公司</div>
  </div>
</div></footer>'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600;700&family=Noto+Sans+TC:wght@300;400;500&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

def page(fname, title, desc, active, main, extra_head=""):
    html = f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="khrishu">
<link rel="icon" href="img/logo.png" type="image/png">
{FONTS}
<link rel="stylesheet" href="css/site.css">{extra_head}
</head>
<body>
<a class="skip" href="#main" style="position:absolute;left:-999px">跳至主要內容</a>
{header(active)}
<main id="main">
{main}
</main>
{FOOTER}
<script defer src="js/site.js"></script>
</body>
</html>'''
    (ROOT / fname).write_text(html, encoding="utf-8")
    print("wrote", fname)

def phero(crumb, h1, sub):
    return f'''<section class="page-hero"><div class="wrap">
  <nav class="crumb" aria-label="麵包屑導覽"><a href="index.html">首頁</a><span>/</span>{crumb}</nav>
  <h1>{h1}</h1>
  <p class="ph-sub">{sub}</p>
</div></section>'''

def cta(h2, sub, ptxt, phref, tel, teldisp):
    return f'''<section class="cta"><div class="wrap">
  <span class="eyebrow on-dark">Let's Talk</span>
  <h2 style="margin-top:16px">{h2}</h2>
  <p class="sub">{sub}</p>
  <div class="cta-act">
    <a class="link-gold" href="{phref}" style="background:var(--grad-gold);color:var(--ink)">{ptxt} <span class="arw">→</span></a>
    <a class="link-line" href="tel:{tel}">撥打 {teldisp}</a>
  </div></div></section>'''

def media(img, alt, eyebrow, h2, paras, checks=None, link=None, reverse=False):
    rc = " reverse" if reverse else ""
    ch = ""
    if checks:
        ch = '<ul class="checks">' + "".join(f"<li>{c}</li>" for c in checks) + "</ul>"
    lk = f'<p style="margin-top:28px">{link}</p>' if link else ""
    ps = "".join(f'<p style="font-weight:300;color:#4a545f;margin-top:0">{p}</p>' for p in paras)
    return f'''<div class="media{rc}">
  <div class="media-fig reveal"><img src="img/{img}" alt="{alt}" loading="lazy"></div>
  <div class="media-text reveal">
    <span class="eyebrow"><span class="rule"></span>{eyebrow}</span>
    <h2 style="margin-top:16px">{h2}</h2>
    {ps}{ch}{lk}
  </div>
</div>'''

# ================= 各頁 main =================

# ---------- 首頁 ----------
INDEX_MAIN = '''<section class="hero">
  <img class="hero-img" src="img/hero.jpg" alt="現代都市摩天大樓群仰視景觀">
  <div class="hero-emblem" aria-hidden="true"><div class="he-ring"></div><div class="he-ring2"></div><img src="assets/logo-mark-light.svg" alt=""></div>
  <div class="wrap">
    <span class="eyebrow on-dark">Beedoo Realty ・ 不動產整合顧問</span>
    <h1>從一塊土地到一座家園<br><span class="g">貝多</span>陪您看得更遠</h1>
    <p class="lead">深耕不動產代銷二十年，貝多整合土地開發、工業廠房、都市更新與危老重建專業，以誠信協助地主、建商與投資人，實現土地的最大價值。</p>
    <div class="hero-act">
      <a class="link-gold" href="contact.html">預約免費諮詢 <span class="arw">→</span></a>
      <a class="link-line" href="services.html">了解服務項目 <span class="arw">→</span></a>
    </div>
    <div class="hero-tags"><span>土地開發</span><span>工業廠房</span><span>都市更新</span><span>危老重建</span><span>行銷顧問</span></div>
  </div>
</section>
<section class="sec sec-paper" style="padding:78px 0"><div class="wrap"><div class="stats">
  <div class="stat reveal"><div class="n">20<em>年</em></div><div class="l">不動產代銷經驗</div></div>
  <div class="stat reveal"><div class="n">5<em>大</em></div><div class="l">核心專業領域</div></div>
  <div class="stat reveal"><div class="n">2026</div><div class="l">最新服務個案</div></div>
  <div class="stat reveal"><div class="n">全程</div><div class="l">一站式整合服務</div></div>
</div></div></section>
<section class="sec" id="services"><div class="wrap">
  <div class="head reveal"><span class="eyebrow"><span class="rule"></span>Our Services</span>
    <h2>五大核心專業，一站到位</h2>
    <p class="sub">從土地評估、整合開發到行銷代銷，以完整的專業鏈，協助每一筆不動產走向最適合的未來。</p></div>
  <div class="svc">
    <div class="svc-row reveal"><div class="no">01</div><div class="txt"><h3>土地開發</h3><p>土地潛力評估、地目與法規分析、開發整合與素地活化，協助地主與建商找出最具效益的開發方向。</p></div><a class="go" href="services.html#development" aria-label="了解土地開發"><i>→</i></a></div>
    <div class="svc-row reveal"><div class="no">02</div><div class="txt"><h3>工業廠房</h3><p>工業用地與廠房之買賣、租賃與開發規劃，對接製造業、物流業選址需求，提升資產運用效率。</p></div><a class="go" href="services.html#industrial" aria-label="了解工業廠房"><i>→</i></a></div>
    <div class="svc-row reveal"><div class="no">03</div><div class="txt"><h3>都市更新</h3><p>協助老舊社區整合、權利變換與都更流程推動，串聯地主、建商與專業團隊，重塑居住環境。</p></div><a class="go" href="urban-renewal.html" aria-label="了解都市更新"><i>→</i></a></div>
    <div class="svc-row reveal"><div class="no">04</div><div class="txt"><h3>危老重建</h3><p>危老建築重建一條龍輔導，協助住戶評估容積獎勵、整合意願並媒合可靠重建團隊，安心成家。</p></div><a class="go" href="urban-renewal.html#weilao" aria-label="了解危老重建"><i>→</i></a></div>
    <div class="svc-row reveal"><div class="no">05</div><div class="txt"><h3>不動產行銷顧問</h3><p>從產品定位、訂價策略到完整代銷執行，以二十年實戰經驗，協助建案精準鎖定客群、加速去化。</p></div><a class="go" href="services.html#consulting" aria-label="了解行銷顧問"><i>→</i></a></div>
  </div>
  <div class="svc-note reveal"><div><h3>不確定您的土地或房屋如何規劃？</h3><p>無論是手中的素地、老屋，或正在尋找廠房，貝多都能提供客觀的專業評估。</p></div>
    <a class="link-line" href="contact.html">預約免費諮詢 <span class="arw">→</span></a></div>
</div></section>
<section class="sec sec-paper"><div class="wrap"><div class="media">
  <div class="media-fig reveal"><img src="img/planning.jpg" alt="不動產顧問於圖紙上進行建築規劃" loading="lazy"></div>
  <div class="media-text reveal"><span class="eyebrow"><span class="rule"></span>Why Beedoo</span>
    <h2 style="margin-top:16px">二十年代銷實力<br>做您最可靠的不動產夥伴</h2>
    <p style="font-weight:300;color:#4a545f;margin-top:18px">不動產的價值，來自對市場、法規與時機的精準判斷。貝多自代銷領域累積二十年實戰經驗，熟悉土地開發到產品銷售的每一個環節，讓每一個決策都建立在專業之上。</p>
    <ul class="checks"><li>整合土地、開發、重建到行銷代銷的完整服務鏈</li><li>熟悉都更與危老法規，協助爭取合理權益</li><li>以誠信為本，提供客觀中立的評估建議</li><li>專人對接，從諮詢到成交全程陪伴</li></ul>
    <p style="margin-top:30px"><a class="link-line" href="about.html" style="color:var(--gold-dp);border-color:var(--line-gold)">認識貝多團隊 <span class="arw">→</span></a></p>
  </div></div></div></section>
<section class="sec" id="project"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">2026 Featured Project</span><h2>最新服務個案</h2>
    <p class="sub">持續以專業參與優質個案，協助住戶與投資人掌握每一次安居與置產的契機。</p></div>
  <div class="proj reveal">
    <div class="proj-img"><span class="proj-badge">2026 服務個案</span><img src="img/project-architecture.jpg" alt="天母蒔麗精緻現代住宅建築外觀" loading="lazy"></div>
    <div class="proj-body"><h3>威帝・天母蒔麗</h3><p class="en">Tianmu Elite Garden</p>
      <p class="d">座落天母生活圈的精緻住宅個案，規劃 15–25 坪的舒適坪數，貼近都會生活機能，是首購與換屋族群理想的安居選擇。</p>
      <ul class="specs"><li><span class="k">個案名稱</span><span class="v">威帝・天母蒔麗</span></li><li><span class="k">規劃坪數</span><span class="v">15 – 25 坪</span></li><li><span class="k">服務年度</span><span class="v">2026</span></li><li><span class="k">服務角色</span><span class="v">行銷代銷顧問</span></li></ul>
      <a class="link-line" href="projects.html" style="color:var(--gold-lt);border-color:var(--line-gold)">查看個案介紹 <span class="arw">→</span></a>
    </div></div>
</div></section>
<section class="sec sec-ink"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow on-dark">How We Work</span><h2>清楚透明的合作流程</h2></div>
  <div class="flow">
    <div class="step reveal"><div class="dot"><i>i</i></div><h3>需求諮詢</h3><p>了解您的土地、房屋現況與目標，提供初步方向建議。</p></div>
    <div class="step reveal"><div class="dot"><i>ii</i></div><h3>專業評估</h3><p>進行法規、市場與效益分析，量身提出可行的開發或行銷策略。</p></div>
    <div class="step reveal"><div class="dot"><i>iii</i></div><h3>整合執行</h3><p>媒合建商與專業團隊，推動開發、重建或代銷流程。</p></div>
    <div class="step reveal"><div class="dot"><i>iv</i></div><h3>全程陪伴</h3><p>從簽約到結案，專人持續追蹤，守護您的權益。</p></div>
  </div></div></section>
''' + cta("讓專業，為您的不動產加值",
          "一通電話，開啟土地與房屋的更多可能。貝多提供免費初步諮詢，歡迎與我們聯繫。",
          "線上預約諮詢","contact.html","+886226005619","02-2600-5619")

# ---------- 關於我們 ----------
ABOUT_MAIN = phero("關於我們","專業源於累積，信任來自陪伴",
    "貝多不動產以二十年不動產代銷實力，成為地主、建商與投資人最值得信賴的整合夥伴。") + f'''
<section class="sec"><div class="wrap">{media("skyline.jpg","都市天際線建築群","About Beedoo","貝多不動產・貝多行銷有限公司",
    ["貝多不動產長期深耕不動產代銷領域，累積超過二十年的市場實戰經驗。我們深知每一筆土地、每一棟房屋背後，都承載著家庭的期待與投資的判斷，因此始終以誠信、專業、整合為核心，協助客戶在複雜的不動產市場中做出最有利的決策。",
     "從土地開發、工業廠房，到都市更新與危老重建，貝多串聯地主、建商與各領域專業團隊，提供從評估、整合到行銷代銷的完整服務，讓土地與資產發揮最大價值。"],
    link='<a class="link-line" href="services.html" style="color:var(--gold-dp);border-color:var(--line-gold)">查看服務項目 <span class="arw">→</span></a>')}</div></section>
<section class="sec sec-paper"><div class="wrap">
  <div class="head reveal"><span class="eyebrow"><span class="rule"></span>Our Values</span><h2>我們堅持的三件事</h2></div>
  <div class="vals">
    <div class="val reveal"><div class="rn">I</div><h3>誠信為本</h3><p>提供客觀、中立的專業評估，不誇大、不隱瞞，讓每一個建議都經得起檢驗。</p></div>
    <div class="val reveal"><div class="rn">II</div><h3>專業整合</h3><p>橫跨土地、開發、重建到行銷，以系統化的專業鏈，提供一站式的不動產解決方案。</p></div>
    <div class="val reveal"><div class="rn">III</div><h3>全程陪伴</h3><p>專人對接、即時溝通，從第一次諮詢到最後成交，貝多始終站在客戶這一邊。</p></div>
  </div></div></section>
<section class="sec"><div class="wrap">{media("office.jpg","現代專業辦公空間","Consultant","專業顧問・胡銍芃 AlecHu",
    ["胡銍芃（志強）為貝多不動產資深行銷顧問，長期投入不動產代銷與整合開發，熟悉土地開發、都市更新與危老重建之實務與法規，協助無數地主與住戶完成資產規劃與重建決策。",
     "無論您是手中持有素地、面臨老屋重建，或正在尋找適合的工業廠房，都歡迎與胡顧問直接聯繫，取得專屬的專業建議。"],
    checks=["專長：土地開發整合・都市更新・危老重建・行銷代銷","電話諮詢：<a href='tel:+886919935618' style='color:var(--gold-dp)'>0919-935-618</a>","電子信箱：<a href='mailto:alechu2628@gmail.com' style='color:var(--gold-dp)'>alechu2628@gmail.com</a>"],
    link='<a class="link-line" href="contact.html" style="color:var(--gold-dp);border-color:var(--line-gold)">與顧問聯繫 <span class="arw">→</span></a>',
    reverse=True)}</div></section>
''' + cta("想更了解您的不動產潛力？","歡迎預約免費初步諮詢，讓貝多以二十年經驗，為您指引方向。",
          "立即預約諮詢","contact.html","+886226005619","02-2600-5619")

# ---------- 服務項目 ----------
SERVICES_MAIN = phero("服務項目","從土地到成屋，五大專業整合服務",
    "貝多以完整的不動產服務鏈，協助每一筆土地與資產，走向最適合的開發與行銷方向。") + f'''
<section class="sec" id="development"><div class="wrap">{media("land.jpg","開發前的開闊土地與夕陽景觀","01 ・ Land Development","土地開發",
    ["土地的價值，取決於用對方法與看準時機。貝多協助地主與建商進行土地潛力評估、地目與法規分析，盤點素地的最適開發方向，並媒合可靠的開發團隊，讓閒置土地轉化為實質效益。"],
    checks=["土地潛力與可行性評估","地目、容積與相關法規分析","素地整合、合建與開發媒合","開發效益試算與策略建議"])}</div></section>
<section class="sec sec-paper" id="industrial"><div class="wrap">{media("blueprint.jpg","廠房建築設計藍圖細部","02 ・ Industrial Property","工業廠房",
    ["面對製造、物流與產業升級的選址需求，貝多提供工業用地與廠房的買賣、租賃及開發規劃服務，協助企業找到符合營運與法規的最適場域，也協助持有者活化工業資產。"],
    checks=["工業用地與廠房買賣、租賃媒合","廠房開發與更新規劃","產業選址與營運效益評估","工業資產活化與投資建議"],reverse=True)}</div></section>
<section class="sec" id="urban"><div class="wrap">{media("urban-renewal.jpg","都市更新後的城市街景","03 ・ Urban Renewal","都市更新・危老重建",
    ["面對老舊建物與居住安全議題，貝多協助住戶與地主推動都市更新及危老重建，從意願整合、權利變換到容積獎勵試算，串聯建商與專業團隊，讓老屋蛻變為安全宜居的新家。"],
    checks=["都更與危老可行性評估","住戶意願整合與溝通協調","容積獎勵與權利變換試算","建商與專業團隊媒合"],
    link='<a class="link-line" href="urban-renewal.html" style="color:var(--gold-dp);border-color:var(--line-gold)">深入了解都市更新・危老 <span class="arw">→</span></a>')}</div></section>
<section class="sec sec-paper" id="consulting"><div class="wrap">{media("planning.jpg","行銷顧問進行建案規劃討論","04 ・ Marketing Consulting","不動產行銷顧問",
    ["好的產品，也需要對的行銷策略。貝多以二十年不動產代銷實戰經驗，提供建案從產品定位、訂價策略到完整代銷執行的顧問服務，協助建商精準鎖定客群、加速去化、提升成交效率。"],
    checks=["市場分析與產品定位","訂價策略與銷售計畫擬定","銷售團隊組建與代銷執行","來客經營與成交追蹤"],reverse=True)}</div></section>
<section class="sec"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">FAQ</span><h2>常見問題</h2></div>
  <div class="faq">
    <details><summary>我手中有一塊土地，該如何開始評估？</summary><p class="fa">歡迎先與貝多聯繫，提供土地的位置與基本資料，我們將協助進行初步的潛力與法規評估，並說明可能的開發或合作方向。初步諮詢免費，無任何負擔。</p></details>
    <details><summary>都市更新與危老重建有什麼不同？</summary><p class="fa">都市更新著重一定規模的街廓整合，流程與獎勵機制較完整；危老重建則針對符合資格的個別老舊或危險建物，程序相對簡便、時程較快。貝多會依您的建物條件，建議最合適的途徑，詳情可參考<a href="urban-renewal.html">都市更新・危老頁面</a>。</p></details>
    <details><summary>貝多的服務範圍涵蓋哪些區域？</summary><p class="fa">貝多以新北、台北、桃園等大台北地區為主要服務範圍，並依個案性質彈性評估。若您不確定是否在服務範圍內，歡迎直接來電洽詢。</p></details>
    <details><summary>行銷代銷服務適合什麼樣的建案？</summary><p class="fa">無論是中小型建案或都更、危老重建案，只要需要專業的產品定位與銷售執行，貝多都能依個案規模量身規劃行銷與代銷方案。</p></details>
  </div></div></section>
''' + cta("找到最適合您的不動產方案","不論是土地、廠房、老屋或建案行銷，貝多都能提供專業評估與整合服務。",
          "預約免費諮詢","contact.html","+886226005619","02-2600-5619")

# ---------- 都市更新・危老 ----------
SUPPORT = [("01","資格與可行性評估","協助確認建物是否符合危老或都更資格，初步評估基地條件與重建可行性。"),
           ("02","住戶意願整合","以中立第三方協助溝通協調，舉辦說明會，凝聚住戶共識、化解疑慮。"),
           ("03","容積獎勵試算","協助評估可能的容積獎勵與分回條件，讓住戶清楚掌握重建效益。"),
           ("04","權利變換規劃","協調權利變換與分配方案，確保住戶權益在透明的基礎上獲得保障。"),
           ("05","建商與團隊媒合","媒合具實績、財務健全的建商與專業團隊，為重建品質把關。"),
           ("06","全程陪伴監督","從動工到交屋，持續追蹤進度，做住戶最堅實的後盾。")]
support_rows = "".join(f'<div class="svc-row reveal"><div class="no">{n}</div><div class="txt"><h3>{t}</h3><p>{d}</p></div></div>' for n,t,d in SUPPORT)
URBAN_MAIN = phero("都市更新・危老重建","讓老屋安心蛻變，重建美好生活",
    "從意願整合到完工交屋，貝多以專業與耐心陪伴每一位住戶，走過都市更新與危老重建的每一步。") + f'''
<section class="sec"><div class="wrap">{media("urban-renewal.jpg","都市更新後嶄新的城市街道與建築","Why Now","為什麼要重視都更與危老？",
    ["台灣許多建物屋齡偏高，面對地震風險與居住安全議題，老舊建築的更新與重建已是刻不容緩的課題。透過都市更新或危老重建，不僅能提升建物的耐震與居住品質，也能藉由容積獎勵等機制，為住戶創造資產與生活的雙重升級。",
     "然而，重建之路牽涉法規、權利變換、住戶溝通與建商選擇等複雜環節。貝多以中立、專業的整合角色，協助住戶釐清權益、凝聚共識，讓重建之路走得更安心。"])}</div></section>
<section class="sec sec-paper" id="weilao"><div class="wrap">
  <div class="head reveal"><span class="eyebrow"><span class="rule"></span>Our Support</span><h2>貝多的一條龍整合輔導</h2>
    <p class="sub">從第一場說明會到完工交屋，每個階段都有專業陪伴。</p></div>
  <div class="svc">{support_rows}</div></div></section>
<section class="sec"><div class="wrap">
  <div class="head center reveal"><span class="eyebrow">FAQ</span><h2>都更・危老常見問題</h2></div>
  <div class="faq">
    <details open><summary>危老重建需要符合什麼條件？</summary><p class="fa">危老重建主要適用於屋齡達一定年限且經結構評估認定耐震能力不足，或屬於合法建築物中經認定為危險、老舊的建物，並需取得該基地全體土地及合法建築物所有權人之同意。貝多可協助您進行初步資格評估。</p></details>
    <details><summary>都市更新和危老重建有什麼差別？</summary><p class="fa">都市更新著重一定規模街廓的整合重建，流程與審議較完整、獎勵機制多元；危老重建針對個別符合資格的老舊或危險建物，採全體同意制，程序相對簡便、推動時程較快。實際應依基地條件與住戶意願選擇合適途徑。</p></details>
    <details><summary>參與重建可以獲得哪些獎勵？</summary><p class="fa">依現行法令，危老及都更重建可能享有容積獎勵與稅捐減免等誘因，實際額度需視基地條件、建物耐震、推動時程及各地方政府規定而定。貝多會協助您進行容積獎勵試算與效益分析。</p></details>
    <details><summary>整合住戶意願通常需要多久？</summary><p class="fa">整合時程依住戶人數、權屬複雜度與溝通狀況而有所不同，可能從數個月到數年不等。貝多以中立第三方角色協助溝通協調，盡力加速凝聚共識。</p></details>
  </div>
  <p class="faq-note">以上內容為一般性說明，實際資格、流程與獎勵以主管機關最新法令與審查結果為準。</p></div></section>
''' + cta("您的老屋，也有重建的可能","歡迎提供建物資料，讓貝多協助您進行免費的初步評估。",
          "預約重建諮詢","contact.html","+886919935618","0919-935-618")

# ---------- 服務個案 ----------
PROJECTS_MAIN = phero("服務個案","以專業，參與每一個美好個案",
    "貝多持續以行銷顧問與代銷專業，協助優質建案找到對的買家，也協助買家找到理想的家。") + '''
<section class="sec"><div class="wrap">
  <div class="proj reveal">
    <div class="proj-img"><span class="proj-badge">2026 服務個案</span><img src="img/project-architecture.jpg" alt="天母蒔麗精緻現代住宅建築外觀" loading="lazy"></div>
    <div class="proj-body"><h3>威帝・天母蒔麗</h3><p class="en">Tianmu Elite Garden</p>
      <p class="d">座落天母生活圈的精緻住宅個案，規劃 15–25 坪的舒適坪數，鄰近成熟的生活與教育機能，是首購族與換屋族群理想的安居選擇。貝多於此個案擔任行銷代銷顧問，協助產品定位與銷售推動。</p>
      <ul class="specs"><li><span class="k">個案名稱</span><span class="v">威帝・天母蒔麗</span></li><li><span class="k">英文名稱</span><span class="v">Tianmu Elite Garden</span></li><li><span class="k">規劃坪數</span><span class="v">15 – 25 坪</span></li><li><span class="k">生活圈</span><span class="v">天母</span></li><li><span class="k">服務年度</span><span class="v">2026</span></li><li><span class="k">貝多角色</span><span class="v">行銷代銷顧問</span></li></ul>
      <a class="link-line" href="contact.html" style="color:var(--gold-lt);border-color:var(--line-gold)">洽詢個案資訊 <span class="arw">→</span></a>
    </div></div></div></section>
<section class="sec sec-paper"><div class="wrap">
  <div class="head reveal"><span class="eyebrow"><span class="rule"></span>Project Highlights</span><h2>個案亮點</h2></div>
  <div class="vals">
    <div class="val reveal"><div class="rn">I</div><h3>精緻坪數規劃</h3><p>15–25 坪的實用格局，滿足首購與小家庭對機能與舒適的雙重需求。</p></div>
    <div class="val reveal"><div class="rn">II</div><h3>天母成熟生活圈</h3><p>鄰近完善的生活、商業與教育資源，享受便利又宜居的都會節奏。</p></div>
    <div class="val reveal"><div class="rn">III</div><h3>專業代銷服務</h3><p>由貝多以二十年代銷經驗操盤，提供專業、誠信的購屋諮詢與服務。</p></div>
  </div>
  <p class="faq-note">個案相關坪數、規劃及銷售資訊以現場銷售中心及正式銷售文件公告為準。</p></div></section>
''' + cta("想了解天母蒔麗或其他個案？","歡迎與貝多聯繫，由專人提供最新個案資訊與購屋諮詢。",
          "立即洽詢","contact.html","+886226005619","02-2600-5619")

# ---------- 聯絡我們 ----------
MAP_SRC = "https://maps.google.com/maps?q=%E6%96%B0%E5%8C%97%E5%B8%82%E6%9E%97%E5%8F%A3%E5%8D%80%E6%96%87%E5%8C%96%E4%B8%89%E8%B7%AF%E4%B8%80%E6%AE%B5468%E8%99%9F&output=embed"
CONTACT_MAIN = phero("聯絡我們","歡迎與貝多聯繫",
    "無論是土地、廠房、老屋重建或建案行銷，留下您的需求，由專人提供免費的初步諮詢。") + f'''
<section class="sec"><div class="wrap"><div class="contact-grid">
  <div>
    <span class="eyebrow"><span class="rule"></span>Get In Touch</span>
    <h2 style="margin-top:14px">聯絡資訊</h2>
    <p style="font-weight:300;color:var(--muted)">歡迎來電、來信或親自蒞臨，我們很樂意為您服務。</p>
    <div class="info-card">
      <div class="info-row"><div class="ic"><svg viewBox="0 0 24 24"><path d="M12 21s-7-5.5-7-11a7 7 0 0 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg></div><div><div class="lbl">公司地址</div><div class="val2">新北市林口區文化三路一段468號</div></div></div>
      <div class="info-row"><div class="ic"><svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.6a2 2 0 0 1-.5 2.1L8 9.6a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.8.3 1.7.5 2.6.6a2 2 0 0 1 1.7 2z"/></svg></div><div><div class="lbl">公司電話</div><div class="val2"><a href="tel:+886226005619">02-2600-5619</a></div></div></div>
      <div class="info-row"><div class="ic"><svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg></div><div><div class="lbl">行銷顧問・胡銍芃</div><div class="val2"><a href="tel:+886919935618">0919-935-618</a></div></div></div>
      <div class="info-row"><div class="ic"><svg viewBox="0 0 24 24"><path d="M4 5h16v14H4z"/><path d="M4 7l8 6 8-6"/></svg></div><div><div class="lbl">電子信箱</div><div class="val2"><a href="mailto:alechu2628@gmail.com">alechu2628@gmail.com</a></div></div></div>
      <div class="info-row"><div class="ic"><svg viewBox="0 0 24 24"><path d="M3 21h18M5 21V8l7-4 7 4v13M9 21v-5h6v5"/></svg></div><div><div class="lbl">公司全名</div><div class="val2">貝多行銷有限公司（統編 82864762）</div></div></div>
    </div>
    <div class="map-wrap"><iframe title="貝多不動產位置地圖" src="{MAP_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
  <div>
    <span class="eyebrow"><span class="rule"></span>Online Inquiry</span>
    <h2 style="margin-top:14px">線上諮詢表單</h2>
    <p style="font-weight:300;color:var(--muted)">請填寫以下資料，我們將盡快與您聯繫。至少填寫姓名與一種聯絡方式即可。</p>
    <form class="cform" novalidate>
      <div class="row"><label>姓名<input name="name" autocomplete="name"></label></div>
      <div class="row"><label>電子信箱<input name="email" type="email" autocomplete="email"></label></div>
      <div class="row"><label>聯絡電話<input name="phone" type="tel" autocomplete="tel"></label></div>
      <div class="row"><label>諮詢主題<input name="subject" placeholder="例如：土地開發、危老重建、個案洽詢"></label></div>
      <div class="row"><label>諮詢內容<textarea name="message" rows="4" placeholder="請簡述您的需求或想了解的項目"></textarea></label></div>
      <button class="form-submit" type="submit">送出諮詢</button>
      <div class="form-result" role="status" aria-live="polite"></div>
    </form>
  </div>
</div></div></section>'''

# ---------- 法務頁 ----------
def prose_page(crumb, h1, hero_sub, body):
    return phero(crumb, h1, hero_sub) + f'<section class="sec"><div class="wrap"><div class="prose">{body}</div></div></section>'

PRIVACY_BODY = '''<p class="meta">最後更新日期：2026年6月｜適用對象：貝多不動產（貝多行銷有限公司）官方網站之所有使用者。</p>
<p>貝多行銷有限公司（以下簡稱「本公司」）非常重視您的隱私權。本隱私權政策說明本公司如何於您使用本網站時，蒐集、處理、利用及保護您的個人資料。當您使用本網站，即表示您已了解並同意本政策之內容。</p>
<h2>一、個人資料之蒐集</h2><p>當您透過本網站的線上諮詢表單與我們聯繫時，我們可能蒐集您主動提供的資料，包括姓名、電子信箱、聯絡電話、諮詢主題及諮詢內容等。若您僅瀏覽本網站而未主動提供資料，我們不會要求您提供任何個人資料。</p>
<h2>二、個人資料之利用目的</h2><p>本公司蒐集您的個人資料，係基於下列目的：</p><ul><li>回覆您的諮詢、提供不動產相關服務與資訊。</li><li>與您聯繫、安排諮詢或後續服務。</li><li>本公司內部之客戶服務管理與業務聯繫。</li></ul><p>本公司不會將您的個人資料用於上述目的以外之用途，亦不會在未經您同意的情況下提供予無關之第三方。</p>
<h2>三、個人資料之保護</h2><p>本公司將採取合理的技術與管理措施，保護您的個人資料免於未經授權之存取、使用、竄改或洩漏。惟網際網路傳輸無法保證百分之百安全，請您於提供資料時一併注意自身資料之保護。</p>
<h2>四、Cookie 與分析工具</h2><p>本網站目前以提供資訊與聯繫服務為主。若未來導入 Cookie 或網站分析工具以改善使用體驗，將另行於本政策更新說明，並依相關法令取得必要之同意。</p>
<h2>五、您的權利</h2><p>依個人資料保護法之規定，您就本公司保有之個人資料，得行使查詢、閱覽、製給複製本、補充或更正、請求停止蒐集處理利用及請求刪除等權利。如欲行使上述權利，歡迎透過下列方式與我們聯繫。</p>
<h2>六、第三方連結</h2><p>本網站可能包含前往第三方網站（如 Google 地圖）之連結，該等網站有其各自的隱私權政策，本公司對其內容與隱私作業方式不負責任，建議您於使用前詳閱該網站之相關規範。</p>
<h2>七、政策修訂</h2><p>本公司保留隨時修訂本隱私權政策之權利，修訂後將公告於本網站。建議您不定期查閱，以了解最新內容。</p>
<h2>八、聯絡我們</h2><p>如您對本隱私權政策有任何疑問，歡迎與我們聯繫：</p><ul><li>地址：新北市林口區文化三路一段468號</li><li>電話：<a href="tel:+886226005619">02-2600-5619</a></li><li>電子信箱：<a href="mailto:alechu2628@gmail.com">alechu2628@gmail.com</a></li></ul>'''

TERMS_BODY = '''<p class="meta">最後更新日期：2026年6月。本條款規範您與貝多行銷有限公司（以下簡稱「本公司」）間就本網站使用之權利義務。</p>
<p>歡迎使用貝多不動產官方網站。當您瀏覽或使用本網站，即表示您已閱讀、了解並同意接受本服務條款之全部內容。若您不同意本條款，請停止使用本網站。</p>
<h2>一、服務內容</h2><p>本網站旨在介紹本公司之不動產服務，包括土地開發、工業廠房、都市更新、危老重建及不動產行銷顧問等資訊，並提供線上諮詢管道。網站所載內容僅供一般參考，不構成任何要約、投資建議或交易承諾。</p>
<h2>二、資訊正確性與免責聲明</h2><p>本公司致力於維持網站資訊之正確與更新，惟不動產相關法規、個案內容、坪數規劃及銷售資訊均可能隨時變動，實際內容應以主管機關最新規定、正式銷售文件及現場公告為準。對於因依賴本網站資訊所生之任何損失，本公司於法令允許範圍內不負賠償責任。</p>
<h2>三、智慧財產權</h2><p>本網站所有內容，包括但不限於文字、圖片、商標、標誌及版面設計，均為本公司或合法權利人所有，受相關法律保護。未經事前書面同意，您不得以任何形式重製、散布、改作或為商業使用。</p>
<h2>四、使用者義務</h2><p>您同意於使用本網站時，遵守相關法令並不從事下列行為：提供不實資料、干擾或破壞網站運作、傳輸惡意程式，或以任何方式侵害本公司或第三人之權益。</p>
<h2>五、第三方連結</h2><p>本網站可能提供前往第三方網站之連結，僅為使用者便利之目的。該等網站之內容與服務由其各自經營者負責，本公司不對其正確性、合法性或可用性負責。</p>
<h2>六、條款修訂</h2><p>本公司保留隨時修改本服務條款之權利，修改後將公告於本網站，並自公告時起生效。您於修訂後繼續使用本網站，即視為同意修訂後之條款。</p>
<h2>七、準據法與爭議解決</h2><p>本條款之解釋與適用，以中華民國（台灣）法律為準據法。因本網站或本公司服務所生之爭議，雙方同意應先以誠信原則進行協商；協商不成時，同意以本公司所在地之地方法院為第一審管轄法院。</p>
<h2>八、聯絡我們</h2><p>如您對本服務條款有任何疑問，歡迎與我們聯繫：</p><ul><li>地址：新北市林口區文化三路一段468號</li><li>電話：<a href="tel:+886226005619">02-2600-5619</a></li><li>電子信箱：<a href="mailto:alechu2628@gmail.com">alechu2628@gmail.com</a></li></ul>'''

ACCESS_BODY = '''<p class="meta">最後更新日期：2026年6月。本網站致力於遵循 WCAG 2.1 AA 等級之無障礙設計原則。</p>
<p>貝多行銷有限公司（以下簡稱「本公司」）致力於提供所有使用者，包括身心障礙者與年長者，皆能便利使用的網站環境。本網站於設計與開發過程中，參考全球資訊網協會（W3C）所制定之網頁內容無障礙指引（WCAG 2.1）AA 等級，持續優化使用體驗。</p>
<h2>一、本網站的無障礙設計</h2><ul><li>提供「跳至主要內容」連結，方便使用鍵盤與螢幕報讀器的使用者快速導覽。</li><li>所有圖片均提供替代文字（alt），協助螢幕報讀器描述影像內容。</li><li>採用語意化的 HTML 標籤與地標（landmark），讓輔助科技更容易解析頁面結構。</li><li>文字與背景維持足夠的色彩對比，提升可讀性。</li><li>所有互動元素均可使用鍵盤操作，並提供清楚的焦點顯示。</li><li>採用響應式設計，支援文字縮放與不同裝置尺寸瀏覽。</li></ul>
<h2>二、鍵盤操作說明</h2><p>您可使用鍵盤的 <strong>Tab</strong> 鍵在連結與互動元素間切換，使用 <strong>Enter</strong> 或 <strong>空白鍵</strong> 進行確認操作。瀏覽過程中，目前所在的元素會顯示清楚的焦點外框。</p>
<h2>三、持續改善</h2><p>無障礙是一段持續精進的過程。本公司將定期檢視並改善網站的無障礙程度。若您在使用本網站時遇到任何無障礙相關的困難，或有任何建議，誠摯歡迎您與我們聯繫，我們將盡力協助並改善。</p>
<h2>四、聯絡我們</h2><p>如您在瀏覽本網站時遇到無障礙障礙，歡迎透過以下方式與我們聯繫：</p><ul><li>地址：新北市林口區文化三路一段468號</li><li>電話：<a href="tel:+886226005619">02-2600-5619</a></li><li>電子信箱：<a href="mailto:alechu2628@gmail.com">alechu2628@gmail.com</a></li></ul>'''

# ================= 產生所有頁面 =================
page("index.html","貝多不動產 BEEDOO REALTY｜土地開發・都市更新・危老重建顧問",
     "貝多不動產（貝多行銷有限公司）深耕不動產代銷二十年，提供土地開發、工業廠房、都市更新、危老重建及不動產行銷顧問服務。","index.html",INDEX_MAIN)
page("about.html","關於貝多不動產｜二十年不動產代銷經驗的整合顧問團隊",
     "貝多不動產深耕代銷二十年，專注土地開發、都市更新、危老重建與行銷顧問，以誠信專業為地主與建商創造價值。","about.html",ABOUT_MAIN)
page("services.html","服務項目｜土地開發・工業廠房・行銷顧問｜貝多不動產",
     "貝多提供土地開發、工業廠房、都市更新、危老重建與不動產行銷顧問五大服務，一站到位。","services.html",SERVICES_MAIN)
page("urban-renewal.html","都市更新與危老重建｜整合輔導與容積獎勵｜貝多不動產",
     "貝多協助都市更新與危老重建：意願整合、容積獎勵試算、權利變換與建商媒合一條龍輔導。","urban-renewal.html",URBAN_MAIN)
page("projects.html","服務個案｜威帝・天母蒔麗 Tianmu Elite Garden｜貝多不動產",
     "貝多 2026 服務個案「威帝・天母蒔麗」，規劃15–25坪精緻住宅，座落天母生活圈。","projects.html",PROJECTS_MAIN)
page("contact.html","聯絡我們｜預約免費不動產諮詢｜貝多不動產",
     "聯絡貝多不動產：新北市林口區文化三路一段468號，電話 02-2600-5619。歡迎線上預約免費諮詢。","contact.html",CONTACT_MAIN)
page("privacy.html","隱私權政策｜貝多不動產","貝多不動產隱私權政策，說明我們如何蒐集、使用與保護您的個人資料。","privacy.html",
     prose_page("隱私權政策","隱私權政策","我們重視並保護您的個人資料安全。",PRIVACY_BODY))
page("terms.html","服務條款｜貝多不動產","貝多不動產官方網站服務條款，說明使用規範、免責聲明與爭議解決方式。","terms.html",
     prose_page("服務條款","服務條款","使用本網站前，請詳閱以下條款內容。",TERMS_BODY))
page("accessibility.html","無障礙聲明｜貝多不動產","貝多不動產無障礙聲明，說明本網站採行的無障礙設計與持續改善措施。","accessibility.html",
     prose_page("無障礙聲明","無障礙聲明","讓每一位使用者都能順暢瀏覽，是我們的目標。",ACCESS_BODY))
print("ALL DONE")
