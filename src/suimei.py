from meishiki import build_meishiki
from datetime import datetime as dt

if __name__ == '__main__':

    # birthday = dt(year = 1978, month = 7, day = 18, hour = 14, minute = 47)
    # sex = 1
    birthday = dt(year = 1978, month = 9, day = 26, hour = 13, minute = 51)
    sex = 0

    build_meishiki(birthday, sex)
