import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from corp.models import (Industry, IndustryCategory, IndustryDetail,
                         IndustrySubcategory)


class Command(BaseCommand):
    help = "Load industry categories and industries from CSV file"

    def handle(self, *args, **kwargs):
        # CSVファイルのパスを補完します
        file_path = os.path.join(settings.BASE_DIR, "static", "industry_data1.csv")

        # 既存のデータを削除します
        IndustryDetail.objects.all().delete()
        IndustrySubcategory.objects.all().delete()
        Industry.objects.all().delete()
        IndustryCategory.objects.all().delete()

        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                headers = reader.fieldnames
                headers[0] = headers[0].lstrip("\ufeff")
                self.stdout.write(self.style.SUCCESS(f"CSV Headers: {headers}"))

                for row in reader:
                    row = {key.lstrip("\ufeff"): value for key, value in row.items()}
                    self.stdout.write(self.style.SUCCESS(f"CSV Row: {row}"))
                    category_code = row["大分類コード"]
                    category_name = row["大分類名"]
                    industry_code = row["中分類コード"]
                    industry_name = row["中分類名"]
                    subcategory_code = row["小分類コード"]
                    subcategory_name = row["小分類名"]
                    detail_code = row["細分類コード"]
                    detail_name = row["細分類名"]

                    # Create or get the industry category
                    category, created = IndustryCategory.objects.get_or_create(
                        code=category_code, defaults={"name": category_name}
                    )
                    if not created:
                        category.name = category_name
                        category.save()

                    # Create or get the industry
                    industry, created = Industry.objects.get_or_create(
                        code=industry_code,
                        defaults={"name": industry_name, "category": category},
                    )
                    if not created:
                        industry.name = industry_name
                        industry.category = category
                        industry.save()

                    # Create or get the industry subcategory
                    subcategory, created = IndustrySubcategory.objects.get_or_create(
                        code=subcategory_code,
                        defaults={"name": subcategory_name, "industry": industry},
                    )
                    if not created:
                        subcategory.name = subcategory_name
                        subcategory.industry = industry
                        subcategory.save()

                    # Create or get the industry detail
                    detail, created = IndustryDetail.objects.get_or_create(
                        code=detail_code,
                        defaults={"name": detail_name, "subcategory": subcategory},
                    )
                    if not created:
                        detail.name = detail_name
                        detail.subcategory = subcategory
                        detail.save()

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully loaded industry categories and industries"
                )
            )
        except KeyError as e:
            self.stdout.write(
                self.style.ERROR(f"KeyError: {e} - Check CSV column headers")
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
