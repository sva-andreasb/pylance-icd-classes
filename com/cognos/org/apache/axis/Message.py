REQUEST = "String  \"request\""
RESPONSE = "String  \"response\""
MIME_MULTIPART_RELATED = "String  \"multipart/related\""
MIME_APPLICATION_DIME = "String  \"application/dime\""
CONTENT_TYPE_MTOM = "String  \"application/xop+xml\""
DEFAULT_ATTACHMNET_IMPL = "String  \"com.cognos.org.apache.axis.attachments.AttachmentsImpl\""
MIME_UNKNOWN = "String  \"  \""
def getMessageType():
    '''returns String\n\n
    getMessageType()\n
    '''
def setMessageType():
    '''returns None\n\n
    setMessageType(final String messageType)\n
    '''
def getMessageContext():
    '''returns MessageContext\n\n
    getMessageContext()\n
    '''
def setMessageContext():
    '''returns None\n\n
    setMessageContext(final MessageContext msgContext)\n
    '''
def ():
    '''returns Message\n\n
    (final Object initialContents, final boolean bodyInStream)\n
    (final Object initialContents, final boolean bodyInStream, final javax.xml.soap.MimeHeaders headers)\n
    (final Object initialContents, final MimeHeaders headers)\n
    (final Object initialContents, final boolean bodyInStream, final String contentType, final String contentLocation)\n
    (final Object initialContents)\n
    '''
def getSOAPPartAsString():
    '''returns String\n\n
    getSOAPPartAsString()\n
    '''
def getSOAPPartAsBytes():
    '''returns byte[]\n\n
    getSOAPPartAsBytes()\n
    '''
def getSOAPEnvelope():
    '''returns SOAPEnvelope\n\n
    getSOAPEnvelope()\n
    '''
def getAttachmentsImpl():
    '''returns Attachments\n\n
    getAttachmentsImpl()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType(final SOAPConstants sc)\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream os)\n
    '''
def getSOAPBody():
    '''returns SOAPBody\n\n
    getSOAPBody()\n
    '''
def getSOAPHeader():
    '''returns SOAPHeader\n\n
    getSOAPHeader()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String property, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String property)\n
    '''
def getContentDescription():
    '''returns String\n\n
    getContentDescription()\n
    '''
def setContentDescription():
    '''returns None\n\n
    setContentDescription(final String description)\n
    '''
def saveChanges():
    '''returns None\n\n
    saveChanges()\n
    '''
def saveRequired():
    '''returns boolean\n\n
    saveRequired()\n
    '''
def removeAllAttachments():
    '''returns None\n\n
    removeAllAttachments()\n
    '''
def countAttachments():
    '''returns int\n\n
    countAttachments()\n
    '''
def getAttachments():
    '''returns Iterator\n\n
    getAttachments()\n
    getAttachments(final javax.xml.soap.MimeHeaders headers)\n
    '''
def addAttachmentPart():
    '''returns None\n\n
    addAttachmentPart(final AttachmentPart attachmentpart)\n
    '''
def createAttachmentPart():
    '''returns AttachmentPart\n\n
    createAttachmentPart()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
