from datetime import datetime
if __package__ is None or __package__ == '':
    # uses current directory visibility
    from config import DEBUG_MODE_ON, COLORS, MARKETS, EXCHANGES
else:
    # uses current package visibility
    from .config import DEBUG_MODE_ON, COLORS, MARKETS, EXCHANGES


def say(msg, level=0):
    if DEBUG_MODE_ON:
        print(COLORS[level] + msg + COLORS[0])


if __name__ == '__main__':

    timestamp = str(datetime.now())
    say('Starting pyarboto at ' + timestamp)
    say('Searching for arbitrage opportunities')
    say('Fetching pairs: ' + str(MARKETS))
    say('From: ')
    for exch in EXCHANGES:
        say('\t' + exch)

    order_types = ['bids', 'asks']
    fee = 0.5/100  # assuming a relatively high fee of .5%

    for mkt in MARKETS:
        hi_bid = 0
        hi_bid_vol = -1
        hi_bid_exch = ""
        lo_ask = 1e10
        lo_ask_vol = -1
        lo_ask_exch = ""
        for key in EXCHANGES:
            client = EXCHANGES[key]
            if mkt in client.get_markets():
                order_type = 'bids'
                data = client.get_n_last_orders(order_type, mkt, 1)
                if data:
                    data = data[0]
                    price = float(data['price'])
                    vol = float(data['amount'])
                    if price > hi_bid:
                        hi_bid = price
                        hi_bid_vol = vol
                        hi_bid_exch = key
                order_type = 'asks'
                data = client.get_n_last_orders(order_type, mkt, 1)
                if data:
                    data = data[0]
                    price = float(data['price'])
                    vol = float(data['amount'])
                    if price < lo_ask:
                        lo_ask = price
                        lo_ask_vol = vol
                        lo_ask_exch = key

        if hi_bid > lo_ask:
            roi = (hi_bid*(1-fee)/(lo_ask*(1+fee)) - 1)*100
            roi_gross = (hi_bid/lo_ask - 1)*100
            say("An arbitrage opportunity has been found for " + mkt, 3)
            say("Highest bid of " + str(hi_bid) + " in " + hi_bid_exch)
            say("Lowest ask " + str(lo_ask) + "in " + lo_ask_exch)
            say("Gross ROI: " + str(roi_gross) + '%')
            say("Estimated net ROI: " + str(roi) + '%')
            say("Potential revenue: " +
                str((roi/100)*min(hi_bid_vol, lo_ask_vol)*lo_ask))
        else:
            roi = 0
            say("No arbitrage opportunity found for " + mkt)
