import kanshi_data as kd
from jinja2 import Environment, FileSystemLoader
from datetime import datetime as dt

def output_html(meishiki, unsei):
    
    env = Environment(loader = FileSystemLoader('html/'))
    template = env.get_template('template.html')
    
    birthday_str = meishiki.birthday.strftime('%Y年%-m月%-d日 %-H時%-M分生')
    sex_str = '男命' if meishiki.sex == 0 else '女命'
    
    content = {'birthday': birthday_str, 'sex': sex_str,
               'tenkan1': kd.kan[meishiki.tenkan[0]], 'chishi1': kd.shi[meishiki.chishi[0]], 'zokan1': kd.kan[meishiki.zokan[0]], 'fortune1': kd.twelve_fortune[meishiki.twelve_fortune[0]], 'tsuhen_tenkan1': kd.tsuhen[meishiki.tsuhen[0]], 'tsuhen_zokan1': kd.tsuhen[meishiki.tsuhen[4]],
               'tenkan2': kd.kan[meishiki.tenkan[1]], 'chishi2': kd.shi[meishiki.chishi[1]], 'zokan2': kd.kan[meishiki.zokan[1]], 'fortune2': kd.twelve_fortune[meishiki.twelve_fortune[1]], 'tsuhen_tenkan2': kd.tsuhen[meishiki.tsuhen[1]], 'tsuhen_zokan2': kd.tsuhen[meishiki.tsuhen[5]],
               'tenkan3': kd.kan[meishiki.tenkan[2]], 'chishi3': kd.shi[meishiki.chishi[2]], 'zokan3': kd.kan[meishiki.zokan[2]], 'fortune3': kd.twelve_fortune[meishiki.twelve_fortune[2]], 'tsuhen_tenkan3': kd.tsuhen[meishiki.tsuhen[2]], 'tsuhen_zokan3': kd.tsuhen[meishiki.tsuhen[6]],
               'tenkan4': kd.kan[meishiki.tenkan[3]], 'chishi4': kd.shi[meishiki.chishi[3]], 'zokan4': kd.kan[meishiki.zokan[3]], 'fortune4': kd.twelve_fortune[meishiki.twelve_fortune[3]], 'tsuhen_tenkan4': kd.tsuhen[meishiki.tsuhen[3]], 'tsuhen_zokan4': kd.tsuhen[meishiki.tsuhen[7]],}
    
    result = template.render(content)
    with open('html/' + meishiki.birthday.strftime('%Y_%m%d_%H%M_') + str(meishiki.sex) + '.html', 'w') as f:
        f.write(result)
    
    return 1


def output_stdio(meishiki, unsei):

    return 1

