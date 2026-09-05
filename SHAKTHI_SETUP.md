\# Shakthi AI â€” EdgeML ASR Setup



\## Project Overview



Shakthi AI is an offline EdgeML AI platform designed for localized Karnataka-focused intelligence.



This repository contains the current ASR development environment based on Whisper.cpp, along with the development setup for integrating AI4Bharat's Kannada IndicConformer ASR model.



\---



\## Current Status



\### Whisper.cpp



\- Whisper.cpp source successfully configured and built on Windows.

\- Visual Studio 2026 Build Tools with C++ development tools installed.

\- CMake configuration completed successfully.

\- Release build completed successfully.

\- Whisper CLI is available at:



`build/bin/whisper-cli.exe`



\### Whisper Models



Multilingual Whisper models were tested locally:



\- `ggml-base.bin`

\- `ggml-small.bin`



The models are intentionally NOT included in this repository because of their large size.



\### Kannada ASR Testing



A Kannada voice recording was created and converted to:



\- 16 kHz

\- Mono

\- PCM WAV



Test audio:



`kannada\_test.wav`



Whisper.cpp inference works successfully on the test audio.



The smaller Whisper model produced a phonetically close transcription, but Kannada output was represented using Devanagari rather than native Kannada script. Therefore, Whisper.cpp alone is not considered the final Kannada ASR solution.



\---



\## AI4Bharat IndicConformer



The Kannada-specific AI4Bharat model being integrated is:



`ai4bharat/indicconformer\_stt\_kn\_hybrid\_ctc\_rnnt\_large`



The model supports Kannada speech recognition and is intended to provide better native Kannada transcription.



The model is approximately 523 MB and is NOT stored in this GitHub repository.



The model was downloaded through Hugging Face after accepting the model access conditions.



\---



\## Python Environment



Python 3.10 was installed specifically for compatibility testing with the AI4Bharat/NeMo stack.



Virtual environment:



`ai4bharat-env`



The environment is intentionally NOT included in this repository.



Packages tested include:



\- PyTorch

\- TorchAudio

\- TorchVision

\- NeMo Toolkit

\- Cython



\---



\## Current AI4Bharat Integration Status



The AI4Bharat `.nemo` model was successfully downloaded and extracted locally.



The model configuration was inspected and adjusted to locate the Kannada tokenizer files locally.



The model loads past the tokenizer initialization stage.



The remaining blocker is a NeMo/model-version compatibility issue involving the RNNT decoder configuration.



Current error:



`RNNTDecoder.\_\_init\_\_() got an unexpected keyword argument 'multisoftmax'`



The model configuration reports NeMo version:



`1.19.0`



The installed newer NeMo version is not fully compatible with this model configuration.



Therefore, Kannada IndicConformer integration is currently in progress.



\---



\## Important Local Files



These files exist locally but are intentionally excluded from GitHub:



\- `ggml-base.bin`

\- `ggml-base.en.bin`

\- `ggml-small.bin`

\- `\*.nemo`

\- `kannada\_model/`

\- `ai4bharat-env/`

\- `kannada-asr-env/`

\- `build/`



They should not be committed to the repository.



\---



\## Repository Structure



The repository currently contains the Whisper.cpp source tree, including:



\- `src/`

\- `include/`

\- `examples/`

\- `ggml/`

\- `bindings/`

\- `cmake/`

\- `tests/`

\- `.github/`



The Whisper.cpp source provides the current EdgeML/CPU inference foundation for the project.



\---



\## Development Environment



Primary platform:



\- Windows

\- Visual Studio 2026 Build Tools

\- C++ development tools

\- CMake

\- Git

\- Python 3.10 / 3.11 for ASR experimentation



Whisper.cpp was successfully compiled in Release configuration.



\---



\## Next Development Tasks



1\. Resolve AI4Bharat IndicConformer + NeMo compatibility.

2\. Obtain reliable native Kannada transcription.

3\. Create a simple local ASR inference interface.

4\. Connect the ASR component to the Shakthi AI backend.

5\. Provide a clean API/interface for frontend integration.

6\. Test Kannada voice queries end-to-end.

7\. Optimize CPU inference for standard 8 GB RAM systems.

8\. Integrate the final voice assistant workflow.



\---



\## Frontend Integration



The frontend team can use this repository for the current ASR/EdgeML development source.



The final interface between frontend and ASR should be kept modular so that the frontend does not depend directly on the underlying Whisper.cpp or NeMo implementation.



Recommended architecture:



Frontend  

â†“  

Local ASR Interface  

â†“  

Kannada ASR Model  

â†“  

Shakthi AI Processing / Retrieval  

â†“  

Response



\---



\## Important Note



This repository represents the current development state and is not yet the final production build.



Whisper.cpp compilation and local inference are working.



AI4Bharat Kannada IndicConformer integration is still being completed.

## Kannada ASR — AI4Bharat IndicConformer

The Kannada ASR module uses the AI4Bharat IndicConformer Hybrid CTC/RNNT model.

### Verified Environment

The following environment has been tested successfully on Windows:

* Python: `3.10.11`
* PyTorch: `2.14.0`
* TorchAudio: `2.11.0`
* NeMo: AI4Bharat NeMo `nemo-v2` branch
* nemo-toolkit: `1.23.0rc0`
* NumPy: `1.26.4`

The ASR dependencies should be installed in a separate virtual environment. Do not install them into the main Shakthi AI/RAG environment unless compatibility has been verified.

### Model

Model:

`ai4bharat/indicconformer_stt_kn_hybrid_ctc_rnnt_large`

The `.nemo` model file must be downloaded separately and should not be committed to Git.

Set the model location using the environment variable:

`SHAKTHI_ASR_MODEL_PATH`

Example on Windows:

`set SHAKTHI_ASR_MODEL_PATH=C:\path\to\indicconformer_stt_kn_hybrid_rnnt_large.nemo`

### ASR Interface

The frontend should use:

`transcribe(audio_path) -> str`

The audio file should be a 16 kHz mono WAV file.

Example:

`text = transcribe(audio_path)`

The model is lazy-loaded when `transcribe()` is first called, so importing the module does not immediately load the ASR model.

### Verified Kannada Test

The module has been tested locally with a Kannada 16 kHz WAV recording and successfully produced native Kannada-script transcription.

Example output:

`ನಮಸ್ಕಾರ ನನ್ನ ಹೆಸರು ಶಕ್ತಿಯಾಗಿದೆ ನಾನು ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆಯ ಬಗ್ಗೆ ಕಲಿಯುತ್ತಿದ್ದೇನೆ`
