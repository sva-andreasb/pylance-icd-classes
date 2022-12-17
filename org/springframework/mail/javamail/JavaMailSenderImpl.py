DEFAULT_PROTOCOL = "String  \"smtp\""
DEFAULT_PORT = "int  -1"
def ():
    '''returns JavaMailSenderImpl\n\n
    ()\n
    '''
def setJavaMailProperties():
    '''returns None\n\n
    setJavaMailProperties(final Properties javaMailProperties)\n
    '''
def setSession():
    '''returns None\n\n
    setSession(final Session session)\n
    '''
def getSession():
    '''returns Session\n\n
    getSession()\n
    '''
def setProtocol():
    '''returns None\n\n
    setProtocol(final String protocol)\n
    '''
def getProtocol():
    '''returns String\n\n
    getProtocol()\n
    '''
def setHost():
    '''returns None\n\n
    setHost(final String host)\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def setPort():
    '''returns None\n\n
    setPort(final int port)\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def setUsername():
    '''returns None\n\n
    setUsername(final String username)\n
    '''
def getUsername():
    '''returns String\n\n
    getUsername()\n
    '''
def setPassword():
    '''returns None\n\n
    setPassword(final String password)\n
    '''
def getPassword():
    '''returns String\n\n
    getPassword()\n
    '''
def setDefaultEncoding():
    '''returns None\n\n
    setDefaultEncoding(final String defaultEncoding)\n
    '''
def getDefaultEncoding():
    '''returns String\n\n
    getDefaultEncoding()\n
    '''
def setDefaultFileTypeMap():
    '''returns None\n\n
    setDefaultFileTypeMap(final FileTypeMap defaultFileTypeMap)\n
    '''
def getDefaultFileTypeMap():
    '''returns FileTypeMap\n\n
    getDefaultFileTypeMap()\n
    '''
def send():
    '''returns None\n\n
    send(final SimpleMailMessage simpleMessage)\n
    send(final SimpleMailMessage[] simpleMessages)\n
    send(final MimeMessage mimeMessage)\n
    send(final MimeMessage[] mimeMessages)\n
    send(final MimeMessagePreparator mimeMessagePreparator)\n
    send(final MimeMessagePreparator[] mimeMessagePreparators)\n
    '''
def createMimeMessage():
    '''returns MimeMessage\n\n
    createMimeMessage()\n
    createMimeMessage(final InputStream contentStream)\n
    '''
