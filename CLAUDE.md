# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

eyesim is a Python simulator for the [eyesy](https://www.critterandguitari.com/eyesy) visual synthesizer. It allows developers to create and test eyesy visualization modes without needing the physical hardware. The simulator provides a pygame window with interactive controls that mimic the eyesy's knobs and buttons.

**Note: eyesim now supports EYESY v3 API** - The simulator has been updated to use the v3 naming conventions (`eyesy` instead of `etc`) and includes new v3 features.

## Development Commands

### Installation and Setup
```bash
pip install -e .          # Install in development mode
pip install eyesim         # Install from PyPI
```

### Running the Simulator
```bash
eyesim --mode-folder test                                    # Run built-in test mode
eyesim -m "/path/to/mode/" -a "/path/to/audio.wav"         # Run custom mode with audio
eyesim -m "/path/to/mode/" -w 1920 -t 1080                 # Custom window dimensions
```

### Testing
No formal test suite is present. Test modes manually using the built-in test mode or custom mode folders.

## Architecture

### Core Components

- **`runner.py`**: Main entry point and simulation loop. Handles pygame initialization, widget creation, audio processing, and the main game loop.
- **`etc.py`**: Contains the `System` class that emulates the eyesy hardware environment. Provides knob values, audio data, color utilities, and mode management.
- **`helpers.py`**: Utility functions for directory operations.

### Mode Structure (EYESY v3)

Modes are Python modules that must implement two functions:
- `setup(screen, eyesy)`: Initialize the mode (called once)
- `draw(screen, eyesy)`: Render frame (called every frame at 30 FPS)

The `eyesy` parameter (v3: renamed from `etc`) provides access to:
- `eyesy.knob1` through `eyesy.knob5`: Knob values (0.0-1.0)
- `eyesy.audio_in`: Array of 100 audio samples
- `eyesy.trig`: Audio trigger state (v3: renamed from `audio_trig`)
- `eyesy.xres`, `eyesy.yres`: Screen dimensions
- `eyesy.color_picker()`, `eyesy.color_picker_bg()`: Color utilities
- `eyesy.color_picker_lfo(val, rate)`: New v3 color picker with LFO rate control
- `eyesy.auto_clear`: Whether to clear screen each frame

### Key Simulator Features

- **Interactive Controls**: Press spacebar to toggle visibility of 5 vertical sliders (simulating knobs) and a persist button (toggles auto_clear)
- **Audio Processing**: Real-time audio file playback with sample extraction for visualization
- **Mode Loading**: Dynamic loading of mode folders containing `main.py` files
- **eyesy API Compatibility**: Maintains compatibility with the eyesy Python 2 API while running on Python 3

### EYESY v3 Migration Notes

**API Changes from v2 to v3:**
- Parameter name changed from `etc` to `eyesy` in setup() and draw() functions
- `etc.audio_trig` renamed to `eyesy.trig`
- Removed `eyesy.lastgrab` and `eyesy.lastgrab_thumb` (no longer available)
- Added new `eyesy.color_picker_lfo(val, rate=1.0)` function for LFO-modulated colors

**Python 2/3 Compatibility Notes:**
The simulator runs Python 3 but needs to support eyesy modes written in Python 2. Common issues:
- Print statements: Use `print("foo")` not `print "foo"`
- Integer division: Use `//` for integer division or `int(1/2)` for explicit conversion

### Dependencies

- **pygame**: Graphics and window management
- **pygame_widgets**: UI controls for knob simulation  
- **scipy**: WAV file reading (requires 16-bit WAV files)

## File Structure

```
eyesim/
├── __init__.py          # Empty package init
├── runner.py            # Main simulation engine and CLI
├── etc.py              # System class (eyesy hardware emulation)
├── helpers.py          # Utility functions
└── test-mode/          # Built-in test mode
    ├── main.py         # Simple circle visualization
    └── test.wav        # Test audio file
```