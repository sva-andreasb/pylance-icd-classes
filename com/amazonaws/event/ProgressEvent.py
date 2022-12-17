PREPARING_EVENT_CODE = "int  1"
STARTED_EVENT_CODE = "int  2"
COMPLETED_EVENT_CODE = "int  4"
FAILED_EVENT_CODE = "int  8"
CANCELED_EVENT_CODE = "int  16"
RESET_EVENT_CODE = "int  32"
PART_STARTED_EVENT_CODE = "int  1024"
PART_COMPLETED_EVENT_CODE = "int  2048"
PART_FAILED_EVENT_CODE = "int  4096"
def ():
    '''returns ProgressEvent\n\n
    (final long bytes)\n
    (final ProgressEventType eventType)\n
    (final ProgressEventType eventType, final long bytes)\n
    '''
def getBytes():
    '''returns long\n\n
    getBytes()\n
    '''
def getBytesTransferred():
    '''returns long\n\n
    getBytesTransferred()\n
    '''
def getEventCode():
    '''returns int\n\n
    getEventCode()\n
    '''
def getEventType():
    '''returns ProgressEventType\n\n
    getEventType()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
