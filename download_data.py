"""Скачать 4 официальных CSV Olist для учебного некоммерческого проекта."""
from pathlib import Path
from urllib.request import urlretrieve

root = "https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/"
names = [
    "olist_orders_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_sellers_dataset.csv",
]
folder = Path.home() / "ML_private_datasets" / "olist"
folder.mkdir(parents=True, exist_ok=True)
for name in names:
    dst = folder / name
    if dst.exists() and dst.stat().st_size > 1000:
        print("Уже скачан:", name)
        continue
    print("Загружаю:", name)
    try:
        urlretrieve(root + name, dst)
        print("Готово:", dst, f"({dst.stat().st_size/1e6:.1f} MB)")
    except Exception as exc:
        dst.unlink(missing_ok=True)
        print(f"Ошибка загрузки {name}: {exc}")
        print("Скачайте вручную:", root + name)
        raise SystemExit(1)
print("Данные готовы, откройте delivery_prediction.ipynb в JupyterLab")
