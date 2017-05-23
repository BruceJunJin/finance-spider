# usage: python main.py 399300 yes
#        python main.py 600001 no
import tushare as ts
import sys
import time
from sqlalchemy import create_engine

def main():
    c = sys.argv[1]
    i = True if sys.argv[2] == "yes" else False
    if not ts.get_h_data(code=c, start=time.strftime("%Y-%m-%d"), end=time.strftime("%Y-%m-%d"), index=i).empty:
        engine = create_engine("postgresql+psycopg2://ecnu:orchid@192.168.1.112:5432/ecnu")
        data = ts.get_k_data(code=c, ktype="5", index = i).tail(48)
        data.to_sql("dt", engine, if_exists='append', index=False)

main()
