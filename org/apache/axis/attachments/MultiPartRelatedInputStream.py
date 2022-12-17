MIME_MULTIPART_RELATED = "String  \"multipart/related\""
def ():
    '''returns MultiPartRelatedInputStream\n\n
    (String contentType, InputStream stream)\n
    '''
def getAttachmentByReference():
    '''returns Part\n\n
    getAttachmentByReference(final String[] id)\n
    '''
def getAttachments():
    '''returns Collection\n\n
    getAttachments()\n
    '''
def getContentLocation():
    '''returns String\n\n
    getContentLocation()\n
    '''
def getContentId():
    '''returns String\n\n
    getContentId()\n
    '''
def read():
    '''returns int\n\n
    read(final byte[] b, final int off, final int len)\n
    read(final byte[] b)\n
    read()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
