---
title: "Servidor MCP que conecta a Claude con las series oficiales del BCRP"
excerpt: "¿Responde mejor Claude si consulta la fuente oficial? 10 de 10 aciertos con el MCP y ninguno sin él, en una prueba con cifras recientes.<br/><img src='/images/proyecto-mcp-bcrp.webp' alt='Comparación de aciertos de Claude con y sin el MCP'>"
collection: portfolio
order: 5
---

**Pregunta.** ¿Puede un asistente de IA dar cifras económicas recientes del Perú sin inventarlas?

**Resultado.** En una prueba con 10 preguntas sobre cifras recientes, Claude Haiku acertó 10 de 10 con el MCP y ninguna sin él. El servidor da acceso a 17,167 series estadísticas del Banco Central de Reserva del Perú.

**Qué hice.** Un servidor en Python con cuatro herramientas: buscar series, descargar datos, resumir y comparar. Cada número viene con el código de la serie, el periodo y la URL del BCRP. Las cuentas las hace Python, no el modelo.

<img src="/images/proyecto-mcp-bcrp.webp" alt="Gráfico de aciertos con y sin el MCP" style="width:100%;max-width:900px">

**Otro servidor con el mismo enfoque.** [MCP del Banco Mundial](https://github.com/av-gomez/mcp-bancomundial): compara indicadores de desarrollo entre países, con la URL de la fuente en cada respuesta.

[Código en GitHub](https://github.com/av-gomez/mcp-bcrp){: .btn .btn--primary} [Informe de la prueba](https://github.com/av-gomez/mcp-bcrp/blob/master/informe.md){: .btn}
