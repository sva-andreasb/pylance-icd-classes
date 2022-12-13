def COSAttachmentStorage():
'''public COSAttachmentStorage()
'''
pass
def getAttachmentSize():
'''public long getAttachmentSize(final MboRemote doclink)
'''
pass
def createAttachment():
'''public void createAttachment(final String name, final byte[] data, final String mimeType)
'''
pass
def deleteAttachment():
'''public void deleteAttachment(final MboRemote doclink)
'''
pass
def getAttachment():
'''public byte[] getAttachment(final MboRemote doclink)
public byte[] getAttachment(final String urlName)
'''
pass
def getAttachmentQualifiedName():
'''public String getAttachmentQualifiedName(final MboRemote doclink, final String name)
'''
pass
def setupStorage():
'''public void setupStorage()
'''
pass
def cleanupStorage():
'''public void cleanupStorage()
'''
pass
def streamAttachment():
'''public InputStream streamAttachment(final MboRemote doclink)
'''
pass
def isAttachmentNeedsCustomDatasource():
'''public boolean isAttachmentNeedsCustomDatasource(final String urlName)
'''
pass
def getAttachmentDatasource():
'''public DataSource getAttachmentDatasource(final String urlName)
'''
pass
