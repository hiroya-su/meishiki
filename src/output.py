import kanshi_data as kd
from jinja2 import Environment, FileSystemLoader
from datetime import datetime as dt

def output_html(meishiki, unsei):
    
    env = Environment(loader = FileSystemLoader('html/'))
    template = env.get_template('template.html')
    
    birthday_str = meishiki.birthday.strftime('%Y年%-m月%-d日 %-H時%-M分生')
    sex_str = '男命' if meishiki.sex == 0 else '女命'

    daiun = unsei.daiun
    nenun = unsei.nenun
    
    content = {'birthday': birthday_str, 'sex': sex_str,
               'tenkan1': kd.kan[meishiki.tenkan[0]], 'chishi1': kd.shi[meishiki.chishi[0]], 'zokan1': kd.kan[meishiki.zokan[0]], 'fortune1': kd.twelve_fortune[meishiki.twelve_fortune[0]], 'tsuhen_tenkan1': kd.tsuhen[meishiki.tsuhen[0]], 'tsuhen_zokan1': kd.tsuhen[meishiki.tsuhen[4]],
               'tenkan2': kd.kan[meishiki.tenkan[1]], 'chishi2': kd.shi[meishiki.chishi[1]], 'zokan2': kd.kan[meishiki.zokan[1]], 'fortune2': kd.twelve_fortune[meishiki.twelve_fortune[1]], 'tsuhen_tenkan2': kd.tsuhen[meishiki.tsuhen[1]], 'tsuhen_zokan2': kd.tsuhen[meishiki.tsuhen[5]],
               'tenkan3': kd.kan[meishiki.tenkan[2]], 'chishi3': kd.shi[meishiki.chishi[2]], 'zokan3': kd.kan[meishiki.zokan[2]], 'fortune3': kd.twelve_fortune[meishiki.twelve_fortune[2]], 'tsuhen_tenkan3': kd.tsuhen[meishiki.tsuhen[2]], 'tsuhen_zokan3': kd.tsuhen[meishiki.tsuhen[6]],
               'tenkan4': kd.kan[meishiki.tenkan[3]], 'chishi4': kd.shi[meishiki.chishi[3]], 'zokan4': kd.kan[meishiki.zokan[3]], 'fortune4': kd.twelve_fortune[meishiki.twelve_fortune[3]], 'tsuhen_tenkan4': kd.tsuhen[meishiki.tsuhen[3]], 'tsuhen_zokan4': kd.tsuhen[meishiki.tsuhen[7]],}
    
    p1 = '&nbsp;' + str(daiun[0][0]) if len(str(daiun[0][0])) == 1 else str(daiun[0][0])
    d_nen = {'p1': p1, 'p2': daiun[1][0], 'p3': daiun[2][0], 'p4': daiun[3][0], 'p5': daiun[4][0], 'p6': daiun[5][0], 'p7': daiun[6][0], 'p8': daiun[7][0], 'p9': daiun[8][0], 'p10': daiun[9][0], 'p11': daiun[10][0],
             'd_tsuhen1': kd.tsuhen[daiun[0][3]], 'd_kan1': kd.kan[daiun[0][1]], 'd_shi1': kd.shi[daiun[0][2]],
             'd_tsuhen2': kd.tsuhen[daiun[1][3]], 'd_kan2': kd.kan[daiun[1][1]], 'd_shi2': kd.shi[daiun[1][2]],
             'd_tsuhen3': kd.tsuhen[daiun[2][3]], 'd_kan3': kd.kan[daiun[2][1]], 'd_shi3': kd.shi[daiun[2][2]],
             'd_tsuhen4': kd.tsuhen[daiun[3][3]], 'd_kan4': kd.kan[daiun[3][1]], 'd_shi4': kd.shi[daiun[3][2]],
             'd_tsuhen5': kd.tsuhen[daiun[4][3]], 'd_kan5': kd.kan[daiun[4][1]], 'd_shi5': kd.shi[daiun[4][2]],
             'd_tsuhen6': kd.tsuhen[daiun[5][3]], 'd_kan6': kd.kan[daiun[5][1]], 'd_shi6': kd.shi[daiun[5][2]],
             'd_tsuhen7': kd.tsuhen[daiun[6][3]], 'd_kan7': kd.kan[daiun[6][1]], 'd_shi7': kd.shi[daiun[6][2]],
             'd_tsuhen8': kd.tsuhen[daiun[7][3]], 'd_kan8': kd.kan[daiun[7][1]], 'd_shi8': kd.shi[daiun[7][2]],
             'd_tsuhen9': kd.tsuhen[daiun[8][3]], 'd_kan9': kd.kan[daiun[8][1]], 'd_shi9': kd.shi[daiun[8][2]],
             'd_tsuhen10': kd.tsuhen[daiun[9][3]], 'd_kan10': kd.kan[daiun[9][1]], 'd_shi10': kd.shi[daiun[9][2]],}
    
    content.update(d_nen)
    
    
    
    
    result = template.render(content)
    with open('html/' + meishiki.birthday.strftime('%Y_%m%d_%H%M_') + str(meishiki.sex) + '.html', 'w') as f:
        f.write(result)
    
    return 1


def output_stdio(meishiki, unsei):

    return 1

