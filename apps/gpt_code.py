from selenium import webdriver

# Указываем путь к драйверу браузера (например, Chrome)
driver_path = 'путь_к_драйверу_браузера'

# Создаем экземпляр драйвера
driver = webdriver.Chrome(driver_path)

# Открываем веб-страницу
driver.get('https://www.youtube.com')
