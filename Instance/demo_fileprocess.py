# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py

import requests
from tqdm import tqdm


def tqdm_download(url):
    resp = requests.get(url, stream=True)
    #获取文件的大小
    file_size = int(resp.headers['content-length'])
    with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, ascii=True, desc='vscode.exe') as bar:
        with requests.get(url, stream=True) as r:
            with open('vscode.exe', mode='wb') as fp:
                for chunk in r.iter_content(chunk_size=56):
                    if chunk:
                        fp.write(chunk)
                        bar.update(len(chunk))


tqdm_download(url='https://code.visualstudio.com/Download#')


