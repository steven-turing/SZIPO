# 导入操作系统接口模块 - 提供与操作系统交互的功能，如文件路径操作、目录创建等
import os
# 导入HTTP请求库 - 用于发送HTTP/1.1请求，获取网页内容/API数据等
import requests
# 从bs4库导入BeautifulSoup - HTML/XML解析库，用于从网页中提取和组织数据
from bs4 import BeautifulSoup
# 导入时间模块 - 提供时间相关的功能，如延时、时间戳转换等
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

    """增加if-else来判断HTTP状态码"""
    if response.status_code == 200:
        # 打印响应状态码
        print(f"响应状态码: {response.status_code}")
        # 打印页面内容（前500个字符）
        print(f"页面内容前500个字符: {response.text[:5000]}")
        soup = BeautifulSoup(response.text, 'html.parser')

        pdf_links = []
        # 根据实际页面结构调整选择器
        for link in soup.select('a[href$=".pdf"]'):
            pdf_url = link['href']
            if not pdf_url.startswith('http'):
                pdf_url = f'https://listing.szse.cn{pdf_url}'
            pdf_links.append(pdf_url)
    else:
        print(f"请求失败，状态码: {response.status_code}")
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
