from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()

def place_market_order(symbol, side, quantity):
    client = BinanceClient()
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "MARKET",
        "quantity": quantity,
    }
    logger.info(f"Placing MARKET order → {side} {quantity} {symbol}")
    return client.place_order(params)

def place_limit_order(symbol, side, quantity, price):
    client = BinanceClient()
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC",
    }
    logger.info(f"Placing LIMIT order → {side} {quantity} {symbol} @ {price}")
    return client.place_order(params)

def place_stop_market_order(symbol, side, quantity, stop_price):
    client = BinanceClient()
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "STOP_MARKET",
        "quantity": quantity,
        "stopPrice": stop_price,
    }
    logger.info(f"Placing STOP_MARKET order → {side} {quantity} {symbol} @ stop {stop_price}")
    return client.place_order(params)