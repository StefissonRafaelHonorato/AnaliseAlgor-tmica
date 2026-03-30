from dataclasses import dataclass

@dataclass
class AppConfig:
    user_name: str
    auction_url: str
    bid_selector: str
    bid_selector_type: str
    timeout: int
    poll_interval: int
    target_url: str
    target_input_selector: str
    target_input_selector_type: str
    target_button_selector: str
    target_button_selector_type: str