from vnstock import Vnstock
import pandas as pd, os

os.makedirs("datack", exist_ok=True)

tickers = ["VIC", "VHM", "VNM", "HPG", "VCB", "BID", "CTG", "MBB", "TCB", "FPT"]

for code in tickers:
    stock = Vnstock().stock(symbol=code, source='VCI')
    df = stock.quote.history(start='1990-01-01', end='2025-10-01')
    df = df[['time', 'open', 'high', 'low', 'close', 'volume']]
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    df.to_csv(f"datack/{code}.csv", index=False)
    print(f"Đã lưu {code}.csv")