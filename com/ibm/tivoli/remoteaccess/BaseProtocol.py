RAloggerName = "String  \"remoteAccess.logger\""
def ():
    '''returns BaseProtocol\n\n
    ()\n
    (final String username, final byte[] password, final String hostname)\n
    '''
def getHostname():
    '''returns String\n\n
    getHostname()\n
    '''
def getUsername():
    '''returns String\n\n
    getUsername()\n
    '''
def getPassword():
    '''returns byte[]\n\n
    getPassword()\n
    '''
def getConversionCharset():
    '''returns Charset\n\n
    getConversionCharset()\n
    '''
def beginSession():
    '''returns None\n\n
    beginSession(final String hostname)\n
    beginSession()\n
    '''
def endSession():
    '''returns None\n\n
    endSession()\n
    '''
def inSession():
    '''returns boolean\n\n
    inSession()\n
    '''
def getTextFile():
    '''returns None\n\n
    getTextFile(final String remoteFile, final String localPath)\n
    '''
def putTextFile():
    '''returns None\n\n
    putTextFile(final String localFile, final String remotePath)\n
    '''
def getFileReader():
    '''returns ConvertingReader\n\n
    getFileReader(final String fileName)\n
    getFileReader(final String filename, CharsetDecoder decoder, String lineSeparator)\n
    '''
def getFileWriter():
    '''returns ConvertingWriter\n\n
    getFileWriter(final String fileName, final boolean append)\n
    getFileWriter(final String fileName, CharsetEncoder encoder, String lineSeparator, final boolean append)\n
    '''
def getCanonicalHostname():
    '''returns String\n\n
    getCanonicalHostname()\n
    '''
def getCharset():
    '''returns String\n\n
    getCharset()\n
    '''
def getRemoteCharset():
    '''returns Charset\n\n
    getRemoteCharset()\n
    getRemoteCharset(final CharsetType type)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke()\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
