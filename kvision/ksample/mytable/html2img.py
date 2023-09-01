#encoding=utf8
import re, os, sys

CURFILEDIR = os.path.split(os.path.abspath(__file__))[0]
PYTHONXDIR = r"E:\kSource"
if not sys.path or PYTHONXDIR not in sys.path: # for pythonx
    sys.path.insert(0, PYTHONXDIR)
    sys.path.insert(0, os.path.join(PYTHONXDIR, "pythonx"))
from pythonx.funclib import *

import pyppeteer
from pyppeteer import launch
import asyncio
from tqdm import tqdm

# https://blog.csdn.net/Guo_Python/article/details/124755559
async def get_jpgs(html_path, img_path):
    browser = await launch()
    page = await browser.newPage()

    urlx = "file://"+html_path.replace("\\", "/")
    print(urlx)
    # file://E:/kSource/blog/kvision/ksample/imgtable_2x/table-recognition/linux/resultv3/0033bdebca7d3a927b6349c2a8e0babe_1_0_MSv11.html
    # https://cvsample.sunocean.life/imgtable_2x/table-recognition/linux/resultv3/0033bdebca7d3a927b6349c2a8e0babe_1_0_MSv11.html
    #urlx = urlx.replace("file://E:/kSource/blog/kvision/ksample/", "https://cvsample.sunocean.life/")
    await asyncio.wait_for(page.goto(urlx), timeout=30)

    table_elements = await page.xpath('//table') # tbody
    # 由于一个页面中只包含一个表格，所以只取第一个
    table_element = table_elements[0]
    table_Rect = await table_element.boundingBox()

    # 把table_Rect向四周pad两个像素，让图片包含表格线
    table_Rect["x"] = table_Rect["x"]-2
    table_Rect["y"] = table_Rect["y"]-2
    table_Rect["width"] = table_Rect["width"]+4
    table_Rect["height"] = table_Rect["height"]+4
    await page.screenshot({
            'path': img_path,
            'clip': table_Rect
        })

    # 关闭浏览器
    await page.close()
    await browser.close()


if __name__ == "__main__":
    import glob
    rootdir1 = r"E:\kSource\blog\kvision\ksample\mytable\table-recognition\linux\resultv3"
    rootdir2 = r"E:\kSource\blog\kvision\ksample\imgtable_2x\table-recognition\linux\resultv3"
    #html_path_list = glob.glob('homeguopeiworkspacehtmls.html')
    # html_path必须为绝对路径
    #for html_path in tqdm(html_path_list)
    def globglob(rootdir):
        for _dir in os.listdir(rootdir):
            if not _dir.endswith(".html"):
                continue
            html_path = os.path.join(rootdir, _dir)
            img_path = html_path.replace(".html", ".png")
            asyncio.get_event_loop().run_until_complete(get_jpgs(html_path, img_path))

    globglob(rootdir1)
    globglob(rootdir2)
