# Use the two native ComfyUI graphs

These are the command options from the completed native text and image runs, with editable example paths. Keep the extracted kit at `C:\AI\FLUX2` for this example, and open PowerShell there. Replace the Python and model paths with your own. The existing AMD environment and pinned source installation are described in README.md.

## Prepare the folders

Use a new `manual-run` directory. Create `input`, `output`, `user` and `embeddings` inside it. Copy `model-paths.example.yaml` to `model-paths.yaml`, then set its two base paths to your model directory and the absolute manual-run directory. The model directory contains the `unet`, `text_encoders` and `vae` subfolders from MODELS.json.

## Compute the text

```powershell
$fluxPython = 'C:\AI\venv\Scripts\python.exe'
& $fluxPython .\my-flux-sources\ComfyUI\main.py --listen 127.0.0.1 --port 8188 --disable-pinned-memory --gpu-only --disable-dynamic-vram --input-directory C:\AI\FLUX2\manual-run\input --output-directory C:\AI\FLUX2\manual-run\output --user-directory C:\AI\FLUX2\manual-run\user --extra-model-paths-config C:\AI\FLUX2\model-paths.yaml
```

Open `http://127.0.0.1:8188`. Import `00-TEXT.json`, edit the prompts and press Run. Both Save Conditioning nodes write files under `manual-run/output/conditioning`. After this first run in an empty output folder, the names are:

```text
flux2-compass_00001_.safetensors
flux2-portrait_00001_.safetensors
```

Stop that console with Ctrl+C. Copy the files into `manual-run/embeddings`, naming them `flux2-compass.safetensors` and `flux2-portrait.safetensors`. The original completed conditioning files are also supplied in `example/conditioning`; using them reuses our recorded text instead of computing new text.

## Make the picture

Start the same command again. The new process releases the previous encoder allocation. Refresh the browser, import `FLUX2-PORTRAIT.json` and select `flux2-portrait.safetensors` in Load Conditioning. If an old missing-file notice remains, open its details and click Refresh. The recording used that refresh and the backend confirmed both files.

Set the matching size fields to1024×1024, Euler to20steps, Guidance to4 and the seed control to fixed. These values are already in the supplied graph. Press Run. The actual recorded portrait took407.1s including model load and decode; it is an individual measurement on our setup.

Right-click the completed Save Image preview and select Save Image to download the original PNG. For the other subject, import `FLUX2-FIRST-IMAGE.json`, select the compass conditioning and run it. That separate recorded image run took406.2s.

For a new prompt, compute new conditioning and give its file a new name before selecting it in the image graph. Keep the first PNG and its settings together. Stop your own ComfyUI console with Ctrl+C when finished. The automatic runner adds RAM monitoring and stops only its own child process; this manual console command is for working directly in the native UI.
