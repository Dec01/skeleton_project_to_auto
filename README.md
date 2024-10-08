# от Автора

Привет привет. В этом репозитории собраны ответы на разного рода вопросы с которыми я сталкивался и буду сталкиваться на пути автоматизации API. Надеюсь это может быть полезно не только мне. 
Я часто использую этот скелет в повседневной работе, при тестировании микросервисов и "агрегаторов" - по этому он будет модернизирован в будущем на основе нового опыта.  Для связи:

![image](https://github.com/user-attachments/assets/e1675131-4f02-45bb-bfd5-7a21c20945c9) https://t.me/ParshinEwg

![image](https://github.com/user-attachments/assets/a6da1eb3-b559-4990-b24a-7fcd54eb1d7d) parschin.ewg@yandex.ru


# Инструкция
## Docker: сборка

Для сборки доступны команды:
```
# docker build --build-arg run_env=stage --build-arg run_domain=https://127.0.0.1 -t domainCont .
```
* run_env=name - требуетя указать имя тестируемого окружения (dev/stage)
* run_domain=url - требуется указать имя домена поднятного API интерфейса(адрес стенда) 

## Docker: запуск

```
# docker run {name}
or
# docker run -it {name} bash
```
## Docker: отчет
Результат запуска:
reports/pytest/result.xml
```
# pytest --verbose --junitxml=reports\\pytest\\result.xml src/tests/
```
## Общая структура проекта
```
├── project
    ├───logs - папка с логами, папка будет создана после первого запуска
    ├───reports - папка с репортами, папка будет создана после первого запуска
    │   └───pytest
    └───src - папка с тестами, полезной нагрузкой и разными функциями
        ├───models
        │   ├───paths - пути к эндпоинтам
        │   ├───payloads - полезная нагрузка / модели для валидации
        │   ├───processings - функции обогащения/обработки запросов/ответов
        │   └───utils - вспомогательные функции
        └───tests - папка с тестами
            └───component
```
