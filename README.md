# mshzbeats CLI (Esreal Edition)

[![Python 3](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Esreal Music](https://img.shields.io/badge/Esreal-Music-purple.svg)](https://github.com/esreal)

Calculadora de tempos y frecuencias creada por **Esreal Music**  
para productores de *psytech, deep techno y Zenon style*.

---

## 🇪🇸 Español

### 🧠 Descripción

`mshzbeats` es un programa de línea de comandos (CLI) que convierte un **BPM** en
valores musicales listos para usar en **delays, reverbs, compresores, LFOs y modulaciones**.
Incluye presets de swing, compresión tempo-sync y tiempos de modulación de la
plantilla **Esreal Zenon Template** (Squelch / Atmos).

### 🚀 Uso

```bash
mshzbeats <BPM> [--sr 48000] [--swing 57] [--signature 4/4]
```

**Ejemplos:**
```bash
mshzbeats 130
mshzbeats 128 --sr 44100 --swing 57
mshzbeats 140 --signature 3/4 --swing 60
```

### 🧩 Secciones de salida

- **Figuras rectas**: 1/1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64
- **Con puntillo**: todas las figuras con factor ×1.5
- **En tresillo**: todas las figuras con factor ×(2/3)
- **Swing en corcheas**: comparación entre recto (50%) y swing personalizado
- **Atajos útiles**: presets de delay (slap, corto, clásico, ping-pong, eco, dub)
- **Predelays / Gates**: valores estándar (10, 20, 30, 40, 60, 90, 120 ms)
- **Compresión tempo-sync**: guía de ataque/release sincronizados
- **Bloque Esreal Squelch**: modulaciones para filtros y granulado
- **Bloque Esreal Atmos**: modulaciones para texturas ambientales
- **Resumen final**: compás completo y valores base

### ⚙️ Instalación

```bash
# Hacer ejecutable
chmod +x mshzbeats.py

# Instalar globalmente (opcional)
sudo mv mshzbeats.py /usr/local/bin/mshzbeats
```

### 💡 Ejemplo de salida

```
─────────────────── mshzbeats • BPM=130 • SR=48000 • Compás 4/4 ────────────────────

[Figuras rectas]
Figura        ms       Hz(rate)   muestras
-------------------------------------------
1/1           1846.15  0.542      88523
1/2           923.08   1.083      44261
1/4           461.54   2.168      22154
1/8           230.77   4.333      11077
1/16          115.38   8.667      5538
1/32          57.692   17.333     2769
1/64          28.846   34.667     1384

[Bloque Esreal Squelch]
Parámetro          ms       Hz(rate)   muestras
------------------------------------------------
LFO Rate 1 (1/8)   230.77   4.333      11077
LFO Rate 2 (3/16)  346.15   2.889      16615
Grain Mod (1/32)   57.692   17.333     2769
FM Sweep (1/4)     461.54   2.168      22154

─────────────────────── Resumen ───────────────────────
1 compás 4/4 = 1846.15 ms  •  1 negra = 461.54 ms  •  1 Hz = 1000 ms
```

---

## 🇺🇸 English

### 🧠 Description

`mshzbeats` is a command-line interface (CLI) that converts **BPM** into
musical values ready to use in **delays, reverbs, compressors, LFOs and modulations**.
Includes swing presets, tempo-sync compression and modulation timings from the
**Esreal Zenon Template** (Squelch / Atmos).

### 🚀 Usage

```bash
mshzbeats <BPM> [--sr 48000] [--swing 57] [--signature 4/4]
```

**Examples:**
```bash
mshzbeats 130
mshzbeats 128 --sr 44100 --swing 57
mshzbeats 140 --signature 3/4 --swing 60
```

### 🧩 Output sections

- **Straight figures**: 1/1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64 notes
- **Dotted**: all figures with ×1.5 factor
- **Triplets**: all figures with ×(2/3) factor
- **Swing on eighths**: comparison between straight (50%) and custom swing
- **Useful shortcuts**: delay presets (slap, short, classic, ping-pong, echo, dub)
- **Predelays / Gates**: standard values (10, 20, 30, 40, 60, 90, 120 ms)
- **Tempo-sync compression**: attack/release synchronized guide
- **Esreal Squelch Block**: modulations for filters and granular
- **Esreal Atmos Block**: modulations for ambient textures
- **Final summary**: complete measure and base values

### ⚙️ Installation

```bash
# Make executable
chmod +x mshzbeats.py

# Install globally (optional)
sudo mv mshzbeats.py /usr/local/bin/mshzbeats
```

### 💡 Example output

```
─────────────────── mshzbeats • BPM=130 • SR=48000 • Compás 4/4 ────────────────────

[Figuras rectas]
Figura        ms       Hz(rate)   muestras
-------------------------------------------
1/1           1846.15  0.542      88523
1/2           923.08   1.083      44261
1/4           461.54   2.168      22154
1/8           230.77   4.333      11077
1/16          115.38   8.667      5538
1/32          57.692   17.333     2769
1/64          28.846   34.667     1384

[Bloque Esreal Squelch]
Parámetro          ms       Hz(rate)   muestras
------------------------------------------------
LFO Rate 1 (1/8)   230.77   4.333      11077
LFO Rate 2 (3/16)  346.15   2.889      16615
Grain Mod (1/32)   57.692   17.333     2769
FM Sweep (1/4)     461.54   2.168      22154

─────────────────────── Resumen ───────────────────────
1 compás 4/4 = 1846.15 ms  •  1 negra = 461.54 ms  •  1 Hz = 1000 ms
```

---

## 🎛️ Features

- ✅ **Zero dependencies** - Pure Python 3 standard library
- ✅ **Cross-platform** - macOS, Linux, Windows (PowerShell compatible)
- ✅ **Musical accuracy** - Precise BPM-to-ms calculations
- ✅ **Esreal presets** - Custom modulation timings from Zenon Template
- ✅ **Clean output** - ASCII tables, no colors, terminal-friendly
- ✅ **Flexible parameters** - Customizable sample rate, swing, time signature

## 🎵 Musical Calculations

- **Base quarter note**: `60000 / BPM` ms
- **Dotted notes**: `×1.5`
- **Triplets**: `×(2/3)`
- **Samples**: `ms × SR / 1000`
- **Swing**: Maintains total duration between eighth note pairs

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Credits

**Israel Umaña Sedó** / **Esreal Music**  
*Psytech, Deep Techno & Zenon Style Producer*

---

*Desarrollado para la comunidad de productores de música electrónica experimental.*  
*Developed for the experimental electronic music producer community.*
