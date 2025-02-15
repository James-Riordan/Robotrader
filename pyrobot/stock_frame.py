import numpy as np
import pandas as pd

from datetime import time
from datetime import datetime
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

from pandas.core.groupby import DataFrameGroupBy
from pandas.core.window import RollingGroupby

class StockFrame:
    def __init__(self, data: List[dict]) -> None:

        self._data = data
        self._frame: pd.DataFrame = self.create_frame()
        self._symbol_groups: DataFrameGroupBy = None
        self._symbol_rolling_groups: RollingGroupby = None

    @property
    def frame(self) -> pd.DataFrame:
        return self._frame

    @property
    def symbol_groups(self) -> DataFrameGroupBy:

        self._symbol_groups = self._frame.groupby(
            by='symbol',
            as_index=False,
            sort=True
        )

        return self.symbol_groups

    def symbol_rolling_groups(self, size: int) -> RollingGroupby:
        if not self._symbol_groups:
            self.symbol_groups

        self._symbol_rolling_groups = self._symbol_groups.rolling(size)

        return self._symbol_rolling_groups

    def create_frame(self) -> pd.DataFrame:
        
        #Make a dataframe
        price_df = pd.DataFrame(data=self._data)
        price_df = self._parse_datetime_column(price_df=price_df)
        price_df = self._set_multi_index(price=price_df)

        return price_df
    
    def _parse_datetime_column(self, price_df: pd.DataFrame) -> pd.DataFrame:

        price_df['datetime'] = pd.to_datetime(price_df['datetime'], unit='ms', origin='unix')
        
        return price_df
    
    def _set_multi_index(self, price_df: pd.DataFrame) -> pd.DataFrame:

        price_df = price_df.set_index(keys=['symbol', 'datetime'])

        return price_df

    def add_rows(self, data: dict) -> None:
        
        column_names = ['open', 'close', 'high', 'low', 'volume']

        for symbol in data:

            #Parse timestamp
            time_stamp = pd.to_datetime(
                data[symbol]['quoteTimeInLong'], #TODO get_quotes endpoint / quoteTimeInLong changes depending on what api i use
                unit='ms',
                origin='unix'
            )

            # Define our Index
            row_id = (symbol, time_stamp)

            #Define our Values
            row_values = [
                data[symbol]['openPrice'],
                data[symbol]['closePrice'],
                data[symbol]['highPrice'],
                data[symbol]['lowPrice'],
                data[symbol]['askSize'],
                data[symbol]['bidSize']
            ]

            new_row = pd.Series(data=row_values)
            
            # Add the row
            self.frame.loc[row_id, column_names] = new_row.values
            self.frame.sort_index(inplace=True)


    def do_indicators_exist(self, column_names: List[str]) -> bool:
        pass

    def _check_signals(self, indicators: dict) -> Union[pd.Series, None]:
        pass