# BRI DAO

💠 **BRI DAO** — децентрализованный проект на платформе Internet Computer, направленный на развитие астрологических сервисов, предсказательных моделей и Web3-инфраструктуры.

📄 Whitepaper  
Актуальные версии Белой книги (собираются автоматически через CI/CD):

- [Whitepaper (RU)](https://aibhrigu.github.io/bri-dao-icp/Whitepaper_RU.pdf)
- [Whitepaper (EN)](https://aibhrigu.github.io/bri-dao-icp/Whitepaper_EN.pdf)

## 📁 Структура репозитория

- `docs/` — статические страницы и PDF-файлы, публикуемые через GitHub Pages;
- `whitepaper/` — исходные `.md`-файлы для генерации PDF;
- `.github/workflows/` — CI-сценарии GitHub Actions для сборки и публикации PDF;
- `src/` — исходный код проекта (будущий backend/frontend);
- `README.md` — описание проекта и навигация.

## ⚙️ Автоматическая сборка PDF

Каждое обновление в `main` автоматически запускает GitHub Actions, который:

1. Конвертирует Markdown-файлы в PDF;
2. Кладёт результат в `docs/`;
3. Публикует на GitHub Pages.

---

👉 Подробнее см. в папке `.github/workflows/whitepaper.yml`

---

> Made with ☕ by BRI DAO — follow the stars, not the noise ✨
