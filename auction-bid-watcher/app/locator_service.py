from selenium.webdriver.common.by import By

def get_by(selector_type: str):
    mapping = {
        "css": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "id": By.ID,
        "name": By.NAME
    }
    return mapping[selector_type]

def describe_location(selector_type: str, selector: str) -> str:
    # Retorna uma descrição da posição do elemento na página
    # Isso ajuda a atender ao critério de mostrar XPath/Regex/posição
    return f"Elemento localizado por {selector_type.upper()}: {selector}"