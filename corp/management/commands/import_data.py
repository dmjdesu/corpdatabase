import csv
import os

from django.core.management.base import BaseCommand

from corp.models import OriginIndustry, OriginIndustryCategory
from corpdatabase import settings


class Command(BaseCommand):
    help = "Import data from CSV file"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, "static", "industry_data2.csv")
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            headers[0] = headers[0].lstrip("\ufeff")
            self.stdout.write(self.style.SUCCESS(f"CSV Headers: {headers}"))

            for row in reader:
                # 先頭にあるドットを削除
                row = {
                    key.lstrip("\ufeff"): value.lstrip(".")
                    for key, value in row.items()
                }
                self.stdout.write(self.style.SUCCESS(f"CSV Row: {row}"))
                category_name = row["大分類"]
                category_description = row["大分類の説明"]
                industry_name = row["中分類"]
                industry_description = row["中分類の説明"]

                # Create or get the industry category
                category, created = OriginIndustryCategory.objects.get_or_create(
                    name=category_name, defaults={"description": category_description}
                )
                if not created:
                    category.name = category_name
                    category.save()

                # Create or get the industry
                industry, created = OriginIndustry.objects.get_or_create(
                    name=industry_name,
                    defaults={
                        "description": industry_description,
                        "category": category,
                    },
                )
                if not created:
                    industry.name = industry_name
                    industry.category = category
                    industry.save()

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
