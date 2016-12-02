import xml.etree.ElementTree
from tkinter import *
from tkinter.ttk import *

def check_xml(xmlfile, configfile):
    e = xml.etree.ElementTree.parse(xmlfile).getroot()

    config_tags = {'madatory_tags': '', 'sum_tags': ''}

    f = open(configfile)
    # фильтруем комментарии
    lines = set(filter(lambda x: not x.startswith('#'), f.read().splitlines()))

    for l in lines:
        par =  l.partition('=')
        tag = par[0].strip()
        value = par[2].strip()
        if tag in config_tags and len(value) > 0:
            config_tags[tag] = list(map(lambda x: x.strip(), value.split(',')))

    tag_sums = dict()
    shareh_errors = dict()

    for shareh in e.find('register_list').findall('shareholder'):
        shreholder_name = shareh.find('./shareholder_info/shareholder_dtls/name').text
        for i in shareh.iter():
            if not i.text and i.tag in config_tags['madatory_tags']:
                if shreholder_name not in shareh_errors:
                    shareh_errors[shreholder_name] = list()
                    shareh_errors[shreholder_name].append(i.tag)
                else:
                    shareh_errors[shreholder_name].append(i.tag)
            if i.tag in config_tags['sum_tags']:
                if i.tag not in tag_sums:
                    tag_sums[i.tag] = int(i.text)
                else:
                    tag_sums[i.tag] = int(tag_sums[i.tag]) + int(i.text)

    return {'errors': shareh_errors, 'sums': tag_sums}

if __name__ == '__main__':
    root = Tk()
    btn = Button(root,  # родительское окно
                 text="Click me",  # надпись на кнопке
                 width=30, height=5,  # ширина и высота
                 bg="white", fg="black")  # цвет фона и надписи
    btn.pack()  # расположить кнопку на главном окне
    root.mainloop()

    result = check_xml('C:\\Users\\p.chavdarov\\Downloads\\03.11.2016.xml', 'cfg.txt')

    print(result['sums'])
    print(result['errors'])