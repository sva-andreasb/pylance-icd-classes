QUERY_DIRECTORIES_FAILED = "int  7"
QUERY_DIRECTORIES_SUCCEEDED = "int  8"
OPEN_DIRECTORY_FAILED = "int  9"
OPEN_DIRECTORY_SUCCEEDED = "int  10"
QUERY_ENTRIES_FAILED = "int  11"
QUERY_ENTRIES_SUCCEEDED = "int  12"
SERVICE_AVAILABLE = "int  13"
SERVICE_UNAVAILABLE = "int  14"
def getDirectories():
    '''returns Directory[]\n\n
    getDirectories()\n
    '''
def getReason():
    '''returns int\n\n
    getReason()\n
    '''
def isAtStart():
    '''returns boolean\n\n
    isAtStart()\n
    '''
def isAtEnd():
    '''returns boolean\n\n
    isAtEnd()\n
    '''
def getEntries():
    '''returns STObject[]\n\n
    getEntries()\n
    '''
def getRequestId():
    '''returns Integer\n\n
    getRequestId()\n
    '''
def getDirectory():
    '''returns Directory\n\n
    getDirectory()\n
    '''
def getDirectorySize():
    '''returns int\n\n
    getDirectorySize()\n
    '''
def getChunkSize():
    '''returns short\n\n
    getChunkSize()\n
    '''
