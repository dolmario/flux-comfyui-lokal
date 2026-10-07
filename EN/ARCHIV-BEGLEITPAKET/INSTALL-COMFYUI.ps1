# Source-checked instructions, NOT freshly executed in a clean environment.
# Requires Python 3.12, Git, supported Ryzen hardware and matching AMD driver.
# ROCm 7.2.1 baseline from the episode; inspect current AMD compatibility matrix.
param([string]$Destination = (Join-Path $PWD 'Dolmario-Comfy'))
$ErrorActionPreference = 'Stop'
if (Test-Path -LiteralPath $Destination) { throw 'Destination exists. Choose a NEW folder.' }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Install Git first.' }
& py -3.12 -c 'import sys; print(sys.version)'
if ($LASTEXITCODE -ne 0) { throw 'Python 3.12 is required.' }
New-Item -ItemType Directory -Path $Destination | Out-Null
Set-Location -LiteralPath $Destination
& py -3.12 -m venv venv
if ($LASTEXITCODE -ne 0) { throw 'venv failed.' }
$python = (Resolve-Path -LiteralPath .\venv\Scripts\python.exe).Path
function Install-Pip { & $python -m pip @args; if ($LASTEXITCODE -ne 0) { throw 'pip failed.' } }
Install-Pip install --upgrade pip
$amd = 'https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1'
Install-Pip install "$amd/rocm_sdk_core-7.2.1-py3-none-win_amd64.whl" "$amd/rocm_sdk_devel-7.2.1-py3-none-win_amd64.whl" "$amd/rocm_sdk_libraries_custom-7.2.1-py3-none-win_amd64.whl" "$amd/rocm-7.2.1.tar.gz"
Install-Pip install "$amd/torch-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl" "$amd/torchvision-0.24.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl" "$amd/torchaudio-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl"
& git clone https://github.com/Comfy-Org/ComfyUI.git
if ($LASTEXITCODE -ne 0) { throw 'ComfyUI clone failed.' }
Install-Pip install -r .\ComfyUI\requirements.txt
& git clone https://github.com/city96/ComfyUI-GGUF.git .\ComfyUI\custom_nodes\ComfyUI-GGUF
if ($LASTEXITCODE -ne 0) { throw 'GGUF clone failed.' }
Install-Pip install -r .\ComfyUI\custom_nodes\ComfyUI-GGUF\requirements.txt
& $python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU'); assert torch.cuda.is_available()"
if ($LASTEXITCODE -ne 0) { throw 'AMD PyTorch GPU check failed. Do not start a workflow.' }
& git -C .\ComfyUI rev-parse HEAD | Set-Content .\COMFYUI-COMMIT.txt
& git -C .\ComfyUI\custom_nodes\ComfyUI-GGUF rev-parse HEAD | Set-Content .\GGUF-COMMIT.txt
& $python -m pip freeze | Set-Content .\INSTALLED-PACKAGES.txt
Write-Host 'Read MODEL-FOLDERS.txt, download models separately, then use START-COMFYUI.ps1.'
