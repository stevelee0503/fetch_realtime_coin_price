import requests
import time

SYMBOLS = ('BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'SANDUSDT', 'ETCUSDT')  # defining coins to fetch


def fetch_coin_price(coin):
    """
    Fetch coin price from Binance API
    :param coin:
    :return:
    """
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}"  # defining key/request url
    data = requests.get(key) # requesting data from url
    data = data.json() # converting data to json
    print(f"{data['symbol']} price is {float(data['price']): .1f}")  # printing coin price


def main():
    while True:
        for coin in SYMBOLS:
            fetch_coin_price(coin)
        time.sleep(1)


if __name__ == "__main__":
    main()
