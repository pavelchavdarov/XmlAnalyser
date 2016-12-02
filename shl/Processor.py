import xml.etree.ElementTree

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

    print(config_tags)

    tag_sums = dict()
    shareh_errors = dict()

    for shareh in e.find('register_list').findall('shareholder'):
        shreholder_name = shareh.find('./shareholder_info/shareholder_dtls/name').text
        for i in shareh.iter():
            dummy = 0
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

    print(tag_sums)
    print(shareh_errors)

check_xml('C:\\Users\\p.chavdarov\\Downloads\\03.11.2016.xml', 'C:\\Users\\p.chavdarov\\Downloads\\cfg.txt')