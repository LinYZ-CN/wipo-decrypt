import subprocess
from functools import partial
import json
import pandas as pd
import requests

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs


class BrandDBScraper:
    def __init__(self):
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://branddb.wipo.int',
            'referer': 'https://branddb.wipo.int/',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }

    def scrape_brand_data(self, brand, rows):
        json_data = {
            'sort': 'score desc',
            'rows': rows,
            'asStructure': '{"_id":"800b","boolean":"AND","bricks":[{"_id":"800c","key":"brandName","value":"' + brand + '","strategy":"Simple"}]}',
            'fg': '_void_',
        }

        response = requests.post('https://api.branddb.wipo.int/search', headers=self.headers, json=json_data)
        re_txt = response.content.decode('utf-8')
        with open('decrypt.js', 'r', encoding='utf-8') as file:
            js_code = file.read()
        context = execjs.compile(js_code)
        data = context.call("decryptAES", re_txt)
        json_dict = json.loads(data)
        df = pd.json_normalize(json_dict['response']['docs'])
        df.to_csv(f"商标'{brand}'全球品牌数据.csv")


def main():
    scraper = BrandDBScraper()
    brand = "网易"
    row = 100
    scraper.scrape_brand_data(brand,row)


if __name__ == "__main__":
    main()
