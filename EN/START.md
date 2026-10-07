# Local FLUX.2: from extracted folder to your own image

## Starting point and evidence
Beginner guide for Windows with an appropriate Strix Halo system. Our archive records one EVO-X2 run: 1024×1024, 20 steps, guidance 4.0, Euler, seed 205932306, total 445.7 seconds. A new installation, new UI import and your own run remain untested. This does not validate other Radeon GPUs, RTX cards or Macs.

1. Already working ComfyUI? Back up its installation, versions and workflow; start with that setup.
2. For a new install, match exact hardware, Windows, driver and Python to the SAME AMD package version. ARCHIV-BEGLEITPAKET/INSTALL-COMFYUI.ps1 is a ROCm-7.2.1/Python-3.12 example, not a newly executed clean installation. It fetches then-current ComfyUI/GGUF Git revisions and records them; they are not frozen. Do not mix another documentation version into it. Read the script first; preserve working environments.
3. Read archived MODEL-FOLDERS.txt. Separately required: flux2-dev-Q4_K_M.gguf, mistral_3_small_flux2_fp4_mixed.safetensors, flux2-vae.safetensors. Weights are not bundled. Check each original source and model terms.
4. Archived folders relative to ComfyUI: models/unet, models/text_encoders, models/vae. The current GGUF model card uses models/diffusion_models for the image model. Select a folder recognized by your matching loader and the actual compatible file. Our old startup script explicitly checks unet. A different folder needs an adjusted check, not blindly renamed files.
5. Check available RAM/GPU resources and your own running tasks. Startup loads the image server and requires START. In the extracted archive folder: .\START-COMFYUI.ps1 -Installation "C:\your\Dolmario-Comfy". Do not globally change ExecutionPolicy. Locally unblock only reviewed downloaded files if needed. Do not stop other people's processes.
6. Open http://127.0.0.1:8188 and keep the terminal open. Open or drag FLUX2-Q4-EVO.json into ComfyUI. This is a UI graph, not an API request.
7. Verify loaders: #12 UnetLoaderGGUF image model; #38 CLIPLoader text encoder/type flux2; #10 VAELoader decoder. Resolve missing files/nodes before running.
8. Edit the subject in #6 CLIPTextEncode. The saved actual prompt is a weathered brass compass on a folded nautical chart with morning light. For a first comparison, change the subject only.
9. Match BOTH resolutions: #48 Flux2Scheduler AND #47 EmptyFlux2LatentImage = 1024×1024. #47 batch = 1. #48 steps = 20; #26 FluxGuidance = 4.0; #16 KSamplerSelect = euler; #25 RandomNoise seed = 205932306. A smaller experiment is a different setting, not a reproduction of the archived timing.
10. Overview: #38→#6→#26→#22; #12→#22; noise #25, guider #22, sampler #16, sigmas #48 and latent #47→#13; #13 plus VAE #10→#8→#9. Actual ports are in the workflow; do not reconnect arbitrarily.
11. Submit ONE job. Watch the output and terminal. Do not queue copies because initial loading takes time. Review your actual image's subject, details and errors.
12. Find the image in ComfyUI/output. Also save your own workflow; keep prompt, seed, version records and ERGEBNIS.csv together. Enter your own duration and image path. The sheet contains no invented measurements.
13. Restart: stop only your own Comfy process with Ctrl+C, start again and reopen your workflow. Preserve exact errors and versions. Missing model: check loader/folder. Missing GGUF node: inspect extension/import errors. Out of memory: release your competing tasks and record a smaller changed experiment separately.

## Sources and version boundary
[AMD 7.2.1 Windows](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/windows/install-pytorch.html), [ComfyUI manual installation](https://docs.comfy.org/installation/manual_install), [GGUF extension](https://github.com/city96/ComfyUI-GGUF), [GGUF model card](https://huggingface.co/city96/FLUX.2-dev-gguf), [original model terms](https://huggingface.co/black-forest-labs/FLUX.2-dev).
On 2026-10-07, the opened AMD page covers the 7.2.1 baseline while the opened ComfyUI page describes a different Windows Python/ROCm path. This guide therefore provides no universal latest installer. Today's AMD compatibility-matrix request returned HTTP 429; compatibility approval for your exact setup remains pending. No model weights downloaded, no new server started.
