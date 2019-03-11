if __package__ is None or __package__ == '':
    from exchange_clients.cryptomkt import Cryptomkt
else:
    from ..exchange_clients.cryptomkt import Cryptomkt

ordertype = 'bids'
market = 'ETHEUR'


def test_api():
    assert Cryptomkt.get_orderbook(ordertype, market) is not None

    assert len(Cryptomkt.get_markets()) > 0

    n = 5
    n_last_orders = Cryptomkt.get_n_last_orders(ordertype, market, n)
    assert len(n_last_orders) == n
