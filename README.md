# Автотесты для лендинга JoyMoney

- [Автотесты для проекта JoyMoney](#автотесты-для-проекта-joymoney)
  - [Конфигурация](#конфигурация)
    - [Пути к chromedriver](#пути-к-chromedriver)
    - [ВАЖНО!!!](#важно)
      - [Linux](#linux)
      - [Windows](#windows)
    - [pytest.ini](#pytestini)
  - [Запуск всех автотестов](#запуск-всех-автотестов)
  - [UI](#ui)
    - [Запуск](#запуск)
  - [Allure](#allure)
    - [Генерация отчетов](#генерация-отчетов)
    - [Так как запустить тесты чтобы увидеть их вживую, а потом открыть отчет Allure???](#так-как-запустить-тесты-чтобы-увидеть-их-вживую-а-потом-открыть-отчет-allure)
  - [Docker](#docker)
  - [Лайфхаки](#лайфхаки)
    - [Как отключить режим headless?](#как-отключить-режим-headless)
    - [Ошибка нет такого драйвера](#ошибка-нет-такого-драйвера)
    - [GitLab постоянно просит ввести логин и пароль](#gitlab-постоянно-просит-ввести-логин-и-пароль)
    - [Что делать если драйвер долго инициализируется?](#что-делать-если-драйвер-долго-инициализируется)

## Конфигурация

### Пути к chromedriver

### ВАЖНО!!!

#### Linux

**Перед запуском тестов, укажите прямой путь к драйверу в файле** `config.py`:

``` python
local_path: str | None = "//usr//bin//chromedriver"
# Или
local_path: str | None = None
```

Пример пути к драйверу в Linux. Этот путь можно оставить, чтобы запускать тесты в `CI/CD` (в `Dockerfile` драйвер загружается по этому пути).

#### Windows

По аналогии, укажите путь к драйверу в `Windows`

> Учтите, что если оставить `None`, то `webdriver-manager` будет сам подтягивать этот браузер, скачаивать и обновлять.
> При этом **могут наблюдаться задержки при старте тестов**, например такие:

``` shell
2023-12-13 21:03:52 [INFO] Page.wait_until_stable() - Page wait until driver stable
```

когда драйвер пытается инициализироваться (может занимать до 1-2 минут, а может и сразу стартануть).

> При использовании явного пути я не испытывал никаких проблем с запуском тестов.
> В `Dockerfile` я всегда скачиваю последнюю версию драйвера и `Google Chrome`, поэтому для тестов в `CI/CD` лучше использовать явный путь `//usr//bin//chromedriver`.

### pytest.ini

- `pytest.ini`: Это основной файл конфигурации Pytest, который позволяет вам изменить поведение по умолчанию.

```ini
[pytest]
addopts = --reruns 1 -s -v --durations=10 --clean-alluredir --alluredir allure-results

filterwarnings =
    ignore: .*(X509Extension|pkg_resources).*

markers =
    burger_menu: mark for run only burger menu test
    nav_menu: mark for run only navigation menu test
    lk_button: mark for run only lk_button test
    slider: mark for run only slider test
    footer: mark for run only footer section test
    faq: mark for run only faq section test
    feedback: mark for run only feedback section test
    popular_services: mark for tun only popular_services test
    tariff_cards: mark for tun only tariff_cards test
    how_to: mark for tun only how_to test
    calculator_get_money_button: mark for tun only calculator_get_money_button test
    calculator: mark for tun only calculator test

testpaths = tests/ui

python_classes = Test*

python_functions = test_*

python_files = test_*.py
```

## Запуск всех автотестов

Для запуска всех `ui` автотестов:

```shell
pip install virtualenv
python<version> -m venv <virtual-environment-name>
source <virtual-environment-name>/bin/activate

pip install -r requirements.txt

python -m pytest -m ui --alluredir=./allure-results
```

Можно опустить `ui` и написать `api`, либо просто написать `pytest`.

## UI

### Запуск

Для запуска UI-тестов введите команду:

```shell
pytest -m ui
```

## Allure

**Allure** — фреймворк от Яндекса для создания простых и понятных отчётов автотестов [для любого языка].

### Генерация отчетов

Запуск сервера отчетов локально

```shell
allure serve
```

Или создать отчет

```shell
allure generate
```

Эта команда создаст папку `allure-report`

### Так как запустить тесты чтобы увидеть их вживую, а потом открыть отчет Allure???

Эта команда запустит все тесты:

``` shell
pytest && allure serve
```

Если вам нужно запустить конкретные тесты, укажите нужную метку, например `registration`:

``` shell
pytest -m calculator && allure serve
```

Или:

> Откройте папку `allure-report`, а затем файл `index.html`, тогда вам не придется запускать Live Server.

**Не закрывайте окно браузера вручную, Selenium все сделает за вас. Если закрыть браузер раньше, то по логам вы получите ошибку `target window: target window already closed` и не узнаете истинную причину падения теста, а также вы не увидите скриншот**

## Docker

Для проекта должен использоваться Python версии выше 3.10 (особенности синтаксиса `|`).

```Dockerfile
FROM	--platform=linux/amd64 python:3.11-slim-bookworm
```

Переменные среды:

``` Dockerfile
ENV	PYTHONDONTWRITEBYTECODE=1
ENV	PYTHONUNBUFFERED=1
```

> `PYTHONDONTWRITEBYTECODE` - Если для этого параметра задана непустая строка,
> Python не будет пытаться записывать файлы `.pyc` при импорте исходных модулей
> `PYTHONUNBUFFERED` - Принудительно отключить буферизацию потоков `stdout` и `stderr`

Устанваливаем доп.зависимости и утилиты:

``` Dockerfile
RUN	apt-get -y update && \
    apt-get install -y gnupg && \
    apt-get install -y wget && \
    apt-get install -y curl && \
    apt-get install -y unzip
```

Вручную устанавливаем Chrome последней стабильной версии. Для этого добавляем пакет в `sources.list`,
обновляем списки доступных пакетов и устанавливаем google-chrome-stable.

```Dockerfile
RUN	wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN	sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN	apt-get -y update && apt-get install -y google-chrome-stable
```

Так же устанавливаем утилиту `unzip`, чтобы распаковать `chromedriver`.
`chromedriver` скачаиваем по такой схеме:

1. С помощью EP получаем стабильный номер версии `chromedriver`.

```shell
curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE
```

В ответе будет примерно такое:

```shell
120.0.6099.71
```

Этот номер вставляем в общую ссылку и скачиваем с помощью `wget` и сразу же распаковываем `unzip` по пути `/usr/bin/`.

Итоговый вариант скрипта:

``` Dockerfile
RUN	wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/`curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`/linux64/chromedriver-linux64.zip -q --show-progress
RUN	unzip -j /tmp/chromedriver.zip chromedriver-linux64/chromedriver -d /usr/bin/
```
> Про флаги `wget` и `unzip` можно почитать в документации.

Здесь мы просто смотрим на установленные версии пакетов (chromedriver, google-chrome-stabe, python).
Это поможет при дебаге и поиске ошибок.

```Dockerfile
RUN	python3 --version && \
    /usr/bin/google-chrome-stable --version && \
    /usr/bin/chromedriver --version
```

Создаем пользователя `qa`.
Устанавливаем рабочую директорию `jm-landing`. Скачиваем требуемые зависимости.
Копируем исходники в рабочую директорию.

```Dockerfile
ARG	USERNAME=qa
RUN	useradd -m $USERNAME
USER	$USERNAME
ARG	HOMEPATH=/home/$USERNAME

ENV	PATH=$PATH:$HOMEPATH/.local/bin

RUN	mkdir $HOMEPATH/jm-landing/
WORKDIR	$HOMEPATH/jm-landing/
COPY	 requirements.txt $HOMEPATH/jm-landing/
RUN	cd $HOMEPATH/jm-landing/ \
    pip install --no-cache-dir --upgrade pip \
    pip install --no-cache-dir  -r requirements.txt
COPY	. $HOMEPATH/jm-landing/
```

## Лайфхаки

### Как отключить режим headless?

Откройте файл `config.py` и измените следующий параметр:

```python
# Замените на False
HEADLESS = True
```

Теперь можно увидеть как браузер управляет тестами вживую (отрывок из автоеста регистрации):

![Example non headless](/resources/img/examples/registration_example.gif "Example non headless")

*Браузером Chrome управялет автматизированное тестовое ПО*

### Ошибка нет такого драйвера

> *ValueError: There is no such driver by url ...*

Можно попробовать вылечить

``` shell
pip install --upgrade webdriver-manager
```

### GitLab постоянно просит ввести логин и пароль

``` shell
git remote set-url origin https://oauth2:{{ваш_токен}}@gitlab.joy.money/Mexus/jm_autotests.git

```

Или

``` shell
git remote set-url origin https://{{имя_пользователя}}:{{ваш_токен}}@gitlab.com/rozhkov_m/autotests_jm_landing
```

### Что делать если драйвер долго инициализируется?

Если драйвер долго зависает на этапе подготовки (~1минута) это значит что работает `webdriver-manager`.
Откройте файл `utils/webdriver/factory/builders.py` и посмотрите на эту строку:

``` python
service = ChromeService(local_path or ChromeDriverManager().install())
```

`Service` предоставляет возможность настраивать путь к браузеру. Если не указать этот путь в `config.py`:

``` python
class DriverConfig(BaseSettings):

...

local_path: str = ""
```

то `webdriver-manager` сам будет заниматься этой настройкой (в том числе автоматически скачивать драйвер).

> В разделе [Docker](#Docker) я показал как явно устанавливать драйвер по пути `/usr/bin/chromedriver`

Вместо этого, можно явно указать путь к драйверу:

``` python
local_path: str = "//usr//bin//chromedriver"
```

> `//` - экранирование

То же самое можно проделать для `Windows` и не ждать подолгу инициализации драйвера.
