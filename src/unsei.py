import kanshi_data as kd
from meishiki import is_setsuiri
from dataclasses import field, dataclass
from datetime import datetime

@dataclass(slots = True)
class Unsei:

    daiun: list[int] = field(default_factory = list)
    nenun: list[int] = field(default_factory = list)
    


def convert_year_ratio(birthday):
    
    # ＜機能＞
    # 生年月日から前の節入日までの日数と、生年月日から次の節入日までの日数との比を、
    # 10年に占める割合に直す。
    # 例：8日：22日→3年：7年
    # ＜入力＞
    #   - brithday（datetime）：生年月日
    # ＜出力＞
    #   - year_ratio_list（list）：10年に占める割合
    
    for i, s in enumerate(kd.setsuiri):
        p = is_setsuiri(birthday, birthday.month)
        if (s[0] == birthday.year) and (s[1] == birthday.month):
            if not p:
                k = kd.setsuiri[i+1]
                previous_setsuiri = datetime(year = s[0], month = s[1], day = s[2], hour = s[3], minute = s[4])
                next_setsuiri = datetime(year = k[0], month = k[1], day = k[2], hour = k[3], minute = k[4])
            else:
                k = kd.setsuiri[i-1]
                previous_setsuiri = datetime(year = k[0], month = k[1], day = k[2], hour = k[3], minute = k[4])
                next_setsuiri = datetime(year = s[0], month = s[1], day = s[2], hour = s[3], minute = s[4])
            break
        
    diff_previous = birthday - previous_setsuiri   # 生年月日から前の節入日までの日数
    diff_next = next_setsuiri - birthday           # 生年月日から次の節入日までの日数
    
    # ３日間を１年に置き換えるので、３除した値を丸める
    p_year = round((diff_previous.days + (diff_previous.seconds / 60 / 60 / 24)) / 3)
    n_year = round((diff_next.days + (diff_next.seconds / 60 / 60 / 24)) / 3)
    
    year_ratio_list = [p_year, n_year]
    
    return year_ratio_list


def is_junun_gyakuun(sex, y_kan):
    
    # ＜機能＞
    # 大運が順運か逆運かを判定する
    # ＜入力＞
    #   - y_kan（int）：年柱天干の番号
    #   - self.sex（int）：性別の番号
    # ＜出力＞
    #   - 順運（1）または逆運（0）の二値
    # ＜異常検出＞
    # 取得できなかった場合はエラーメッセージを出力して強制終了する
    
    if (((y_kan % 2) == 0) and (sex == 0)) or (((y_kan % 2) == 1) and (sex == 1)):
        return 1   # 年柱天干が陽干の男命 or 年柱天干が陰干の女命は、順運
        
    elif (((y_kan % 2) == 1) and (sex == 0)) or (((y_kan % 2) == 0) and (sex == 1)):
        return 0   # 年柱天干が陽干の女命 or 年柱天干が陰干の男命は、逆運
    
    else:
        print('大運の順逆を判定できませんでした。')
        exit()
        

def find_kanshi_idx(kan, shi, p):
    
    # 六十干支表から所定の干支のインデクスを返す
    
    for idx, sk in enumerate(kd.sixty_kanshi):
        if (sk[0] == kan) and (sk[1] == shi):
            return idx + p
            
    print('干支が見つかりませんでした。')
    exit()


# def is_hogo(chishi_p):

#     # 方合の有無を判定する
#     for i, h in enumerate(kd.hogo):
#         if (h[0][0] in chishi_p) and (h[0][1] in chishi_p) and (h[0][2] in chishi_p):
#             return i
#     return -1


def is_hogo(chishi, shi):
    
    # 方合の有無を判定する
    for i, h in enumerate(kd.hogo):
        hg = [j for j in h[0]]
        if shi in hg:
            hg.remove(shi)
            if (hg[0] in chishi) and (hg[1] in chishi):
                return i
    return -1


# def is_sango(chishi_p):

#     # 三合の有無を判定する
#     for i, s in enumerate(kd.sango):
#         if (s[0][0] in chishi_p) and (s[0][1] in chishi_p) and (s[0][2] in chishi_p):
#             return i
#     return -1


def is_sango(chishi, shi):

    # 三合の有無を判定する
    for i, s in enumerate(kd.sango):
        sg = [j for j in s[0]]
        if shi in sg:
            sg.remove(shi)
            if (sg[0] in chishi) and (sg[1] in chishi):
                return i
    return -1


def is_hankai(chishi, shi):

    # 半会の有無を判定する
    for i, h in enumerate(kd.hankai):
        if ((h[0][0] in chishi) and (h[0][1] in [shi])) or ((h[0][0] in [shi]) and (h[0][1] in chishi)):
            return i
    return -1


def is_tensen_chichu(nisshi, tsuhen, shi):
    
    if (nisshi == kd.hitsuchu_rev[shi]) and (tsuhen == 6):
        return 1
    return -1
    

def is_chu(chishi, shi):
    
    ch = [chishi[0]] + [-1] + [chishi[2]] + [chishi[3]]
    for i, s in enumerate(ch):
        if s == kd.hitsuchu_nodir[shi]:
            return i
    return -1


def is_kei(chishi, shi):
    
    for i, s in enumerate(chishi):
        if s == kd.kei[shi]:
            return i
    return -1


def is_gai(chishi, shi):

    for i, s in enumerate(chishi):
        if s == kd.gai[shi]:
            return i
    return -1

    
def append_daiun(meishiki):
    
    # ＜機能＞
    # 大運を命式に追加する

    daiun = []
    year_ratio_list = convert_year_ratio(meishiki.birthday)

    if is_junun_gyakuun(meishiki.sex, meishiki.nenchu[0]):  # 順運か逆運か？
        ry = year_ratio_list[1]  # 次の節入日が立運の起算日
        p = 1                    # 六十干支表を順にたどる
    else:
        ry = year_ratio_list[0]  # 前の節入日が立運の起算日
        p = -1                   # 六十干支表を逆にたどる
        
    idx = find_kanshi_idx(meishiki.getchu[0], meishiki.getchu[1], p)
    
    for n in list(range(10, 140, 10)):
        
        if idx >= 60:
            idx = 0
        kan, shi = kd.sixty_kanshi[idx]
        tsuhen = kd.kan_tsuhen[meishiki.nikkan].index(kan)
        
        chishi_p = [i for i in meishiki.chishi] + [shi]
        
        hogo = is_hogo(meishiki.chishi, shi)    # 方合
        sango = is_sango(meishiki.chishi, shi)  # 三合
        if sango == -1:
            hankai = is_hankai(meishiki.chishi, shi)  # 半会
        else:
            hankai = -1
        tc = is_tensen_chichu(meishiki.nitchu[1], tsuhen, shi)  # 天戦地冲
        if tc == -1:
            chu = is_chu(meishiki.chishi, shi)  # 冲
        else:
            chu = -1
        kei = is_kei(meishiki.chishi, shi)  # 刑
        gai = is_gai(meishiki.chishi, shi)  # 害
        
        daiun.append([ry, kan, shi, tsuhen, hogo, sango, hankai, tc, chu, kei, gai])
        ry += 10
        idx += p

    breakpoint()
    return daiun

    
def append_nenun(meishiki, daiun):
    
    # ＜機能＞
    # 年運を命式に追加する

    nenun = []
    idx = (meishiki.birthday.year - 3) % 60 - 1 # + self.meishiki.is_setsuiri(2)
    ry = daiun[0][0]
    d_idx = 0
    
    for n in list(range(0, 120)):
        kan, shi = kd.sixty_kanshi[idx]
        tsuhen = kd.kan_tsuhen[meishiki.nikkan].index(kan)

        if (n != ry) and (n % 10 == ry):
            d_idx += 1
        
        if n >= ry:
            chishi_r = [i for i in meishiki.chishi] + [shi]
            chishi_p = [i for i in meishiki.chishi] + [daiun[d_idx][2]] + [shi]
            
            if daiun[d_idx][4] == -1:
                hogo = is_hogo(chishi_p)  # 方合
            else:
                hogo = is_hogo(chishi_r)
            
            if daiun[d_idx][5] == -1:     # 三合
                sango = is_sango(chishi_p)
                if sango == -1:
                    hankai = 1            # 半会（未実装）
                else:
                    hankai = -1
            else:
                sango = is_sango(chishi_r)
                if sango == -1:
                    hankai = 1            # 半会（未実装）
                else:
                    hankai = -1
            
            tc1 = is_tensen_chichu(meishiki.nitchu[1], tsuhen, shi)  # 天戦地冲（命式）
            tc2 = is_tensen_chichu(daiun[d_idx][2], kd.kan_tsuhen[daiun[d_idx][1]].index(kan), shi)  # 天戦地冲（大運）
            if tc1 == 1:
                tc = 1
            elif tc2 == 1:
                tc = 2
            else:
                tc = -1
            
            nenun.append([n, kan, shi, tsuhen, hogo, sango, hankai, tc])
            
        idx += 1
        if idx >= 60:
            idx = 0

    return nenun


def build_unsei(meishiki):

    # 大運を得る
    daiun = append_daiun(meishiki)

    # 年運を得る
    nenun = append_nenun(meishiki, daiun)

    unsei = Unsei(daiun, nenun)

    return unsei
