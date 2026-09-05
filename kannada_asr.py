import os
from nemo.collections.asr.models import EncDecHybridRNNTCTCBPEModel

_model = None


def _load_model():
    global _model

    if _model is None:
        model_path = os.getenv("SHAKTHI_ASR_MODEL_PATH")

        if not model_path:
            raise RuntimeError(
                "SHAKTHI_ASR_MODEL_PATH is not set. "
                "Set it to the path of the IndicConformer .nemo model."
            )

        if not os.path.isfile(model_path):
            raise FileNotFoundError(
                f"IndicConformer model not found: {model_path}"
            )

        _model = EncDecHybridRNNTCTCBPEModel.restore_from(
            model_path,
            map_location="cpu"
        )

    return _model


def transcribe(audio_path: str) -> str:
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    model = _load_model()

    results = model.transcribe(
        [audio_path],
        batch_size=1,
        language_id="kn"
    )

    return results[0][0].strip()


if __name__ == "__main__":
    audio_file = r"C:\Users\spgow\OneDrive\Documents\Sound Recordings\kannada_test.wav"
    print("\nKannada Transcription:")
    print(transcribe(audio_file))

