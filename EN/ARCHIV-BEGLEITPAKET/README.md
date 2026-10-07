# FLUX.2 on AMD: Installation & ComfyUI Workflow | Strix Halo

Companion package for the English episode.

1. Install Python 3.12 and Git; verify AMD driver and ROCm compatibility.
2. INSTALL-COMFYUI.ps1 creates a NEW directory; it starts no model.
3. Read MODEL-FOLDERS.txt; download models separately.
4. START-COMFYUI.ps1 -Installation "C:\your\Dolmario-Comfy".
5. Open http://127.0.0.1:8188; drag FLUX2-Q4-EVO.json into ComfyUI.
6. Check loader filenames and both resolution nodes, then Run; output in ComfyUI/output.
7. Missing nodes: check ComfyUI/GGUF versions before installing unrelated extensions.

## Teststand / Evidence

Evidence: existing local setup and a recorded image run taking 445.7 seconds total. Clean installation not executed today. INSTALL uses current ComfyUI/GGUF repositories and records their commits; it is not a frozen environment. Only the informational MarkdownNote was translated and aligned with the film total instead of the differing old 7:14 note. All processing nodes and links are unchanged.

Read the PowerShell files first. From the extracted companion folder run .\Filename.ps1. Do not globally disable ExecutionPolicy. If Windows blocks a downloaded file, inspect it before locally unblocking that specific file. INSTALL creates a new directory; START loads a model and needs free resources. No administrator rights assumed.

## Quellen / Sources

AMD installation and driver matrix (ROCm 7.2.1 baseline):
https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/windows/install-pytorch.html
https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityryz/windows/windows_compatibility.html
ComfyUI manual installation and workflow:
https://docs.comfy.org/installation/manual_install
https://github.com/Comfy-Org/ComfyUI
https://github.com/city96/ComfyUI-GGUF
Model files and separate license terms:
https://huggingface.co/city96/FLUX.2-dev-gguf
https://huggingface.co/Comfy-Org/flux2-dev/tree/main/split_files
