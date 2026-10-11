"""Run the supplied FLUX.2 graph in an owned ComfyUI process using existing verified models."""
from pathlib import Path
import argparse,json,os,subprocess,sys
import psutil
import comfy_runner as runner
KIT=Path(__file__).resolve().parent
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--comfyui',type=Path,required=True);parser.add_argument('--python',type=Path,default=Path(sys.executable));parser.add_argument('--models',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);parser.add_argument('--port',type=int,default=18197);parser.add_argument('--timeout',type=int,default=1800);parser.add_argument('--example',choices=['portrait','compass'],default='portrait');parser.add_argument('--check',action='store_true');args=parser.parse_args()
    args.comfyui=args.comfyui.resolve();args.python=args.python.resolve();args.models=args.models.resolve();root=args.output.resolve()
    if not(args.comfyui/'main.py').is_file()or not args.python.is_file():raise RuntimeError('Supply the installed ComfyUI source and existing AMD Python executable')
    graph=runner.read(KIT/('FLUX2-PORTRAIT.api.json'if args.example=='portrait'else'FLUX2-FIRST-IMAGE.api.json'))
    for n in graph.values():
        for value in n['inputs'].values():
            if isinstance(value,list)and len(value)==2 and isinstance(value[0],str)and value[0]not in graph:raise RuntimeError('Broken graph connection')
    models=[]
    for model in runner.read(KIT/'MODELS.json')['models']:
        file=args.models/model['path']
        if not file.is_file()or file.stat().st_size!=model['bytes']or runner.sha(file)!=model['sha256']:raise RuntimeError('Model file differs: '+str(file))
        models.append(model);print('FULL MODEL SHA OK',model['path'],flush=True)
    if args.check:print('Three model files and graph connections checked; no inference.');return
    if root.exists():raise RuntimeError('Choose a new output folder')
    if runner.occupied(args.port):raise RuntimeError('Chosen port is already occupied; no existing server is stopped')
    if psutil.virtual_memory().available/2**30<12:raise RuntimeError('Close your own model work first; start with12GiB available Windows RAM')
    for process in psutil.process_iter(['pid','cmdline'],ad_value=[]):
        if process.pid==os.getpid():continue
        command=process.info['cmdline']or[]
        if any(Path(value).name.lower()in('llama-server.exe','llama-cli.exe','main.py','moss_probe.py','acestep_ui.py')for value in command):raise RuntimeError('Another model process is present; close your own work before starting')
    gpu=subprocess.run(['powershell.exe','-NoProfile','-Command','Get-CimInstance Win32_PerfFormattedData_GPUPerformanceCounters_GPUEngine | Select-Object Name,UtilizationPercentage | ConvertTo-Json -Compress'],capture_output=True,text=True,timeout=30)
    if gpu.returncode!=0 or not gpu.stdout.strip():raise RuntimeError('GPU activity could not be read')
    engines=json.loads(gpu.stdout);engines=engines if isinstance(engines,list)else[engines]
    if any(float(row['UtilizationPercentage'])>10 for row in engines):raise RuntimeError('GPU is active; wait for your other work to finish')
    root.mkdir(parents=True)
    for name in ['input','output','user','results','embeddings']:(root/name).mkdir()
    (root/'extra-model-paths.yaml').write_text('existing_flux2:\n  base_path: '+args.models.as_posix()+'\n  unet: unet\n  diffusion_models: unet\n  text_encoders: text_encoders\n  vae: vae\nown_text:\n  base_path: '+root.as_posix()+'\n  embeddings: embeddings\n','utf-8')
    (root/'MODELS-VERIFIED.json').write_text(json.dumps(models,indent=2)+'\n','utf-8')
    options=['--gpu-only','--disable-dynamic-vram']
    text=runner.read(KIT/'00-TEXT.api.json');runner.stage(args,root,'00-text',text,options)
    outputs=runner.stage(args,root,'01-image',graph,options);source=next(Path(r['path'])for r in outputs if Path(r['path']).suffix.lower()=='.png');target=root/'results/IMAGE.png';target.write_bytes(source.read_bytes())
    from PIL import Image
    with Image.open(target)as image:
        if image.size!=(1024,1024):raise RuntimeError('Unexpected image dimensions')
        image.verify()
    result=dict(status='completed',image=str(target),sha256=runner.sha(target),example=args.example,all_three_models_full_sha_verified=True,new_prompt_conditioning=True,separate_text_and_image_processes=True,owned_server_stopped=True)
    (root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n','utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
