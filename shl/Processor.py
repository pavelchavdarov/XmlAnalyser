import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('C:\\Users\\p.chavdarov\\Downloads\\03.11.2016.xml').getroot()

# madatory_tags = ['country', 'address', 'individual_document_type_code']
config_tags = {'madatory_tags':''}
lines = {}
with open('C:\\Users\\p.chavdarov\\Downloads\\cfg.txt') as f:
    lines = f.read().splitlines()

lines = set(filter(lambda x: not x.startswith('#'), lines))

for l in lines:
    par =  l.partition('=')
    tag = par[0].strip()
    value = par[2].strip()
    if tag in config_tags and len(value) > 0:
        config_tags[tag] = list(map(lambda x: x.strip(), value.split(',')))

print(config_tags)



UnitSum = 0
for shareh in e.find('register_list').findall('shareholder'):
    for i in shareh.iter():
        dummy = 0
        if not i.text and i.tag in config_tags['madatory_tags']:
            dummy = dummy + 1
            if dummy == 1:
                print('Владалец: ', shareh.find('./shareholder_info/shareholder_dtls/name').text)
            print(i.tag)

    UnitSum = UnitSum + int(shareh.find('./security_balances/security_balance/total/units').text)

print('UnitSum: ', UnitSum )
