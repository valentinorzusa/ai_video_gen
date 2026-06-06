# 🎬 AI Video Generator (English / Español)

An automated pipeline that generates full-length (up to 20 minutes) YouTube escapism documentaries from a single topic. 
*Scroll down for the Spanish version.* / *Desplázate hacia abajo para la versión en español.*

---

## 🇬🇧 English

### 1. SETUP

**Prerequisites**
- Python 3.10+
- `ffmpeg` installed and available in your system's PATH.

**Installation**
1. Clone this repository and enter the `youtube_bot` directory:
   ```bash
   git clone https://github.com/valentinorzusa/ai_video_gen.git
   cd ai_video_gen/youtube_bot
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

**Configuration**
1. **Environment Variables**: Copy the example configuration file:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and fill in your API keys (Gemini, ElevenLabs, etc.) and your RunPod ComfyUI URL.
2. **YouTube Credentials**: Place your YouTube OAuth 2.0 Client Secrets JSON file in the `youtube_bot` folder and name it `client_secret.json`.
3. **Background Music**: Place ambient `.mp3` or `.wav` files inside the `youtube_bot/music/` directory. These will be looped and played at a low volume under the voiceover.

### 2. HOW TO USE

Run the main script with the topic you want a documentary about.

**Run the full pipeline (including YouTube upload):**
```bash
python main.py "Europa's Hidden Ocean"
```

**Run the pipeline locally (skip YouTube upload):**
```bash
python main.py "The History of Rome" --no-upload
```

### 3. HOW THIS WORKS

The generation process consists of 5 sequential steps:
1. **The Writer (`01_brain.py`)**: Uses LLMs (Gemini/Anthropic) to write a script with a narrative arc and splits it into scenes. Output: `data.json`
2. **The Voice Actor (`02_voice.py`)**: Uses ElevenLabs to generate a realistic voiceover for the entire script. Output: `voiceover.mp3`
3. **The Scout (`03_vision.py`)**: Generates custom video using ComfyUI (LTXV model) and downloads stock footage using Pexels. Output: `clips/*.mp4`
4. **The Editor (`04_composer.py`)**: Uses MoviePy to stitch the voiceover, video clips, and background music together. Output: `final_render.mp4`
5. **The Distributor (`05_publisher.py`)**: Authenticates with the YouTube API and uploads the final video as a private draft.

*For deep technical details on the architecture and known issues, see [WALKTHROUGH.md](youtube_bot/WALKTHROUGH.md).*

---

## 🇪🇸 Español

### 1. CONFIGURACIÓN (SETUP)

**Requisitos previos**
- Python 3.10+
- `ffmpeg` instalado y disponible en el PATH del sistema.

**Instalación**
1. Clona este repositorio y entra en el directorio `youtube_bot`:
   ```bash
   git clone https://github.com/valentinorzusa/ai_video_gen.git
   cd ai_video_gen/youtube_bot
   ```
2. Instala los paquetes de Python requeridos:
   ```bash
   pip install -r requirements.txt
   ```

**Configuración**
1. **Variables de entorno**: Copia el archivo de configuración de ejemplo:
   ```bash
   cp .env.example .env
   ```
   Abre el archivo `.env` y completa tus claves de API (Gemini, ElevenLabs, etc.) y la URL de RunPod ComfyUI.
2. **Credenciales de YouTube**: Coloca tu archivo JSON de secretos de cliente de YouTube OAuth 2.0 en la carpeta `youtube_bot` y nómbralo `client_secret.json`.
3. **Música de fondo**: Coloca archivos `.mp3` o `.wav` ambientales dentro del directorio `youtube_bot/music/`. Estos se reproducirán en bucle a un volumen bajo detrás de la voz en off.

### 2. CÓMO USAR (HOW TO USE)

Ejecuta el script principal con el tema sobre el que deseas un documental.

**Ejecutar todo el proceso (incluyendo la subida a YouTube):**
```bash
python main.py "El océano oculto de Europa"
```

**Ejecutar el proceso localmente (omitir la subida a YouTube):**
```bash
python main.py "La Historia de Roma" --no-upload
```

### 3. CÓMO FUNCIONA (HOW THIS WORKS)

El proceso de generación consta de 5 pasos secuenciales:
1. **El Escritor (`01_brain.py`)**: Utiliza modelos de lenguaje (Gemini/Anthropic) para escribir un guion con un arco narrativo y lo divide en escenas. Salida: `data.json`
2. **El Actor de Voz (`02_voice.py`)**: Utiliza ElevenLabs para generar una voz en off realista para todo el guion. Salida: `voiceover.mp3`
3. **El Explorador (`03_vision.py`)**: Genera videos personalizados usando ComfyUI (modelo LTXV) y descarga videos de archivo usando Pexels. Salida: `clips/*.mp4`
4. **El Editor (`04_composer.py`)**: Usa MoviePy para unir la voz en off, los clips de video y la música de fondo. Salida: `final_render.mp4`
5. **El Distribuidor (`05_publisher.py`)**: Se autentica con la API de YouTube y sube el video final como un borrador privado.

*Para detalles técnicos profundos sobre la arquitectura y problemas conocidos, consulta [WALKTHROUGH.md](youtube_bot/WALKTHROUGH.md).*
