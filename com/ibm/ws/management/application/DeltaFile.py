ROOTELEMENT = "String  \"app-delta\""
FILES = "String  \"files\""
FILE = "String  \"file\""
URI = "String  \"uri\""
UPDATE_INPUT = "String  \"change_input\""
def ():
    '''returns DeltaFile\n\n
    ()\n
    (final String rootPath)\n
    (final InputStream i)\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def writeToDisk():
    '''returns None\n\n
    writeToDisk()\n
    '''
def sendToStream():
    '''returns None\n\n
    sendToStream(final OutputStream stream)\n
    '''
