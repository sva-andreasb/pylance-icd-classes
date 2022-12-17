def getLineCount():
    '''returns int\n\n
    getLineCount()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def saveChanges():
    '''returns None\n\n
    saveChanges()\n
    '''
def setFrom():
    '''returns None\n\n
    setFrom()\n
    setFrom(final Address address)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getRawInputStream():
    '''returns InputStream\n\n
    getRawInputStream()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream os)\n
    writeTo(final OutputStream os, final String[] ignoreList)\n
    '''
def getContent():
    '''returns Object\n\n
    getContent()\n
    '''
def getContentID():
    '''returns String\n\n
    getContentID()\n
    '''
def getContentMD5():
    '''returns String\n\n
    getContentMD5()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def getDisposition():
    '''returns String\n\n
    getDisposition()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def getMessageID():
    '''returns String\n\n
    getMessageID()\n
    '''
def getSubject():
    '''returns String\n\n
    getSubject()\n
    '''
def getContentLanguage():
    '''returns String[]\n\n
    getContentLanguage()\n
    '''
def addHeaderLine():
    '''returns None\n\n
    addHeaderLine(final String line)\n
    '''
def removeHeader():
    '''returns None\n\n
    removeHeader(final String name)\n
    '''
def setContentID():
    '''returns None\n\n
    setContentID(final String cid)\n
    '''
def setContentMD5():
    '''returns None\n\n
    setContentMD5(final String md5)\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String description)\n
    setDescription(final String description, final String charset)\n
    '''
def setDisposition():
    '''returns None\n\n
    setDisposition(final String disposition)\n
    '''
def setFileName():
    '''returns None\n\n
    setFileName(final String filename)\n
    '''
def setSubject():
    '''returns None\n\n
    setSubject(final String subject)\n
    setSubject(final String subject, final String charset)\n
    '''
def setText():
    '''returns None\n\n
    setText(final String text)\n
    setText(final String text, final String charset)\n
    '''
def isMimeType():
    '''returns boolean\n\n
    isMimeType(final String mimeType)\n
    '''
def setContentLanguage():
    '''returns None\n\n
    setContentLanguage(final String[] languages)\n
    '''
def getReceivedDate():
    '''returns Date\n\n
    getReceivedDate()\n
    '''
def getSentDate():
    '''returns Date\n\n
    getSentDate()\n
    '''
def setSentDate():
    '''returns None\n\n
    setSentDate(final Date d)\n
    '''
def getAllHeaderLines():
    '''returns Enumeration\n\n
    getAllHeaderLines()\n
    '''
def getAllHeaders():
    '''returns Enumeration\n\n
    getAllHeaders()\n
    '''
def getSender():
    '''returns Address\n\n
    getSender()\n
    '''
def getAllRecipients():
    '''returns Address[]\n\n
    getAllRecipients()\n
    '''
def getFrom():
    '''returns Address[]\n\n
    getFrom()\n
    '''
def getReplyTo():
    '''returns Address[]\n\n
    getReplyTo()\n
    '''
def setSender():
    '''returns None\n\n
    setSender(final Address address)\n
    '''
def addFrom():
    '''returns None\n\n
    addFrom(final Address[] addresses)\n
    '''
def setReplyTo():
    '''returns None\n\n
    setReplyTo(final Address[] addresses)\n
    '''
def reply():
    '''returns Message\n\n
    reply(final boolean replyToAll)\n
    '''
def setContent():
    '''returns None\n\n
    setContent(final Multipart mp)\n
    setContent(final Object o, final String type)\n
    '''
def ():
    '''returns MimeMessage\n\n
    (final Session session)\n
    (final MimeMessage source)\n
    (final Session session, final InputStream is)\n
    '''
def getHeader():
    '''returns String\n\n
    getHeader(final String name)\n
    getHeader(final String name, final String delimiter)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final String name, final String value)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String name, final String value)\n
    '''
def addRecipients():
    '''returns None\n\n
    addRecipients(final Message.RecipientType type, final String addresses)\n
    addRecipients(final Message.RecipientType type, final Address[] addresses)\n
    '''
def setRecipients():
    '''returns None\n\n
    setRecipients(final Message.RecipientType type, final String addresses)\n
    setRecipients(final Message.RecipientType type, final Address[] addresses)\n
    '''
def getMatchingHeaderLines():
    '''returns Enumeration\n\n
    getMatchingHeaderLines(final String[] names)\n
    '''
def getMatchingHeaders():
    '''returns Enumeration\n\n
    getMatchingHeaders(final String[] names)\n
    '''
def getNonMatchingHeaderLines():
    '''returns Enumeration\n\n
    getNonMatchingHeaderLines(final String[] names)\n
    '''
def getNonMatchingHeaders():
    '''returns Enumeration\n\n
    getNonMatchingHeaders(final String[] names)\n
    '''
def getRecipients():
    '''returns Address[]\n\n
    getRecipients(final Message.RecipientType type)\n
    '''
