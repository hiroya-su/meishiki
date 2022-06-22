from jinja2 import Environment, FileSystemLoader
from datetime import datetime as dt

def output_html(meishiki, unsei):
    
    env = Environment(loader = FileSystemLoader('html/'))
    template = env.get_template('template.html')
    
    birthday_str = meishiki.birthday.strftime('%Y年%-m月%-d日 %-H時%-M分生')
    sex_str = '男命' if meishiki.sex == 0 else '女命'
    
    content = {'birthday': birthday_str, 'sex': sex_str}
    
    result = template.render(content)
    with open('html/' + meishiki.birthday.strftime('%Y_%m%d_%H%M_') + str(meishiki.sex) + '.html', 'w') as f:
        f.write(result)
    
    return 1


def output_stdio(meishiki, unsei):

    return 1

