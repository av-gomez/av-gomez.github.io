# Genera el sitio estatico en docs/. Uso: python generar.py
# Para agregar un proyecto: suma un diccionario a PROYECTOS y vuelve a correr este archivo.
import html, os, shutil

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
SITE = "https://av-gomez.github.io"
NOMBRE = "Amanda Gomez Flores"
BIO = ("Estudiante de último ciclo de Economía en la PUCP y practicante de investigación en IPA Perú. "
       "Uso microdatos peruanos, econometría aplicada y evaluación de impacto para estudiar salud, desarrollo y políticas sociales.")
CV_PDF = "/files/CV_Amanda_Gomez_Flores.pdf"
CORREO = "amanda.gomez@pucp.edu.pe"
GITHUB = "https://github.com/av-gomez"
LINKEDIN = "https://www.linkedin.com/in/amanda-gomez-flores"
POST_LES = "https://lespucp.wixsite.com/laboratorio-de-estud/post/el-tiempo-que-nos-falta-pobreza-de-tiempo-g%C3%A9nero-y-el-rol-pendiente-de-las-pol%C3%ADticas-p%C3%BAblicas-en-e"

TIPOS = [
    ("datos", "Dashboards y datos", "Sitios que cualquiera puede abrir, filtrar y revisar."),
    ("ia", "IA y agentes", "Herramientas de Claude Code, modelos y texto extraído de archivos."),
    ("inv", "Investigación", "Preguntas de salud, género y brechas con microdatos."),
    ("imp", "Impacto y gestión", "Organizaciones estudiantiles, emprendimiento y rendición de cuentas."),
]

def L(texto, url):
    return f'<a href="{url}">{texto}</a>'

STREAMLIT = "Está en Streamlit Community Cloud: si estuvo inactivo, tarda un momento en despertar."

PROYECTOS = [
 dict(slug="lis-dashboard", tipo="datos", destacado=True,
  titulo="Dashboard de variables del LIS para 54 países",
  pregunta="¿En qué países y años se pueden estudiar a la vez pensiones no contributivas y gasto de bolsillo en salud?",
  num="1,060", num_label="bases auditadas en 54 países", img="lis-dashboard.webp", alt="Matriz de disponibilidad de variables del LIS",
  stats=[("118","variables auditadas"),("1,060","bases de datos"),("54","países"),("5","vistas del sitio")],
  links=[("Abrir demo","https://lis.amandavalery.workers.dev/")],
  texto=[f'Como asistente de investigación de la Dra. Isabel Guerrero (Departamento de Economía, PUCP), revisé la disponibilidad y la calidad de cada variable del {L("Luxembourg Income Study","https://www.lisdatacenter.org/")}, por ejemplo <code>hi31</code> pensión no contributiva, <code>hc6</code> gasto en salud y <code>dhi</code> ingreso disponible.',
         'El sitio tiene cinco vistas: combinaciones sugeridas, matriz de disponibilidad, cruce libre, ficha por país y diccionario. Para cualquier combinación de variables muestra en qué países y años están disponibles al mismo tiempo.'],
  demo="https://lis.amandavalery.workers.dev/", nota="Los microdatos del LIS no se redistribuyen. El sitio solo muestra metadatos de disponibilidad.",
  galeria=[("lis-combinaciones.webp","Vista de combinaciones sugeridas")]),
 dict(slug="portal-180dc", tipo="imp", destacado=True,
  titulo="Portal de transparencia financiera de 180DC PUCP",
  pregunta="¿Cómo verifica cualquier miembro en qué se gasta el dinero del grupo, sin saber programar?",
  num="6", num_label="informes mensuales que cuadran mes a mes", img="180dc-portal.webp", alt="Portada del portal de transparencia de 180DC PUCP",
  stats=[("6","informes mensuales"),("2","ciclos: 2026-1 y 2026-2"),("S/ 92.87","cierre de 2026-1 igual a la apertura de 2026-2")],
  links=[("Abrir portal","https://av-gomez.github.io/sitio_180dc/"),("Código","https://github.com/av-gomez/sitio_180dc")],
  texto=['La tesorería llena un Excel por mes y escribe en <code>config_mes.py</code> para qué fue cada gasto. <code>build.py</code> lee los Excel, calcula ingresos, egresos operativos, inversión y saldo, y genera el sitio estático. GitHub Actions lo publica en cada push.',
         'El script comprueba que el saldo final de cada mes sea el saldo inicial del siguiente. Cada mes trae su Excel descargable para revisar línea por línea. El README está escrito para personas que no programan.']),
 dict(slug="tesis-proveedor-salud", tipo="inv", destacado=True,
  titulo="Tesis: ¿a dónde acude un peruano cuando se enferma?",
  pregunta="¿Qué lleva a una persona con una necesidad de salud a elegir lo público, lo privado, la farmacia o no atenderse?",
  num="50.8 %", num_label="no busca atención", img="proyecto-tesis.webp", alt="Elección de proveedor de salud por percentil de ingreso", fit="contain",
  stats=[("50.8 %","no busca atención"),("23.2 %","va a una farmacia"),("+17.2 pp","uso del sistema público asociado al SIS"),("17,339","observaciones persona-año")],
  links=[("Leer resumen","#resumen"),("Fuente: INEI","https://www.inei.gob.pe/")],
  texto=['ENAHO Panel 2022-2024, personas de 18 a 65 años. Logit multinomial con efectos aleatorios correlacionados (enfoque de Mundlak), que separa lo que cambia en la misma persona entre años de lo que difiere entre personas.',
         'Agrego indicadores provinciales del entorno sanitario: demora para conseguir cita, tiempo de traslado, tiempo de espera y experiencia de atención. Todo en Stata y Python.',
         'Tesis de licenciatura en Economía, PUCP. Asesor: Pedro Francke. Primer puesto (1/87) en Seminario de Tesis 1.'],
  nota="Primera figura: composición de la elección por percentil de ingreso real per cápita. Elaboración propia con la ENAHO Panel 2022-2024.",
  galeria=[("tesis-aluvial.webp","Cómo cambian de proveedor las mismas personas entre 2022, 2023 y 2024. Panel balanceado.")],
  resumen=True),

 dict(slug="salud-ipress", tipo="datos",
  titulo="Dashboard: ¿dónde te atiendes si te enfermas?",
  pregunta="¿Más establecimientos de salud significan más capacidad en cada departamento?",
  num="61.8 %", num_label="de los hospitales de III nivel están en Lima y Callao", img="proyecto-ipress.webp", alt="Dashboard de la oferta de salud en el Perú",
  stats=[("61.8 %","de los hospitales de III nivel, en Lima y Callao (34 de 55)"),("35.7 %","de la población vive ahí"),("16 de 25","departamentos sin hospital de III nivel"),("20,774","establecimientos, corte a 2017")],
  links=[("Abrir demo","https://av-gomez.github.io/salud-peru-ipress/web/"),("Código","https://github.com/av-gomez/salud-peru-ipress"),("LinkedIn","https://lnkd.in/p/du6VJm3q")],
  texto=[f'Limpié el {L("registro IPRESS del MINSA","https://www.datosabiertos.gob.pe/dataset/minsa-ipress")}, lo crucé con el Censo 2017 y publiqué un dashboard con 6 indicadores y 6 visualizaciones que se recalculan con los filtros. La correlación entre densidad de establecimientos y hospitales de II y III nivel por habitante es 0.15.',
         'También hice un reel de 54 segundos narrado con mi voz clonada con IA, con el aviso visible durante todo el video.'],
  galeria=[("ipress-graficos.webp","Ranking, dispersión, composición y aperturas por año"),("ipress-reel.webp","Fotogramas del reel")],
  video="Reel: dónde te atiendes"),
 dict(slug="incendios", tipo="datos",
  titulo="Incendios forestales de octubre de 2026 vistos por satélite",
  pregunta="¿Dónde arde, es una temporada excepcional y cuánto se quemó?",
  num="8,521", num_label="focos de calor en 7 días", img="proyecto-incendios.webp", alt="Mapa de focos de calor por distrito e incendios activos", fit="contain",
  stats=[("8,521","focos en 7 días"),("645","distritos"),("+74 %","sobre la media 2012-2025"),("1,946 ha","quemadas en Curahuasi")],
  links=[("Código e informe","https://github.com/av-gomez/incendios-peru-2026")],
  texto=['Un informe con datos públicos (VIIRS, Sentinel-2, WorldPop), con corte al 21 de octubre de 2026 y sin índices compuestos: cada variable se reporta medida, por separado.',
         'También un reel de 58 segundos, con guion revisado por mí contra el informe y voz clonada con aviso visible.'],
  galeria=[("incendios-dnbr.webp","Área quemada en Curahuasi, Sentinel-2")], video="Reel: incendios forestales"),
 dict(slug="crecimiento-mineria", tipo="datos",
  titulo="Crecimiento regional y minería en el Perú, 2007 a 2019",
  pregunta="¿Qué regiones crecieron más y tuvo que ver la minería?",
  num="+298 %", num_label="VAB por habitante de Apurímac", img="proyecto-crecimiento.webp", alt="Dashboard de crecimiento regional",
  stats=[("+298 %","Apurímac, con el salto en 2016"),("10 a 61 %","peso de la minería en Apurímac"),("24","departamentos"),("13","años")],
  links=[("Abrir demo","https://grupo9-crecimiento-regional.streamlit.app/"),("Código","https://github.com/av-gomez/assignment_2_grupo_9/tree/main/assignment_3")],
  texto=['Trabajo grupal de Fundamentos de Python (Grupo 9). Dashboard en Streamlit con filtros, dispersión, mapa y tabla. Solo Madre de Dios (-23 %) y Moquegua (-3 %) retrocedieron.','Son asociaciones, no causas.'],
  nota=STREAMLIT),

 dict(slug="skills-enaho", tipo="ia",
  titulo="Tres skills que limpian la ENAHO 2024 y replican la pobreza oficial",
  pregunta="¿Puede un agente limpiar la ENAHO y llegar a la cifra del INEI?",
  num="27.58 %", num_label="de pobreza, frente a 27.6 % del INEI", img="proyecto-skills-enaho.webp", alt="Mapa de pobreza monetaria por departamento, Perú 2024", fit="contain",
  stats=[("27.58 %","pobreza obtenida"),("27.6 %","cifra oficial del INEI"),("108,664","residentes, igual que el INEI"),("3","skills encadenadas")],
  links=[("Código","https://github.com/av-gomez/skills-enaho")],
  texto=[f'Escribí tres skills de {L("Claude Code","https://claude.com/claude-code")}: <code>limpiando-enaho</code> une los módulos y valida las cifras, <code>graficando-enaho</code> hace barras por área, sexo o edad, y <code>mapeando-enaho</code> hace un mapa por departamento unido por código de ubigeo.',
         'Las skills de gráfico y mapa piden correr primero la de limpieza si falta la base.'],
  galeria=[("enaho-area.webp","Pobreza por área de residencia, generada por la skill de gráficos")]),
 dict(slug="mcp-bcrp", tipo="ia",
  titulo="Servidor MCP que conecta a Claude con las series oficiales del BCRP",
  pregunta="¿Responde mejor un asistente de IA si consulta la fuente oficial?",
  num="10 de 10", num_label="aciertos con el MCP; ninguno sin él", img="proyecto-mcp-bcrp.webp", alt="Comparación de aciertos de Claude con y sin el MCP", fit="contain",
  stats=[("10 de 10","aciertos con el MCP"),("0 de 10","aciertos sin él"),("17,167","series del BCRP"),("4","herramientas")],
  links=[("Código","https://github.com/av-gomez/mcp-bcrp"),("Informe","https://github.com/av-gomez/mcp-bcrp/blob/master/informe.md"),("MCP Banco Mundial","https://github.com/av-gomez/mcp-bancomundial")],
  texto=[f'Un servidor {L("MCP","https://modelcontextprotocol.io")} en Python para buscar series, descargar datos, resumir y comparar. Cada número viene con el código de la serie, el periodo y la URL de las {L("estadísticas del BCRP","https://estadisticas.bcrp.gob.pe/estadisticas/series/")}. Las cuentas las hace Python, no el modelo.',
         'La prueba usó 10 preguntas sobre cifras recientes con Claude Haiku. Con el mismo enfoque hice un servidor para indicadores del Banco Mundial.']),
 dict(slug="clasificador-titulares", tipo="ia",
  titulo="Clasificador de titulares de noticias peruanas con un Transformer",
  pregunta="¿Se pueden clasificar titulares sin anotación manual masiva?",
  num="0.92", num_label="F1 macro, frente a 0.72 de la línea base", img="proyecto-titulares.webp", alt="Dashboard del clasificador de titulares",
  stats=[("0.92","F1 macro en test"),("0.72","línea base zero-shot"),("400","titulares de 2 medios"),("4","categorías")],
  links=[("Abrir demo","https://clasificador-titulares-pe.streamlit.app/"),("Modelo","https://huggingface.co/av-gomez/clasificador-titulares-pe"),("Código","https://github.com/av-gomez/python-intermedio-qlab/tree/main/tarea_1")],
  texto=['Titulares de La República y El Comercio, recolectados respetando <code>robots.txt</code> y etiquetados por un LLM local. Un DistilBERT ajustado en CPU clasifica titulares nuevos en vivo en un dashboard de Streamlit.'],
  nota=STREAMLIT),
 dict(slug="ocr-voz", tipo="ia",
  titulo="De documentos escaneados y audios peruanos a texto buscable",
  pregunta="¿Se puede volver buscable un archivo de documentos y entrevistas?",
  num="0.032", num_label="de WER en audio con faster-whisper", img="proyecto-ocr-voz.webp", alt="Dashboard de evaluación de OCR y transcripción",
  stats=[("0.032","WER en audio"),("0.475","CER en documentos"),("25","documentos"),("50.5 min","de audio en 26 clips")],
  links=[("Abrir demo","https://av-gomez-tarea2.streamlit.app"),("Código","https://github.com/av-gomez/tarea_2")],
  texto=['Comparé tres motores de OCR y dos de transcripción, con licencias revisadas y seudonimización. El CER de PaddleOCR es 0.22 en fotos, 0.48 en impresos y 0.81 en manuscritos.','Sirve para impresos y habla de estudio. Los manuscritos coloniales y las entrevistas en la calle aún necesitan corrección humana.'],
  nota=STREAMLIT),

 dict(slug="servicios-basicos-censos", tipo="inv",
  titulo="Agua, desagüe y luz por distrito: Censos 2007 y 2017",
  pregunta="¿Se cerró la brecha de servicios básicos entre distritos rurales y urbanos?",
  num="44.6 a 26.1", num_label="puntos de brecha en agua; en desagüe casi no cambió", img="proyecto-censos.webp", alt="Brecha urbano rural en agua, alumbrado y desagüe", fit="contain",
  stats=[("44.6 a 26.1","brecha en agua"),("47.3 a 21.2","brecha en alumbrado"),("57.1 a 53.3","brecha en desagüe"),("1,830","distritos")],
  links=[("Ver reporte","/files/reporte_servicios_basicos.html")],
  texto=['Trabajo final grupal de Fundamentos de R (diplomatura Q-LAB PUCP), con Oscar Chávez, Fabricio Luna y Karen Macedo. Limpieza de los Censos Nacionales 2007 y 2017, indicadores por distrito y reporte reproducible en Quarto. A nivel nacional, el acceso a agua subió de 63.7 % a 78.6 %.'],
  galeria=[("censos-departamentos.webp","Acceso a servicios por departamento, 2007 y 2017")]),
 dict(slug="pobreza-de-tiempo", tipo="inv",
  titulo="Pobreza de tiempo y género en el Perú",
  pregunta="¿Cómo se reparte el trabajo no remunerado y qué falta en las políticas públicas?",
  num="4 h 48", num_label="al día en mujeres, frente a 1 h 35 en hombres", img="les-enut-grafico.webp", alt="Horas diarias por tipo de trabajo, según sexo", fit="contain", oscuro=True,
  stats=[("4 h 48 min","trabajo no remunerado, mujeres"),("1 h 35 min","trabajo no remunerado, hombres"),("2010 a 2024","periodo del estudio")],
  links=[("Leer estudio",POST_LES),("Post","https://www.instagram.com/p/DKNPkrjuEAY/"),("Reel","https://www.instagram.com/p/DKN07YyMM3v/")],
  texto=[f'Estudio de caso publicado en el {L("Laboratorio de Estudios Sociales","https://lespucp.wixsite.com/laboratorio-de-estud")}: Ybañez, M. y Gomez, A. (2025). <em>El tiempo que nos falta: Pobreza de tiempo, género y el rol pendiente de las políticas públicas en el Perú</em>. Las cifras vienen de la Encuesta Nacional de Uso del Tiempo 2024 (INEI).'],
  galeria=[("les-enut-efectos.webp","Pieza de difusión del LES sobre los efectos en las mujeres")]),
 dict(slug="elecciones-edicion-les", tipo="inv",
  titulo="Comparación de planes de gobierno y edición académica en el LES",
  pregunta="¿Lo que un candidato dice en el debate está en su plan de gobierno?",
  num="3 colores", num_label="para comparar 2 candidatos en salud y educación", img="les-semaforo.webp", alt="Explicación del semáforo: verde, amarillo y rojo", fit="contain", oscuro=False,
  stats=[("2","candidatos comparados"),("2","temas: salud y educación"),("3","colores del semáforo"),("3","columnas revisadas, aquí abajo")],
  links=[("LES en Instagram","https://www.instagram.com/les.pucp/"),("Sitio del LES","https://lespucp.wixsite.com/laboratorio-de-estud")],
  texto=['Apoyé directamente la comparación de planes de gobierno de las Elecciones 2026. El semáforo indica si la propuesta está y se explica, está pero no se explica, o no se encuentra en el plan. También apoyé la guía <em>Propuestas en verde</em> y el conversatorio <em>Nakama y nación</em>.',
         f'Como coordinadora de investigación académica reviso que los textos estén bien escritos, tengan buen contenido académico y puedan pasar por otros expertos. Algunas columnas que revisé: {L("PBI y bienestar social","https://www.instagram.com/p/DYkuoJrFgam/")}, {L("vouchers y educación pública","https://www.instagram.com/p/DOY-XBbDgQp/")} y {L("polarización y derechos humanos","https://www.instagram.com/p/DdmeCgHltEh/")}.'],
  galeria=[("les-semaforo-educacion.webp","Semáforo aplicado a educación"),("les-propuestas-verde.webp","Guía Propuestas en verde"),("les-nakama.webp","Conversatorio Nakama y nación")]),

 dict(slug="rikuy-salud", tipo="imp",
  titulo="Rikuy Salud: orientarse en el sistema de salud público",
  pregunta="¿Cómo ayudar a un paciente a saber a qué establecimiento ir?",
  num="41.8 %", num_label="de 8,946 establecimientos en Lima sin ubicación válida", img="proyecto-rikuy.webp", alt="Mapa de establecimientos de salud en Lima por institución",
  stats=[("8,946","establecimientos activos en Lima"),("41.8 %","sin ubicación válida"),("92.9 %","privados u otros"),("5","personas en el equipo")],
  links=[("Abrir mapa","/files/mapa_rikuy.html")],
  texto=[f'Sobre el {L("registro RENIPRESS","https://www.datosabiertos.gob.pe/dataset/registro-nacional-de-entidades-prestadoras-de-servicios-de-salud-renipress")} (corte al 30 de septiembre de 2026) planteamos un MVP centrado en una sola función: orientar y rutear. Lo desarrollamos en el Laboratorio de Emprendimientos 2026 de EQUIPU PUCP, un programa con más de 80 instituciones.',
         'Dejamos fuera la reserva de citas (no hay APIs públicas) y la historia clínica personal (exige cumplir la Ley 29733 de datos personales). Modelo híbrido: gratis para el usuario, ingresos por convenios con el Estado.'],
  galeria=[("rikuy-escena1.webp","Primera escena del mapa")], video="Pitch Rikuy Salud"),
 dict(slug="180dc-gestion", tipo="imp",
  titulo="Finanzas y consultoría en 180 Degrees Consulting PUCP",
  pregunta="¿Cómo consigue fondos una organización estudiantil y cómo rinde cuentas?",
  num="3 talleres", num_label="de Conexión 180, además de una rifa pro fondos", img="180dc-conexion-1.webp", alt="Afiche de un taller de Conexión 180",
  stats=[("3","talleres virtuales de Conexión 180"),("1","rifa pro fondos"),("1","ONG asesorada: Sálvame Pucallpa")],
  links=[("Conexión 180","https://www.instagram.com/p/DaGVMIxEdIf/"),("Sálvame Pucallpa","https://www.instagram.com/salvamepucallpa/"),("180DC PUCP","https://www.instagram.com/180dcpucp/")],
  texto=[f'Como directora de finanzas organicé <em>Conexión 180</em>, tres talleres virtuales del 1 al 3 de julio sobre emprendimiento, finanzas con IA y finanzas personales, además de una rifa pro fondos. También sumé el {L("portal de transparencia financiera","/proyectos/portal-180dc/")}.',
         f'Antes fui consultora de estrategia para la ONG {L("Sálvame Pucallpa","https://www.facebook.com/salvamepucallpa/")}: diagnóstico organizacional y estrategia de recaudación de fondos.'],
  galeria=[("180dc-conexion-2.webp","Taller de Conexión 180"),("180dc-conexion-3.webp","Taller de Conexión 180")]),
]

PIEZAS = [
 ("les-enut-grafico.webp","ENUT 2010 y 2024","https://www.instagram.com/p/DKNPkrjuEAY/"),
 ("les-propuestas-verde.webp","Guía Propuestas en verde","https://www.instagram.com/les.pucp/"),
 ("les-semaforo.webp","Semáforo de planes de gobierno","/proyectos/elecciones-edicion-les/"),
 ("les-nakama.webp","Conversatorio Nakama y nación","https://www.instagram.com/les.pucp/"),
 ("les-enut-efectos.webp","Efectos de la pobreza de tiempo","https://www.instagram.com/p/DKN07YyMM3v/"),
]

PUBLICACIONES = [
 ("2026","Factores asociados a la elección de proveedor de salud ante un episodio de morbilidad: evidencia a partir de la ENAHO Panel (2022-2024)","Gomez, A. Tesis de licenciatura en curso, PUCP.","/proyectos/tesis-proveedor-salud/#resumen","Leer resumen","inv"),
 ("2025","El tiempo que nos falta: Pobreza de tiempo, género y el rol pendiente de las políticas públicas en el Perú","Ybañez, M. y Gomez, A. Blog del Laboratorio de Estudios Sociales (LES), PUCP.",POST_LES,"Leer estudio","imp"),
 ("2025","Determinantes del uso de servicios de salud formales en la población adulta mayor en el Perú","Gomez, A. Documento de trabajo.",None,None,"datos"),
]

RESUMEN_TESIS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"resumen_tesis.txt"),encoding="utf-8").read().strip()

e = html.escape
BY_SLUG = {p["slug"]: p for p in PROYECTOS}
TIPO = {t[0]: t for t in TIPOS}

def link_attr(u):
    return ' target="_blank" rel="noopener"' if u.startswith("http") else ""

def pagina(ruta, titulo, cuerpo, desc=BIO, clase=""):
    full = f"{titulo} | {NOMBRE}" if titulo != NOMBRE else NOMBRE
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/images/foto.jpg">
<meta property="og:url" content="{SITE}{ruta}">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/estilos.css">
</head>
<body class="{clase}">
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="barra">
  <a class="marca" href="/"><span class="punto"></span>Amanda Gomez</a>
  <nav>
    <a href="/#proyectos">Proyectos</a>
    <a href="/publicaciones/">Publicaciones</a>
    <a href="/cv/">CV</a>
    <a class="cta" href="{CV_PDF}">PDF</a>
  </nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <div>
    <strong>{NOMBRE}</strong><br>Lima, Perú
  </div>
  <div class="pie-links">
    <a href="mailto:{CORREO}">Correo</a>
    <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
    <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    <a href="{CV_PDF}">CV en PDF</a>
  </div>
</footer>
</body>
</html>
'''

def pills(p, con_detalle=True):
    out = []
    for lab, url in p["links"]:
        u = f'/proyectos/{p["slug"]}/{url}' if url.startswith("#") else url
        out.append(f'<a class="pill pill-fuerte" href="{u}"{link_attr(u)}>{e(lab)} <span aria-hidden="true">↗</span></a>')
    if con_detalle:
        out.append(f'<a class="pill" href="/proyectos/{p["slug"]}/">Ver detalle</a>')
    return "".join(out)

def tarjeta(p, grande=False):
    t = TIPO[p["tipo"]]
    fit = " ajustar" if p.get("fit") == "contain" else ""
    osc = " oscuro" if p.get("oscuro") else ""
    return f'''<article class="caja tipo-{p["tipo"]}{' grande' if grande else ''}">
  <a class="caja-img{fit}{osc}" href="/proyectos/{p["slug"]}/" aria-label="{e(p["titulo"])}">
    <img src="/images/{p["img"]}" alt="{e(p["alt"])}" loading="lazy">
  </a>
  <div class="caja-cuerpo">
    <span class="etiqueta">{e(t[1])}</span>
    <div class="cifra"><b>{e(p["num"])}</b><span>{e(p["num_label"])}</span></div>
    <h3><a href="/proyectos/{p["slug"]}/">{e(p["titulo"])}</a></h3>
    <p>{e(p["pregunta"])}</p>
    <div class="pills">{pills(p)}</div>
  </div>
</article>'''

def inicio():
    dest = [p for p in PROYECTOS if p.get("destacado")]
    chips = "".join(f'<a class="chip tipo-{k}" href="#{k}">{e(n)} <small>{sum(p["tipo"]==k for p in PROYECTOS)}</small></a>' for k, n, _ in TIPOS)
    secciones = ""
    for k, n, d in TIPOS:
        resto = [p for p in PROYECTOS if p["tipo"] == k and not p.get("destacado")]
        top = [p for p in PROYECTOS if p["tipo"] == k and p.get("destacado")]
        aviso = f'<p class="tambien">Destacado de este tipo: <a href="/proyectos/{top[0]["slug"]}/">{e(top[0]["titulo"])}</a></p>' if top else ""
        secciones += f'''<section class="tipo-seccion tipo-{k}" id="{k}">
  <div class="tipo-cabeza"><h2>{e(n)}</h2><p>{e(d)}</p>{aviso}</div>
  <div class="rejilla">{"".join(tarjeta(p) for p in resto)}</div>
</section>'''
    piezas = "".join(f'<a class="pieza" href="{u}"{link_attr(u)}><img src="/images/{i}" alt="{e(a)}" loading="lazy"><span>{e(a)}</span></a>' for i, a, u in PIEZAS)
    c = f'''<section class="hero">
  <div class="hero-texto">
    <p class="sobre">Economía · Datos · Salud y desarrollo</p>
    <h1>Amanda<br>Gomez <em>Flores</em></h1>
    <p class="bio">{e(BIO)}</p>
    <div class="botones">
      <a class="boton amarillo" href="{CV_PDF}">Descargar CV</a>
      <a class="boton" href="#proyectos">Ver proyectos</a>
      <a class="boton linea" href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
      <a class="boton linea" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="boton linea" href="mailto:{CORREO}">Correo</a>
    </div>
  </div>
  <div class="hero-foto">
    <div class="sol"></div>
    <img src="/images/foto-recorte.webp" alt="Foto de Amanda Gomez Flores">
    <a class="flota f1 tipo-datos" href="/proyectos/lis-dashboard/"><b>54</b> países en un dashboard</a>
    <a class="flota f2 tipo-ia" href="/proyectos/mcp-bcrp/"><b>10/10</b> aciertos con mi MCP</a>
    <a class="flota f3 tipo-inv" href="/proyectos/tesis-proveedor-salud/"><b>1/87</b> Seminario de Tesis 1</a>
  </div>
</section>
<section class="cintas">
  <a class="cinta tipo-datos" href="/proyectos/lis-dashboard/"><b>1,060</b>bases auditadas</a>
  <a class="cinta tipo-inv" href="/proyectos/tesis-proveedor-salud/"><b>17,339</b>observaciones en mi tesis</a>
  <a class="cinta tipo-ia" href="/proyectos/skills-enaho/"><b>27.58 %</b>pobreza replicada de la ENAHO</a>
  <a class="cinta tipo-imp" href="/proyectos/portal-180dc/"><b>6</b>informes financieros públicos</a>
</section>
<section class="destacados" id="proyectos">
  <div class="titular"><h2>Mis tres mejores proyectos</h2><p>Abre la demo, mira el código o entra al detalle.</p></div>
  <div class="bento">{tarjeta(dest[0], True)}{tarjeta(dest[1])}{tarjeta(dest[2])}</div>
</section>
<section class="filtro">
  <h2>Todos los proyectos, por tipo</h2>
  <div class="chips">{chips}</div>
</section>
{secciones}
<section class="piezas">
  <div class="titular claro"><h2>Investigación convertida en piezas para todos</h2><p>Parte de lo que coordiné y apoyé en el <a href="https://lespucp.wixsite.com/laboratorio-de-estud" target="_blank" rel="noopener">Laboratorio de Estudios Sociales</a>.</p></div>
  <div class="carrusel">{piezas}</div>
</section>
<section class="ruta">
  <div class="titular"><h2>Dónde he trabajado</h2><p><a href="/cv/">Ver el CV completo</a></p></div>
  <div class="ruta-cajas">
    <a class="paso tipo-ia" href="https://www.poverty-action.org/peru" target="_blank" rel="noopener"><small>ago. 2026 - presente</small><b>IPA Perú</b>Practicante de investigación</a>
    <a class="paso tipo-datos" href="/proyectos/lis-dashboard/"><small>mar. - ago. 2026</small><b>Departamento de Economía, PUCP</b>Asistente de investigación</a>
    <a class="paso tipo-inv" href="/proyectos/pobreza-de-tiempo/"><small>mar. 2025 - presente</small><b>Laboratorio de Estudios Sociales</b>Coordinadora de investigación académica</a>
    <a class="paso tipo-imp" href="/proyectos/180dc-gestion/"><small>ago. 2025 - presente</small><b>180 Degrees Consulting PUCP</b>Consultora y directora de finanzas</a>
  </div>
  <div class="herramientas">{"".join(f"<span>{h}</span>" for h in ["Stata","R y Quarto","Python","SQL","SurveyCTO","LaTeX","GitHub Actions","Claude Code"])}</div>
</section>'''
    return pagina("/", NOMBRE, c, clase="portada")

def proyecto(p, i):
    t = TIPO[p["tipo"]]
    stats = "".join(f'<div class="stat"><b>{e(n)}</b><span>{e(l)}</span></div>' for n, l in p["stats"])
    txt = "".join(f"<p>{x}</p>" for x in p["texto"])
    fit = " ajustar" if p.get("fit") == "contain" else ""
    osc = " oscuro" if p.get("oscuro") else ""
    demo = ""
    if p.get("demo"):
        demo = f'''<section class="demo"><h2>Pruébalo aquí</h2><iframe src="{p["demo"]}" title="{e(p["titulo"])}" loading="lazy"></iframe></section>'''
    gal = ""
    if p.get("galeria"):
        gal = '<section class="galeria">' + "".join(f'<figure><a href="/images/{a}"><img src="/images/{a}" alt="{e(b)}" loading="lazy"></a><figcaption>{e(b)}</figcaption></figure>' for a, b in p["galeria"]) + "</section>"
    resumen = f'<section class="resumen" id="resumen"><h2>Resumen de la tesis</h2><p>{e(RESUMEN_TESIS)}</p></section>' if p.get("resumen") else ""
    nota = f'<p class="nota">{e(p["nota"])}</p>' if p.get("nota") else ""
    video = ""
    if p.get("video"):
        video = f'\n<!-- Cuando el video esté en YouTube como no listado, pega aquí:\n<iframe width="100%" height="400" src="https://www.youtube.com/embed/ID_DEL_VIDEO" title="{e(p["video"])}" allowfullscreen></iframe>\n-->\n'
    ant = PROYECTOS[i-1]; sig = PROYECTOS[(i+1) % len(PROYECTOS)]
    c = f'''<div class="tipo-{p["tipo"]}">
<section class="pcabeza">
  <a class="volver" href="/#{p["tipo"]}">← {e(t[1])}</a>
  <h1>{e(p["titulo"])}</h1>
  <p class="ppregunta">{e(p["pregunta"])}</p>
  <div class="pills">{pills(p, False)}</div>
</section>
<section class="stats">{stats}</section>
<div class="pcuerpo">
  <a class="pimg{fit}{osc}" href="/images/{p["img"]}"><img src="/images/{p["img"]}" alt="{e(p["alt"])}"></a>
  <div class="ptexto"><h2>Qué hice</h2>{txt}{nota}</div>
</div>
{demo}{video}{gal}{resumen}
<nav class="vecinos">
  <a href="/proyectos/{ant["slug"]}/"><small>Anterior</small>{e(ant["titulo"])}</a>
  <a href="/proyectos/{sig["slug"]}/"><small>Siguiente</small>{e(sig["titulo"])}</a>
</nav>
</div>'''
    return pagina(f'/proyectos/{p["slug"]}/', p["titulo"], c, desc=p["pregunta"])

def publicaciones():
    items = ""
    for anio, tit, cita, url, lab, tp in PUBLICACIONES:
        b = f'<div class="pills"><a class="pill pill-fuerte" href="{url}"{link_attr(url)}>{lab} <span aria-hidden="true">↗</span></a></div>' if url else ""
        items += f'<article class="pub tipo-{tp}"><span class="anio">{anio}</span><div><h2>{e(tit)}</h2><p>{e(cita)}</p>{b}</div></article>'
    c = f'<section class="interior tipo-inv"><h1>Publicaciones</h1><p class="ppregunta">Tesis, estudios de caso y documentos de trabajo.</p></section><section class="pubs">{items}</section>'
    return pagina("/publicaciones/", "Publicaciones", c)

def bloque(titulo, tipo, entradas):
    filas = ""
    for cab, sub, items in entradas:
        li = "".join(f"<li>{x}</li>" for x in items)
        filas += f'<div class="entrada"><h3>{cab}</h3><p class="sub">{sub}</p>{"<ul>"+li+"</ul>" if li else ""}</div>'
    return f'<section class="cv-bloque tipo-{tipo}"><h2>{titulo}</h2>{filas}</section>'

def cv():
    PJ = "/proyectos/"
    c = f'''<section class="interior tipo-datos"><h1>CV</h1><p class="ppregunta">{e(BIO)}</p><div class="pills"><a class="pill pill-fuerte" href="{CV_PDF}">Descargar PDF <span aria-hidden="true">↗</span></a></div></section>
<div class="cv">''' + bloque("Experiencia en investigación","ia",[
  (L("Innovations for Poverty Action (IPA) Perú","https://www.poverty-action.org/peru"),"Practicante de Investigación · ago. 2026 - presente",[
    "Apoyo en una evaluación de impacto (RCT) sobre capital semilla para microemprendimientos: actualización de reportes en LaTeX para los investigadores principales y control de referencias de tablas.",
    "Desarrollo de proyectos: fortalecimiento de la matriz de emparejamiento entre ideas de investigación y fondos, y notas conceptuales para donantes.",
    "Apoyo en un piloto cualitativo con gobiernos locales (entrevistas semiestructuradas y notas de campo)."]),
  ("Departamento de Economía, PUCP",f'Asistente de Investigación, Profs. Isabel Guerrero y {L("Fabiola Alba-Vivar","https://fabiolaalbavivar.com/")} · mar. 2026 - ago. 2026',[
    L("Auditoría de 118 variables del Luxembourg Income Study",PJ+"lis-dashboard/")+" en 1,060 bases de 54 países para un estudio sobre pensiones no contributivas y gasto de bolsillo en salud; dashboard web de disponibilidad de variables.",
    "Análisis de datos de movilidad urbana, educación y bienestar con econometría y geolocalización en Python.",
    "Revisión sistemática de literatura y análisis mixto para diagnósticos económicos."]),
  ("PUCP","Asistente de Investigación, Prof. Pedro Francke · dic. 2025 - mar. 2026",["Procesamiento de microdatos censales en Stata y modelos econométricos sobre maternidad infantil e interseccionalidad."]),
  ("PUCP","Asistente de Investigación · ago. 2025 - nov. 2025",["Revisión de literatura y marco teórico sobre liderazgo político femenino y violencia contra la mujer."]),
 ]) + bloque("Educación","datos",[
  (L("Pontificia Universidad Católica del Perú (PUCP)","https://www.pucp.edu.pe/"),"Bachillerato en Economía · 2021 - presente (último ciclo, 2026-2; término de cursos previsto: dic. 2026)",[
    "Cursos relevantes: Microeconometría Intermedia, Economía Pública, Pobreza, Desigualdad y Políticas Sociales, Finanzas Corporativas, Regulación Financiera, Temas de Desarrollo Económico, Temas en Políticas Públicas y Gestión Pública.",
    L("Tesis",PJ+"tesis-proveedor-salud/")+': "Factores asociados a la elección de proveedor de salud ante un episodio de morbilidad: evidencia a partir de la ENAHO Panel (2022-2024)". Asesor: Pedro Francke.']),
  (L("Q-LAB PUCP","https://qlab.pucp.edu.pe/"),"Diplomatura de Especialización en Ciencia de Datos para las Ciencias Sociales y Gestión Pública · ago. 2026 - abr. 2027 (en curso)",["Cursos: Fundamentos de Python, Fundamentos de R, Estadística para Ciencia de Datos, Matemática para Ciencia de Datos, entre otros."]),
  ("Q-LAB PUCP, Summer School de Métodos Cuantitativos","ene. - feb. 2025",[
    "Econometría Aplicada Avanzada (32 h; Rubin, DiD, IV, control sintético, RDD). Nota 16.","Introducción a Machine Learning para CCSS y Gestión Pública (32 h). Nota 16.","Machine Learning para Macroeconomía (32 h; series de tiempo, deep learning). Nota 16.","Fundamentos de Programación en Python (16 h). Nota 18."]),
 ]) + bloque("Consultoría, emprendimiento y liderazgo","imp",[
  (L("180 Degrees Consulting PUCP",PJ+"180dc-gestion/"),"Consultora y directora de finanzas · ago. 2025 - presente",[
    "Consultora de estrategia del proyecto "+L("Sálvame Pucallpa","https://www.instagram.com/salvamepucallpa/")+" (ciclo 2025-2): diagnóstico organizacional y estrategia de recaudación de fondos para una ONG.",
    "Directora de finanzas: organización de una rifa pro fondos y de los talleres "+L("Conexión 180","https://www.instagram.com/p/DaGVMIxEdIf/")+".",
    "Desarrollo del "+L("Portal de Transparencia Financiera",PJ+"portal-180dc/")+" del grupo (Python, GitHub Actions)."]),
  (L("Laboratorio de Estudios Sociales (LES), PUCP",PJ+"elecciones-edicion-les/"),"Coordinadora de Investigación Académica · mar. 2025 - presente",["Líneas de investigación sobre "+L("pobreza de tiempo y género",PJ+"pobreza-de-tiempo/")+"; supervisión de publicaciones estudiantiles; traducción de resultados técnicos a notas de política."]),
  ("ID-One","Responsable de Finanzas y Modelo de Negocio · 2026 - presente",["Startup B2B de verificación de identidad digital; costos unitarios por verificación y modelo de negocio. Programa de incubación NEXPRO 2026-2 (NEXUM, CIDE PUCP)."]),
  (L("Rikuy Salud",PJ+"rikuy-salud/"),"Cofundadora · 2026",["Idea de app para orientar a pacientes en el sistema de salud público peruano (datos abiertos de RENIPRESS y SUSALUD). Laboratorio de Emprendimientos 2026, EQUIPU PUCP. Equipo de cinco personas."]),
 ]) + bloque("Reconocimientos","inv",[("Premios y puestos","",[
    "2025 · Primer puesto (1/87), Seminario de Tesis 1, PUCP. Nota 18.","2025 · Primer puesto (1/44), Laboratorio de Programación: R y Python, PUCP. Nota 18.",
    "2025 · Finalista global (top 14), Project Green Challenge, "+L("Turning Green","https://turninggreen.org/")+".","2024 · Primer puesto (1/14), Laboratorio de Escritura Académica, PUCP. Nota 17.",
    '2024 · Participante, "Menos barreras, más competencia", INDECOPI.',"2024 · Editatón 2024-2 (Wikipedia, PUCP): mejora de contenidos de economía de género."])
 ]) + bloque("Voluntariado y trabajo de campo","datos",[("Campo y comunidad","",[
    "Dirección de Responsabilidad Social y Desarrollo Sostenible, PUCP. Levantamiento de datos socioeconómicos y de riesgo de desastres en el torrente de Quirio. ago. - nov. 2025 (15 h de campo).",
    "Universitarios sin Fronteras. Encuestadora y asistente de campo, 2024. Programación del instrumento en ODK/SurveyCTO, aleatorización espacial y chequeos de consistencia.",
    "RSU PUCP. Facilitadora de alfabetización digital para adultos mayores, 2024.",
    "Asociación de Estudiantes de Economía (AEE) PUCP. Organización de eventos y talleres; talleres de economía para escolares, 2022 - 2024."])
 ]) + bloque("Cursos y habilidades","ia",[("Cursos y certificados","",[
    "Excel Avanzado: Macros, INFOPUCP, feb. 2025, 24 h, nota 20.","Taller de Programación en Economía Experimental, LEEX-PUCP, E2LabUP y CREE-UDEP, feb. - mar. 2025, 25 h.","Taller de Programación en Stata aplicado a CCSS, Q-LAB PUCP, 2025-1, 10 h."]),
   ("Habilidades","",[
    "Datos: Stata (avanzado), R (tidyverse, Quarto), Python (pandas, NumPy), SQL, Excel/VBA.","Métodos: RCT, DiD, IV, RDD, control sintético, logit multinomial con panel (Mundlak), ML supervisado y no supervisado, series de tiempo.",
    "Campo: SurveyCTO, ODK, KoBoToolbox, controles de calidad (HFC, back checks).","Reporte: LaTeX/Overleaf, Quarto, GitHub Actions, Claude Code con skills y MCP.","Idiomas: español nativo; inglés intermedio."])
 ]) + "</div>"
    return pagina("/cv/", "CV", c)

def escribir(ruta, contenido):
    p = os.path.join(DOCS, ruta.strip("/"), "index.html") if not ruta.endswith(".html") else os.path.join(DOCS, ruta.strip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)

if os.path.isdir(os.path.join(DOCS, "proyectos")):
    shutil.rmtree(os.path.join(DOCS, "proyectos"))
escribir("/", inicio())
for i, p in enumerate(PROYECTOS):
    escribir(f'/proyectos/{p["slug"]}/', proyecto(p, i))
escribir("/publicaciones/", publicaciones())
escribir("/cv/", cv())
escribir("/404.html", pagina("/404.html", "Página no encontrada", '<section class="interior tipo-inv"><h1>Esta página no existe</h1><div class="pills"><a class="pill pill-fuerte" href="/">Volver al inicio</a></div></section>'))
open(os.path.join(DOCS, ".nojekyll"), "w").close()
print("Sitio generado en", DOCS, "con", len(PROYECTOS), "proyectos")
