import datetime as dt
import pandas_datareader.data as web

from machineTime import getMachineData


now = dt.datetime.combine(dt.datetime.now(), dt.time())

date = dt.datetime.fromtimestamp(1588341840)

start =date
end = date + dt.timedelta(days=1)  # dt.datetime.now()

start = dt.datetime(2015, 7, 1)

end = dt.datetime(2020, 7, 14)

'''if(end > now):
    end = date'''
dfs = []
symbols = ["NBEV", "NEM", "AMD", "MKTX", "NVDA", "REGN",
               'NLOK', 'HUM', 'VRTX', 'RMD', 'APPL', 'ODFL', 'MSCI', 'CTXS', 'DVA', 'SBAC', 'TGT', 'DG', 'MSFT', 'LDOS', 'ANSS']
for count, symbol in enumerate(symbols):
  try:
    dfs.append(web.DataReader(symbol, 'yahoo', start, end))
  except:
    pass 
getMachineData(dfs)