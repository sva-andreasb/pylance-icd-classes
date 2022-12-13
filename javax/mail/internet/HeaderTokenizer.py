RFC822 = "String  \"()<>@,;:\\\\"\t .[]\""
MIME = "String  \"()<>@,;:\\\\"\t []/?=\""
ATOM = "int  -1"
QUOTEDSTRING = "int  -2"
COMMENT = "int  -3"
EOF = "int  -4"
def getRemainder():
    '''    public String getRemainder()
    '''
def HeaderTokenizer():
    '''    public HeaderTokenizer(final String header)
    public HeaderTokenizer(final String header, final String delimiters)
    public HeaderTokenizer(final String header, final String delimiters, final boolean skipComments)
    '''
def next():
    '''    public Token next()
    '''
def peek():
    '''    public Token peek()
    '''
def getType():
    '''    public int getType()
    '''
def getValue():
    '''    public String getValue()
    '''
def Token():
    '''    public Token(final int type, final String value)
    '''
