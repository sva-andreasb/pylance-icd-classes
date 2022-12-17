def ():
    '''returns MimeMessageHelper\n\n
    (final MimeMessage mimeMessage)\n
    (final MimeMessage mimeMessage, final String encoding)\n
    (final MimeMessage mimeMessage, final boolean multipart)\n
    (final MimeMessage mimeMessage, final boolean multipart, final String encoding)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setFileTypeMap():
    '''returns None\n\n
    setFileTypeMap(final FileTypeMap fileTypeMap)\n
    '''
def getFileTypeMap():
    '''returns FileTypeMap\n\n
    getFileTypeMap()\n
    '''
def setValidateAddresses():
    '''returns None\n\n
    setValidateAddresses(final boolean validateAddresses)\n
    '''
def isValidateAddresses():
    '''returns boolean\n\n
    isValidateAddresses()\n
    '''
def setFrom():
    '''returns None\n\n
    setFrom(final InternetAddress from)\n
    setFrom(final String from)\n
    setFrom(final String from, final String personal)\n
    '''
def setReplyTo():
    '''returns None\n\n
    setReplyTo(final InternetAddress replyTo)\n
    setReplyTo(final String replyTo)\n
    setReplyTo(final String replyTo, final String personal)\n
    '''
def setTo():
    '''returns None\n\n
    setTo(final InternetAddress to)\n
    setTo(final InternetAddress[] to)\n
    setTo(final String to)\n
    setTo(final String[] to)\n
    '''
def addTo():
    '''returns None\n\n
    addTo(final InternetAddress to)\n
    addTo(final String to)\n
    addTo(final String to, final String personal)\n
    '''
def setCc():
    '''returns None\n\n
    setCc(final InternetAddress cc)\n
    setCc(final InternetAddress[] cc)\n
    setCc(final String cc)\n
    setCc(final String[] cc)\n
    '''
def addCc():
    '''returns None\n\n
    addCc(final InternetAddress cc)\n
    addCc(final String cc)\n
    addCc(final String cc, final String personal)\n
    '''
def setBcc():
    '''returns None\n\n
    setBcc(final InternetAddress bcc)\n
    setBcc(final InternetAddress[] bcc)\n
    setBcc(final String bcc)\n
    setBcc(final String[] bcc)\n
    '''
def addBcc():
    '''returns None\n\n
    addBcc(final InternetAddress bcc)\n
    addBcc(final String bcc)\n
    addBcc(final String bcc, final String personal)\n
    '''
def setSentDate():
    '''returns None\n\n
    setSentDate(final Date sentDate)\n
    '''
def setSubject():
    '''returns None\n\n
    setSubject(final String subject)\n
    '''
def setText():
    '''returns None\n\n
    setText(final String text)\n
    setText(final String text, final boolean html)\n
    setText(final String plainText, final String htmlText)\n
    '''
def addInline():
    '''returns None\n\n
    addInline(final String contentId, final DataSource dataSource)\n
    addInline(final String contentId, final File file)\n
    addInline(final String contentId, final Resource resource)\n
    addInline(final String contentId, final InputStreamSource inputStreamSource, final String contentType)\n
    '''
def addAttachment():
    '''returns None\n\n
    addAttachment(final String attachmentFilename, final DataSource dataSource)\n
    addAttachment(final String attachmentFilename, final File file)\n
    addAttachment(final String attachmentFilename, final InputStreamSource inputStreamSource)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
