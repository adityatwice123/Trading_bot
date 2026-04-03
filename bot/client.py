import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.secret_key = os.getenv("SECRET_KEY")

        if not self.api_key or not self.secret_key:
            raise ValueError("API_KEY or SECRET_KEY missing in .env file")

        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        })

    def _sign(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self.secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, params: dict) -> dict:
        signed_params = self._sign(params)
        url = f"{BASE_URL}/fapi/v1/order"
        logger.debug(f"REQUEST → POST {url} | Params: {params}")

        try:
            response = self.session.post(url, data=signed_params)
            response.raise_for_status()
            data = response.json()
            logger.debug(f"RESPONSE ← {data}")
            return data

        except requests.exceptions.HTTPError as e:
            error_body = e.response.json() if e.response else {}
            logger.error(f"HTTP Error: {e} | Response: {error_body}")
            raise

        except requests.exceptions.ConnectionError:
            logger.error("Network error: Could not connect to Binance Testnet.")
            raise

        except requests.exceptions.Timeout:
            logger.error("Request timed out.")
            raise