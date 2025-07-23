from skyfield.api import Loader
from pathlib import Path

# Папка назначения
target_dir = Path('utils/ephem_data').resolve()
print(f"Скачиваем эфемериды в {target_dir}...")

# Создаем загрузчик Skyfield с указанием директории
loader = Loader(str(target_dir))
loader.download('data/de440s.bsp')  # загружаем файл эфемерид
