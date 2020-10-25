#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

glist = r"""
marathon\.gitignore
marathon\clear_all_result.bat
marathon\lanczos.exe.bak
marathon\README.md
marathon\rebuild_all.bat
marathon\reindent.py
marathon\input_images\phase1\phase1_input.jpg
marathon\input_images\phase1\phase1_input_optional.jpg
marathon\input_images\phase2\phase2_broken.jpg
marathon\input_images\phase3\phase3_sky.jpg
marathon\input_images\phase3\phase3_watermark.jpg
marathon\output_images\phase1\phase1_output.jpg
marathon\output_images\phase1\phase1_output_optional.jpg
marathon\output_images\phase1\phase1_output_optional.jpg.1.jpg
marathon\output_images\phase1\phase1_output_optional.jpg.2.jpg
marathon\output_images\phase2\phase2_broken.histEqualization.png
marathon\output_images\phase2\phase2_broken.histManipulation.png
marathon\output_images\phase2\phase2_broken.Original.png
marathon\output_images\phase2\phase2_broken_bc.jpg
marathon\output_images\phase2\phase2_broken_bl.jpg
marathon\output_images\phase2\phase2_broken_gaussian_filter.jpg
marathon\output_images\phase2\phase2_broken_hist_equalization.jpg
marathon\output_images\phase2\phase2_broken_hist_manipulation.jpg
marathon\output_images\phase2\phase2_broken_Lanczos.jpg
marathon\output_images\phase2\phase2_broken_mean_filter.jpg
marathon\output_images\phase2\phase2_broken_median_filter.jpg
marathon\output_images\phase2\phase2_broken_nn.jpg
marathon\output_images\phase2\phase2_broken_nn.jpg.png
marathon\output_images\phase2\phase2_broken_repair.jpg
marathon\output_images\phase2\phase2_broken_repair.jpg.heal.png
marathon\output_images\phase2\phase2_broken_repair.jpg.mask.png
marathon\output_images\phase2\phase2_broken_sharpen_spatial.jpg
marathon\output_images\phase2\phase2_sharpen_frequency_gaussian.jpg
marathon\output_images\phase3\phase3_broken_bl_with_wm.jpg
marathon\output_images\phase3\phase3_broken_with_wm_spatial.png
marathon\output_images\phase3\phase3_repair.png
marathon\output_images\phase3\phase3_repair_mask.png
marathon\output_images\phase3\phase3_repair_mask.png.mask.line.png
marathon\output_images\phase3\phase3_repair_original.png
marathon\output_images\phase3\phase3_repair_original.png.mask.line.png
marathon\output_images\phase3\phase3_repair_original.png.mask.png
marathon\output_images\phase3\phase3_sky.jpg_fisher_girl.png
marathon\output_images\phase3\phase3_sky.jpg_fisher_girl_mask.png
marathon\output_images\phase3\phase3_sky.jpg_ocean_wave_mask.png
marathon\output_images\phase3\phase3_sky.jpg_sky_cloud.png
marathon\output_images\phase3\phase3_sky.jpg_sky_mask.png
marathon\output_images\phase3\phase3_sky_final.png
marathon\output_images\phase3\phase3_sky_final.png_glod.png
marathon\output_images\phase3\phase3_sky_final.png_mask_sea.png
marathon\output_images\phase3\phase3_watermark_64x64.jpg
marathon\output_images\phase3\phase3_watermark_recover.jpg
marathon\output_images\phase3\phase3_watermark_recover_spatial.png
marathon\output_images\phase3\Y_U_V\Uphase3_watermark_recover.jpg
marathon\output_images\phase3\Y_U_V\Vphase3_watermark_recover.jpg
marathon\output_images\phase3\Y_U_V\Yphase3_watermark_recover.jpg
marathon\src\phase1.py
marathon\src\phase2.py
marathon\src\phase2_broken_repair.py
marathon\src\phase2_contrast.py
marathon\src\phase2_contrastUI.py
marathon\src\phase2_interpolate.py
marathon\src\phase2_sharpen_frequency.py
marathon\src\phase2_sharpen_spatial.py
marathon\src\phase3_final.py
marathon\src\phase3_sky.py
marathon\src\phase3_watermark_final.py
marathon\src\phase3_watermark_spatial.py
marathon\src\lib\__init__.py
marathon\src\lib\kaffine.py
marathon\src\lib\kalgorithm.py
marathon\src\lib\kcolor.py
marathon\src\lib\kfilter.py
marathon\src\lib\khist.py
marathon\src\lib\kinterpolate.py
marathon\src\lib\kio.py
marathon\src\lib\kmorphology.py
marathon\src\lib\kthreshold.py
marathon\src\lib\pyheal.py
marathon\src\lib\sky.py
marathon\src\lib\watermark.py
marathon\src\lib\wtools.py
marathon\src\phase2_interpolate_Lanczos\.gitignore
marathon\src\phase2_interpolate_Lanczos\lanczos.cpp
marathon\src\phase2_interpolate_Lanczos\lanczos.sln
marathon\src\phase2_interpolate_Lanczos\lanczos.vcxproj
marathon\src\phase2_interpolate_Lanczos\lanczos.vcxproj.filters
marathon\src\phase2_interpolate_Lanczos\ReadMe.txt
marathon\src\phase2_interpolate_Lanczos\stdafx.cpp
marathon\src\phase2_interpolate_Lanczos\stdafx.h
marathon\src\phase2_interpolate_Lanczos\targetver.h
""".strip().split("\n")

glist = [line.strip() for line in glist if line.strip()]
glist.sort()

def main():
    zipName = r"hackathon2020_team24.zip"
    filelist = [[line.strip(), line.strip()] for line in glist]
    gzipflist(zipName, filelist)

if __name__ == "__main__":
    main()
