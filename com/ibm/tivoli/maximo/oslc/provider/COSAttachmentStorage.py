def ():
    '''returns COSAttachmentStorage\n\n
    ()\n
    '''
def getAttachmentSize():
    '''returns long\n\n
    getAttachmentSize(final MboRemote doclink)\n
    '''
def createAttachment():
    '''returns None\n\n
    createAttachment(final String name, final byte[] data, final String mimeType)\n
    '''
def deleteAttachment():
    '''returns None\n\n
    deleteAttachment(final MboRemote doclink)\n
    '''
def getAttachment():
    '''returns byte[]\n\n
    getAttachment(final MboRemote doclink)\n
    getAttachment(final String urlName)\n
    '''
def getAttachmentQualifiedName():
    '''returns String\n\n
    getAttachmentQualifiedName(final MboRemote doclink, final String name)\n
    '''
def setupStorage():
    '''returns None\n\n
    setupStorage()\n
    '''
def cleanupStorage():
    '''returns None\n\n
    cleanupStorage()\n
    '''
def streamAttachment():
    '''returns InputStream\n\n
    streamAttachment(final MboRemote doclink)\n
    '''
def isAttachmentNeedsCustomDatasource():
    '''returns boolean\n\n
    isAttachmentNeedsCustomDatasource(final String urlName)\n
    '''
def getAttachmentDatasource():
    '''returns DataSource\n\n
    getAttachmentDatasource(final String urlName)\n
    '''
