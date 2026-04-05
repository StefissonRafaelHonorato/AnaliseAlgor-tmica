from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.locator_service import get_by
from app.user_logger import log_app

def notify_change(
        driver,
        target_url: str,
        input_selector: str,
        input_selector_type: str,
        button_selector: str,
        button_selector_type: str,
        old_value: float,
        new_value: float
):
    # Abre outra página pública
    # Insere a mensagem e clica em um botão

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(target_url)

    wait = WebDriverWait(driver, 20)

    input_by = get_by(input_selector_type)
    button_by = get_by(button_selector_type)

    input_element = wait.until(
        EC.presence_of_element_located((input_by, input_selector))
    )

    message = f"O valor do lance mudou de {old_value} para {new_value}."
    input_element.clear()
    input_element.send_keys(message)

    button_element = wait.until(
        EC.element_to_be_clickable((button_by, button_selector))
    )
    button_element.click()

    log_app(f"Notificação registrada em outra página: {message}")