# your_app/management/commands/extract_keywords.py

import csv
import os
import re

from django.core.management.base import BaseCommand

from corp.models import Keyword
from corpdatabase import settings


class Command(BaseCommand):
    help = 'Extract keywords from the "事業概要" field in a fixed CSV file and store them in the database'

    def handle(self, *args, **kwargs):
        # 固定のファイルパスを指定
        csv_file = os.path.join(
            settings.BASE_DIR, "static", "sample_company_data.csv"
        )  # ファイルパスを指定

        # 正規表現で "キーワード:" 部分を取得
        keyword_pattern = re.compile(r"キーワード:\s*(.*)")

        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                business_summary = row["事業概要"]  # CSVの事業概要列を指定

                match = keyword_pattern.search(business_summary)
                if match:
                    # '、' または ',' で区切る
                    keywords = re.split(r"[、,]", match.group(1))
                    for keyword in keywords:
                        # キーワードを空白を除去して登録
                        Keyword.objects.create(keyword=keyword.strip())
