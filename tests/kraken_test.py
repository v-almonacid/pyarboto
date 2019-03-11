if __package__ is None or __package__ == '':
    from exchange_clients.kraken import Kraken
else:
    from ..exchange_clients.kraken import Kraken

market = 'etheur'
ordertype = 'asks'


def test_api():
    assert Kraken.get_orderbook(market) is not None

    assert len(Kraken.get_markets()) > 0

    n = 5
    n_last_orders = Kraken.get_n_last_orders(ordertype, market, n)
    assert len(n_last_orders) == n
