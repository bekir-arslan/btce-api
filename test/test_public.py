import decimal
import unittest
from btceapi.public import *
import btceapi


class TestPublic(unittest.TestCase):
    def test_getTicker(self):
        connection = btceapi.BTCEConnection()
        info = btceapi.APIInfo(connection)
        for pair in info.pair_names:
            btceapi.getTicker(pair, connection, info)
            btceapi.getTicker(pair, connection)
            btceapi.getTicker(pair, info=info)
            btceapi.getTicker(pair)

    def test_getHistory(self):
        connection = btceapi.BTCEConnection()
        info = btceapi.APIInfo(connection)
        for pair in info.pair_names:
            btceapi.getTradeHistory(pair, connection, info)
            btceapi.getTradeHistory(pair, connection)
            btceapi.getTradeHistory(pair, info=info)
            btceapi.getTradeHistory(pair)

    def test_getDepth(self):
        connection = btceapi.BTCEConnection()
        info = btceapi.APIInfo(connection)
        for pair in info.pair_names:
            btceapi.getDepth(pair, connection, info)
            btceapi.getDepth(pair, connection)
            btceapi.getDepth(pair, info=info)
            btceapi.getDepth(pair)

    def test_constructTrade(self):
        d = {"pair": "btc_usd",
             "trade_type": "bid",
             "price": decimal.Decimal("1.234"),
             "tid": 1,
             "amount": decimal.Decimal("3.2"),
             "date": 1368805684.878004}

        t = Trade(**d)
        self.assertEqual(t.pair, d.get("pair"))
        self.assertEqual(t.trade_type, d.get("trade_type"))
        self.assertEqual(t.price, d.get("price"))
        self.assertEqual(t.tid, d.get("tid"))
        self.assertEqual(t.amount, d.get("amount"))
        assert type(t.date) is datetime
        test_date = datetime.fromtimestamp(1368805684.878004)
        self.assertEqual(t.date, test_date)

        # check conversion of decimal dates
        d["date"] = decimal.Decimal("1368805684.878004")
        t = Trade(**d)
        assert type(t.date) is datetime
        self.assertEqual(t.date, test_date)

        # check conversion of integer dates
        d["date"] = 1368805684
        test_date = datetime.fromtimestamp(1368805684)
        t = Trade(**d)
        assert type(t.date) is datetime
        self.assertEqual(t.date, test_date)

        # check conversion of string dates with no fractional seconds
        d["date"] = "2013-05-17 08:48:04"
        t = Trade(**d)
        assert type(t.date) is datetime
        self.assertEqual(t.date, datetime(2013, 5, 17, 8, 48, 4, 0))

        # check conversion of string dates with fractional seconds
        d["date"] = "2013-05-17 08:48:04.878004"
        t = Trade(**d)
        assert type(t.date) is datetime
        self.assertEqual(t.date,
                         datetime(2013, 5, 17, 8, 48, 4, 878004))

        # check conversion of unicode dates with no fractional seconds
        d["date"] = u"2013-05-17 08:48:04"
        t = Trade(**d)
        assert type(t.date) is datetime
        self.assertEqual(t.date, datetime(2013, 5, 17, 8, 48, 4, 0))

        # check conversion of string dates with fractional seconds
        d["date"] = u"2013-05-17 08:48:04.878004"
        t = Trade(**d)
        assert type(t.date) is datetime
        self.assertEqual(t.date,
                         datetime(2013, 5, 17, 8, 48, 4, 878004))


if __name__ == '__main__':
    unittest.main()
