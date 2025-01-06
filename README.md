# 🎮 Sega Games Emulator Web Platform

## 📝 Описание
Веб-платформа для эмуляции игр Sega, построенная на Django с использованием EmulatorJS. Позволяет играть в классические игры Sega прямо в браузере.

## 🚀 Возможности
- Эмуляция игр Sega в веб-браузере
- Поддержка сохранений игр
- Удобный пользовательский интерфейс
- Библиотека классических игр
- Кроссплатформенность (работает на ПК, мобильных устройствах и планшетах)

## 🛠 Технологии
- Django
- EmulatorJS
- Python
- JavaScript
- HTML/CSS

## ⚙️ Установка и запуск

1. Клонируйте репозиторий: git clone https://github.com/SergNik38/SegaEmu.git
2. Создайте и активируйте виртуальное окружение:
      bash
      python -m venv venv
      source venv/bin/activate # для Linux/Mac
      venv\Scripts\activate # для Windows
3. Установите зависимости:
      bash
      pip install -r requirements.txt
4. Выполните миграции:
      bash
      python manage.py migrate
5. Запустите сервер:
      bash
      python manage.py runserver

