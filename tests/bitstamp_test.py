if __package__ is None or __package__ == '':
    from exchange_clients.bitstamp import Bitstamp
else:
    from ..exchange_clients.bitstamp import Bitstamp

market = 'etheur'
ordertype = 'asks'


def test_api():
    assert Bitstamp.get_orderbook(market) is not None

    assert len(Bitstamp.get_markets()) > 0

    n = 5
    n_last_orders = Bitstamp.get_n_last_orders(ordertype, market, n)
    assert len(n_last_orders) == n
