# Voice_Commands.py

простой голосовой помощник в консоли на Python для Windows 10.   
управляющийся в основном `голосовыми` командами.   
реагирует на фразы или слова, нажимает клавиши, пишет голос, переводит, и прочие функции.  
функции можно посмотреть командой `покажи`
<hr>

### Основные требования

* [Python](https://www.python.org/downloads/release/python-3113/)
* [распаковать сам помощник](https://github.com/Rimtex/Voice_Commands.py/archive/refs/heads/master.zip)
* запустить **Voice_Commands.py** модели должны загрузится сами  

<hr>

   1 https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip  
   2 https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip  


<hr>

* если нужно переключаться   
   3 https://alphacephei.com/vosk/models/vosk-model-ru-0.42.zip   
   4 https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip  

<hr>

### для запуска файлов голосом

* копируем файл
* вставляем ярлык в папку **ярлыки**
* переименовываем ярлык в нужные **слова** **или фразы**
* запускаем его устно этим `словом` `или фразой`
* также можно запускать ярлыки адресов браузера
<hr>

### по-умолчанию

Caps Lock или `пиши` пишет русский голос  
Num Lock или `инглиш` пишет английский голос  
Caps Lock и Num Lock или `переводчик` пишет переведённый на английский голос  
Ctrl - Alt выключает Caps Lock и Num Lock  
название `ассистент` настроено для запуска помощника с ярлыка 
<hr>

* **Voice_Commands.py**
    * **address_config.py**        конфигурации адресов файлов
    * **Heavy_writer.py**          `писатель` для более точной модели **ru-0.42**
    * **converter.py**             `покажи` преобразователь для показа команд
    * **loader.py**                для генерации всяких вещей
    * **vocabulary.py**            словарь ассистента
    * **keyboard_scripts.py**      для скриптов клавиш
