from django.core.management import BaseCommand
import xlrd

from common.models import District
from senat_cms import settings
from senat_cms.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, **options):
        if not settings.DEBUG:
            print("can't be run in non-debug mode")
            return

        print("Generating data Districts...")
        self.generate_districts()
        print('Districts created')
        print("Data was successfully generated!")

    def generate_districts(self):
        wb = xlrd.open_workbook(f'{BASE_DIR}/common/initial_data/districts.xls')
        sheet = wb.sheet_by_index(0)

        for r in range(1, sheet.nrows):
            reg_id = sheet.cell(r, 0).value
            title_en = sheet.cell(r, 1).value
            title_uz = sheet.cell(r, 2).value
            title_ru = sheet.cell(r, 3).value
            title_qr = sheet.cell(r, 4).value
            title_oz = sheet.cell(r, 5).value
            District.objects.get_or_create(
                region_id=int(reg_id),
                title_en=title_en,
                title_uz=title_uz,
                title_ru=title_ru,
                title_qr=title_qr,
                title_oz=title_oz,
            )
