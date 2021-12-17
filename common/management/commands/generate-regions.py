from django.core.management import BaseCommand
import xlrd

from core.models.product import Region
from sprinter_settings import settings
from sprinter_settings.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, **options):
        if not settings.DEBUG:
            print("can't be run in non-debug mode")
            return

        print("Generating data Regions...")
        self.generate_regions()
        print('Regions created')
        print("Data was successfully generated!")

    def generate_regions(self):
        wb = xlrd.open_workbook(f'{BASE_DIR}/common/initial_data/regions.xls')
        sheet = wb.sheet_by_index(0)

        for r in range(1, sheet.nrows):
            id_ = sheet.cell(r, 0).value
            title_en = sheet.cell(r, 1).value
            title_uz = sheet.cell(r, 2).value
            title_ru = sheet.cell(r, 3).value
            # title_qr = sheet.cell(r, 4).value
            # title_oz = sheet.cell(r, 5).value

            Region.objects.update_or_create(
                id=id_,
                name_ru=title_ru,
                name_uz=title_uz,
                name_en=title_en,
                # title_oz=title_oz,
                # title_qr=title_qr
            )
