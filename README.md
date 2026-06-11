# AlbumMind 🏆 2026

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-darkgreen.svg)

**AlbumMind** es una aplicación de escritorio moderna desarrollada en Python para la gestión integral y el seguimiento del álbum físico Panini de la Copa del Mundo 2026. 
El proyecto traduce un objeto físico complejo en un modelo de datos digital estricto, permitiendo llevar un control exacto del inventario, visualizar el progreso mediante una interfaz gráfica responsiva y exportar automáticamente listas de intercambio.

---

## 🚀 Características Principales

* **Control de Inventario de Precisión:** Mapeo exacto de casi 1,000 registros físicos, incluyendo los 48 equipos nacionales, secciones del Museo FIFA (FWC) y los cromos promocionales de Coca-Cola.
* **Interfaz de Usuario Moderna:** Diseñada con `CustomTkinter`, ofrece una experiencia de usuario fluida con soporte nativo para modo oscuro y una arquitectura basada en vistas intercambiables.
* **Generación Automática de Reportes:** Integración con `python-docx` para exportar dinámicamente listas de figuritas repetidas o faltantes en formato Word, facilitando el intercambio con otros coleccionistas.
* **Inicialización Automatizada:** Script de despliegue (`db_init.py`) que compila la base de datos desde cero a partir de los archivos semilla.

---

## 🧠 Arquitectura de la Base de Datos

El núcleo de AlbumMind es su robusta base de datos **SQLite**. Lejos de ser una simple lista plana, el modelo relacional fue diseñado con un alto nivel de exigencia técnica:

* **Integridad Referencial Estricta:** Uso intensivo de claves foráneas (`PRAGMA foreign_keys = ON`) para conectar Páginas, Países y Figuritas.
* **Disyunción de Subtipos:** Separación lógica entre cromos de jugadores (`FJUGADOR`) y cromos de escudos/fotos de equipo (`FESPECIAL`), evitando campos nulos innecesarios y normalizando los datos.
* **Claves Compuestas:** Identificación única de cada figurita mediante la combinación matemática de su número impreso y el código ISO-3 de su país.
* **Manejo de Caracteres Internacionales:** Registro fidedigno de nombres con diacríticos especiales (alfabetos eslavos, nórdicos, árabes, etc.) para mantener un 100% de fidelidad con la edición impresa.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Base de Datos:** SQLite3
* **Interfaz Gráfica:** CustomTkinter
* **Gestión de Documentos:** python-docx
* **Empaquetado:** PyInstaller (para compilación de ejecutables `.exe`)

---

## 📦 Compilación a Ejecutable (.exe)

El repositorio incluye el archivo de configuración build.spec. Este archivo contiene la "receta" con todas las instrucciones de empaquetado optimizadas (rutas de datos, exclusión de consolas, dependencias), evitando tener que escribir comandos largos en la terminal.
Para compilar la aplicación y generar el ejecutable autónomo ejecutable en cualquier computadora:

1. **Asegúrate de tener el entorno virtual activo y las dependencias de requirements.txt instaladas.**
   ``` text
   Bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```
3. **Ejecuta el comando de compilación:**
   ``` text
   Bash
   pyinstaller albumind.spec
   ```
4. **Una vez finalizado el proceso, se habrán generado las carpetas build/ y dist/. Encontrarás el ejecutable listo para producción dentro de:**
   ``` text
   AlbumMind/dist/AlbumMind/AlbumMind.exe
   ```

---

## 📥 Descarga Directa (Para Usuarios)
Si no eres desarrollador y solo quieres usar la aplicación, no necesitas instalar Python ni descargar el código. 
Ve a la sección de **[Releases](../../releases/latest)** a la derecha de esta página y descarga el archivo ejecutable (`.exe`) más reciente.

---

## 💡 Sobre el Desarrollo
Este proyecto es una demostración clara de desarrollo de software orientado a resolver problemas reales mediante la estructuración de datos. Construir AlbumMind requirió traducir reglas de negocio no convencionales (como la distribución física y asimétrica de las hojas de un álbum) a código limpio y bases de datos relacionales.
El desarrollo de esta herramienta refleja una profunda adaptabilidad para abordar requerimientos complejos y un fuerte compromiso con el crecimiento continuo y el aprendizaje de nuevas arquitecturas dentro de la ingeniería de software.
