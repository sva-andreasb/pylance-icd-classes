def AttachmentsImpl():
    '''    public AttachmentsImpl(final Object intialContents, final String contentType, String contentLocation)
    '''
def removeAttachmentPart():
    '''    public Part removeAttachmentPart(final String reference)
    '''
def addAttachmentPart():
    '''    public Part addAttachmentPart(final Part newPart)
    '''
def createAttachmentPart():
    '''    public Part createAttachmentPart(final Object datahandler)
    public Part createAttachmentPart()
    '''
def setAttachmentParts():
    '''    public void setAttachmentParts(final Collection parts)
    '''
def getAttachmentByReference():
    '''    public Part getAttachmentByReference(String reference)
    '''
def getAttachments():
    '''    public Collection getAttachments()
    public Iterator getAttachments(final MimeHeaders headers)
    '''
def getRootPart():
    '''    public Part getRootPart()
    '''
def setRootPart():
    '''    public void setRootPart(final Part newRoot)
    '''
def getContentLength():
    '''    public long getContentLength()
    '''
def writeContentToStream():
    '''    public void writeContentToStream(final OutputStream os)
    '''
def getContentType():
    '''    public String getContentType()
    '''
def getAttachmentCount():
    '''    public int getAttachmentCount()
    '''
def isAttachment():
    '''    public boolean isAttachment(final Object value)
    '''
def removeAllAttachments():
    '''    public void removeAllAttachments()
    '''
def setSendType():
    '''    public void setSendType(final int sendtype)
    '''
def getSendType():
    '''    public int getSendType()
    public static int getSendType(final String value)
    '''
def dispose():
    '''    public void dispose()
    '''
def getSendTypeString():
    '''    public static String getSendTypeString(final int value)
    '''
def getIncomingAttachmentStreams():
    '''    public IncomingAttachmentStreams getIncomingAttachmentStreams()
    '''
