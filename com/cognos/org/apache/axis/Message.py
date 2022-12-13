REQUEST = "String  request""
RESPONSE = "String  response""
MIME_MULTIPART_RELATED = "String  multipart/related""
MIME_APPLICATION_DIME = "String  application/dime""
CONTENT_TYPE_MTOM = "String  application/xop+xml""
DEFAULT_ATTACHMNET_IMPL = "String  com.cognos.org.apache.axis.attachments.AttachmentsImpl""
MIME_UNKNOWN = "String    ""
def getAttachmentImplClassName():
'''public static String getAttachmentImplClassName()
'''
pass
def getMessageType():
'''public String getMessageType()
'''
pass
def setMessageType():
'''public void setMessageType(final String messageType)
'''
pass
def getMessageContext():
'''public MessageContext getMessageContext()
'''
pass
def setMessageContext():
'''public void setMessageContext(final MessageContext msgContext)
'''
pass
def Message():
'''public Message(final Object initialContents, final boolean bodyInStream)
public Message(final Object initialContents, final boolean bodyInStream, final javax.xml.soap.MimeHeaders headers)
public Message(final Object initialContents, final MimeHeaders headers)
public Message(final Object initialContents, final boolean bodyInStream, final String contentType, final String contentLocation)
public Message(final Object initialContents)
'''
pass
def getSOAPPartAsString():
'''public String getSOAPPartAsString()
'''
pass
def getSOAPPartAsBytes():
'''public byte[] getSOAPPartAsBytes()
'''
pass
def getSOAPEnvelope():
'''public SOAPEnvelope getSOAPEnvelope()
'''
pass
def getAttachmentsImpl():
'''public Attachments getAttachmentsImpl()
'''
pass
def getContentType():
'''public String getContentType(final SOAPConstants sc)
'''
pass
def getContentLength():
'''public long getContentLength()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream os)
'''
pass
def getSOAPBody():
'''public SOAPBody getSOAPBody()
'''
pass
def getSOAPHeader():
'''public SOAPHeader getSOAPHeader()
'''
pass
def setProperty():
'''public void setProperty(final String property, final Object value)
'''
pass
def getProperty():
'''public Object getProperty(final String property)
'''
pass
def getContentDescription():
'''public String getContentDescription()
'''
pass
def setContentDescription():
'''public void setContentDescription(final String description)
'''
pass
def saveChanges():
'''public void saveChanges()
'''
pass
def saveRequired():
'''public boolean saveRequired()
'''
pass
def removeAllAttachments():
'''public void removeAllAttachments()
'''
pass
def countAttachments():
'''public int countAttachments()
'''
pass
def getAttachments():
'''public Iterator getAttachments()
public Iterator getAttachments(final javax.xml.soap.MimeHeaders headers)
'''
pass
def addAttachmentPart():
'''public void addAttachmentPart(final AttachmentPart attachmentpart)
'''
pass
def createAttachmentPart():
'''public AttachmentPart createAttachmentPart()
'''
pass
def dispose():
'''public void dispose()
'''
pass
