from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # 1. Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # 2. Ждем, когда цена станет $100 (не менее 12 секунд)
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена уменьшилась до $100")
    
    # 3. Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    print("Нажата кнопка Book")
    
    # Ждем появления элемента с задачей
    x_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    )
    # 4. Решаем математическую задачу
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    print("Ответ введен в поле")
    
    # Отправляем решение
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    print("Форма отправлена")
    
    # 5. Получаем результат из алерта
    result_alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    result_text = result_alert.text
    result_alert.accept()
    print("Ответ:", result_text.split()[-1])

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    # Для отладки можно сделать скриншот
    browser.save_screenshot("error.png")

finally:
    # Пауза для визуальной проверки
    time.sleep(5)
    browser.quit()