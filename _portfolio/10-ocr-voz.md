---
title: "De documentos escaneados y audios peruanos a texto buscable"
excerpt: "¿Se puede volver buscable un archivo de documentos y entrevistas? WER de 0.032 en audio y CER de 0.475 en documentos.<br/><img src='/images/proyecto-ocr-voz.webp' alt='Dashboard de evaluación de OCR y transcripción'>"
collection: portfolio
order: 10
---

**Pregunta.** ¿Pueden convertirse documentos escaneados y entrevistas en audio peruanos en un archivo de texto estructurado y buscable?

**Resultado.** En audio, faster-whisper llega a un WER de 0.032. En documentos, PaddleOCR llega a un CER de 0.475 en promedio: 0.22 en fotos, 0.48 en impresos y 0.81 en manuscritos. Sirve para impresos y habla de estudio; los manuscritos coloniales y las entrevistas en la calle aún necesitan corrección humana.

**Qué hice.** Un corpus de 25 documentos y 26 clips de audio (50.5 minutos) con licencias revisadas, comparación de tres motores de OCR y dos de transcripción, seudonimización y un dashboard de búsqueda.

<img src="/images/proyecto-ocr-voz.webp" alt="Captura del dashboard" style="width:100%;max-width:900px">

*El dashboard está en Streamlit Community Cloud: si estuvo inactivo, tarda un momento en despertar.*

[Abrir el dashboard](https://av-gomez-tarea2.streamlit.app){: .btn .btn--primary} [Código en GitHub](https://github.com/av-gomez/tarea_2){: .btn}
