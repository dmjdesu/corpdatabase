# import_prefectures_cities.py

import csv
import os
from django.core.management.base import BaseCommand
from corp.models import Prefecture, City
from corpdatabase import settings

class Command(BaseCommand):
    help = 'Imports prefectures and cities data from CSV'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'static', 'industry_address.csv')
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # ヘッダーのキーを整形
            reader.fieldnames = [header.strip().replace('\ufeff', '').replace('\n', '').replace('"', '') for header in reader.fieldnames]
            print(f'CSVファイルのヘッダー: {reader.fieldnames}')

            for row in reader:
                # 各キーを整形
                row = {key.strip().replace('\n', '').replace('"', ''): value.strip() for key, value in row.items()}
                print(f'CSVファイルの行: {row}')
                prefecture_code = row['団体コード']
                prefecture_name = row['都道府県名（漢字）']
                prefecture_name_kana = row['都道府県名（カナ）']
                city_name = row['市区町村名（漢字）']
                city_name_kana = row['市区町村名（カナ）']

                #市を作成する場合
                if city_name:
                    # 市のコードとして市区町村名（漢字）を使用
                    city_code = prefecture_code

                    # 同一の都道府県内で市名がすでに存在するか確認
                    prefecture = Prefecture.objects.get(
                        name=prefecture_name,
                    )

                    city, city_created = City.objects.get_or_create(
                        prefecture=prefecture,
                        code=city_code,
                        defaults={
                            'name': city_name,
                            'name_kana': city_name_kana,
                        }
                    )

                    if city_created:
                        self.stdout.write(self.style.SUCCESS(f'市を作成しました: {city.name}'))
                    else:
                        self.stdout.write(f'市 {city.name} はすでに存在しています。')

                else:
                    # 都道府県を作成または取得
                    prefecture, prefecture_created = Prefecture.objects.get_or_create(
                        code=prefecture_code,
                        defaults={
                            'name': prefecture_name,
                            'name_kana': prefecture_name_kana,
                        }
                    )

                if prefecture_created:
                    self.stdout.write(self.style.SUCCESS(f'都道府県を作成しました: {prefecture.name}'))

        self.stdout.write(self.style.SUCCESS('Data import completed successfully'))
