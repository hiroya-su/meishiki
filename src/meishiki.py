import kanshi_data as kd
from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta


@dataclass(slots = True)
class Meishiki:

    birthday: datetime
    sex: int


def is_setsuiri(birthday, month):
    
    # ＜機能＞
    # birthday の年月日が、month で与えられた月に対して節入りしているか否かを判定する
    # ＜入力＞
    #   - month（int）：基準となる月
    # ＜出力＞
    #   - 節入りしている（0）またはしていない（-1）の二値
    # ＜異常検出＞
    # 判定不可能の場合はエラーメッセージを出力して強制終了する
    
    for s in kd.setsuiri:
        if (s[0] == birthday.year) and (s[1] == month):
            _setsuiri = datetime(year = s[0], month = s[1], day = s[2], hour = s[3], minute = s[4])
            if _setsuiri < birthday:
                return 0    # 節入りしている
            else:
                return -1   # 節入りしていない
            
    print('節入りを判定できませんでした。')
    exit()


def find_year_kanshi(birthday):
    
    # ＜機能＞
    # birthday の生年月日の年干支を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    # ＜出力＞
    #   - y_kan（int）：年干の番号
    #   - y_shi（int）：年支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する
    
    sixty_kanshi_idx = (birthday.year - 3) % 60 - 1 + is_setsuiri(birthday, 2)
    try:
        y_kan, y_shi = kd.sixty_kanshi[sixty_kanshi_idx]
        return y_kan, y_shi
    except:
        print('年干支の計算で例外が送出されました。')
        exit()


def find_month_kanshi(birthday, y_kan):
    
    # ＜機能＞
    # birthday の生年月日の月干支を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - y_kan（int）：年干の番号
    # ＜出力＞
    #   - m_kan（int）：月干の番号
    #   - m_shi（int）：月支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する
    
    month = birthday.month - 1 + is_setsuiri(birthday, birthday.month)
    try:
        m_kan, m_shi = kd.month_kanshi[y_kan][month]
        return m_kan, m_shi
    except:
        print('月干支の計算で例外が送出されました。')
        exit()


def find_day_kanshi(birthday):
    
    # ＜機能＞
    # birthday で与えられた生年月日の日干支を取得する
    # ＜入力＞
    #   - birthday（daytime）：誕生日
    # ＜出力＞
    #   - d_kan（int）：日干の番号
    #   - d_shi（int）：日支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する
    
    d = birthday.day + kd.kisu_table[birthday.year - 1926][birthday.month - 1] - 1
    if d >= 60:
        d -= 60  # d が 60 を超えたら 60 を引く
        
    try:
        d_kan, d_shi = kd.sixty_kanshi[d]
        return d_kan, d_shi
    except:
        print('日干支の計算で例外が送出されました。')
        exit()


def find_time_kanshi(birthday, d_kan):
    
    # ＜機能＞
    # birthday で与えられた生年月日の時干支を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - d_kan（int）：日干の番号
    # ＜出力＞
    #   - t_kan（int）：時干の番号
    #   - t_shi（int）：時支の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する
    
    time_span = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 24]
    
    for i in range(len(time_span) - 1):
        
        from_dt = datetime(year = birthday.year, month = birthday.month, day = birthday.day,
                           hour = time_span[i], minute = 0)

        if (i == 0) or (i == len(time_span)):
            to_dt = from_dt + timedelta(hours = 0, minutes = 59)
        else:
            to_dt = from_dt + timedelta(hours = 1, minutes = 59)
        
        if from_dt <= birthday <= to_dt:
            try:
                t_kan, t_shi = kd.time_kanshi[d_kan][i]
                return t_kan, t_shi
            except:
                print('時干支の計算で例外が送出されました。')
                exit()

    print('時干支を得られませんでした。')
    exit()        


def find_zokan(birthday, shi):
    
    # ＜機能＞
    # birthday で与えられた生年月日の shi に対応する蔵干を取得する
    # ＜入力＞
    #   - birthday（datetime）：誕生日
    #   - shi（int）：年支、月支、日支、時支の番号
    # ＜出力＞
    #   - z_kan（int）：蔵干の番号
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する
        
    p = is_setsuiri(birthday, birthday.month)
    for s in kd.setsuiri:
        if (s[0] == birthday.year) and (s[1] == birthday.month):
            if s[1] + p <= 0:
                y = s[0] - 1
                m = 12
            else:
                y = s[0]
                m = s[1] + p
            _setsuiri =  datetime(year = y, month = m, day = s[2], hour = s[3], minute = s[4])

    if shi == 6:
        delta1 = timedelta(days = kd.zokan_time[shi][0][0], hours = kd.zokan_time[shi][0][1])
        delta2 = timedelta(days = kd.zokan_time[shi][1][0], hours = kd.zokan_time[shi][1][1])
    else:
        delta = timedelta(days = kd.zokan_time[shi][0], hours = kd.zokan_time[shi][1])

    try:
        if shi == 6:
            if _setsuiri + delta1 >= birthday:
                zokan = kd.zokan[shi][0]
            elif _setsuiri + delta1 < birthday <= _setsuiri + delta2:
                zokan = kd.zokan[shi][1]
            else:
                zokan = kd.zokan[shi][2]
        else:
            if _setsuiri + delta >= birthday:
                zokan = kd.zokan[shi][0]
            else:
                zokan = kd.zokan[shi][1]
        return zokan
    except:
        print('蔵干の計算で例外が送出されました。')
        exit()
    
            
def build_meishiki(birthday, sex):

    # 天干・地支を得る
    y_kan, y_shi = find_year_kanshi(birthday)
    m_kan, m_shi = find_month_kanshi(birthday, y_kan)
    d_kan, d_shi = find_day_kanshi(birthday)
    t_kan, t_shi = find_time_kanshi(birthday, d_kan)
    
    # 蔵干を得る
    y_zkan = find_zokan(birthday, y_shi)
    m_zkan = find_zokan(birthday, m_shi)
    d_zkan = find_zokan(birthday, d_shi)
    t_zkan = find_zokan(birthday, t_shi)
    
    tenkan = [y_kan, m_kan, d_kan, t_kan]
    chishi = [y_shi, m_shi, d_shi, t_shi]
    zokan = [y_zkan, m_zkan, d_zkan, t_zkan]

    nenchu = [y_kan, y_shi, y_zkan]
    getchu = [m_kan, m_shi, m_zkan]
    nitchu = [d_kan, d_shi, d_zkan]
    jichu  = [t_kan, t_shi, t_zkan]
    
    
    
