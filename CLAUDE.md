# cerrajero24horasmurcia.es

Web estática en HTML con una hoja de estilos común (`styles.css`), desplegada en Vercel desde `main`.

## Modelo de negocio (IMPORTANTE)

- Es una **red de cerrajeros colaboradores**: el titular recibe la llamada en su centralita y la pasa a proveedores que hacen el servicio 24 horas. La web lo dice con claridad en «Cómo trabajamos» y en el aviso legal. Nunca dar a entender que es una empresa con furgonetas o local propios.
- Sin ficha de Google Business por ahora. Sin dirección física en la web ni en el schema (no usar `LocalBusiness`/`Locksmith`).
- Totalmente independiente de las otras webs del propietario: no enlazarlas ni copiar sus textos.

## Reglas del propietario

- Siempre en español. Trabajar solo en esta web.
- No tocar lo que ya funciona: solo añadir.
- Contenido único en cada página. Nada de páginas plantilla por pedanía en las que solo cambia el nombre.
- Sin precios. Sin reseñas, testimonios, tiempos de llegada ni datos inventados. Si falta un dato, preguntarlo.
- Cada página: title ≤60, description ≤155, un H1, canonical, Open Graph con `og:image`, JSON-LD que coincida con lo visible (`Service`, `FAQPage`, `BreadcrumbList`; `BlogPosting` en guías), enlaces internos en los dos sentidos, alta en `sitemap.xml` y sin scroll horizontal a 390 px.
- Botón de llamar y de WhatsApp arriba, repetidos y fijos en el móvil.
- Antes de cambiar nada, explicar pros y contras y esperar el «sí». Riesgo con Google: 🟢 / 🟡 / 🔴.
- Formato de respuesta: resumen → propuesta → riesgo → lo que se le escapa → siguiente paso.
- Enlaces internos relativos con `.html`; en `404.html` empiezan por `/`.
- Agrupar cada petición en un solo commit.

## Cómo se genera la web

- Las páginas HTML, `sitemap.xml` y `robots.txt` se generan con `python3 _gen/build.py` (necesita Pillow). No editar los HTML a mano: cambiar los textos en `_gen/` y volver a generar.
- Contenido: `_gen/zonas_data.py` (zonas), `_gen/servicios_data.py` (servicios), `_gen/blog_data.py` (guías), `_gen/extra_content.py` (secciones y preguntas añadidas). Teléfono, dominio y titular, al principio de `_gen/build.py`.
- `_gen/check.py .` revisa un H1 por página, JSON-LD y enlaces rotos. `_gen/` no se publica (`.vercelignore`).
- La portada lleva una tarjeta compacta de aviso urgente (qué pasa + zona) que abre WhatsApp con el mensaje escrito; el formulario completo está en `aviso-urgente.html`.
- `styles.css` se enlaza con `?v=` (huella del archivo) para que los móviles no usen una copia vieja.
