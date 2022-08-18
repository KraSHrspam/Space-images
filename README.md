# Космический Телеграм

Данный код отпровляет картинки земли в специальный телеграм канал.

### Как установить

Для начала вам нужно создать файлик `.env` Он должен выглядеть вот так
```
TELEGRAM_TOKEN=5136941251:AAG7HY1337YHrSyg0gZNS64sLрsvFJxF2UE
VK_IMPLICIT_FLOW_TOKEN=YjSmH3pN6d3J7YGlSmNN1NdlYnXnHvmak9DpbLbV
PERIOD=10.0
SPACEX_LAUNCH_NUMBER=10
```
+ В переменной `TELEGRAM_TOKEN` лежит ваш токен бота о том как его узнать я расскажу ниже.
+ В переменной `VK_IMPLICIT_FLOW_TOKEN` лежит ваш апи ключ с помощью которого бот получает картинки космоса.
+ В переменной `PERIOD` лежит время через которое бот будет отправлять картинки. Время указываеться в секундах _точку с нулем писать обязательно!_
+ В переменной `SPACEX_LAUNCH_NUMBER` лежит количество раз сколько будет запускаться функция `get_spacex_picture_url`.  *_Вы можете менять это число_*

#### Как узнать ApiToken
- Вы можете узнать свой апи на этом [сайте](https://api.nasa.gov/#apod).
Вам понадобиться зайти в раздел *Generate API Key*. Далее вписываем свои **имя**, **фамилию** и **Почту**. 
Последнее окошко не обязательно.
Далее копируете свой апи. *Он выглядит вот так*
`jQUwHXi9BJI6trxp4hgCC3UfMhfjFgI9z1HMqE21`

#### Как узнать Token
- Для того чтобы узнать Токен бота вам понадобится Телеграм бот [BotFather](https://t.me/BotFather).
Дальше переходим по [сыллке](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) (там все написанно) 

Далее просто вставляем все как написанно выше в файл `.env`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Для запуска нужно
+ Чтобы открыть командную строку нужно нажать win+r Вписываем в открывшееся окошко `cmd`
+ В командную строку вписать `python main.py`

#### Команды для запуска
+ fetch_apod_pictures - Скачивает apod картинки
+ fetch_EPIC_photos - скачивает EPIC картинки (картинки с землёй)
+ fetch_spacex_photos - скачивет картинки SpaceX

```
python *название скрипта*
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
