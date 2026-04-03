import argparse
import sys
from bot.validators import validate_inputs
from bot.orders import place_market_order, place_limit_order, place_stop_market_order
from bot.logging_config import setup_logger

logger = setup_logger()

def print_order_summary(symbol, side, order_type, quantity, price=None):
    print("\n" + "="*50)
    print("         ORDER REQUEST SUMMARY")
    print("="*50)
    print(f"  Symbol     : {symbol.upper()}")
    print(f"  Side       : {side.upper()}")
    print(f"  Order Type : {order_type.upper()}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("="*50 + "\n")

def print_order_response(response):
    print("\n" + "="*50)
    print("         ORDER RESPONSE")
    print("="*50)
    print(f"  Order ID     : {response.get('orderId', 'N/A')}")
    print(f"  Symbol       : {response.get('symbol', 'N/A')}")
    print(f"  Status       : {response.get('status', 'N/A')}")
    print(f"  Side         : {response.get('side', 'N/A')}")
    print(f"  Type         : {response.get('type', 'N/A')}")
    print(f"  Executed Qty : {response.get('executedQty', 'N/A')}")
    print(f"  Avg Price    : {response.get('avgPrice', 'N/A')}")
    print("="*50)
    print("  ✅ ORDER PLACED SUCCESSFULLY")
    print("="*50 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol",   required=True,  help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side",     required=True,  help="BUY or SELL")
    parser.add_argument("--type",     required=True,  help="MARKET, LIMIT, or STOP_MARKET")
    parser.add_argument("--quantity", required=True,  help="Order quantity e.g. 0.01")
    parser.add_argument("--price",    required=False, help="Price for LIMIT or STOP_MARKET")

    args = parser.parse_args()

    errors = validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

    if errors:
        print("\n❌ Validation Errors:")
        for e in errors:
            print(f"   - {e}")
        logger.error(f"Validation failed: {errors}")
        sys.exit(1)

    print_order_summary(args.symbol, args.side, args.type, args.quantity, args.price)

    try:
        order_type = args.type.upper()

        if order_type == "MARKET":
            response = place_market_order(args.symbol, args.side, float(args.quantity))
        elif order_type == "LIMIT":
            response = place_limit_order(args.symbol, args.side, float(args.quantity), float(args.price))
        elif order_type == "STOP_MARKET":
            response = place_stop_market_order(args.symbol, args.side, float(args.quantity), float(args.price))

        print_order_response(response)
        logger.info(f"Order success: ID={response.get('orderId')} Status={response.get('status')}")

    except Exception as e:
        print(f"\n❌ Order Failed: {e}")
        logger.error(f"Order failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()