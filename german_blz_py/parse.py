import codecs

LENGTHS = (
    ('blz', '10000000'),
    ('type', '1'),
    ('name', "Volksbank Chemnitz                                        "),
    ('plz', '10591'),
    ('city', 'Berlin                             '),
    ('name_short', 'BBk Berlin                 '),
    ('pan', '20100'),
    ('bic', 'MARKDEF1100'),
    ('checksum', '09'),
    ('id', '011380'),
    ('change_type', 'U'),
    ('succsessor_blz', '000000000')
)


def parse_bic_db(filename):
    f = codecs.open(filename, "r", "iso-8859-1")

    blz_to_bic = {}
    pan_to_bic = {}

    for line in f:
        record = {}
        offset = 0
        for spec in LENGTHS:
            length = len(spec[1])
            value = line[offset:offset + length]
            record[spec[0]] = value
            offset += length
        if record['type'] == u'1':
            pan_to_bic[record['pan']] = record['bic']
        if not record['pan'] in pan_to_bic:
            continue
        blz_to_bic[record['blz']] = pan_to_bic[record['pan']]

    return blz_to_bic
