import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('C:\\Users\\p.chavdarov\\Downloads\\03.11.2016.xml').getroot()

amdatory_tags = {'country', 'address', 'individual_document_type_code'}

UnitSum = 0
for shareh in e.find('register_list').findall('shareholder'):

    for i in shareh.iter():
        dummy = 0
        if not i.text and i.tag in amdatory_tags:
            dummy = dummy + 1
            if dummy == 1:
                print('Владалец: ', shareh.find('./shareholder_info/shareholder_dtls/name').text)
            print(i.tag)

    shareh.find('./security_balances/security_balance/total/units').text
    UnitSum = UnitSum + int(shareh.find('./security_balances/security_balance/total/units').text)

print('UnitSum: ', UnitSum )
