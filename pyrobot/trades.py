from datetime import datetime

from typing import List
from typing import Dict
from typing import Union

class Trade:

    def __init__(self):
        
        self.order = {}
        self.trade_id = ""

        self.side = ""
        self.side_opposite = ""
        self.enter_or_exit = ""
        self.enter_or_exit_opposite = ""
        
        self._order_response = {}
        self._triggered_added = False
        self._multi_leg = False


    def new_trade(self, trade_id: str, order_type: str, side: str, enter_or_exit: str, price: float = 0.00, stop_limit_price: float = 0.00) -> Dict:

        self.trade_id = trade_id