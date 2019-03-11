import abc


class ExchangeClientInterface(abc.ABC):

    @abc.abstractmethod
    def get_n_last_orders(self, ordertype, market, n):
        """
        :param ordertype: <str> 'bids' or 'asks'
        :param market: <str> in the form <^\w{3}-?\w{3}\Z'> e.g. 'etheur' or
        'eth-eur'
        :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
        """
        pass

    @abc.abstractmethod
    def get_orderbook(self, market):
        """
        returns the orderbook in json format. The actual output format depends
        on the specific API endpoint.
        :param market: <str> in the form <^\w{3}-?\w{3}\Z'> e.g. 'etheur' or
        'eth-eur'
        :return <dict>
        """
        pass

    @abc.abstractmethod
    def get_markets(self):
        """
        Returns a list of all available markets in this exchange in the format:
        ['ETHCLP', 'ETHBTC',...]
        The method must be implemented taking care of this output syntaxis.
        :return <list>
        """
        pass
