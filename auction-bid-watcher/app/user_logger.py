import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)

user_logger = logging.getLogger("user_logger")
user_logger.setLevel(logging.INFO)

app_handler = logging.FileHandler(os.path.join(LOG_DIR, "app.log"), encoding="utf-8")
user_handler = logging.FileHandler(os.path.join(LOG_DIR, "user_actions.log"), encoding="utf-8")

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

app_handler.setFormatter(formatter)
user_handler.setFormatter(formatter)

if not app_logger.handlers:
    app_logger.addHandler(user_handler)

if not user_logger.handlers:
    user_logger.addHandler(user_handler)

def log_app(message: str):
    print(message)
    app_logger.info(message)

def log_user_action(user_name: str, action: str):
    message = f"Usuário: {user_name} | Ação: {action}"
    print(message)
    user_logger.info(message)
