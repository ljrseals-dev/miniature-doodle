"""Numpy-only drop-in TTS engine with a HarmoniaCodec slot."""
from .engine import TTSEngine, available_codecs
__all__=["TTSEngine","available_codecs"]
