# FastAPI Optional Sections

Главная страница работает без настройки. Два дополнительных блока включаются независимо.

| Переменная окружения | Блок | Пример значения |
| --- | --- | --- |
| `SITE_ANNOUNCEMENT` | Объявление | Обновили расписание |
| `SITE_CONTACT` | Контакты | team@example.com |

Если переменная отсутствует, пуста или содержит только пробельные символы, её блок отсутствует в HTML. Значения отображаются посетителям как текст.

## Запуск

Требуется Python 3.10 или новее. В активированном виртуальном окружении выполните:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app
```

Откройте [главную страницу](http://127.0.0.1:8000/).

Чтобы включить блоки, остановите сервер, задайте одну или обе переменные в терминале и запустите сервер снова.

**PowerShell**

```powershell
$env:SITE_ANNOUNCEMENT = "Обновили расписание"
$env:SITE_CONTACT = "team@example.com"
python -m uvicorn main:app
```

**Bash или Zsh**

```bash
export SITE_ANNOUNCEMENT="Обновили расписание"
export SITE_CONTACT="team@example.com"
python -m uvicorn main:app
```
