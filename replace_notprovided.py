import sys

from german_blz_py import parse

db_file = sys.argv[1]
sepa_file = sys.argv[2]

import xml.etree.ElementTree as ET

blz_to_bic =  parse.parse_bic_db(db_file)

ns = {'sepa': 'urn:iso:std:iso:20022:tech:xsd:pain.008.003.02'}

tree = ET.parse(sepa_file)
root = tree.getroot()

transactions = root.find('sepa:CstmrDrctDbtInitn', ns).find('sepa:PmtInf', ns)

for tx in transactions.findall('sepa:DrctDbtTxInf', ns):
    IBAN = tx.find('sepa:DbtrAcct', ns).find('sepa:Id', ns).find('sepa:IBAN', ns).text
    BLZ = IBAN[len('DE12'):len('DE12')+8]
    BIC = tx.find('sepa:DbtrAgt', ns).find('sepa:FinInstnId', ns).find('sepa:BIC', ns)
    BIC.text = blz_to_bic[BLZ]

tree.write(sepa_file + '.new')


