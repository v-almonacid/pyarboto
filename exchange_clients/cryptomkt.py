""" Cryptomkt API client implementation.
    Cryptomkt currently supports the following markets:
        ETHCLP
        ETHARS
        ETHEUR
        ETHBRL
        XLMCLP
        XLMARS
        XLMEUR
        XLMBRL
        BTCCLP
        BTCARS
        BTCEUR
        BTCBRL
"""
import requests
if __package__ is None or __package__ == '':
    # uses current directory visibility
    from exchange_client_interface import ExchangeClientInterface
else:
    # uses current package visibility
    from .exchange_client_interface import ExchangeClientInterface


class Cryptomkt(ExchangeClientInterface):

    order_dict = {'bids': 'buy', 'asks': 'sell'}

    @staticmethod
    def get_n_last_orders(ordertype, market, n):
        """
        :param ordertype: <str> 'bids' or 'asks'
        :param market: <str> e.g. 'etheur' or 'eth-eur'
        :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
        """
        r = Cryptomkt.get_orderbook(ordertype, market)
        last_orders = []
        if r is not None:
            for elem in r['data'][0:n]:
                last_orders.append(
                    {'price': elem['price'], 'amount': elem['amount']}
                )
        return last_orders

    @staticmethod
    def get_orderbook(ordertype, market):
        """
        returns bids or asks from the orderbook in json format
        :param ordertype: <str> 'buy' or 'sell'
        :param market: <str> e.g. 'etheur' or 'eth-eur'
        """
        market = market.replace('-', '')
        order = Cryptomkt.order_dict[ordertype]
        payload = {'market': market, 'type': order, 'page': 0}
        r = requests.get("https://api.cryptomkt.com/v1/book", params=payload)
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None

    @staticmethod
    def get_markets():
        """
        returns a list of all available markets in this exchange in the format
        ['ETHCLP', 'BTCCLP', ...]
        :return: <list>
        """
        markets = []
        r = requests.get("https://api.cryptomkt.com/v1/market")
        if r.status_code == requests.codes.ok:
            for mkt in r.json()['data']:
                markets.append(mkt.upper())
        return markets
