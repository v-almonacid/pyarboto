if __package__ is None or __package__ == '':
    from exchange_clients.buda import Buda
else:
    from ..exchange_clients.buda import Buda

market = 'ETHBTC'
ordertype = 'asks'


def test_api():
    assert Buda.get_orderbook(market) is not None

    assert len(Buda.get_markets()) > 0

    n = 5
    n_last_orders = Buda.get_n_last_orders(ordertype, market, n)
    assert len(n_last_orders) == n
