import os
import requests
from bs4 import BeautifulSoup
import time

# 创建保存PDF的目录
os.makedirs('szipo_pdfs', exist_ok=True)

BASE_URL = 'https://listing.szse.cn/disclosure/ipo/index.html'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def download_pdf(url, filename):
    """下载PDF文件"""
    response = requests.get(url, headers=HEADERS, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)


def get_pdf_links():
    """获取页面上的PDF链接"""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    pdf_links = []
    # 根据实际页面结构调整选择器
    for link in soup.select('a[href$=".pdf"]'):
        pdf_url = link['href']
        if not pdf_url.startswith('http'):
            pdf_url = f'https://listing.szse.cn{pdf_url}'
        pdf_links.append(pdf_url)

    return pdf_links


def main():
    pdf_links = get_pdf_links()
    print(f"找到 {len(pdf_links)} 个PDF文件")

    for i, pdf_url in enumerate(pdf_links):
        filename = os.path.join('szipo_pdfs', f'document_{i + 1}.pdf')
        print(f"正在下载: {pdf_url}")
        download_pdf(pdf_url, filename)
        time.sleep(20)  # 礼貌性延迟


if __name__ == '__main__':
    main()
