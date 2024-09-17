import random

from django.core.management.base import BaseCommand
from faker import Faker

from corp.models import Company, Industry, IndustryCategory


class Command(BaseCommand):
    help = "Populate the database with random companies"

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = ["Technology", "Healthcare", "Finance", "Education", "Retail"]
        industries = [
            "Software",
            "Medical Devices",
            "Banking",
            "Universities",
            "E-commerce",
        ]

        # Create Industry Categories
        for category in categories:
            IndustryCategory.objects.get_or_create(name=category)

        # Create Industries
        for industry in industries:
            category = random.choice(IndustryCategory.objects.all())
            Industry.objects.get_or_create(name=industry, category=category)

        # Create Companies
        for _ in range(100):
            industry = random.choice(Industry.objects.all())
            Company.objects.create(
                name=fake.company(),
                industry=industry,
                description=fake.text(),
                established_date=fake.date(),
                employees=random.randint(1, 10000),
                revenue=round(random.uniform(1e5, 1e8), 2),
                website=fake.url(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                address=fake.address(),
                city=fake.city(),
                state=fake.state(),
                country=fake.country(),
                postal_code=fake.postcode(),
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated the database with random companies"
            )
        )
