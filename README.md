# Voice_Commands.py

простой голосовой помощник в консоли на Python для Windows 10.   
реагирует в основном на слова или фразы:  
нажимает клавиши, пишет голос, переводит, и прочие функции.  
команды можно посмотреть словом `покажи`  

### Основные требования

* [Python](https://www.python.org/downloads/release/python-3113/)
* [распаковать сам помощник](https://github.com/Rimtex/Voice_Commands.py/archive/refs/heads/master.zip)
* запустить **Voice_Commands.py**

<hr>

    автозагрузка  
      1 https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip  
      2 https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip  

если нужно переключаться на более точные модели распаковать  
 **voskmodels**\
  * 3 https://alphacephei.com/vosk/models/vosk-model-ru-0.42.zip   
  * 4 https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip   

[для мужского голоса](http://balabolka.site/pavel.windows10.zip)
<hr>

### для запуска файлов голосом

* создаем ярлык файла в папке - **ярлыки**
* переименовываем ярлык в нужные **слова** **или фразы**
* запускаем его устно этим `словом` `или фразой`
* также можно запускать ярлыки адресов браузера

<hr>

### по-умолчанию

* **Caps Lock** или `пиши` пишет русский голос
* **Num Lock** или `инглиш` пишет английский голос
* **Caps Lock** и **Num Lock** или `переводчик` пишет переведённый на английский голос
* **Ctrl - Alt** выключает **Caps Lock** и **Num Lock**
* **Ctrl - Win** режим паузы - `пауза`
* **Shift - Ctrl - Alt** G4f_action - `действие`
<hr>

* **Voice_Commands**
    * **Voice_Commands.py**          ассистент
      * **setup_config.py**          конфигурации адресов файлов
      * **converter.py**             `покажи` преобразователь показа команд
      * **loader.py**                генератор загрузок
      * **vocabulary.py**            словарь ассистента
      * **keyboard_scripts.py**      для скриптов клавиш, и встраивания доп. команд

* разные утилиты.   
    * **Heavy_writer.py**          `писатель` для более точной модели  
    **[ru-0.42](https://alphacephei.com/vosk/models/vosk-model-ru-0.42.zip)**  
    * **Discord_bot_g4f.py**         простой бот дискорд для общения с нейронкой  
    * **Voice_talking_g4f.py**     `болтать` вслух с нейронкой  
  * **apps**  
    * **screen_tesseract.py**    изображение в текст. -**ALT**- выделение области >  
     создание изображения\иконки > **[преобразование в текст](https://github.com/UB-Mannheim/tesseract/wiki)** >   
     в буфер обмена > перевод на русский в консоль
    * **windows_size_position.py** закрепитель окон
    * **simple_g4f.py** нейронка в консоли



