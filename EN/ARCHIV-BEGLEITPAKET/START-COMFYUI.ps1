param([Parameter(Mandatory=$true)][string]$Installation)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $Installation).Path
$python = Join-Path $root 'venv\Scripts\python.exe'
$comfy = Join-Path $root 'ComfyUI'
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) { throw 'Python environment missing.' }
if (Get-NetTCPConnection -LocalPort 8188 -State Listen -ErrorAction SilentlyContinue) { throw 'Port 8188 is occupied. Do not stop another service.' }
$files = @('models\unet\flux2-dev-Q4_K_M.gguf','models\text_encoders\mistral_3_small_flux2_fp4_mixed.safetensors','models\vae\flux2-vae.safetensors')
foreach ($file in $files) { if (-not (Test-Path -LiteralPath (Join-Path $comfy $file) -PathType Leaf)) { throw "Model file missing: $file" } }
Write-Host 'Before continuing: ensure other image/LLM jobs are idle and enough RAM/GPU memory is free.'
if ((Read-Host 'Type START to confirm your resource check') -cne 'START') { throw 'Not started.' }
Set-Location -LiteralPath $comfy
& $python main.py --listen 127.0.0.1 --port 8188
if ($LASTEXITCODE -ne 0) { throw 'ComfyUI exited with an error.' }
