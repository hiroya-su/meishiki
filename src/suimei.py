from meishiki import build_meishiki
from datetime import datetime as dt

if __name__ == '__main__':

    birthday = dt(year = 1978, month = 9, day = 26, hour = 13, minute = 51)
    sex = 0

    build_meishiki(birthday, sex)
