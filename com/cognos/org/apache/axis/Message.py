REQUEST = "String  \"request\""
RESPONSE = "String  \"response\""
MIME_MULTIPART_RELATED = "String  \"multipart/related\""
MIME_APPLICATION_DIME = "String  \"application/dime\""
CONTENT_TYPE_MTOM = "String  \"application/xop+xml\""
DEFAULT_ATTACHMNET_IMPL = "String  \"com.cognos.org.apache.axis.attachments.AttachmentsImpl\""
MIME_UNKNOWN = "String  \"  \""
def getAttachmentImplClassName():
    '''public static String getAttachmentImplClassName()
    '''
def getMessageType():
    '''public String getMessageType()
    '''
def setMessageType():
    '''public void setMessageType(final String messageType)
    '''
def getMessageContext():
    '''public MessageContext getMessageContext()
    '''
def setMessageContext():
    '''public void setMessageContext(final MessageContext msgContext)
    '''
def Message():
    '''public Message(final Object initialContents, final boolean bodyInStream)
    public Message(final Object initialContents, final boolean bodyInStream, final javax.xml.soap.MimeHeaders headers)
    public Message(final Object initialContents, final MimeHeaders headers)
    public Message(final Object initialContents, final boolean bodyInStream, final String contentType, final String contentLocation)
    public Message(final Object initialContents)
    '''
def getSOAPPartAsString():
    '''public String getSOAPPartAsString()
    '''
def getSOAPPartAsBytes():
    '''public byte[] getSOAPPartAsBytes()
    '''
def getSOAPEnvelope():
    '''public SOAPEnvelope getSOAPEnvelope()
    '''
def getAttachmentsImpl():
    '''public Attachments getAttachmentsImpl()
    '''
def getContentType():
    '''public String getContentType(final SOAPConstants sc)
    '''
def getContentLength():
    '''public long getContentLength()
    '''
def writeTo():
    '''public void writeTo(final OutputStream os)
    '''
def getSOAPBody():
    '''public SOAPBody getSOAPBody()
    '''
def getSOAPHeader():
    '''public SOAPHeader getSOAPHeader()
    '''
def setProperty():
    '''public void setProperty(final String property, final Object value)
    '''
def getProperty():
    '''public Object getProperty(final String property)
    '''
def getContentDescription():
    '''public String getContentDescription()
    '''
def setContentDescription():
    '''public void setContentDescription(final String description)
    '''
def saveChanges():
    '''public void saveChanges()
    '''
def saveRequired():
    '''public boolean saveRequired()
    '''
def removeAllAttachments():
    '''public void removeAllAttachments()
    '''
def countAttachments():
    '''public int countAttachments()
    '''
def getAttachments():
    '''public Iterator getAttachments()
    public Iterator getAttachments(final javax.xml.soap.MimeHeaders headers)
    '''
def addAttachmentPart():
    '''public void addAttachmentPart(final AttachmentPart attachmentpart)
    '''
def createAttachmentPart():
    '''public AttachmentPart createAttachmentPart()
    '''
def dispose():
    '''public void dispose()
    '''
