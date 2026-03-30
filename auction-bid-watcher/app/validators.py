import re
import validators

def validate_user_name(name: str) -> bool:
    if not isinstance(name, str):
        return False
    
    name = name.strip()

    if len(name) < 3:
        return False
    
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", name))

def validate_url(url: str) -> bool:
    return bool(validators.url(url))

def validate_positive_integer(value) -> bool:
    try:
        value = int(value)
        return value > 0
    except (TypeError, ValueError):
        return False
    
def validate_selector(selector: str) -> bool:
    return isinstance(selector, str) and len(selector.strip()) > 0

def validate_selector_type(selector_type: str) -> bool:
    return selector_type in {"css", "xpath", "id", "name"}