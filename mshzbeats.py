#!/usr/bin/env python3
"""
mshzbeats CLI (Esreal Edition) - Versión Extendida Ableton/Digital
Calculadora de tempos y frecuencias para productores de psytech, deep techno y Zenon style.
Incluye todas las divisiones rítmicas estándar (1/128 hasta 8 barras) compatibles con DAWs modernos.
Creado por Israel Umaña Sedó / Esreal Music
"""

import argparse
import sys
import math

def format_number(value, is_ms=True):
    """Format numbers with appropriate decimal places"""
    if is_ms and value < 100:
        return f"{value:.3f}"
    elif is_ms and value >= 100:
        return f"{value:.2f}"
    else:
        return f"{value:.2f}"

def calculate_musical_values(bpm, sample_rate=48000):
    """Calculate all musical timing values for given BPM"""
    # Base quarter note in milliseconds
    quarter_note_ms = 60000 / bpm
    
    # Musical note divisions - Extended Ableton/Digital Version
    note_divisions = {
        "8B": 32,          # 8 bars (4/4)
        "4B": 16,          # 4 bars (4/4)
        "2B": 8,           # 2 bars (4/4)
        "2/1": 8,          # double whole note (breve)
        "1/1": 4,          # whole note
        "1/2": 2,          # half note
        "1/4": 1,          # quarter note
        "1/8": 0.5,        # eighth note
        "1/16": 0.25,      # sixteenth note
        "1/32": 0.125,     # thirty-second note
        "1/64": 0.0625,    # sixty-fourth note
        "1/128": 0.03125   # hundred-twenty-eighth note
    }
    
    # Calculate values for each note division
    values = {}
    for note_name, division in note_divisions.items():
        ms = quarter_note_ms * division
        hz = 1000 / ms if ms > 0 else 0
        samples = ms * sample_rate / 1000
        
        values[note_name] = {
            'ms': ms,
            'hz': hz,
            'samples': int(round(samples))
        }
    
    return values, quarter_note_ms

def calculate_dotted_values(base_values):
    """Calculate dotted note values (×1.5) - excludes bar-based divisions"""
    dotted = {}
    for note_name, values in base_values.items():
        # Skip bar-based divisions (2B, 4B, 8B) for dotted notes
        if note_name in ['2B', '4B', '8B']:
            continue
        dotted[note_name] = {
            'ms': values['ms'] * 1.5,
            'hz': values['hz'] / 1.5,
            'samples': int(round(values['samples'] * 1.5))
        }
    return dotted

def calculate_triplet_values(base_values):
    """Calculate triplet note values (×2/3) - excludes bar-based divisions"""
    triplets = {}
    for note_name, values in base_values.items():
        # Skip bar-based divisions (2B, 4B, 8B) for triplets
        if note_name in ['2B', '4B', '8B']:
            continue
        triplets[note_name] = {
            'ms': values['ms'] * (2/3),
            'hz': values['hz'] / (2/3),
            'samples': int(round(values['samples'] * (2/3)))
        }
    return triplets

def calculate_swing_values(quarter_note_ms, swing_percent):
    """Calculate swing values for eighth notes"""
    eighth_note_ms = quarter_note_ms * 0.5
    
    # Swing calculation: maintain total duration
    # First note gets longer, second note gets shorter
    swing_factor = swing_percent / 50.0  # 50% = straight, 100% = maximum swing
    swing_factor = min(swing_factor, 1.8)  # Cap at reasonable maximum
    
    first_note_ms = eighth_note_ms * swing_factor
    second_note_ms = (eighth_note_ms * 2) - first_note_ms
    
    return {
        'straight': eighth_note_ms,
        'first_note': first_note_ms,
        'second_note': second_note_ms,
        'swing_percent': swing_percent
    }

def print_header(bpm, sample_rate, signature, swing):
    """Print the main header"""
    width = 80
    title = f"mshzbeats • BPM={bpm} • SR={sample_rate} • Compás {signature}"
    if swing != 50:
        title += f" • Swing {swing}%"
    
    print("─" * width)
    print(f"{title:^{width}}")
    print("─" * width)

def print_section(title, values, sample_rate):
    """Print a section with musical values"""
    print(f"\n[{title}]")
    
    # Add special subtitle for straight figures
    if title == "Figuras rectas":
        print("──────────────── Divisiones estándar (analógicas / DAW) ────────────────")
    
    print(f"{'Figura':<15} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 50)
    
    for note_name, data in values.items():
        ms_str = format_number(data['ms'])
        hz_str = format_number(data['hz'], False)
        print(f"{note_name:<15} {ms_str:<10} {hz_str:<10} {data['samples']:<10}")

def print_swing_section(swing_data, sample_rate):
    """Print swing section"""
    print(f"\n[Swing en corcheas - {swing_data['swing_percent']}%]")
    print(f"{'Tipo':<20} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 55)
    
    # Straight reference
    straight_hz = 1000 / swing_data['straight']
    straight_samples = int(swing_data['straight'] * sample_rate / 1000)
    print(f"{'Recto (50%)':<20} {format_number(swing_data['straight']):<10} {format_number(straight_hz, False):<10} {straight_samples:<10}")
    
    # Swing values
    first_hz = 1000 / swing_data['first_note']
    first_samples = int(swing_data['first_note'] * sample_rate / 1000)
    second_hz = 1000 / swing_data['second_note']
    second_samples = int(swing_data['second_note'] * sample_rate / 1000)
    
    print(f"{'Corchea larga':<20} {format_number(swing_data['first_note']):<10} {format_number(first_hz, False):<10} {first_samples:<10}")
    print(f"{'Corchea corta':<20} {format_number(swing_data['second_note']):<10} {format_number(second_hz, False):<10} {second_samples:<10}")

def print_delay_presets(base_values, sample_rate):
    """Print delay presets"""
    print(f"\n[Atajos útiles - Delays]")
    print(f"{'Preset':<20} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 55)
    
    presets = {
        'Delay slap (1/32)': base_values['1/32'],
        'Delay corto (1/16)': base_values['1/16'],
        'Delay clásico (1/8)': base_values['1/8'],
        'Ping-pong (3/16)': {
            'ms': base_values['1/8']['ms'] * 1.5,
            'hz': base_values['1/8']['hz'] / 1.5,
            'samples': int(base_values['1/8']['samples'] * 1.5)
        },
        'Eco (1/4)': base_values['1/4'],
        'Dub largo (1/2)': base_values['1/2']
    }
    
    for preset_name, data in presets.items():
        ms_str = format_number(data['ms'])
        hz_str = format_number(data['hz'], False)
        print(f"{preset_name:<20} {ms_str:<10} {hz_str:<10} {data['samples']:<10}")

def print_predelays(sample_rate):
    """Print predelay/gate values"""
    print(f"\n[Predelays / Gates]")
    print(f"{'Tiempo':<15} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 50)
    
    predelays = [10, 20, 30, 40, 60, 90, 120]
    for ms in predelays:
        hz = 1000 / ms
        samples = int(ms * sample_rate / 1000)
        print(f"{ms} ms{'':<8} {format_number(ms):<10} {format_number(hz, False):<10} {samples:<10}")

def print_compression_guide(base_values, sample_rate):
    """Print compression tempo-sync guide"""
    print(f"\n[Compresión tempo-sync]")
    print(f"{'Parámetro':<25} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 60)
    
    compression = {
        'Ataque rápido (~1/64)': base_values['1/64'],
        'Ataque medio (~1/32)': base_values['1/32'],
        'Release corto (~1/8)': base_values['1/8'],
        'Release musical (~1/4)': base_values['1/4']
    }
    
    for param_name, data in compression.items():
        ms_str = format_number(data['ms'])
        hz_str = format_number(data['hz'], False)
        print(f"{param_name:<25} {ms_str:<10} {hz_str:<10} {data['samples']:<10}")

def print_esreal_blocks(base_values, sample_rate):
    """Print Esreal Template modulation blocks"""
    # Squelch block
    print(f"\n[Bloque Esreal Squelch]")
    print(f"{'Parámetro':<25} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 60)
    
    squelch = {
        'LFO Rate 1 (1/8)': base_values['1/8'],
        'LFO Rate 2 (3/16)': {
            'ms': base_values['1/8']['ms'] * 1.5,
            'hz': base_values['1/8']['hz'] / 1.5,
            'samples': int(base_values['1/8']['samples'] * 1.5)
        },
        'Grain Mod (1/32)': base_values['1/32'],
        'FM Sweep (1/4)': base_values['1/4']
    }
    
    for param_name, data in squelch.items():
        ms_str = format_number(data['ms'])
        hz_str = format_number(data['hz'], False)
        print(f"{param_name:<25} {ms_str:<10} {hz_str:<10} {data['samples']:<10}")
    
    # Atmos block
    print(f"\n[Bloque Esreal Atmos]")
    print(f"{'Parámetro':<25} {'ms':<10} {'Hz(rate)':<10} {'muestras':<10}")
    print("─" * 60)
    
    # Calculate 1/8T (eighth note triplet)
    eighth_triplet = {
        'ms': base_values['1/8']['ms'] * (2/3),
        'hz': base_values['1/8']['hz'] / (2/3),
        'samples': int(base_values['1/8']['samples'] * (2/3))
    }
    
    # Calculate 2B (2 bars = 8 quarter notes)
    two_bars = {
        'ms': base_values['1/4']['ms'] * 8,
        'hz': base_values['1/4']['hz'] / 8,
        'samples': base_values['1/4']['samples'] * 8
    }
    
    atmos = {
        'Grain Cloud Speed (1/16)': base_values['1/16'],
        'Random LFO (1/8T)': eighth_triplet,
        'Filter Drift (1/2)': base_values['1/2'],
        'Pan Motion (2B)': two_bars
    }
    
    for param_name, data in atmos.items():
        ms_str = format_number(data['ms'])
        hz_str = format_number(data['hz'], False)
        print(f"{param_name:<25} {ms_str:<10} {hz_str:<10} {data['samples']:<10}")

def print_summary(quarter_note_ms, bpm, signature):
    """Print final summary"""
    print(f"\n{'─' * 50} Resumen {'─' * 50}")
    
    # Calculate one measure (4/4 = 4 quarter notes)
    measure_ms = quarter_note_ms * 4
    measure_str = format_number(measure_ms)
    quarter_str = format_number(quarter_note_ms)
    
    print(f"1 compás {signature} = {measure_str} ms  •  1 negra = {quarter_str} ms  •  1 Hz = 1000 ms")

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description='mshzbeats CLI (Esreal Edition) - Calculadora de tempos y frecuencias',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  mshzbeats 130
  mshzbeats 128 --sr 44100 --swing 57
  mshzbeats 140 --signature 3/4 --swing 60
        """
    )
    
    parser.add_argument('bpm', type=float, help='BPM (Beats Per Minute)')
    parser.add_argument('--sr', type=int, default=48000, help='Sample rate (default: 48000)')
    parser.add_argument('--swing', type=int, default=57, help='Swing percentage (default: 57)')
    parser.add_argument('--signature', type=str, default='4/4', help='Time signature (default: 4/4)')
    
    args = parser.parse_args()
    
    if args.bpm <= 0:
        print("Error: BPM debe ser mayor que 0", file=sys.stderr)
        sys.exit(1)
    
    if args.sr <= 0:
        print("Error: Sample rate debe ser mayor que 0", file=sys.stderr)
        sys.exit(1)
    
    if not (0 <= args.swing <= 100):
        print("Error: Swing debe estar entre 0 y 100", file=sys.stderr)
        sys.exit(1)
    
    # Calculate all values
    base_values, quarter_note_ms = calculate_musical_values(args.bpm, args.sr)
    dotted_values = calculate_dotted_values(base_values)
    triplet_values = calculate_triplet_values(base_values)
    swing_data = calculate_swing_values(quarter_note_ms, args.swing)
    
    # Print all sections
    print_header(args.bpm, args.sr, args.signature, args.swing)
    
    print_section("Figuras rectas", base_values, args.sr)
    print_section("Con puntillo", dotted_values, args.sr)
    print_section("En tresillo", triplet_values, args.sr)
    print_swing_section(swing_data, args.sr)
    print_delay_presets(base_values, args.sr)
    print_predelays(args.sr)
    print_compression_guide(base_values, args.sr)
    print_esreal_blocks(base_values, args.sr)
    print_summary(quarter_note_ms, args.bpm, args.signature)

if __name__ == '__main__':
    main()
