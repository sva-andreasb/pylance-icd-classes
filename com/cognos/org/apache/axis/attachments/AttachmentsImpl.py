def ():
    '''returns AttachmentsImpl\n\n
    (final Object intialContents, final String contentType, String contentLocation)\n
    '''
def removeAttachmentPart():
    '''returns Part\n\n
    removeAttachmentPart(final String reference)\n
    '''
def addAttachmentPart():
    '''returns Part\n\n
    addAttachmentPart(final Part newPart)\n
    '''
def createAttachmentPart():
    '''returns Part\n\n
    createAttachmentPart(final Object datahandler)\n
    createAttachmentPart()\n
    '''
def setAttachmentParts():
    '''returns None\n\n
    setAttachmentParts(final Collection parts)\n
    '''
def getAttachmentByReference():
    '''returns Part\n\n
    getAttachmentByReference(String reference)\n
    '''
def getAttachments():
    '''returns Iterator\n\n
    getAttachments()\n
    getAttachments(final MimeHeaders headers)\n
    '''
def getRootPart():
    '''returns Part\n\n
    getRootPart()\n
    '''
def setRootPart():
    '''returns None\n\n
    setRootPart(final Part newRoot)\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def writeContentToStream():
    '''returns None\n\n
    writeContentToStream(final OutputStream os)\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getAttachmentCount():
    '''returns int\n\n
    getAttachmentCount()\n
    '''
def isAttachment():
    '''returns boolean\n\n
    isAttachment(final Object value)\n
    '''
def removeAllAttachments():
    '''returns None\n\n
    removeAllAttachments()\n
    '''
def setSendType():
    '''returns None\n\n
    setSendType(final int sendtype)\n
    '''
def getSendType():
    '''returns int\n\n
    getSendType()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getIncomingAttachmentStreams():
    '''returns IncomingAttachmentStreams\n\n
    getIncomingAttachmentStreams()\n
    '''
