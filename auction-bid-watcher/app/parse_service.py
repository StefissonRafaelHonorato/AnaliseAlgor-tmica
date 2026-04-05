from datetime import datetime
from app.models import PriceSnapshot
from app.utils import extract_number
from app.locator_service import get_by, describe_location

def read_price(driver, selector: str, selector_type: str) -> PriceSnapshot:
    # Lê o texto do elemento
    # Extrai o número e devolve um snapshot
    by = get_by(selector_type)
    element = driver.find_element(by, selector)

    raw_text = element.text
    value = extract_number(raw_text)
    location_description = describe_location(selector_type, selector)

    return PriceSnapshot(
        value=value,
        raw_text=raw_text,
        located_by=location_description,
        timestamp=datetime.now()
    )