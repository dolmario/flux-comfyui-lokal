# FLUX.2 auf AMD: Installation & ComfyUI-Workflow | Strix Halo

Begleitpaket fuer die deutsche Folge.

1. Installiere Python 3.12 und Git; pruefe AMD-Treiber und ROCm-Matrix.
2. INSTALL-COMFYUI.ps1 richtet einen NEUEN Ordner ein. Kein Modellstart.
3. MODEL-FOLDERS.txt lesen; Modelle separat laden.
4. START-COMFYUI.ps1 -Installation "C:\dein\Dolmario-Comfy".
5. Browser http://127.0.0.1:8188; FLUX2-Q4-EVO.json hineinziehen.
6. Loadernamen und beide Aufloesungen pruefen; Run. Bild in ComfyUI/output.
7. Wenn fehlende Nodes gemeldet werden: ComfyUI-/GGUF-Versionen pruefen. Kein beliebiges Node-Paket installieren.

## Teststand / Evidence

Belegt: vorhandener lokaler Aufbau und ein Bildlauf mit 445,7 Sekunden gesamt. Neuinstallation heute nicht ausgefuehrt. INSTALL verwendet aktuelle ComfyUI-/GGUF-Repository-Staende und schreibt deren Commits mit; das ist kein eingefrorener Nachbau. Der Hinweisnode wurde sprachlich angepasst und von der abweichenden alten 7:14-Angabe auf den Gesamtlauf aus dem Film vereinheitlicht; alle Verarbeitungsknoten und Links bleiben identisch.

Die PowerShell-Dateien vorher lesen. In PowerShell im entpackten Begleitordner mit .\Dateiname.ps1 starten. Keine ExecutionPolicy global abschalten. Falls Windows blockiert: nach Dateipruefung nur die betreffenden selbst heruntergeladenen Skripte lokal entsperren. INSTALL erstellt einen neuen Ordner; START laedt ein Modell und benoetigt freie Ressourcen. Keine Administratorrechte vorausgesetzt.

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
