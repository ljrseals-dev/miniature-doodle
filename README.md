# Drop-In TTS Engine with HarmoniaCodec Slot

A dependency-minimal Python 3.9+ text-to-speech engine. The baseline codec synthesizes English speech with a deterministic numpy-only formant source. Harmonia is discovered through the registry and can replace the baseline without engine/frontend/DSP imports.

## Install

```bash
python -m pip install numpy
```

For tests:

```bash
python -m pip install pytest
```

## Run

```bash
python -m tts.cli "hello world" out.wav
```

The result is mono 16-bit PCM WAV at 22.05 kHz.

Try the Harmonia slot:

```bash
python -m tts.cli "hello world" out.wav harmonia
```

Until Harmonia weights/runtime are installed, the engine emits one warning and renders the utterance again with the baseline codec. The fallback never attempts to decode a Harmonia latent with the baseline decoder.

## Architecture

`text -> frontend -> codec registry -> encode -> decode -> NoiseBed -> compressor -> dither -> WAV`

The codec contract is frozen in `tts/codec/interface.py`. Codec selection is string-based; `tts/engine.py` does not import `codec.harmonia`.

## Tests

```bash
python -m pytest -q
```

## Harmonia integration

Implement `load`, `encode`, and `decode` in `tts/codec/harmonia.py` while preserving `CodecConfig`, `CodecLatent`, and `BaseCodec`. The engine contract does not need to change.
