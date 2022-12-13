PREPARING_EVENT_CODE = "int  1"
STARTED_EVENT_CODE = "int  2"
COMPLETED_EVENT_CODE = "int  4"
FAILED_EVENT_CODE = "int  8"
CANCELED_EVENT_CODE = "int  16"
RESET_EVENT_CODE = "int  32"
PART_STARTED_EVENT_CODE = "int  1024"
PART_COMPLETED_EVENT_CODE = "int  2048"
PART_FAILED_EVENT_CODE = "int  4096"
def ProgressEvent():
'''public ProgressEvent(final long bytes)
public ProgressEvent(final ProgressEventType eventType)
public ProgressEvent(final ProgressEventType eventType, final long bytes)
'''
pass
def getBytes():
'''public long getBytes()
'''
pass
def getBytesTransferred():
'''public long getBytesTransferred()
'''
pass
def getEventCode():
'''public int getEventCode()
'''
pass
def getEventType():
'''public ProgressEventType getEventType()
'''
pass
def toString():
'''public String toString()
'''
pass
