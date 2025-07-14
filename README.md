# BRI DAO on Internet Computer (ICP)

## 🚀 О проекте

**BRI DAO** — децентрализованная автономная организация на платформе Internet Computer (ICP).  
Проект объединяет токен BRI, модуль управления и фронтенд для взаимодействия с участниками сети.

---

## 📂 Структура репозитория

- **bri-token-backend/** — Rust canister для ICRC-1 токена BRI.
- **governance-module/** — Rust canister для управления DAO (голосование, staking).
- **frontend/** — SvelteKit / React интерфейс для пользователей и админов DAO.

---

## ⚙️ Сборка и деплой

```bash
# Установи DFX
dfx --version

# Собери и запусти локально
dfx start --background
dfx deploy
