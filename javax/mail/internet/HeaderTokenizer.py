RFC822 = "String  ()<>@,;:\\\"\t .[]""
MIME = "String  ()<>@,;:\\\"\t []/?=""
ATOM = "int  -1"
QUOTEDSTRING = "int  -2"
COMMENT = "int  -3"
EOF = "int  -4"
def getRemainder():
'''public String getRemainder()
'''
pass
def HeaderTokenizer():
'''public HeaderTokenizer(final String header)
public HeaderTokenizer(final String header, final String delimiters)
public HeaderTokenizer(final String header, final String delimiters, final boolean skipComments)
'''
pass
def next():
'''public Token next()
'''
pass
def peek():
'''public Token peek()
'''
pass
def getType():
'''public int getType()
'''
pass
def getValue():
'''public String getValue()
'''
pass
def Token():
'''public Token(final int type, final String value)
'''
pass
