# cerrajeros24horasmurcia.es

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
