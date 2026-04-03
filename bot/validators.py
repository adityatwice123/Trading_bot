VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT", "STOP_MARKET"]

def validate_inputs(symbol, side, order_type, quantity, price=None):
    errors = []

    if not symbol or len(symbol) < 3:
        errors.append("Invalid symbol. Example: BTCUSDT")

    if side.upper() not in VALID_SIDES:
        errors.append(f"Invalid side '{side}'. Must be BUY or SELL.")

    if order_type.upper() not in VALID_ORDER_TYPES:
        errors.append(f"Invalid order type '{order_type}'. Must be MARKET, LIMIT, or STOP_MARKET.")

    try:
        qty = float(quantity)
        if qty <= 0:
            errors.append("Quantity must be greater than 0.")
    except ValueError:
        errors.append("Quantity must be a number.")

    if order_type.upper() in ["LIMIT", "STOP_MARKET"]:
        if price is None:
            errors.append("Price is required for LIMIT and STOP_MARKET orders.")
        else:
            try:
                p = float(price)
                if p <= 0:
                    errors.append("Price must be greater than 0.")
            except ValueError:
                errors.append("Price must be a number.")

    return errors