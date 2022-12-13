def getAttachmentSize():
    '''public long getAttachmentSize(final MboRemote doclink)
    '''
def createAttachment():
    '''public void createAttachment(final String name, final byte[] data, final String mimeType)
    '''
def deleteAttachment():
    '''public void deleteAttachment(final MboRemote doclink)
    '''
def getAttachment():
    '''public byte[] getAttachment(final MboRemote doclink)
    public byte[] getAttachment(final String urlName)
    '''
def getAttachmentQualifiedName():
    '''public String getAttachmentQualifiedName(final MboRemote doclink, final String documentName)
    '''
def setupStorage():
    '''public void setupStorage()
    '''
def cleanupStorage():
    '''public void cleanupStorage()
    '''
def streamAttachment():
    '''public InputStream streamAttachment(final MboRemote doclink)
    '''
def isAttachmentNeedsCustomDatasource():
    '''public boolean isAttachmentNeedsCustomDatasource(final String urlName)
    '''
def getAttachmentDatasource():
    '''public DataSource getAttachmentDatasource(final String urlName)
    '''
