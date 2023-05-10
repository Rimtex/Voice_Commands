# Voice_Commands.py

простой голосовой помощник в консоли на Python для Windows   
управляющийся в основном `голосовыми` командами.   
реагирует на фразы или слова, нажимает клавиши, двигает курсор, пишет голос, переводит, и прочие функции  
функции можно посмотреть командой `покажи`  
<hr>

### Основные требования
* Python 
* модель распознавании голоса
1. https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
   * если нужно переключаться
2. https://alphacephei.com/vosk/models/vosk-model-ru-0.42.zip
3. https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
4. https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
   * можно подключить локальную нейро модель для `голосового` общения   
     https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin               
     https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin  
     в папку - **models**
<hr>

### для запуска файлов голосом
* копируем файл
* вставляем ярлык в папку **ярлыки**
* переименовываем ярлык в нужное `слово`
* запускаем его устно этим `слово`м
* также можно запускать ярлыки адресов браузера
<hr>

### по-умолчанию 
Caps Lock или `пиши` пишет голос и выключает Caps Lock  
Num Lock или `перевод` пишет переведённый голос и выключает Num Lock
<hr>

* **Voice_Commands.py**
    * **address_config.py**        переменные адресов для файлов
    * **Heavy_writer.py**          `писатель` для более точной модели **ru-0.42** на Num Lock или `цифры`
    * **Voice_neuro_responder.py** `поговорим` для голосового общения с языковой моделью
    * **converter.py**             `покажи` преобразователь для показа команд
    * **loader.py**                для генерации всяких вещей
    * **vocabulary.py**            словарь ассистента
    * **keyboard_scripts.py**      для скриптов клавиш
    * **Tester.py**                для теста функций
