# Voice_Commands.py

голосовой ассистент управляющийся `голосовыми` командами  
со встроенной локальной нейро моделью для `голосового` общения
<hr>

## Основные требования

* модель распознавании голоса

1. https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip - в эту же папку
    * если нужно переключаться
2. https://alphacephei.com/vosk/models/vosk-model-ru-0.42.zip
3. https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
4. https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip

* если нужна языковая модель  
  http://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin            - в папку - **models**

<hr>

### для запуска файлов голосом

* копируем файл
* вставляем ярлык в папку **ярлыки**
* переименовываем ярлык в нужное `слово`
* запускаем его устно этим `слово`м
* также можно запускать ярлыки адресов браузера

<hr>

#### по-умолчанию нажатый Caps Lock или `голос` записывает голос в курсор и выключает Caps Lock

<hr>

* **Voice_Commands.py**
    * **Heavy_writer.py**          точный `писатель` на Num Lock или `цифры`
    * **address_config.py**        переменные адресов для файлов
    * **Voice_neuro_responder.py** `поговорим` для голосового общения с языковой моделью
    * **converter.py**             `покажи` преобразователь для показа команд
    * **loader.py**                для генерации всяких вещей
    * **vocabulary.py**            словарь ассистента
    * **Coloring.py**              просто напоминалка для всяких вещей
    * **keyboard_scripts.py**      для скриптов клавиш
    * **Tester_models.py**         `модель` для теста языковых моделей
    * **Tester.py**                для теста функций
    * **mouse.py**                 для теста мышиных функций
