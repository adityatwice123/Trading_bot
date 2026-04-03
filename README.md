# Binance Futures Testnet Trading Bot

A Python CLI trading bot for placing orders on Binance Futures Testnet (USDT-M).

## Setup

1. Clone the repo:
   git clone https://github.com/YOUR_USERNAME/trading_bot.git
   cd trading_bot

2. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Add your API keys in a `.env` file:
   API_KEY=your_api_key_here
   SECRET_KEY=your_secret_key_here

## How to Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000

### Stop Market Order (Bonus)
python cli.py --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.01 --price 75000

## Assumptions
- Uses Binance Futures USDT-M Testnet only
- LIMIT orders use GTC (Good Till Cancelled) by default
- Logs are saved to logs/trading_bot.log
