# OLX parsing

https://starodead.pythonanywhere.com

login: test@gmail.com

pass: 1qazcde3
## Bugs
- Я не знаю почему, но обьявления не отображаются в Google Chrome
## Features

- Пользователь может авторизироваться по логину и паролю.
- Неавторизированный пользователь может зарегистрироваться.

- На главной странице по нажатию кнопки "Обновить динамически подгружаются последние 100 обьявлений из категории Мобильные телефоны"

- Каждый элемент имеет кнопку "удалить", при нажатии на которую обьявление исчезает


# Technology Stack:

- Python 3.10
- Flask
- MDBootstrap
- AJAX requests
- JavaScript

# Local installation

```sh
git clone https://github.com/IvanStored/olx_scrap
cd olx_scrap
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python app.py
```
