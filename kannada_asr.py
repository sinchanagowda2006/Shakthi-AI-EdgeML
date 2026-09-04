from nemo.collections.asr.models import EncDecHybridRNNTCTCBPEModel

MODEL_PATH = (
    r"C:\Users\spgow\.cache\huggingface\hub"
    r"\models--ai4bharat--indicconformer_stt_kn_hybrid_ctc_rnnt_large"
    r"\snapshots\c42a17ebe0c461cb230664c2e46c42f381973a5b"
    r"\indicconformer_stt_kn_hybrid_rnnt_large.nemo"
)

model = EncDecHybridRNNTCTCBPEModel.restore_from(
    MODEL_PATH,
    map_location="cpu"
)

def transcribe(audio_path: str) -> str:
    results = model.transcribe(
        [audio_path],
        batch_size=1,
        language_id="kn"
    )
    return results[0][0].strip()

if __name__ == "__main__":
    audio_file = r"C:\Users\spgow\OneDrive\Documents\Sound Recordings\kannada_test.wav"
    text = transcribe(audio_file)
    print("\nKannada Transcription:")
    print(text)