import time
from app.parse_service import read_current_bid
from app.notifier_service import notify_bid_change
from app.user_logger import log_app

def monitor_auction_bid(driver, config):
    previous_snapshot = read_current_bid(
        driver,
        config.bid_selector,
        config.bid_selector_type
    )

    log_app(f"Lance inicial encontrado: {previous_snapshot.value}")
    log_app(f"Posição encontrada: {previous_snapshot.located_by}")

    while True:
        time.sleep(config.poll_interval)

        try:
            current_snapshot = read_current_bid(
                driver,
                config.bid_selector,
                config.bid_selector_type
            )

            if current_snapshot.value != previous_snapshot.value:
                log_app(
                    f"Alteração indentificada no lance: "
                    f"{previous_snapshot.value} -> {current_snapshot.value}"
                )

                notify_bid_change(
                    driver=driver,
                    target_url=config.target_url,
                    input_selector=config.target_input_selector,
                    input_selector_type=config.target_input_selector_type,
                    button_selector=config.target_button_selector,
                    button_selector_type=config.target_button_selector_type,
                    old_value=previous_snapshot.value,
                    new_value=current_snapshot.value
                )

                previous_snapshot = current_snapshot
            else:
                log_app(f"Sem alteração no lance. Valor atual: {current_snapshot.value}")

        except Exception as error:
            log_app(f"Erro durante o monitoramento: {error}")