from app.browser import create_browser
from app.config import AppConfig
from app.validators import (
    validate_user_name,
    validate_url,
    validate_positive_integer,
    validate_selector,
    validate_selector_type
)
from app.auction_monitor_service import monitor_auction_bid
from app.user_logger import log_app, log_user_action

def get_user_input() -> AppConfig:
    user_name = input("Digite seu nome: ").strip()
    while not validate_user_name(user_name):
        print("Nome inválido. Use apenas letras e espaços, com ao menos três caracteres.")
        user_name = input("Digite seu nome: ").strip()

    auction_url = input("Digite a URL do leilão: ").strip()
    while not validate_url(auction_url):
        print("URL inválida.")
        auction_url = input("Digite a URL do leilão: ").strip()

    bid_selector = input("Digite o seletor do lance atual: ").strip()
    while not validate_selector(bid_selector):
        print("Seletor inválido.")
        bid_selector = input("Tipo do seletor do lance (css/xpath/id/name): ").strip().lower()

    timeout = input("Digite o timeout em segundos: ").strip()
    while not validate_positive_integer(timeout):
        print("Timeout inválido")
        timeout = input("Digite o timeout em segundos: ").strip()
    timeout = int(timeout)

    poll_interval = input("Digite o intervalo de monitoramento em segundos: ").strip()
    while not validate_positive_integer(poll_interval):
        print("Intervalo inválido")
        poll_interval = input("Digite o intervalo de monitoramento em segundos: ").strip()
    poll_interval = int(poll_interval)

    target_url = input("Digite a URL da segunda página publica: ").strip()
    while not validate_url(target_url):
        print("URL inválida")
        target_url = input("Digite a URL da segunda página publica: ").strip()

    target_input_selector = input("Digite o seletor do campo de texto: ").strip()
    while not validate_selector_type(target_input_selector):
        print("Seletor inválido")
        target_input_selector = input("Digite o seletor do campo de texto: ").strip()

    target_input_selector_type = input("Tipo do seletor do campo (css/xpath/id/name): ").strip().lower()
    while not validate_selector_type(target_input_selector_type):
        print("Tipo inválido")
        target_input_selector_type = input("Tipo do seletor do campo (css/xpath/id/name): ").strip().lower()