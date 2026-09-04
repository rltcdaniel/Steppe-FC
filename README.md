# Steppe FC

Sitio estático (HTML plano, sin build step) para GitHub Pages, pensado para
usar más adelante un dominio personalizado vía Namecheap (steppefc.com),
siguiendo el mismo patrón que el resto de proyectos.

## Estado del dominio

steppefc.com **todavía no está comprado**. Por eso:
- No hay archivo `CNAME` en este repo (se añade en cuanto se compre el dominio).
- Todos los enlaces internos (nav, CSS, etc.) usan **rutas relativas**, no
  absolutas, para que el sitio funcione igual de bien servido desde la raíz
  de un dominio propio que desde una subcarpeta de GitHub Pages
  (`https://rltcdaniel.github.io/steppefc/`).
- Las etiquetas `hreflang` y las URLs de `sitemap.xml`/`robots.txt` sí usan
  `https://steppefc.com/...` en absoluto porque son metadatos para cuando el
  dominio esté activo — no afectan a la navegación mientras tanto.

Para previsualizar: activar GitHub Pages en Settings → Pages (rama `main`,
carpeta `/root`) y visitar `https://rltcdaniel.github.io/steppefc/es/`.

Cuando se compre el dominio: añadir el archivo `CNAME` con `steppefc.com`,
configurar los registros DNS en Namecheap y (opcional, no obligatorio)
volver a pasar todas las rutas relativas a absolutas si se prefiere.

## Estructura

- `/es/` y `/en/` — versiones por idioma, misma estructura de páginas en ambas
- `/css/style.css` — hoja de estilos compartida
- `index.html` (raíz) — selector/redirector de idioma según navigator.language
- `sitemap.xml`, `robots.txt` — SEO básico (con URLs absolutas de producción)

## Añadir una página nueva

Duplicar una página existente dentro de `/es/` o `/en/`, actualizar el
`<title>`, la meta description y las etiquetas hreflang. Añadir el enlace
correspondiente al nav en `generate.py` si se quiere regenerar todo el sitio,
o editar el `<nav>` a mano en cada página existente.

## Pendiente

- Definir contenido real de cada sección (noticias, jugadores, clubes)
- Página de aviso legal / política de privacidad + cookie consent (como en
  los otros proyectos)
- Alta en Google Search Console + AdSense cuando haya contenido suficiente
