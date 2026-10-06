#!/usr/bin/env python3
"""Genera la web estática de cerrajero24horasmurcia.es en la raíz del repositorio"""
import json, os, html, hashlib

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DOM = "https://www.cerrajero24horasmurcia.es"
NAME = "Cerrajero 24 Horas en Murcia"
# --- Datos que debe cambiar el propietario (buscar y reemplazar) ---
TEL_LINK = "+34622663157"     # p. ej. +34968123456
TEL_TXT = "622 66 31 57"      # p. ej. 968 12 34 56
WA = "34622663157"            # p. ej. 34612345678 (sin +)
EMAIL = "murciacerrajerourgente@gmail.com"
UPDATED = "2026-10-06"
CSS_VER = hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "styles.css"), "rb").read()).hexdigest()[:8]
import sys as _s0; _s0.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extra_content import EXTRA, EXTRA_FAQ
PHOTOS = {
    "zonas.html": ("cerrajero-24-horas-murcia.webp", "Cerrajero trabajando en la cerradura de una puerta en Murcia, con la catedral al fondo"),
    "cambio-de-cerraduras.html": ("cambio-de-bombin-murcia.webp", "Cerrajero extrayendo el bombín de una puerta para cambiarlo por uno de seguridad en Murcia"),
    "apertura-de-puertas.html": ("apertura-de-puertas-murcia.webp", "Cerrajero abriendo con llave la cerradura de una puerta de vivienda en Murcia"),
}

WA_MSG = "Hola%2C%20necesito%20un%20cerrajero%20en%20Murcia"

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3 .78.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.25-.12-1.47-.72-1.7-.8s-.39-.12-.56.12-.64.8-.78.97-.29.18-.54.06a6.7 6.7 0 0 1-3.3-2.9c-.25-.43.25-.4.71-1.33a.45.45 0 0 0-.02-.42c-.06-.12-.56-1.35-.77-1.85s-.4-.42-.56-.43h-.48a.92.92 0 0 0-.67.31 2.8 2.8 0 0 0-.87 2.08 4.9 4.9 0 0 0 1.02 2.6 11.2 11.2 0 0 0 4.3 3.8c1.6.69 2.23.75 3.03.63a2.6 2.6 0 0 0 1.7-1.2 2.1 2.1 0 0 0 .15-1.2c-.06-.1-.23-.17-.48-.29z"/></svg>'
ICON_KEY = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#0f1f33" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.3-9.3M17 6l3 3M14.5 8.5l2 2"/></svg>'
ICON_DOOR = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#0f1f33" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21h16M6 21V3h12v18"/><circle cx="14.5" cy="12" r="1"/></svg>'
ICON_LOCK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#0f1f33" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#0f1f33" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg>'
LOGO = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="#ffb800"/><circle cx="15" cy="24" r="6.5" fill="none" stroke="#0f1f33" stroke-width="3"/><path d="m19.6 19.4 10-10M26 13l3.5 3.5M22.8 16.2l2.3 2.3" stroke="#0f1f33" stroke-width="3" stroke-linecap="round"/></svg>'

NAV = [  # (página, texto en móvil, texto corto en ordenador o None)
    ("index.html", "Inicio", None),
    ("apertura-de-puertas.html", "Apertura de puertas", "Apertura"),
    ("cambio-de-cerraduras.html", "Cambio de cerraduras", "Cerraduras"),
    ("cerraduras-de-seguridad.html", "Cerraduras de seguridad", "Seguridad"),
    ("apertura-de-coches.html", "Apertura de coches", None),
    ("apertura-de-cajas-fuertes.html", "Cajas fuertes", None),
    ("persianas-y-cierres-de-local.html", "Persianas y locales", None),
    ("cerrajeria-para-comunidades.html", "Comunidades", None),
    ("zonas.html", "Zonas", "Zonas"),
    ("blog.html", "Blog y guías", "Blog"),
    ("como-trabajamos.html", "Cómo trabajamos", None),
    ("contacto.html", "Contacto", "Contacto"),
    ("aviso-urgente.html", "🚨 Aviso urgente", "Urgencias"),
]


def url(slug):
    return DOM + "/" if slug == "index.html" else f"{DOM}/{slug}"


def call_btn(label="Llamar ahora", cls="btn btn-call"):
    return f'<a class="{cls}" href="tel:{TEL_LINK}">{ICON_PHONE}{label}</a>'


def wa_btn(label="WhatsApp", cls="btn btn-wa"):
    return f'<a class="{cls}" href="https://wa.me/{WA}?text={WA_MSG}" rel="nofollow noopener" target="_blank">{ICON_WA}{label}</a>'


def faq_html(faqs):
    items = "".join(
        f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in faqs)
    return f'<div class="faq">{items}</div>'


def faq_schema(faqs):
    import re
    strip = lambda t: re.sub(r"<[^>]+>", "", t)
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": strip(q),
                        "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}


def org_schema():
    return {"@type": "Organization", "@id": DOM + "/#org", "name": NAME, "url": DOM + "/",
            "telephone": TEL_LINK, "logo": DOM + "/img/logo.png",
            "description": "Red de cerrajeros colaboradores que atiende urgencias de cerrajería las 24 horas en Murcia y municipios cercanos."}


def service_schema(name, desc, slug, stype):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": stype,
            "description": desc, "url": url(slug),
            "areaServed": {"@type": "City", "name": "Murcia",
                           "containedInPlace": {"@type": "AdministrativeArea", "name": "Región de Murcia"}},
            "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": TEL_LINK, "contactType": "urgencias de cerrajería", "availableLanguage": "es", "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}},
            "provider": org_schema()}


def crumbs_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(s)}
                                 for i, (s, n) in enumerate(trail)]}


def crumbs_html(trail):
    lis = []
    for i, (s, n) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li aria-current="page">{n}</li>')
        else:
            lis.append(f'<li><a href="{s}">{n}</a></li>')
    return f'<nav class="crumbs" aria-label="Migas de pan"><ol>{"".join(lis)}</ol></nav>'


def header(slug, root=""):
    def link(s, n):
        cur = ' aria-current="page"' if s == slug else ""
        cls = ' class="urg"' if s == "aviso-urgente.html" else ""
        return f'<li><a href="{root}{s}"{cur}{cls}>{n}</a></li>'
    items = "".join(link(s, n) for s, n, _ in NAV)
    desk = "".join(link(s, c) for s, _, c in NAV if c)
    return f"""<div class="topbar">Urgencias de cerrajería en Murcia · Llama a cualquier hora, también domingos y festivos</div>
<header class="site"><div class="wrap head">
<a class="logo" href="{root or ''}{'index.html' if not root else ''}"><img src="{root}img/logo-cerrajero-24-horas-murcia.webp" alt="Cerrajero 24 Horas en Murcia" width="186" height="84"></a>
<nav class="menu" aria-label="Menú principal">
<ul class="desk">{desk}</ul>
<details><summary>Menú</summary><ul>{items}</ul></details>
</nav>
{call_btn("Llamar", "btn btn-call head-call")}
</div></header>"""


def footer(root="", slug=""):
    aviso_href = {"index.html": "#aviso-rapido", "aviso-urgente.html": "#aviso"}.get(slug, f"{root}aviso-urgente.html")
    return f"""<footer class="site"><div class="wrap">
<div class="foot-grid">
<div><h2>{NAME}</h2>
<p>Red de cerrajeros colaboradores para urgencias en Murcia capital, barrios y pedanías. Un solo teléfono, a cualquier hora.</p>
<p><a href="tel:{TEL_LINK}">📞 Llamar ahora</a><br><a href="https://wa.me/{WA}?text={WA_MSG}" rel="nofollow noopener" target="_blank">💬 WhatsApp</a></p></div>
<div><h2>Servicios</h2><ul>
<li><a href="{root}apertura-de-puertas.html">Apertura de puertas</a></li>
<li><a href="{root}cambio-de-cerraduras.html">Cambio de cerraduras y bombines</a></li>
<li><a href="{root}cerraduras-de-seguridad.html">Cerraduras de seguridad</a></li>
<li><a href="{root}apertura-de-coches.html">Apertura de coches</a></li>
<li><a href="{root}apertura-de-cajas-fuertes.html">Apertura de cajas fuertes</a></li>
<li><a href="{root}persianas-y-cierres-de-local.html">Persianas y locales</a></li>
<li><a href="{root}cerrajeria-para-comunidades.html">Comunidades de vecinos</a></li>
</ul></div>
<div><h2>Información</h2><ul>
<li><a href="{root}zonas.html">Zonas de Murcia</a></li>
<li><a href="{root}aviso-urgente.html">Aviso urgente</a></li>
<li><a href="{root}blog.html">Blog y guías</a></li>
<li><a href="{root}como-trabajamos.html">Cómo trabajamos</a></li>
<li><a href="{root}contacto.html">Contacto</a></li>
</ul></div>
</div>
<div class="legal">© 2026 {NAME} · <a href="{root}aviso-legal.html">Aviso legal</a> · <a href="{root}politica-privacidad.html">Privacidad</a> · <a href="{root}politica-cookies.html">Cookies</a></div>
</div></footer>
<div class="mobile-bar"><a class="call" href="tel:{TEL_LINK}">{ICON_PHONE}Llamar</a><a class="wa" href="https://wa.me/{WA}?text={WA_MSG}" rel="nofollow noopener" target="_blank">{ICON_WA}WhatsApp</a><a class="urg" href="{aviso_href}">🚨 Aviso</a></div>
{'' if aviso_href.startswith("#") else f'<a class="float-aviso" href="{aviso_href}">🚨 ¿Urgencia? Envía un aviso</a>'}"""


def page(slug, title, desc, body, schemas, robots="index,follow", root="", og_type="website"):
    assert len(title) <= 60, (slug, len(title), title)
    assert len(desc) <= 155, (slug, len(desc), desc)
    # Fotos: solo se muestran si el archivo existe en img/
    ph = PHOTOS.get(slug)
    if ph and os.path.exists(os.path.join(OUT, "img", ph[0])):
        from PIL import Image as _I
        w, h = _I.open(os.path.join(OUT, "img", ph[0])).size
        iv = hashlib.md5(open(os.path.join(OUT, "img", ph[0]), "rb").read()).hexdigest()[:8]
        img = f'<img class="photo" src="img/{ph[0]}?v={iv}" alt="{ph[1]}" width="{w}" height="{h}" loading="lazy">'
        if len(ph) > 2 and ph[2]:
            img = f'<a href="tel:{TEL_LINK}" aria-label="Llamar al cerrajero 24 horas">{img}</a>'
        figure = f'<section style="padding-bottom:0"><div class="wrap">{img}</div></section>'
        k = body.find("</section>") + len("</section>")
        body = body[:k] + figure + body[k:]
    extra = EXTRA.get(slug, "")
    if extra:
        k = max(body.rfind('<section class="alt"><div class="wrap">\n<h2>Preguntas'), body.rfind('<section><div class="wrap">\n<h2>Preguntas'))
        if k < 0:
            k = body.rfind('<section><div class="wrap"><div class="cta">')
        body = body[:k] + extra + body[k:]
    canon = url(slug)
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    css = f"{root}styles.css?v={CSS_VER}"
    doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0f1f33">
<link rel="icon" href="{root}img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{root}img/apple-touch-icon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOM}/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{css}">
<script defer src="/_vercel/insights/script.js"></script>
{'<link rel="preload" as="image" href="img/cerrajero-24-horas-murcia.webp" fetchpriority="high">' if slug == "index.html" else ""}
{ld}
</head>
<body>
{header(slug, root)}
<main>
{body}
</main>
{footer(root, slug)}
</body>
</html>
"""
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(doc)


def cta(title="¿Necesitas un cerrajero ahora?", text="Llama y te pasamos con el cerrajero de guardia de tu zona. Te dirá qué hay que hacer y cuánto cuesta antes de salir."):
    return f"""<section><div class="wrap"><div class="cta"><h2>{title}</h2><p>{text}</p>
<div class="btns">{call_btn("Llamar ahora")}{wa_btn()}</div></div></div></section>"""


def hero(h1, lead, trail=None, chips=None, small=False, bg=None):
    cr = crumbs_html(trail) if trail else ""
    ch = ""
    if chips:
        ch = '<ul class="chips">' + "".join(f"<li>{c}</li>" for c in chips) + "</ul>"
    style = f' style="background-image:linear-gradient(90deg,rgba(15,31,51,.94) 0%,rgba(15,31,51,.82) 55%,rgba(15,31,51,.45) 100%),url(img/{bg})"' if bg else ""
    return f"""<section class="hero{' small' if small else ''}{' has-bg' if bg else ''}"{style}><div class="wrap">{cr}
<h1>{h1}</h1><p class="lead">{lead}</p>
<div class="btns">{call_btn()}{wa_btn()}</div>
<p class="aviso-link"><a href="aviso-urgente.html">¿Prefieres escribir? Envía un aviso urgente con tus datos →</a></p>{ch}</div></section>"""


def aviso_rapido():
    zonas = ["Murcia (centro y barrios)"] + [z.get("short", z["name"]) for z in ZONAS if z["slug"] != "cerrajero-centro-murcia.html"] + ["Otra zona"]
    zopts = "".join(f"<option>{z}</option>" for z in zonas)
    qopts = "".join(f"<option>{q}</option>" for q in ["Me he quedado fuera", "Llave rota", "La cerradura no gira", "Robo o puerta forzada", "Cambiar bombín", "Coche", "Caja fuerte", "Persiana de local", "Otro problema"])
    return f"""<form id="aviso-rapido" class="quick" novalidate>
<p class="quick-title">🚨 Aviso urgente por WhatsApp</p>
<label>¿Qué pasa?<select name="que" required><option value="">Elige una opción</option>{qopts}</select></label>
<label>¿Dónde estás?<select name="zona" required><option value="">Elige tu zona</option>{zopts}</select></label>
<p class="quick-err" role="alert"></p>
<button class="btn btn-wa full" type="submit">{ICON_WA}Enviar aviso</button>
<p class="quick-note">Te contestamos al momento. Al enviarlo aceptas la <a href="politica-privacidad.html">privacidad</a>. ¿Más detalles? <a href="aviso-urgente.html">Aviso completo</a>.</p>
</form>
<script>
document.getElementById('aviso-rapido').addEventListener('submit', function (e) {{
  e.preventDefault();
  var f = e.target, q = f.elements['que'].value, z = f.elements['zona'].value;
  if (!q || !z) {{ f.querySelector('.quick-err').textContent = 'Elige qué pasa y dónde estás.'; return; }}
  var msg = '🚨 AVISO URGENTE DE CERRAJERÍA\\n🔧 Qué pasa: ' + q + '\\n🗺️ Zona: ' + z;
  window.location.href = 'https://wa.me/{WA}?text=' + encodeURIComponent(msg);
}});
</script>"""


def hero_home(h1, lead, bg=None, chips=None):
    ch = '<ul class="chips">' + "".join(f"<li>{c}</li>" for c in chips) + "</ul>" if chips else ""
    style = f' style="background-image:linear-gradient(90deg,rgba(15,31,51,.94) 0%,rgba(15,31,51,.82) 55%,rgba(15,31,51,.45) 100%),url(img/{bg})"' if bg else ""
    return f"""<section class="hero has-bg"{style}><div class="wrap home-grid">
<div class="h-text"><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="btns">{call_btn()}{wa_btn()}</div>{ch}</div>
<div class="h-form">{aviso_rapido()}</div>
</div></section>"""


# ============================================================ INICIO
def build_index():
    faqs = [
        ("¿De verdad cogéis el teléfono de madrugada?",
         "Sí. El número está desviado a cerrajeros de guardia las 24 horas, todos los días del año, incluidos domingos y festivos. Si es de noche, no tienes que dejar un mensaje ni esperar a que abra una tienda."),
        ("¿Sois una empresa de cerrajería?",
         "Somos una red de cerrajeros colaboradores que trabajan en Murcia. Tú llamas a un único número y la llamada pasa al profesional de guardia que está más cerca. El trabajo lo hace y lo factura ese cerrajero. Lo explicamos con detalle en <a href=\"como-trabajamos.html\">cómo trabajamos</a>."),
        ("¿Cuánto cuesta abrir una puerta?",
         "Depende de si la puerta está solo cerrada de golpe o con la llave echada, del tipo de cerradura y de la hora. Por eso no publicamos una tarifa cerrada: el cerrajero te pregunta cómo es tu puerta y te da el precio por teléfono antes de salir. Si no te convence, no hay compromiso."),
        ("¿Cuánto tarda en llegar el cerrajero?",
         "Depende de la zona y de la hora. Al llamar, el cerrajero te dice cuánto tardará en llegar a tu dirección concreta, para que no estés esperando en la calle sin saber nada."),
        ("¿Me van a pedir que demuestre que vivo ahí?",
         "Sí, y es buena señal. Un cerrajero serio comprueba que la vivienda es tuya o que vives en ella: DNI con la dirección, contrato de alquiler, un recibo o un vecino que te conozca. Si alguien abre cualquier puerta sin preguntar nada, desconfía."),
        ("¿Quién me hace la factura?",
         "El cerrajero que realiza el trabajo. Pídela siempre: es tu garantía si la cerradura o el bombín que te han puesto da problemas."),
    ]
    faqs = faqs + EXTRA_FAQ.get("index.html", [])
    body = hero_home(
        "Cerrajero 24 horas en Murcia",
        "¿Te has quedado fuera, se ha partido la llave o la cerradura no gira? Llama a cualquier hora y te ponemos al momento con un cerrajero de guardia en Murcia. Te da el precio por teléfono antes de salir.",
        bg="cerrajero-24-horas-murcia.webp", chips=["Abierto 24 h · 365 días", "Murcia capital y pedanías", "Precio antes de salir", "Apertura sin romper siempre que se pueda"])
    body += f"""
<section><div class="wrap">
<h2>Urgencias de cerrajería en Murcia</h2>
<p>Las urgencias de cerrajería casi nunca pasan en horario de oficina: la puerta se cierra con el aire cuando sacas la basura, la llave se parte un domingo o te das cuenta de que te han intentado forzar el bombín al volver de la playa. Por eso este teléfono no cierra.</p>
<div class="grid three">
<div class="card"><div class="ico">{ICON_DOOR}</div><h3>Apertura de puertas</h3><p>Puertas cerradas de golpe o con llave, llave partida dentro, puertas acorazadas, trasteros y garajes.</p><a class="more" href="apertura-de-puertas.html">Ver apertura de puertas →</a></div>
<div class="card"><div class="ico">{ICON_KEY}</div><h3>Cambio de cerraduras y bombines</h3><p>Al mudarte, al cambiar de inquilino, si has perdido las llaves o si el bombín se atasca.</p><a class="more" href="cambio-de-cerraduras.html">Ver cambio de cerraduras →</a></div>
<div class="card"><div class="ico">{ICON_SHIELD}</div><h3>Cerraduras de seguridad</h3><p>Bombines antibumping, escudos protectores y cerraduras multipunto para que no te abran en un minuto.</p><a class="more" href="cerraduras-de-seguridad.html">Ver cerraduras de seguridad →</a></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Qué pasa cuando llamas</h2>
<ol class="steps">
<li><strong>Te atiende el cerrajero de guardia</strong>Tu llamada pasa directamente al profesional que cubre tu zona a esa hora. Sin centralitas eternas.</li>
<li><strong>Le cuentas qué ocurre</strong>Si la puerta está cerrada de golpe o con llave, si es acorazada, si hay una llave rota dentro… Con eso ya sabe qué herramientas llevar.</li>
<li><strong>Te da el precio y el tiempo de llegada</strong>Antes de salir sabes cuánto va a costar y cuánto va a tardar. Si te parece bien, sale hacia tu dirección.</li>
<li><strong>Abre, arregla y te da la factura</strong>Comprueba que la vivienda es tuya, hace el trabajo y te entrega la factura con su garantía.</li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Cómo evitar un cerrajero abusivo en Murcia</h2>
<p>En cerrajería hay mucha gente seria, pero también hay quien aprovecha los nervios del momento. Ten en cuenta esto, nos llames a nosotros o a cualquier otro:</p>
<ul class="list">
<li><strong>Pide el precio antes de que salga.</strong> Si no te lo quieren decir por teléfono, cuelga y busca otro.</li>
<li><strong>Desconfía de «desde 30 €».</strong> Es el truco más habitual: el precio final acaba multiplicado al añadir desplazamiento, nocturnidad y «material».</li>
<li><strong>Una puerta cerrada de golpe casi siempre se abre sin romper nada.</strong> Si te dicen de entrada que hay que taladrar, pregunta por qué.</li>
<li><strong>Exige factura</strong> con los datos del profesional. Sin factura no tienes garantía ni forma de reclamar.</li>
<li><strong>No pagues por adelantado</strong> un trabajo que todavía no se ha hecho.</li>
</ul>
<div class="note">Lo explicamos con más detalle, paso a paso, en la guía <a href="guia-te-has-quedado-fuera-de-casa.html">qué hacer si te has quedado fuera de casa</a>.</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Cerrajeros en toda Murcia</h2>
<p>Cubrimos Murcia capital y las pedanías del municipio: del centro y barrios como El Carmen, Vistalegre o Santa María de Gracia a Espinardo, El Palmar, Puente Tocinos, Beniaján, La Alberca, Cabezo de Torres o el Campo de Murcia.</p>
<p>Zonas con página propia: {", ".join(f'<a href="{z["slug"]}">{z.get("short", z["name"])}</a>' for z in ZONAS)}.</p>
<p><a class="btn btn-call" href="zonas.html">Ver todas las zonas</a></p>
</div></section>

<section><div class="wrap">
<h2>Preguntas frecuentes</h2>
{faq_html(faqs)}
</div></section>
{cta()}"""
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": DOM + "/", "inLanguage": "es-ES", "publisher": {"@id": DOM + "/#org"}}
    org = dict(org_schema()); org["@context"] = "https://schema.org"
    page("index.html", "Cerrajero 24 Horas en Murcia | Urgencias a cualquier hora",
         "Cerrajero 24 horas en Murcia: apertura de puertas, cambio de cerraduras y bombines. Te damos el precio por teléfono antes de salir. Llama ahora.",
         body, [org, website,
                service_schema("Cerrajero 24 horas en Murcia", "Servicio de cerrajería urgente las 24 horas en Murcia: apertura de puertas, cambio de cerraduras y bombines y cerraduras de seguridad.", "index.html", "Cerrajería urgente"),
                faq_schema(faqs)])


# ============================================================ APERTURA
def build_apertura():
    trail = [("index.html", "Inicio"), ("apertura-de-puertas.html", "Apertura de puertas")]
    faqs = [
        ("¿Se puede abrir mi puerta sin romper la cerradura?",
         "Si la puerta está cerrada solo de golpe, con el resbalón, en la gran mayoría de casos sí. Si está cerrada con la llave echada, depende del bombín: muchos se abren con técnica, pero los de alta seguridad a veces obligan a extraerlo, y entonces hay que poner uno nuevo en el momento."),
        ("Se me ha partido la llave dentro de la cerradura, ¿qué hago?",
         "No intentes sacar el trozo con pinzas o con otra llave: lo empujarías más hacia dentro y puedes dañar los pitones del bombín. Llama y explica que la llave está partida; normalmente se extrae el trozo con una herramienta específica y, si el bombín ha sufrido, se cambia."),
        ("¿Abrís puertas acorazadas?",
         "Sí. Son más lentas de abrir y cada fabricante es distinto, por eso conviene decir por teléfono la marca si la ves en la puerta o en la llave. Con ese dato el cerrajero te puede dar un precio más ajustado."),
        ("¿Y si dentro hay un niño, una persona mayor o el fuego encendido?",
         "Si hay una persona en peligro o riesgo de incendio, llama primero al 112. Los bomberos y la policía actúan antes que cualquier cerrajero en una emergencia de verdad. Después nos llamas para reparar o cambiar la cerradura."),
        ("¿Abrís también trasteros, garajes y buzones?",
         "Sí: trasteros, cuartos de contadores, puertas de cochera y buzones. Indica por teléfono qué tipo de cerradura es para que el cerrajero lleve lo necesario."),
    ]
    faqs = faqs + EXTRA_FAQ.get("apertura-de-puertas.html", [])
    body = hero("Apertura de puertas en Murcia",
                "Si te has quedado en la calle, llama a cualquier hora. Siempre que se pueda, el cerrajero abre sin romper nada y, si hace falta cambiar el bombín, lo cambia en el momento.",
                trail=trail, small=True)
    body += f"""
<section><div class="wrap">
<h2>No es lo mismo una puerta cerrada de golpe que una cerrada con llave</h2>
<p>Es la pregunta que te hará el cerrajero nada más descolgar, y la respuesta cambia el trabajo y el precio:</p>
<h3>Puerta cerrada de golpe (solo con el resbalón)</h3>
<p>Es el caso más habitual: sales a tender, a tirar la basura o a por el correo y la corriente cierra la puerta. La cerradura solo está sujeta por el resbalón, la pieza inclinada que encaja sola. Casi siempre se abre sin daños y en pocos minutos, sin tocar el bombín.</p>
<h3>Puerta cerrada con la llave echada</h3>
<p>Aquí hay que actuar sobre el bombín, la pieza donde metes la llave. Con un bombín corriente, un buen profesional suele abrirlo con técnica. Con un bombín de seguridad, diseñado precisamente para resistir esos métodos, a veces la única forma es extraerlo, y entonces se pone uno nuevo antes de irse para que la puerta no quede abierta.</p>
<h3>Llave partida o atascada</h3>
<p>Si la llave se ha roto dentro o no gira, no fuerces. Un trozo de llave empujado hacia dentro complica mucho la extracción. Explícalo por teléfono tal cual.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Puertas que abrimos en Murcia</h2>
<div class="grid">
<div class="card"><h3>Pisos y fincas del centro</h3><p>Puertas de madera de los edificios más antiguos de los barrios del centro, muchas con cerradura de sobreponer o cerrojo añadido, y portales de comunidad.</p></div>
<div class="card"><h3>Puertas acorazadas y blindadas</h3><p>Muy habituales en los pisos más modernos y en las zonas de nueva construcción. Si sabes la marca de la puerta o de la llave, dila al llamar.</p></div>
<div class="card"><h3>Casas de pedanías y de huerta</h3><p>Puertas de calle de hierro o madera, cancelas, cerrojos y candados en patios y almacenes.</p></div>
<div class="card"><h3>Trasteros, garajes y locales</h3><p>Trasteros de comunidad, puertas de cochera, cuartos de contadores y persianas de local comercial que no abren por la cerradura.</p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>Mientras esperas al cerrajero</h2>
<ul class="list">
<li><strong>Ten a mano algo que demuestre que vives ahí</strong>: DNI con la dirección, contrato, un recibo en el móvil o un vecino que te conozca.</li>
<li><strong>No intentes abrir con una tarjeta o una radiografía</strong>: además de que rara vez funciona, puedes doblar el resbalón o dañar el marco.</li>
<li><strong>Si es un piso de alquiler</strong>, avisa al propietario: puede que tenga copia de la llave y te ahorres la apertura.</li>
<li><strong>Comprueba si alguien más tiene llave</strong>: familiares, el vecino de confianza, la persona que limpia.</li>
</ul>
<div class="warn">Si dentro hay un niño o una persona que no puede abrir, o hay algo al fuego, llama primero al <strong>112</strong>.</div>
<p>Si después de la apertura ves que el bombín ha quedado tocado o quieres más seguridad, mira las opciones de <a href="cambio-de-cerraduras.html">cambio de cerraduras y bombines</a>.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Preguntas sobre la apertura de puertas</h2>
{faq_html(faqs)}
</div></section>
{cta("¿Te has quedado fuera?", "Llama ahora: el cerrajero de guardia te pregunta cómo está la puerta y te da el precio antes de salir.")}"""
    page("apertura-de-puertas.html", "Apertura de Puertas en Murcia 24 h | Sin romper la cerradura",
         "Apertura de puertas en Murcia a cualquier hora: cerradas de golpe o con llave, acorazadas y llaves partidas. Precio por teléfono antes de salir.",
         body, [service_schema("Apertura de puertas en Murcia", "Apertura de puertas cerradas de golpe o con llave, puertas acorazadas, llaves partidas, trasteros y garajes en Murcia, las 24 horas.", "apertura-de-puertas.html", "Apertura de puertas"),
                faq_schema(faqs), crumbs_schema(trail)])


# ============================================================ CAMBIO
def build_cambio():
    trail = [("index.html", "Inicio"), ("cambio-de-cerraduras.html", "Cambio de cerraduras")]
    faqs = [
        ("¿Tengo que cambiar toda la cerradura o basta con el bombín?",
         "En la mayoría de puertas de piso basta con cambiar el bombín, que es la pieza donde entra la llave. La cerradura completa (la caja metida en la puerta) solo se cambia si está rota, si falla el mecanismo o si quieres pasar a una cerradura multipunto."),
        ("¿Cómo sé qué medida de bombín tiene mi puerta?",
         "Se mide desde el tornillo que lo sujeta hacia cada lado, por ejemplo 30 × 40 mm. No hace falta que lo midas tú: el cerrajero lo comprueba en el momento y lleva varias medidas en la furgoneta."),
        ("Me acabo de mudar a un piso de alquiler, ¿puedo cambiar el bombín?",
         "Es muy recomendable, porque no sabes cuántas copias de la llave existen. Lo habitual es avisar al propietario y guardar el bombín antiguo para volver a ponerlo al irte, o dejarle una copia de la llave nueva si así lo habéis acordado."),
        ("¿Cambiáis la cerradura del portal o del buzón de la comunidad?",
         "Sí, pero la cerradura del portal es de la comunidad: lo normal es que lo pida el presidente o el administrador de la finca, que es quien reparte las llaves nuevas a los vecinos."),
        ("Me han robado o he perdido las llaves con la dirección, ¿es urgente?",
         "Sí. Si las llaves pueden asociarse a tu casa, por ejemplo porque iban con el DNI o en el bolso con algún papel, cambia el bombín cuanto antes, aunque sea de madrugada."),
    ]
    faqs = faqs + EXTRA_FAQ.get("cambio-de-cerraduras.html", [])
    body = hero("Cambio de cerraduras y bombines en Murcia",
                "Te mudas, has perdido las llaves o la llave ya no entra bien: el cerrajero cambia el bombín o la cerradura en el momento, a cualquier hora.",
                trail=trail, small=True)
    body += f"""
<section><div class="wrap">
<h2>Cuándo conviene cambiar el bombín</h2>
<ul class="list">
<li><strong>Al entrar a vivir en una casa o piso</strong>, comprado o alquilado. Nadie sabe cuántas copias de la llave han circulado.</li>
<li><strong>Al cambiar de inquilino</strong> si alquilas tu vivienda: es lo primero que debería hacer el propietario entre un contrato y otro.</li>
<li><strong>Cuando pierdes las llaves</strong> o te roban el bolso o la mochila con ellas.</li>
<li><strong>Después de un intento de robo</strong>, aunque la puerta siga abriendo: un bombín forzado puede fallar en cualquier momento.</li>
<li><strong>Si la llave entra dura, se atasca o tienes que hacer fuerza</strong>. Es el aviso de que el bombín está desgastado y un día no abrirá.</li>
<li><strong>Tras una separación</strong> o cuando alguien que tenía llave deja de vivir en casa.</li>
</ul>
</div></section>

<section class="alt"><div class="wrap">
<h2>Bombín, cerradura y cerrojo: qué es cada cosa</h2>
<h3>El bombín o cilindro</h3>
<p>Es la pieza donde metes la llave. Se cambia en pocos minutos sin tocar la puerta y es lo que hay que cambiar en la mayoría de los casos. Aquí está también la mayor diferencia de seguridad: un bombín básico y uno de seguridad parecen iguales por fuera, pero no se parecen en nada por dentro.</p>
<h3>La cerradura</h3>
<p>Es el mecanismo metido en el canto de la puerta, el que mueve el resbalón y los pestillos. Solo se cambia si se ha roto o si quieres ganar seguridad con una cerradura de varios puntos de cierre.</p>
<h3>El cerrojo adicional</h3>
<p>Una segunda cerradura, por encima o por debajo de la principal. Muy útil en puertas de madera antiguas y en casas de planta baja donde no compensa cambiar toda la puerta.</p>
</div></section>

<section><div class="wrap">
<h2>Qué bombín elegir</h2>
<p>Si la puerta da a la calle o a un rellano por el que pasa gente, no te quedes con el bombín más barato. Pide que te enseñen al menos estas dos opciones y elige con el precio delante:</p>
<ul class="list">
<li><strong>Bombín de gama básica</strong>: sirve para trasteros, puertas interiores o como cambio provisional.</li>
<li><strong>Bombín de seguridad</strong>: con protección antibumping, antiganzúa, antitaladro y antiextracción, y llaves que solo se copian con tarjeta de propiedad. Te lo explicamos en <a href="cerraduras-de-seguridad.html">cerraduras de seguridad</a>.</li>
</ul>
<div class="note">Pide siempre las llaves en su blíster o bolsa original y, si el bombín es de seguridad, la tarjeta de propiedad. Sin la tarjeta no podrás hacer copias oficiales.</div>
<p>Si ahora mismo estás fuera de casa y no puedes entrar, lo primero es la <a href="apertura-de-puertas.html">apertura de la puerta</a>; el cambio de bombín se hace a continuación en la misma visita.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Preguntas sobre el cambio de cerraduras</h2>
{faq_html(faqs)}
</div></section>
{cta("¿Quieres cambiar el bombín hoy?", "Llama y cuéntale al cerrajero qué puerta es. Te dice las opciones y el precio antes de ir.")}"""
    page("cambio-de-cerraduras.html", "Cambio de Cerraduras y Bombines en Murcia | 24 horas",
         "Cambio de bombines y cerraduras en Murcia al mudarte, perder las llaves o tras un robo. Cerrajero a cualquier hora y precio antes de salir.",
         body, [service_schema("Cambio de cerraduras y bombines en Murcia", "Cambio de bombines, cerraduras y cerrojos en viviendas, locales y comunidades de Murcia, a cualquier hora.", "cambio-de-cerraduras.html", "Cambio de cerraduras"),
                faq_schema(faqs), crumbs_schema(trail)])


# ============================================================ SEGURIDAD
def build_seguridad():
    trail = [("index.html", "Inicio"), ("cerraduras-de-seguridad.html", "Cerraduras de seguridad")]
    faqs = [
        ("¿Qué es el bumping y cómo sé si mi bombín lo resiste?",
         "El bumping consiste en abrir el bombín con una llave manipulada golpeándola para que los pitones salten a la vez. Lo hacen en segundos y sin dejar marcas. Para saber si el tuyo lo resiste, mira el embalaje o la ficha del fabricante: debe indicar expresamente protección antibumping. Si no lo sabes, el cerrajero lo identifica por la marca y el modelo grabados en el bombín."),
        ("¿Qué significa que un bombín sea antiextracción o antirrotura?",
         "Que está preparado para que, si intentan arrancarlo o partirlo con una herramienta, se rompa por un punto de sacrificio y la parte que bloquea la cerradura quede dentro de la puerta. Es una de las protecciones más importantes, porque el ataque por extracción es muy rápido."),
        ("¿Para qué sirve un escudo protector?",
         "Es una placa de acero que se coloca por fuera, alrededor del bombín, para que no se pueda agarrar ni taladrar. Muchos llevan una pieza giratoria que tapa la entrada de la llave. Es de lo más eficaz que se puede añadir a una puerta normal."),
        ("¿Merece la pena poner una puerta acorazada?",
         "En un piso de una finca sin portero, en una planta baja o en una segunda residencia que pasa tiempo vacía, sí suele merecer la pena. En otros casos, un buen bombín con escudo protector en la puerta actual ya mejora mucho la seguridad por bastante menos dinero."),
        ("¿Qué normas tiene que cumplir un bombín de seguridad?",
         "En Europa los cilindros se clasifican con la norma UNE-EN 1303, que indica, entre otras cosas, su grado de seguridad frente a ataques. Pide que te digan la clasificación del bombín que te ofrecen y compárala antes de decidir."),
    ]
    faqs = faqs + EXTRA_FAQ.get("cerraduras-de-seguridad.html", [])
    body = hero("Cerraduras de seguridad y bombines antibumping en Murcia",
                "La mayoría de robos en viviendas no rompen la puerta: atacan el bombín. Te ayudamos a elegir y a instalar el bombín, el escudo o la cerradura que de verdad protegen tu casa.",
                trail=trail, small=True)
    body += f"""
<section><div class="wrap">
<h2>Cómo intentan abrir una puerta los ladrones</h2>
<p>Conocer los métodos ayuda a entender qué protección necesitas:</p>
<h3>Bumping</h3>
<p>Una llave manipulada que se golpea dentro del bombín. Es silencioso, rápido y no deja apenas marcas, por lo que muchas veces ni el seguro detecta que ha sido un robo.</p>
<h3>Ganzúa e impresioning</h3>
<p>Manipular los pitones uno a uno o fabricar una copia de la llave a partir de las marcas que deja una llave virgen. Requiere más tiempo, pero los bombines básicos no ofrecen resistencia.</p>
<h3>Extracción y rotura del bombín</h3>
<p>Arrancar o partir el bombín con una herramienta para acceder al mecanismo. Es el método más rápido cuando el bombín sobresale de la puerta.</p>
<h3>Taladro</h3>
<p>Perforar la línea de pitones para que el bombín gire. Los bombines de seguridad llevan piezas de acero endurecido para impedirlo.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Qué protección poner según tu vivienda</h2>
<div class="grid">
<div class="card"><h3>Piso en finca con portal</h3><p>Bombín de seguridad antibumping y antiextracción, con escudo protector. Es la mejora con mejor relación entre lo que cuesta y lo que protege.</p></div>
<div class="card"><h3>Bajo, ático o casa de planta baja</h3><p>Además del bombín y el escudo, un cerrojo de seguridad adicional o una cerradura multipunto, porque suelen tener más accesos y menos vecinos que vean algo.</p></div>
<div class="card"><h3>Segunda residencia o casa de campo</h3><p>Pasa semanas vacía, así que conviene la máxima resistencia: puerta acorazada o, al menos, cerradura multipunto y escudo. Revisa también los accesos por patio y almacén.</p></div>
<div class="card"><h3>Local comercial</h3><p>Cerraduras de seguridad en la puerta y candados o cerraduras reforzadas en la persiana, que suele ser el punto débil.</p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>Qué mirar antes de pagar un bombín «de seguridad»</h2>
<ul class="list">
<li><strong>Que indique por escrito sus protecciones</strong>: antibumping, antiganzúa, antitaladro y antiextracción. «De seguridad» a secas no significa nada.</li>
<li><strong>Que tenga clasificación según la norma UNE-EN 1303</strong>, y que te digan qué grado tiene.</li>
<li><strong>Que la copia de la llave esté protegida</strong> con tarjeta de propiedad, para que nadie pueda hacer copias en cualquier ferretería.</li>
<li><strong>Que no sobresalga de la puerta</strong> más de unos pocos milímetros, o que vaya cubierto por un escudo.</li>
<li><strong>Que te den factura</strong> con la marca y el modelo instalados.</li>
</ul>
<p>Si te urge porque has perdido las llaves o han intentado entrar, mira cómo funciona el <a href="cambio-de-cerraduras.html">cambio de bombín urgente</a>.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Preguntas sobre cerraduras de seguridad</h2>
{faq_html(faqs)}
</div></section>
{cta("¿Quieres reforzar tu puerta?", "Llama y cuéntale al cerrajero cómo es tu puerta. Te recomienda la protección adecuada y te da el precio antes de ir.")}"""
    page("cerraduras-de-seguridad.html", "Bombines Antibumping y Cerraduras de Seguridad en Murcia",
         "Bombines antibumping, escudos protectores y cerraduras multipunto en Murcia. Te explicamos qué protección necesita tu puerta y la instalamos.",
         body, [service_schema("Instalación de cerraduras de seguridad en Murcia", "Instalación de bombines antibumping, escudos protectores, cerrojos y cerraduras multipunto en Murcia.", "cerraduras-de-seguridad.html", "Instalación de cerraduras de seguridad"),
                faq_schema(faqs), crumbs_schema(trail)])


# ============================================================ ZONAS
CHIP_LINKS = {
    "Centro": "cerrajero-centro-murcia.html", "El Carmen": "cerrajero-el-carmen-murcia.html", "Vistalegre": "cerrajero-vistalegre-la-flota.html",
    "La Flota": "cerrajero-vistalegre-la-flota.html", "Santa María de Gracia": "cerrajero-vistalegre-la-flota.html", "San Antón": "cerrajero-vistalegre-la-flota.html", "San Basilio": "cerrajero-vistalegre-la-flota.html",
    "Infante Juan Manuel": "cerrajero-el-carmen-murcia.html", "Barriomar": "cerrajero-el-carmen-murcia.html", "Santiago el Mayor": "cerrajero-el-carmen-murcia.html",
    "San Andrés": "cerrajero-centro-murcia.html", "San Antolín": "cerrajero-centro-murcia.html",
    "Santiago y Zaraiche": "cerrajero-santiago-y-zaraiche-zarandona.html", "Zarandona": "cerrajero-santiago-y-zaraiche-zarandona.html",
    "Monteagudo": "cerrajero-monteagudo-el-esparragal.html", "Cobatillas": "cerrajero-monteagudo-el-esparragal.html",
    "Llano de Brujas": "cerrajero-llano-de-brujas-el-raal.html", "El Raal": "cerrajero-llano-de-brujas-el-raal.html", "Alquerías": "cerrajero-llano-de-brujas-el-raal.html", "Santa Cruz": "cerrajero-llano-de-brujas-el-raal.html",
    "Javalí Nuevo": "cerrajero-javali-sangonera-la-seca.html", "Javalí Viejo": "cerrajero-javali-sangonera-la-seca.html", "Sangonera la Seca": "cerrajero-javali-sangonera-la-seca.html",
    "Aljucer": "cerrajero-aljucer-era-alta-nonduermas.html", "Era Alta": "cerrajero-aljucer-era-alta-nonduermas.html", "Nonduermas": "cerrajero-aljucer-era-alta-nonduermas.html",
    "La Raya": "cerrajero-aljucer-era-alta-nonduermas.html", "Rincón de Seca": "cerrajero-aljucer-era-alta-nonduermas.html", "Puebla de Soto": "cerrajero-aljucer-era-alta-nonduermas.html",
    "Espinardo": "cerrajero-espinardo-churra.html", "Churra": "cerrajero-espinardo-churra.html", "Cabezo de Torres": "cerrajero-cabezo-de-torres.html",
    "La Ñora": "cerrajero-guadalupe-la-nora.html", "Guadalupe": "cerrajero-guadalupe-la-nora.html",
    "El Palmar": "cerrajero-el-palmar.html", "La Alberca": "cerrajero-la-alberca-santo-angel.html", "Santo Ángel": "cerrajero-la-alberca-santo-angel.html",
    "Algezares": "cerrajero-algezares-los-garres.html", "Los Garres": "cerrajero-algezares-los-garres.html",
    "Beniaján": "cerrajero-beniajan-torreaguera.html", "Torreagüera": "cerrajero-beniajan-torreaguera.html",
    "Sangonera la Verde": "cerrajero-sangonera-la-verde.html", "Puente Tocinos": "cerrajero-puente-tocinos.html",
    "Corvera": "cerrajero-campo-de-murcia.html", "Sucina": "cerrajero-campo-de-murcia.html", "Valladolises": "cerrajero-campo-de-murcia.html", "Lobosillo": "cerrajero-campo-de-murcia.html",
    "Molina de Segura": "cerrajero-molina-de-segura.html", "Alcantarilla": "cerrajero-alcantarilla.html",
    "Las Torres de Cotillas": "cerrajero-las-torres-de-cotillas.html", "Santomera": "cerrajero-santomera.html",
}


def build_zonas():
    trail = [("index.html", "Inicio"), ("zonas.html", "Zonas")]
    zonas = [
        ("Centro y barrios de Murcia", "Fincas antiguas con portal de comunidad, pisos con puerta acorazada y muchos locales comerciales con persiana.",
         ["Centro", "El Carmen", "Vistalegre", "La Flota", "Santa María de Gracia", "San Andrés", "San Antolín", "San Antón", "San Basilio", "Vistabella", "La Fama", "Infante Juan Manuel", "Barriomar", "Santiago el Mayor"]),
        ("Norte", "Zona de pisos nuevos, residenciales con garaje y trastero y la zona universitaria, con mucho piso de estudiantes.",
         ["Espinardo", "Churra", "Cabezo de Torres", "El Puntal", "Santiago y Zaraiche", "Zarandona", "Monteagudo", "Cobatillas"]),
        ("Huerta oeste", "Casas de huerta y de planta baja, cancelas, almacenes y patios, junto a urbanizaciones más recientes.",
         ["La Ñora", "Guadalupe", "Javalí Nuevo", "Javalí Viejo", "Era Alta", "Rincón de Seca", "Nonduermas", "Aljucer", "La Raya", "Puebla de Soto", "Sangonera la Seca"]),
        ("Sur y faldas de la sierra", "Pedanías grandes con mezcla de pisos y casas, y viviendas unifamiliares en la falda de la sierra.",
         ["El Palmar", "La Alberca", "Santo Ángel", "Algezares", "Los Garres", "Beniaján", "Torreagüera", "Los Ramos", "Sangonera la Verde"]),
        ("Este", "Pedanías de huerta con casas de planta baja y pequeños núcleos de pisos.",
         ["Puente Tocinos", "Llano de Brujas", "El Raal", "Alquerías", "Santa Cruz", "Zeneta", "Casillas", "Los Dolores", "Rincón de Beniscornia"]),
        ("Campo de Murcia", "Casas de campo y segundas residencias que pasan tiempo vacías, donde la seguridad de puertas y almacenes es clave.",
         ["Corvera", "Sucina", "Valladolises", "Lobosillo", "Baños y Mendigo", "Gea y Truyols", "Jerónimo y Avileses", "Cañadas de San Pedro", "Los Martínez del Puerto"]),
        ("Municipios cercanos", "Fuera del municipio de Murcia, atendemos los municipios vecinos con más vivienda: cascos urbanos, urbanizaciones y polígonos.",
         ["Molina de Segura", "Alcantarilla", "Las Torres de Cotillas", "Santomera"]),
    ]
    zlinks = "".join(f'<div class="card"><h3><a href="{z['slug']}">Cerrajero en {z.get("short", z['name'])}</a></h3><p>{z['lead']}</p></div>' for z in ZONAS)
    blocks = ""
    for t, d, lst in zonas:
        lis = "".join(f'<li><a href="{CHIP_LINKS[z]}">{z}</a></li>' if z in CHIP_LINKS else f"<li>{z}</li>" for z in lst)
        blocks += f'<div class="card"><h3>{t}</h3><p>{d}</p><ul>{lis}</ul></div>'
    faqs = [
        ("¿Vais también a pedanías alejadas como Sucina o Corvera?",
         "Sí, cubrimos todo el municipio de Murcia, también el Campo de Murcia. Al estar más lejos del centro, el cerrajero te dirá al llamar el tiempo de llegada real a tu dirección."),
        ("¿El precio es el mismo en todas las zonas?",
         "El precio depende sobre todo del trabajo y de la hora, y también de la distancia. Por eso el cerrajero te da el precio exacto por teléfono, sabiendo ya dónde estás, antes de salir."),
        ("Mi pueblo no está en la lista, ¿podéis venir?",
         "Además del municipio de Murcia, atendemos <a href='cerrajero-molina-de-segura.html'>Molina de Segura</a> , <a href='cerrajero-alcantarilla.html'>Alcantarilla</a>, <a href='cerrajero-las-torres-de-cotillas.html'>Las Torres de Cotillas</a> y <a href='cerrajero-santomera.html'>Santomera</a>. Si estás en otro municipio cercano, llama y te dirán al momento si hay un cerrajero disponible para tu zona."),
    ]
    body = hero("Cerrajeros en barrios y pedanías de Murcia",
                "Trabajamos en todo el municipio de Murcia, del centro a las pedanías de la huerta y el Campo de Murcia, y también en Molina de Segura, Alcantarilla, Las Torres de Cotillas y Santomera. Al llamar, te pasamos con el cerrajero de guardia que cubre tu zona.",
                trail=trail, small=True)
    body += f"""
<section><div class="wrap">
<h2>Zonas de Murcia donde trabajamos</h2>
<p>Cada zona tiene un tipo de vivienda distinto, y eso cambia el trabajo habitual del cerrajero: no es lo mismo abrir una acorazada en un piso de Juan de Borbón que una cancela en una casa de huerta.</p>
<div class="zones">{blocks}</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Páginas de cerrajero por zona</h2>
<p>Para las zonas con más avisos tenemos una página propia, con su tipo de vivienda, los trabajos más habituales y consejos para dar bien la ubicación:</p>
<div class="grid">{zlinks}</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Qué decir al llamar para que el cerrajero llegue antes</h2>
<ol class="list">
<li><strong>La dirección completa</strong>, con la pedanía si estás fuera del casco urbano. En la huerta hay muchas calles con nombres parecidos.</li>
<li><strong>Una referencia</strong>: una iglesia, un bar, el número de una carretera o un carril. En el campo, la ubicación del móvil por WhatsApp ayuda mucho.</li>
<li><strong>Cómo está la puerta</strong>: cerrada de golpe o con llave, si es acorazada y, si la ves, la marca.</li>
<li><strong>Un teléfono con batería</strong> por si el cerrajero necesita llamarte al llegar.</li>
</ol>
<p>Consulta los servicios de <a href="apertura-de-puertas.html">apertura de puertas</a>, <a href="cambio-de-cerraduras.html">cambio de cerraduras</a> y <a href="cerraduras-de-seguridad.html">cerraduras de seguridad</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Preguntas sobre las zonas</h2>
{faq_html(faqs)}
</div></section>
{cta()}"""
    page("zonas.html", "Cerrajeros en Barrios y Pedanías de Murcia | 24 horas",
         "Cerrajero 24 horas en Murcia capital y pedanías: El Palmar, Espinardo, Puente Tocinos, Beniaján, La Alberca, Campo de Murcia y más zonas.",
         body, [service_schema("Cerrajero 24 horas en barrios y pedanías de Murcia", "Servicio de cerrajería urgente en Murcia capital, sus barrios y las pedanías del municipio.", "zonas.html", "Cerrajería urgente"),
                faq_schema(faqs), crumbs_schema(trail)])


# ============================================================ CÓMO TRABAJAMOS
def build_como():
    trail = [("index.html", "Inicio"), ("como-trabajamos.html", "Cómo trabajamos")]
    faqs = [
        ("¿Por qué una red de cerrajeros y no una sola empresa?",
         "Porque un solo cerrajero no puede estar a la vez en El Palmar y en Churra a las tres de la mañana. Con varios profesionales de guardia repartidos por Murcia, siempre hay alguien disponible y más cerca de ti."),
        ("¿Quién responde si hay un problema con el trabajo?",
         "El cerrajero que hace el trabajo es quien lo factura y quien te da la garantía. Si tienes cualquier problema, escríbenos también a nosotros: queremos saberlo, porque solo trabajamos con profesionales que cumplen."),
        ("¿Qué datos míos se guardan al llamar?",
         "Solo los necesarios para atenderte: tu teléfono y, si nos la das, la dirección. Se comparten únicamente con el cerrajero que va a hacer el trabajo. Lo explicamos en la <a href=\"politica-privacidad.html\">política de privacidad</a>."),
    ]
    body = hero("Cómo trabajamos",
                "Somos una red de cerrajeros colaboradores en Murcia. Te lo contamos claro, porque en este sector la confianza lo es todo.",
                trail=trail, small=True)
    body += f"""
<section><div class="wrap">
<h2>Qué es Cerrajero 24 Horas en Murcia</h2>
<p>Cerrajero 24 Horas en Murcia es un servicio que pone en contacto a quien necesita un cerrajero urgente con profesionales de cerrajería que trabajan en el municipio de Murcia. No somos una única empresa con furgonetas propias: somos el teléfono que te conecta, a cualquier hora, con el cerrajero de guardia de tu zona.</p>
<p>El servicio de contacto es gratuito para ti. Pagas únicamente el trabajo que haga el cerrajero, al precio que él te ha dado por teléfono y aceptado por ti antes de salir.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Lo que pedimos a cada cerrajero de la red</h2>
<ul class="list">
<li><strong>Que sea un profesional dado de alta</strong>, autónomo o empresa, y que tenga seguro de responsabilidad civil.</li>
<li><strong>Que dé el precio por teléfono antes de salir</strong> y lo respete, salvo que al llegar el trabajo sea distinto al descrito; en ese caso, te lo explica y decides tú antes de empezar.</li>
<li><strong>Que compruebe que la vivienda es tuya</strong> o que vives en ella antes de abrir.</li>
<li><strong>Que entregue factura</strong> a su nombre, con el trabajo realizado y el material instalado.</li>
<li><strong>Que abra sin romper siempre que sea posible</strong> y explique por qué si no lo es.</li>
</ul>
</div></section>

<section><div class="wrap">
<h2>Si algo no ha ido bien</h2>
<p>Si el cerrajero no ha cumplido el precio acordado, no te ha dado factura o el trabajo tiene algún problema, escríbenos por <a href="https://wa.me/{WA}?text={WA_MSG}" rel="nofollow noopener" target="_blank">WhatsApp</a> con la fecha, la dirección y lo que ha pasado. Lo revisamos con el profesional y, si no cumple con estas condiciones, deja de recibir avisos.</p>
<p>Recuerda que también tienes derecho a pedir la hoja de reclamaciones y a acudir a la oficina de consumo del Ayuntamiento de Murcia o de la Región de Murcia.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Preguntas sobre el servicio</h2>
{faq_html(faqs)}
</div></section>
{cta()}"""
    page("como-trabajamos.html", "Cómo Trabajamos | Cerrajero 24 Horas en Murcia",
         "Somos una red de cerrajeros colaboradores en Murcia: precio por teléfono antes de salir, factura del profesional y apertura sin romper si es posible.",
         body, [faq_schema(faqs), crumbs_schema(trail)])


# ============================================================ GUÍA
def build_guia():
    slug = "guia-te-has-quedado-fuera-de-casa.html"
    trail = [("index.html", "Inicio"), (slug, "Guía: te has quedado fuera de casa")]
    faqs = [
        ("¿Puedo llamar a los bomberos si me he quedado fuera de casa?",
         "Solo si hay una emergencia real: una persona dentro que no puede abrir, un niño pequeño, algo al fuego o un escape. Para eso está el 112. Si simplemente te has dejado las llaves, lo que corresponde es un cerrajero."),
        ("¿Lo cubre el seguro del hogar?",
         "Muchos seguros del hogar incluyen la apertura de puertas por pérdida o robo de llaves, a veces con un límite. Revisa la póliza o llama a tu aseguradora: si lo cubre, te dirán cómo gestionarlo."),
        ("¿Y si vivo de alquiler?",
         "Llama primero al propietario o a la inmobiliaria: pueden tener una copia. Si no es posible, la apertura la pagas tú normalmente, y si hay que cambiar el bombín, avisa al propietario y dale una copia de la llave nueva."),
    ]
    body = f"""<section class="hero small"><div class="wrap article">{crumbs_html(trail)}
<h1>Te has quedado fuera de casa en Murcia: qué hacer paso a paso</h1>
<p class="lead">Una guía rápida para no perder la calma, no gastar de más y no estropear la puerta.</p>
<p class="meta">Actualizado el 6 de octubre de 2026</p>
<div class="btns">{call_btn()}{wa_btn()}</div></div></section>

<section><div class="wrap article">
<h2>1. Comprueba primero si es una emergencia</h2>
<p>Si dentro hay un niño, una persona mayor o alguien que no puede abrir, o si te has dejado algo al fuego, <strong>llama al 112</strong> antes que a nadie. En ese caso los servicios de emergencia actúan antes que cualquier cerrajero.</p>

<h2>2. Piensa quién más tiene llave</h2>
<p>Pareja, padres, hijos, un vecino de confianza, la persona que limpia, el propietario si vives de alquiler… Una llamada puede ahorrarte la apertura. Si el que tiene la copia tarda en llegar, compara: a veces compensa esperar y a veces no.</p>

<h2>3. No intentes abrir tú</h2>
<p>Los vídeos de abrir con una tarjeta o una radiografía funcionan en puertas muy concretas y sin la llave echada. En el resto de casos, lo normal es doblar el resbalón, rayar el marco o, peor, romper algo que luego hay que cambiar. Tampoco intentes entrar por un balcón o una ventana: no merece la pena jugarse un disgusto.</p>

<h2>4. Mira cómo está la puerta</h2>
<p>Antes de llamar al cerrajero, fíjate en dos cosas, porque de ellas depende el precio:</p>
<ul class="list">
<li><strong>¿Se cerró sola o echaste la llave?</strong> Si solo se cerró de golpe, casi siempre se abre sin daños.</li>
<li><strong>¿Es una puerta acorazada?</strong> Si ves la marca en la puerta o en la cerradura, apúntala.</li>
</ul>

<h2>5. Llama y pide el precio antes de que salga</h2>
<p>Un cerrajero serio te pregunta cómo está la puerta y te da un precio cerrado o, como mucho, una horquilla muy concreta. Si te dicen «ya lo vemos allí», desconfía. Pregunta también cuánto tardará en llegar.</p>
<div class="note">Al llamarnos, el cerrajero de guardia te dirá el precio y el tiempo de llegada antes de salir. Si no te encaja, no hay compromiso.</div>

<h2>6. Prepara algo que demuestre que vives ahí</h2>
<p>El cerrajero debe comprobar que la vivienda es tuya o que vives en ella. Sirve el DNI con la dirección, el contrato de alquiler, un recibo en el móvil o un vecino que te conozca. Si alguien abre sin preguntar nada, es mala señal.</p>

<h2>7. Pide factura y revisa el bombín</h2>
<p>Cuando la puerta esté abierta, pide la factura. Si para abrir ha habido que extraer el bombín, el cerrajero debe poner uno nuevo antes de irse: aprovecha para pedir uno de seguridad y no el más básico. Te explicamos cómo elegirlo en <a href="cerraduras-de-seguridad.html">cerraduras de seguridad</a>.</p>

<h2>Cómo evitar que te vuelva a pasar</h2>
<ul class="list">
<li>Deja una copia de la llave a alguien de confianza que viva cerca.</li>
<li>Acostúmbrate a cerrar la puerta con la llave en la mano, no tirando del pomo.</li>
<li>Si la llave ya entra dura, cambia el bombín antes de que se quede atascado un domingo por la noche: mira el <a href="cambio-de-cerraduras.html">cambio de cerraduras y bombines</a>.</li>
</ul>

<h2>Preguntas frecuentes</h2>
{faq_html(faqs)}
</div></section>
{cta("¿Sigues en la calle?", "Llama ahora. Te pasamos con el cerrajero de guardia y te dice precio y tiempo de llegada antes de salir.")}"""
    post = {"@context": "https://schema.org", "@type": "BlogPosting",
            "headline": "Te has quedado fuera de casa en Murcia: qué hacer paso a paso",
            "description": "Guía para saber qué hacer si te quedas fuera de casa en Murcia: emergencias, quién tiene llave, precio antes de salir y factura.",
            "datePublished": UPDATED, "dateModified": UPDATED, "inLanguage": "es-ES",
            "mainEntityOfPage": url(slug), "image": DOM + "/img/og-image.jpg",
            "author": {"@type": "Organization", "name": NAME, "url": DOM + "/"},
            "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": DOM + "/img/logo.png"}}}
    page(slug, "Te Has Quedado Fuera de Casa en Murcia: Qué Hacer",
         "Qué hacer si te quedas fuera de casa en Murcia: cuándo llamar al 112, quién puede tener llave, cómo evitar abusos y qué pedir al cerrajero.",
         body, [post, faq_schema(faqs), crumbs_schema(trail)], og_type="article")


# ============================================================ CONTACTO
def build_contacto():
    trail = [("index.html", "Inicio"), ("contacto.html", "Contacto")]
    body = hero("Contacto: cerrajero urgente en Murcia",
                "Para urgencias, llama: es lo más rápido. Por WhatsApp puedes mandarnos la ubicación y una foto de la cerradura.",
                trail=trail, small=True)
    body += f"""
<section><div class="wrap">
<div class="grid">
<div class="card"><div class="ico">{ICON_PHONE.replace('fill="currentColor"', 'fill="#0f1f33"')}</div><h2>Teléfono 24 horas</h2><p><a href="tel:{TEL_LINK}"><strong>Llamar ahora</strong></a></p><p class="muted">Todos los días, a cualquier hora. Es la vía más rápida para una urgencia.</p></div>
<div class="card"><div class="ico">{ICON_WA.replace('fill="currentColor"', 'fill="#0f1f33"')}</div><h2>WhatsApp</h2><p><a href="https://wa.me/{WA}?text={WA_MSG}" rel="nofollow noopener" target="_blank"><strong>Escribir por WhatsApp</strong></a></p><p class="muted">Manda tu ubicación y una foto de la cerradura o de la llave.</p></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Qué necesitamos saber</h2>
<ul class="list">
<li>La dirección, con la pedanía si estás fuera del casco urbano. Consulta las <a href="zonas.html">zonas donde trabajamos</a>.</li>
<li>Qué ha pasado: puerta cerrada de golpe o con llave, llave partida, bombín que no gira, intento de robo…</li>
<li>El tipo de puerta y, si la ves, la marca de la cerradura.</li>
</ul>
<p>Con esos datos, el cerrajero de guardia te da el precio y el tiempo de llegada antes de salir. Si es la primera vez que nos llamas, puedes leer antes <a href="como-trabajamos.html">cómo trabajamos</a>.</p>
</div></section>
{cta()}"""
    page("contacto.html", "Contacto | Cerrajero Urgente en Murcia 24 horas",
         "Contacta con un cerrajero urgente en Murcia por teléfono o WhatsApp a cualquier hora. Precio y tiempo de llegada antes de salir.",
         body, [crumbs_schema(trail)])


# ============================================================ LEGALES
def legal(slug, title, h1, content, desc):
    trail = [("index.html", "Inicio"), (slug, h1)]
    body = f"""<section class="hero small"><div class="wrap">{crumbs_html(trail)}<h1>{h1}</h1></div></section>
<section><div class="wrap article">{content}</div></section>"""
    page(slug, title, desc, body, [crumbs_schema(trail)], robots="noindex,follow")


TITULAR = "Alberto López"
NIF = "[NIF]"
DOMICILIO = "España"


def build_legales():
    legal("aviso-legal.html", "Aviso Legal | Cerrajero 24 Horas en Murcia", "Aviso legal", f"""
<h2>Titular del sitio web</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
<ul class="list">
<li>Titular: {NAME}</li>
<li>Domicilio: {DOMICILIO}</li>
<li>Correo electrónico: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>Sitio web: cerrajero24horasmurcia.es</li>
</ul>
<h2>Objeto y naturaleza del servicio</h2>
<p>Este sitio web ofrece un servicio de intermediación que pone en contacto a los usuarios que necesitan un servicio de cerrajería con profesionales cerrajeros colaboradores que trabajan en Murcia y municipios cercanos. Los trabajos de cerrajería los presta, factura y garantiza el profesional que los realiza, que es quien informa del precio al usuario antes de prestar el servicio.</p>
<h2>Condiciones de uso</h2>
<p>El acceso a este sitio web es gratuito. El usuario se compromete a hacer un uso adecuado de los contenidos y a no emplearlos para actividades ilícitas o contrarias a la buena fe.</p>
<h2>Propiedad intelectual</h2>
<p>Los textos, el diseño y el código de este sitio web son propiedad del titular o se usan con autorización. Queda prohibida su reproducción sin permiso expreso.</p>
<h2>Responsabilidad</h2>
<p>El titular procura que la información de este sitio sea correcta y esté actualizada, pero no garantiza la ausencia de errores. La información sobre cerraduras y seguridad tiene carácter orientativo; la valoración de cada caso corresponde al profesional que lo atiende.</p>
<h2>Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española.</p>""",
          "Aviso legal de cerrajero24horasmurcia.es: datos del titular, naturaleza del servicio de intermediación y condiciones de uso.")

    legal("politica-privacidad.html", "Política de Privacidad | Cerrajero 24 Horas en Murcia", "Política de privacidad", f"""
<h2>Responsable del tratamiento</h2>
<p>{NAME}, con domicilio en {DOMICILIO}. Correo electrónico: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Qué datos tratamos</h2>
<p>Cuando nos llamas, nos escribes por WhatsApp o nos envías el formulario de aviso urgente (que se envía a través de WhatsApp) tratamos tu número de teléfono, tu nombre si nos lo das, la dirección donde necesitas el servicio y la información que nos cuentes sobre la incidencia.</p>
<h2>Para qué los usamos</h2>
<ul class="list">
<li>Atender tu solicitud y ponerte en contacto con el cerrajero colaborador que va a realizar el trabajo.</li>
<li>Gestionar las incidencias o reclamaciones que nos comuniques sobre el servicio.</li>
</ul>
<h2>Base legal</h2>
<p>La aplicación de medidas precontractuales a petición tuya (artículo 6.1.b del Reglamento General de Protección de Datos) y, en la gestión de reclamaciones, nuestro interés legítimo en controlar la calidad del servicio (artículo 6.1.f).</p>
<h2>A quién se comunican</h2>
<p>Al cerrajero colaborador que atiende tu servicio, que necesita tus datos para contactarte y desplazarse a tu dirección. También pueden acceder a ellos los proveedores que nos prestan los servicios de telefonía, correo y alojamiento web, con los que tenemos los contratos exigidos por la ley. No se ceden datos a otros terceros salvo obligación legal.</p>
<h2>Estadísticas de la web</h2>
<p>Medimos las visitas a la web con Vercel Web Analytics, sin cookies y de forma agregada y anónima (página visitada, procedencia, país, tipo de dispositivo y navegador), con el fin de mejorar la web. No permite identificarte. Más información en la <a href="politica-cookies.html">política de cookies</a>.</p>
<h2>Cuánto tiempo los conservamos</h2>
<p>El tiempo necesario para atender tu solicitud y, después, durante los plazos en que puedan derivarse responsabilidades legales.</p>
<h2>Tus derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. Si consideras que no se han respetado tus derechos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (www.aepd.es).</p>""",
          "Política de privacidad de cerrajero24horasmurcia.es: qué datos tratamos al atender tu llamada, para qué, con quién se comparten y tus derechos.")

    legal("politica-cookies.html", "Política de Cookies | Cerrajero 24 Horas en Murcia", "Política de cookies", f"""
<h2>¿Usa cookies este sitio web?</h2>
<p>Este sitio web no utiliza cookies propias ni de terceros, ni con fines analíticos, publicitarios o de seguimiento. Por eso no te mostramos ningún aviso para aceptarlas.</p>
<h2>Estadísticas de visitas sin cookies</h2>
<p>Para saber cuántas personas visitan la web y qué páginas consultan, usamos <strong>Vercel Web Analytics</strong>, el servicio de estadísticas de nuestro proveedor de alojamiento. Funciona <strong>sin cookies</strong> y sin guardar nada en tu dispositivo: no te identifica personalmente ni te sigue en otras webs. Solo recoge datos agregados y anónimos, como la página visitada, la web de procedencia, el país y el tipo de dispositivo y navegador.</p>
<h2>Enlaces a servicios externos</h2>
<p>Los botones de WhatsApp abren la aplicación o la web de WhatsApp, que tiene su propia política de privacidad y de cookies.</p>
<h2>Cambios en esta política</h2>
<p>Si en el futuro se incorporan herramientas que usen cookies, se actualizará esta página y se pedirá tu consentimiento cuando sea necesario.</p>""",
          "Política de cookies de cerrajero24horasmurcia.es: no usamos cookies. Las estadísticas de visitas se miden sin cookies con Vercel Web Analytics.")


# ============================================================ 404
def build_404():
    body = f"""<section class="hero"><div class="wrap">
<h1>Esta página no existe</h1>
<p class="lead">Puede que el enlace esté mal escrito o que la página se haya movido. Si necesitas un cerrajero ahora, llama: atendemos a cualquier hora.</p>
<div class="btns">{call_btn()}{wa_btn()}<a class="btn btn-ghost" href="/">Ir al inicio</a></div>
</div></section>
<section><div class="wrap"><h2>Páginas útiles</h2><ul class="list">
<li><a href="/apertura-de-puertas.html">Apertura de puertas</a></li>
<li><a href="/cambio-de-cerraduras.html">Cambio de cerraduras y bombines</a></li>
<li><a href="/cerraduras-de-seguridad.html">Cerraduras de seguridad</a></li>
<li><a href="/zonas.html">Zonas de Murcia</a></li>
<li><a href="/contacto.html">Contacto</a></li>
</ul></div></section>"""
    page("404.html", "Página no encontrada | Cerrajero 24 Horas en Murcia",
         "La página que buscas no existe. Si necesitas un cerrajero urgente en Murcia, llama a cualquier hora.",
         body, [], robots="noindex,follow", root="/")


# ============================================================ PÁGINAS DE ZONA
import sys as _sys
_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zonas_data import ZONAS


def build_zona_pages():
    for z in ZONAS:
        zf = z["faqs"] + EXTRA_FAQ.get(z["slug"], [])
        trail = [("index.html", "Inicio"), ("zonas.html", "Zonas"), (z["slug"], z.get("short", z["name"]))]
        chips = "".join(f"<li>{x}</li>" for x in z["zones"])
        vec = " · ".join(f'<a href="{s}">{n}</a>' for s, n in z["vecinos"])
        body = hero(z["h1"], z["lead"], trail=trail, small=True)
        body += z["body"]
        body += f"""
<section><div class="wrap">
<h2>Zonas que cubrimos en {z["name"]}</h2>
<div class="zones"><div class="card"><ul>{chips}</ul></div>
<div class="card"><h3>Servicios</h3><ul class="list" style="display:block;margin-top:.4rem">
<li style="background:none;border:0;padding:0"><a href="apertura-de-puertas.html">Apertura de puertas</a></li>
<li style="background:none;border:0;padding:0"><a href="cambio-de-cerraduras.html">Cambio de cerraduras y bombines</a></li>
<li style="background:none;border:0;padding:0"><a href="cerraduras-de-seguridad.html">Cerraduras de seguridad</a></li>
</ul></div></div>
<p style="margin-top:1rem">Zonas cercanas: {vec}.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Preguntas frecuentes en {z["name"]}</h2>
{faq_html(zf)}
</div></section>
{cta(f"¿Necesitas un cerrajero en {z['name']}?", "Llama ahora: el cerrajero de guardia te da el precio y el tiempo de llegada antes de salir.")}"""
        svc = service_schema(f"Cerrajero 24 horas en {z['name']}", z["desc"], z["slug"], "Cerrajería urgente")
        svc["areaServed"] = {"@type": "Place", "name": f"{z.get('short', z['name'])}, Murcia"}
        page(z["slug"], z["title"], z["desc"], body, [svc, faq_schema(zf), crumbs_schema(trail)])


# ============================================================ SERVICIOS NUEVOS, BLOG Y AVISO
from servicios_data import SERVICIOS
from blog_data import POSTS


def build_servicios():
    for sv in SERVICIOS:
        trail = [("index.html", "Inicio"), (sv["slug"], sv["short"])]
        body = hero(sv["h1"], sv["lead"], trail=trail, small=True)
        body += sv["body"]
        body += f"""
<section class="alt"><div class="wrap">
<h2>Preguntas sobre {sv["short"].lower()}</h2>
{faq_html(sv["faqs"])}
<p style="margin-top:1rem">Atendemos en Murcia capital, sus pedanías y municipios cercanos: consulta las <a href="zonas.html">zonas donde trabajamos</a>. Otros servicios: <a href="apertura-de-puertas.html">apertura de puertas</a>, <a href="cambio-de-cerraduras.html">cambio de cerraduras</a> y <a href="cerraduras-de-seguridad.html">cerraduras de seguridad</a>.</p>
</div></section>
{cta()}"""
        page(sv["slug"], sv["title"], sv["desc"], body,
             [service_schema(sv["h1"], sv["desc"], sv["slug"], sv["stype"]), faq_schema(sv["faqs"]), crumbs_schema(trail)])


def build_blog():
    all_posts = POSTS + [{"slug": "guia-te-has-quedado-fuera-de-casa.html", "h1": "Te has quedado fuera de casa en Murcia: qué hacer paso a paso",
                          "lead": "Una guía rápida para no perder la calma, no gastar de más y no estropear la puerta."}]
    for po in POSTS:
        trail = [("index.html", "Inicio"), ("blog.html", "Blog"), (po["slug"], po["h1"])]
        others = "".join(f'<li><a href="{o["slug"]}">{o["h1"]}</a></li>' for o in all_posts if o["slug"] != po["slug"])
        body = f"""<section class="hero small"><div class="wrap article">{crumbs_html(trail)}
<h1>{po["h1"]}</h1>
<p class="lead">{po["lead"]}</p>
<p class="meta">Actualizado el 6 de octubre de 2026</p>
<div class="btns">{call_btn()}{wa_btn()}</div></div></section>
<section><div class="wrap article">
{po["body"]}
<h2>Preguntas frecuentes</h2>
{faq_html(po["faqs"])}
<h2>Otras guías</h2>
<ul class="list">{others}</ul>
</div></section>
{cta()}"""
        post = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": po["h1"], "description": po["desc"],
                "datePublished": po["date"], "dateModified": po["date"], "inLanguage": "es-ES",
                "mainEntityOfPage": url(po["slug"]), "image": DOM + "/img/og-image.jpg",
                "author": {"@type": "Organization", "name": NAME, "url": DOM + "/"},
                "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": DOM + "/img/logo.png"}}}
        page(po["slug"], po["title"], po["desc"], body, [post, faq_schema(po["faqs"]), crumbs_schema(trail)], og_type="article")
    # índice del blog
    trail = [("index.html", "Inicio"), ("blog.html", "Blog")]
    cards = "".join(f'<div class="card"><h2 style="font-size:1.15rem"><a href="{o["slug"]}">{o["h1"]}</a></h2><p>{o["lead"]}</p></div>' for o in all_posts)
    body = hero("Blog de cerrajería: guías prácticas", "Qué hacer si te quedas fuera, si se parte la llave o después de un robo, y cómo mejorar la seguridad de tu puerta. Consejos claros de cerrajeros de Murcia.", trail=trail, small=True)
    body += f"""<section><div class="wrap"><div class="grid">{cards}</div></div></section>{cta()}"""
    blog = {"@context": "https://schema.org", "@type": "Blog", "name": f"Blog de {NAME}", "url": url("blog.html"), "inLanguage": "es-ES",
            "blogPost": [{"@type": "BlogPosting", "headline": o["h1"], "url": url(o["slug"])} for o in all_posts]}
    page("blog.html", "Blog de Cerrajería en Murcia: Guías y Consejos",
         "Guías prácticas de cerrajería: llave rota, robo en casa, bombines antibumping, seguro del hogar y cómo elegir un cerrajero de confianza.",
         body, [blog, crumbs_schema(trail)])


def aviso_form(compact=False):
    locs = ["Murcia (centro y barrios)"] + [z.get("short", z["name"]) for z in ZONAS if z["slug"] != "cerrajero-centro-murcia.html"] + ["Otra zona de Murcia", "Otro municipio"]
    opts = "".join(f"<option>{l}</option>" for l in locs)

    def chips(name, items):
        return "".join(f'<label class="opt"><input type="radio" name="{name}" value="{v}" required><span>{v}</span></label>' for v in items)
    head = '<p class="aviso-title">🚨 Aviso urgente: te contactamos al momento</p>' if compact else ""
    return f"""<form id="aviso" class="aviso{' compact' if compact else ''}" novalidate>
{head}
<fieldset><legend>1. ¿Dónde es?</legend><div class="opts">{chips("donde", ["Casa o piso", "Comunidad", "Negocio", "Coche"])}</div></fieldset>
<fieldset><legend>2. ¿Qué pasa?</legend><div class="opts">{chips("que", ["Me he quedado fuera", "Llave rota", "La cerradura no gira", "Robo o puerta forzada", "Cambiar bombín", "Caja fuerte", "Persiana de local", "Otro problema"])}</div></fieldset>
<fieldset><legend>3. Tus datos</legend>
<div class="fields">
<label>Tipo de puerta<select name="puerta"><option>No lo sé</option><option>Normal de madera</option><option>Blindada</option><option>Acorazada</option><option>Cancela o puerta de calle</option><option>Persiana metálica</option></select></label>
<label>Localidad<select name="zona" required><option value="">Elige tu zona</option>{opts}</select></label>
<label class="full">Dirección (opcional)<input name="dir" autocomplete="street-address" placeholder="Calle, número, piso o urbanización"></label>
<label>Nombre<input name="nombre" autocomplete="name" required placeholder="Tu nombre"></label>
<label>Teléfono<input name="tel" type="tel" inputmode="tel" autocomplete="tel" required placeholder="6XX XXX XXX"></label>
<label class="full">Detalles (opcional)<textarea name="det" rows="3" placeholder="Ej.: la puerta se ha cerrado de golpe y las llaves están dentro"></textarea></label>
</div></fieldset>
<label class="check"><input type="checkbox" name="ok" required> He leído la <a href="politica-privacidad.html">política de privacidad</a> y acepto que mis datos se compartan con el cerrajero que atienda el aviso.</label>
<p class="err" id="err" role="alert"></p>
<button class="btn btn-wa full" type="submit">{ICON_WA}Enviar aviso por WhatsApp</button>
<p class="muted small">Se abrirá WhatsApp con el mensaje ya escrito. Solo tienes que pulsar enviar.</p>
</form>
<script>
document.getElementById('aviso').addEventListener('submit', function (e) {{
  e.preventDefault();
  var f = e.target, err = document.getElementById('err');
  var v = function (n) {{ var el = f.elements[n]; return el ? (el.value || '').trim() : ''; }};
  var r = function (n) {{ var c = f.querySelector('input[name="' + n + '"]:checked'); return c ? c.value : ''; }};
  var tel = v('tel').replace(/[^0-9+]/g, '');
  if (!r('donde') || !r('que')) {{ err.textContent = 'Indica dónde es y qué pasa.'; return; }}
  if (!v('zona') || !v('nombre') || tel.length < 9) {{ err.textContent = 'Completa tu zona, tu nombre y un teléfono válido.'; return; }}
  if (!f.elements['ok'].checked) {{ err.textContent = 'Acepta la política de privacidad para enviar el aviso.'; return; }}
  err.textContent = '';
  var msg = '🚨 AVISO URGENTE DE CERRAJERÍA\\n' +
    '📍 Dónde: ' + r('donde') + '\\n' +
    '🔧 Qué pasa: ' + r('que') + '\\n' +
    '🚪 Puerta: ' + v('puerta') + '\\n' +
    '🗺️ Zona: ' + v('zona') + '\\n' +
    (v('dir') ? '🏠 Dirección: ' + v('dir') + '\\n' : '') +
    '👤 Nombre: ' + v('nombre') + '\\n' +
    '📞 Teléfono: ' + tel + '\\n' +
    (v('det') ? '📝 Detalles: ' + v('det') : '');
  window.location.href = 'https://wa.me/{WA}?text=' + encodeURIComponent(msg);
}});
</script>"""


def build_aviso():
    trail = [("index.html", "Inicio"), ("aviso-urgente.html", "Aviso urgente")]
    locs = ["Murcia (centro y barrios)"] + [z.get("short", z["name"]) for z in ZONAS if z["slug"] != "cerrajero-centro-murcia.html"] + ["Otra zona de Murcia", "Otro municipio"]
    opts = "".join(f"<option>{l}</option>" for l in locs)

    def chips(name, items):
        return "".join(f'<label class="opt"><input type="radio" name="{name}" value="{v}" required><span>{v}</span></label>' for v in items)
    body = f"""<section class="hero small"><div class="wrap">{crumbs_html(trail)}
<h1>Aviso urgente de cerrajería</h1>
<p class="lead">Rellena el aviso en un minuto: nos llega al momento por WhatsApp con todos los datos y el cerrajero de guardia de tu zona se pone en contacto contigo.</p>
<div class="btns">{call_btn("Llamar ahora")}</div></div></section>

<section><div class="wrap aviso-grid">
<div>
<h2>Mientras llega el cerrajero</h2>
<ul class="list">
<li><strong>No fuerces la cerradura</strong> ni metas objetos en el bombín.</li>
<li>Si la llave se ha partido, <strong>no intentes sacar el trozo</strong> con otra llave.</li>
<li>Ten a mano algo que demuestre que vives ahí: <strong>DNI, contrato o un recibo</strong>.</li>
<li>Si dentro hay un niño, una persona dependiente o algo al fuego, <strong>llama al 112</strong>.</li>
</ul>
<div class="note">Para una urgencia, <strong>llamar es siempre lo más rápido</strong>. Usa este aviso si no puedes hablar o prefieres escribir.</div>
</div>

{aviso_form()}
</div></section>"""
    page("aviso-urgente.html", "Aviso Urgente de Cerrajería en Murcia | Por WhatsApp",
         "Envía un aviso urgente de cerrajería en Murcia: dinos dónde estás y qué pasa, y el cerrajero de guardia de tu zona te contacta enseguida.",
         body, [crumbs_schema(trail)])


def build_extras():
    pages = [("index.html", "1.0"), ("apertura-de-puertas.html", "0.9"), ("cambio-de-cerraduras.html", "0.9"),
             ("cerraduras-de-seguridad.html", "0.8"), ("zonas.html", "0.8"),
             ("guia-te-has-quedado-fuera-de-casa.html", "0.7"),
             *[(sv["slug"], "0.8") for sv in SERVICIOS], ("blog.html", "0.6"), *[(po["slug"], "0.6") for po in POSTS],
             ("aviso-urgente.html", "0.5"),
             *[(z["slug"], "0.8") for z in ZONAS], ("como-trabajamos.html", "0.6"), ("contacto.html", "0.6")]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for s, p in pages:
        xml += f"  <url><loc>{url(s)}</loc><lastmod>{UPDATED}</lastmod><priority>{p}</priority></url>\n"
    xml += "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(xml)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOM}/sitemap.xml\n")


if __name__ == "__main__":
    build_index(); build_apertura(); build_cambio(); build_seguridad(); build_zonas()
    build_como(); build_guia(); build_contacto(); build_legales(); build_404(); build_zona_pages(); build_servicios(); build_blog(); build_aviso(); build_extras()
    print("ok")
