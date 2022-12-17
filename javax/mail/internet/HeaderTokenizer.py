RFC822 = "String  \"()<>@,;:\\\\"\t .[]\""
MIME = "String  \"()<>@,;:\\\\"\t []/?=\""
ATOM = "int  -1"
QUOTEDSTRING = "int  -2"
COMMENT = "int  -3"
EOF = "int  -4"
def getRemainder():
    '''returns String\n\n
    getRemainder()\n
    '''
def ():
    '''returns Token\n\n
    (final String header)\n
    (final String header, final String delimiters)\n
    (final String header, final String delimiters, final boolean skipComments)\n
    (final int type, final String value)\n
    '''
def next():
    '''returns Token\n\n
    next()\n
    '''
def peek():
    '''returns Token\n\n
    peek()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
