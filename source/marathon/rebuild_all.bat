
python src\phase1.py

python src\phase2.py

lanczos.exe
python src\phase2_interpolate.py

python src\phase2_contrast.py
rem python src\phase2_contrastUI.py

python src\phase2_broken_repair.py

python src\phase2_sharpen_spatial.py
python src\phase2_sharpen_frequency.py

python src\phase3_watermark_spatial.py
python src\phase3_watermark_final.py

python src\phase3_sky.py
python src\phase3_final.py
