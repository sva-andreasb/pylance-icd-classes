AUTO = "String  \"auto\""
MIME = "String  \"mime\""
UU = "String  \"uu\""
PLAIN = "String  \"plain\""
def ():
    '''returns EmailTask\n\n
    ()\n
    '''
def setUser():
    '''returns None\n\n
    setUser(final String user)\n
    '''
def setPassword():
    '''returns None\n\n
    setPassword(final String password)\n
    '''
def setSSL():
    '''returns None\n\n
    setSSL(final boolean ssl)\n
    '''
def setEnableStartTLS():
    '''returns None\n\n
    setEnableStartTLS(final boolean b)\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final Encoding encoding)\n
    '''
def setMailport():
    '''returns None\n\n
    setMailport(final int port)\n
    '''
def setMailhost():
    '''returns None\n\n
    setMailhost(final String host)\n
    '''
def setSubject():
    '''returns None\n\n
    setSubject(final String subject)\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final String message)\n
    '''
def setMessageFile():
    '''returns None\n\n
    setMessageFile(final File file)\n
    '''
def setMessageMimeType():
    '''returns None\n\n
    setMessageMimeType(final String type)\n
    '''
def addMessage():
    '''returns None\n\n
    addMessage(final Message message)\n
    '''
def addFrom():
    '''returns None\n\n
    addFrom(final EmailAddress address)\n
    '''
def setFrom():
    '''returns None\n\n
    setFrom(final String address)\n
    '''
def addReplyTo():
    '''returns None\n\n
    addReplyTo(final EmailAddress address)\n
    '''
def setReplyTo():
    '''returns None\n\n
    setReplyTo(final String address)\n
    '''
def addTo():
    '''returns None\n\n
    addTo(final EmailAddress address)\n
    '''
def setToList():
    '''returns None\n\n
    setToList(final String list)\n
    '''
def addCc():
    '''returns None\n\n
    addCc(final EmailAddress address)\n
    '''
def setCcList():
    '''returns None\n\n
    setCcList(final String list)\n
    '''
def addBcc():
    '''returns None\n\n
    addBcc(final EmailAddress address)\n
    '''
def setBccList():
    '''returns None\n\n
    setBccList(final String list)\n
    '''
def setFailOnError():
    '''returns None\n\n
    setFailOnError(final boolean failOnError)\n
    '''
def setFiles():
    '''returns None\n\n
    setFiles(final String filenames)\n
    '''
def addFileset():
    '''returns None\n\n
    addFileset(final FileSet fs)\n
    '''
def createAttachments():
    '''returns Path\n\n
    createAttachments()\n
    '''
def createHeader():
    '''returns Header\n\n
    createHeader()\n
    '''
def setIncludefilenames():
    '''returns None\n\n
    setIncludefilenames(final boolean includeFileNames)\n
    '''
def getIncludeFileNames():
    '''returns boolean\n\n
    getIncludeFileNames()\n
    '''
def setIgnoreInvalidRecipients():
    '''returns None\n\n
    setIgnoreInvalidRecipients(final boolean b)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def setCharset():
    '''returns None\n\n
    setCharset(final String charset)\n
    '''
def getCharset():
    '''returns String\n\n
    getCharset()\n
    '''
def getValues():
    '''returns String[]\n\n
    getValues()\n
    '''
