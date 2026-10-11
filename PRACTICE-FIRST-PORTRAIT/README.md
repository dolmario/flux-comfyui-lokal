# FLUX.2: your first local image on AMD

Open `00-TEXT.json`, write your prompt and run it to save conditioning. Then open `FLUX2-PORTRAIT.json` to make the picture. The two stages run in separate ComfyUI processes so the text encoder is released before loading the image model. The download also supplies the compass example.

## Install the source into a new folder

Use your existing Python3.12 AMD environment with PyTorch2.9.1+ROCm7.2.1. `ENVIRONMENT.json` records the tested packages; the [AMD guide](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/windows/install-pytorch.html) covers the ROCm prerequisite. The installer below downloads two pinned official source archives and checks their full SHA256 and CRC. It reuses your Python environment and driver.

In PowerShell, from the extracted kit folder:

```powershell
py -3.12 install_sources.py --output my-flux-sources --python 'C:\AI\venv\Scripts\python.exe'
```

Replace the Python path with the one from your existing AMD environment. Keep the matching ComfyUI and GGUF source versions in `SOURCES.json` together.

## Put the three model files in place

`MODELS.json` contains pinned download links, file sizes and full checksums:

- `unet/flux2-dev-Q4_K_M.gguf`: the image model.
- `text_encoders/mistral_3_small_flux2_fp4_mixed.safetensors`: the text encoder.
- `vae/flux2-vae.safetensors`: the image decoder.

Our example uses existing downloaded weights. Model weights are not bundled. To download the pinned files into an empty folder, run:

```powershell
py -3.12 download_models.py --output C:\Models\FLUX2
```

Existing matching files are verified and kept; an unverified existing file is preserved. The full network weight-download path was not run during this recording. Model use follows the [FLUX.2-dev model card](https://huggingface.co/black-forest-labs/FLUX.2-dev) and the linked model sources; source installation does not grant a model licence.

## Run both stages automatically

```powershell
& 'C:\AI\venv\Scripts\python.exe' run_image.py --comfyui .\my-flux-sources\ComfyUI --python 'C:\AI\venv\Scripts\python.exe' --models 'C:\Models\FLUX2' --output my-first-portrait
```

The runner verifies all three complete model files, computes new prompt conditioning, stops that process, generates a1024×1024portrait, saves the PNG and stops its own image process. Use `--example compass` for the still-life example. Start from a new output directory with your other model work closed; the runner keeps12GiB available Windows RAM at startup and stops its own process if available RAM remains below256MiB for five seconds. It leaves existing servers and work untouched.

## Work with the actual native graphs

The runner writes the local address to the stage log. Open it in a browser and import the corresponding graph. `00-TEXT.json` shows the encoder, both prompts and Save Conditioning outputs. The image graphs show the saved conditioning, GGUF model, Guidance4, matching1024×1024fields,20Euler steps, fixed seed, VAE and Save Image.

For manual stages, the detailed startup commands and actual exported conditioning files are supplied with the execution record. Change the words in the text stage, run that stage again, then choose its new saved conditioning in the image stage. Changing a source prompt without computing its conditioning does not change the generated picture.

Recorded on our64GB Strix Halo Windows machine. Windows exposes about32GB system RAM with the current GPU reservation; software-reported GPU memory is a separate figure. Other hardware can differ. The earlier combined attempt and the final separate-stage records are retained in `VALIDATION.json`.

English narration, German subtitles. Advertisement / affiliate link: I may earn a commission through this link.
https://de.gmktec.com/?ref=DolmarioAi

## Deutsch

Der Download enthält zwei getrennte Schritte: Text mit Mistral berechnen und als Conditioning speichern; danach FLUX.2 starten und das Bild erzeugen. Vorhandene AMD-Python-Umgebung und Treiber werden verwendet. Der Sourceinstaller legt neue, festgelegte ComfyUI-/GGUF-Quellen an und prüft SHA256/CRC. Modellgewichte werden separat geladen. Die drei Modelle, fertigen Beispiele, native Graphen und genaue Befehle liegen im Paket. Stimme55 bleibt englisch, deutsche Untertitel und Studio-Texte gehören zum Film. Affiliate nur `ref=DolmarioAi`.
