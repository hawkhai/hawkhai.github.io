#encoding=utf8
import os
import pyppeteer
from pyppeteer import launch
import asyncio
from tqdm import tqdm

async def get_jpgs(html_path, img_path)
    browser = await launch()
    page = await browser.newPage()
    await asyncio.wait_for(page.goto('file'+ html_path), timeout=30)

    table_elements = await page.xpath('tabletbody')
    # 由于一个页面中只包含一个表格，所以只取第一个
    table_element = table_elements[0]
    table_Rect = await table_element.boundingBox()

    # 把table_Rect向四周pad两个像素，让图片包含表格线
    table_Rect[x] = table_Rect[x]-2
    table_Rect[y] = table_Rect[y]-2
    table_Rect[width] = table_Rect[width]+4
    table_Rect[height] = table_Rect[height]+4
    await page.screenshot({
            'path' img_path,
            'clip' table_Rect
        })

    # 关闭浏览器
    await page.close()
    await browser.close()


if __name__ == __main__
    import glob
    html_path_list = glob.glob('homeguopeiworkspacehtmls.html')
    # html_path必须为绝对路径
    for html_path in tqdm(html_path_list)
        img_path = html_path.replace(.html, .jpg)
        asyncio.get_event_loop().run_until_complete(get_jpgs(html_path, img_path))
