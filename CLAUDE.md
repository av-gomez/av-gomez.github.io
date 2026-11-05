# CLAUDE.md del sitio av-gomez.github.io

Sitio personal de Amanda Gomez Flores (Economía PUCP, IPA Perú). Es HTML y CSS propios, sin template. Se publica desde `docs/`.

## Dónde va cada cosa
- Contenido (proyectos, CV, publicaciones): `generar.py`. Para agregar un proyecto, suma un diccionario a `PROYECTOS`.
- Versión en inglés: `contenido_en.py`, con las mismas claves que `PROYECTOS`. Todo proyecto nuevo debe tener su entrada ahí.
- Diseño: `docs/estilos.css`. Cada tipo de proyecto tiene su color (`.tipo-datos`, `.tipo-ia`, `.tipo-inv`, `.tipo-imp`).
- Fotos y figuras: `docs/images/` (JPG o WebP, menos de 400 KB).
- PDFs y reportes: `docs/files/`.
- Después de editar: `python generar.py`. Nunca edites a mano los `index.html` de `docs/`, porque se sobrescriben.
- Los proyectos se publican en `/proyectos/` porque `/portfolio/` lo ocupa el repo antiguo av-gomez/portfolio.

## Cómo escribir una tarjeta de proyecto
1. Título que diga qué se hizo.
2. Pregunta en una línea.
3. Una cifra verificable, grande.
4. Imagen que se entienda sin leer el texto.
5. Links: código, demo, PDF.

## Reglas
- Español, literal y directo. Sin metáforas. Sin guiones largos.
- No inventar datos, cifras ni links.
- Nunca publicar: teléfono, código de alumna, DNI, números de constancia, resultados o bases de IPA, microdatos no redistribuibles (LIS), datos de otras personas, claves o .env. Tampoco las imágenes de la rifa de 180DC, que muestran datos de pago.
- Videos solo embebidos desde YouTube. Ningún archivo de más de 50 MB.
- Antes de cada push: buscar claves y datos personales.
- Después de cada push: esperar el check verde en Actions y revisar el sitio a 390 px de ancho.
