from core.models import Product, Catalog


def get_similar_products(instance: Product) -> list:
    catalog = Catalog.objects.filter(products__in=[instance]).first()
    root_parent_catalog = catalog.get_root()
    id_descendants = [obj.id for obj in root_parent_catalog.get_descendants()]
    similar_products = Product.objects.filter(catalogs__in=id_descendants).exclude(id=instance.id).distinct()
    return similar_products
