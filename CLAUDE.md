# CLAUDE.md del sitio av-gomez.github.io

Sitio personal de Amanda Gomez Flores (Economía PUCP, IPA Perú), hecho con academicpages y publicado con GitHub Actions.

## Dónde va cada cosa
- Inicio: _pages/about.md
- Proyectos: _portfolio/ (una tarjeta por archivo; el campo order define el orden, el mejor primero). Se publican en /proyectos/ porque /portfolio/ lo ocupa el repo antiguo av-gomez/portfolio
- Publicaciones: _publications/
- CV web: _pages/cv.md; CV en PDF: files/CV_Amanda_Gomez_Flores.pdf
- Fotos y figuras: images/ (JPG o WebP, menos de 400 KB)
- Configuración: _config.yml; menú: _data/navigation.yml

## Cómo escribir una tarjeta de proyecto
1. Título que diga qué se hizo.
2. **Pregunta.** una línea.
3. **Resultado.** un número verificable.
4. Imagen que se entienda sin leer el texto.
5. Links: código, demo, PDF.

## Reglas
- Español, literal y directo. Sin metáforas. Sin guiones largos.
- No inventar datos, cifras ni links.
- Nunca publicar: teléfono, código de alumna, DNI, números de constancia, resultados o bases de IPA, microdatos no redistribuibles (LIS), datos de otras personas, claves o .env.
- Videos solo embebidos desde YouTube. Ningún archivo de más de 50 MB.
- Antes de cada push: buscar textos del template ("Your Name", "Lorem"), claves y datos personales.
- Después de cada push: esperar el check verde en Actions y revisar el sitio a 390 px de ancho.
