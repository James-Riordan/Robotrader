import pandas as pd
import robin_stocks as r

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

# class PyRobot():

#     def __init__(self, client_id: str, redirect_uri: str, credentials_path: str = None, trading_account: str = None) -> None:
        

#         self.trading_account: str = trading_account
#         self.client_id: str = client_id
#         self.redirect_uri: str = redirect_uri
#         self.credentials_path: str = credentials_path
#         self.session: r = self._create_session()
#         self.trades: dict = {}
#         self.historical_prices: dict = {}
#         self.stock_frame = None
 
#     def _create_session(self) -> r:
     


class PyRobot:
    def __init__(self):
        pass

    def login(self, username: str, password: str):
        r.login(username, password)


    # TODO config capabilities for non-us markets
    @property
    def pre_market_open(self) -> bool:

        pre_market_start_time = datetime.now().replace(hour=12, minutes=00, second=00, tzinfo=timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour=13, minutes=30, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_start_time >= right_now >= pre_market_start_time:
            return True
        else: 
            return False
    @property
    def post_market_open(self) -> bool:

        post_market_end_time = datetime.now().replace(hour=22, minutes=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minutes=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if post_market_end_time >= right_now >= market_end_time:
            return True
        else: 
            return False

    @property
    def regular_market_open(self) -> bool:

        market_start_time = datetime.now().replace(hour=13, minutes=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minutes=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_end_time >= right_now >= market_start_time:
            return True
        else: 
            return False


    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List[Dict]:
        pass


    