import kanshi_data as kd
from dataclasses import dataclass
from datetime import datetime

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
    #   なし
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


def build_meishiki(birthday, sex):
    print(find_year_kanshi(birthday))


