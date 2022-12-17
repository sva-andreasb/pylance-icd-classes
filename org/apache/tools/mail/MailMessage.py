DEFAULT_HOST = "String  \"localhost\""
DEFAULT_PORT = "int  25"
def ():
    '''returns MailMessage\n\n
    ()\n
    (final String host)\n
    (final String host, final int port)\n
    '''
def setPort():
    '''returns None\n\n
    setPort(final int port)\n
    '''
def from():
    '''returns None\n\n
    from(final String from)\n
    '''
def replyto():
    '''returns None\n\n
    replyto(final String rto)\n
    '''
def to():
    '''returns None\n\n
    to(final String to)\n
    '''
def cc():
    '''returns None\n\n
    cc(final String cc)\n
    '''
def bcc():
    '''returns None\n\n
    bcc(final String bcc)\n
    '''
def setSubject():
    '''returns None\n\n
    setSubject(final String subj)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String name, final String value)\n
    '''
def getPrintStream():
    '''returns PrintStream\n\n
    getPrintStream()\n
    '''
def sendAndClose():
    '''returns None\n\n
    sendAndClose()\n
    '''
