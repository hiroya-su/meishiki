from meishiki import build_meishiki
from unsei import build_unsei
from output import output_html, output_stdio
from datetime import datetime as dt

if __name__ == '__main__':

    # birthday = dt(year = 1978, month = 7, day = 18, hour = 14, minute = 47)
    # sex = 1
    birthday = dt(year = 1978, month = 9, day = 26, hour = 13, minute = 51)
    sex = 0
    # birthday = dt(year = 1984, month = 7, day = 17, hour = 18, minute = 25)
    # sex = 0
    # birthday = dt(year = 1983, month = 12, day = 28, hour = 4, minute = 35)
    # sex = 1

    # 命式を組成する
    meishiki = build_meishiki(birthday, sex)

    # 運勢を組成する
    unsei = build_unsei(meishiki)
    
    # 命式・運勢を出力する
    f1 = output_html(meishiki, unsei)
    f2 = output_stdio(meishiki, unsei)
    
    breakpoint()
    
