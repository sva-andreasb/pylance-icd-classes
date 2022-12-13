BULKLOAD_STAT = "int  0"
FILEPARSE_STAT = "int  1"
UPDATEAPI_STAT = "int  2"
OBJECTS_STAT = "int  3"
EXPLICITREL_STAT = "int  5"
ERROR_OCCURRED = "int  6"
def printStats():
    '''public static void printStats()
    public static void printStats(final int statusField)
    '''
def startBulkload():
    '''public static void startBulkload()
    '''
def stopBulkload():
    '''public static void stopBulkload()
    '''
def startFileParse():
    '''public static void startFileParse()
    '''
def stopFileParse():
    '''public static void stopFileParse()
    '''
def startUpdate():
    '''public static void startUpdate()
    '''
def stopUpdate():
    '''public static void stopUpdate()
    '''
def updateFoundObjects():
    '''public static void updateFoundObjects(final int numObjs)
    '''
def updateTriedObjects():
    '''public static void updateTriedObjects(final int numObjs)
    '''
def setGoodObjects():
    '''public static void setGoodObjects(final int numObjs)
    '''
def updateGoodObjects():
    '''public static void updateGoodObjects(final int numObjs)
    '''
def updateFoundRelns():
    '''public static void updateFoundRelns(final int numObjs)
    '''
def updateTriedExplicitRelns():
    '''public static void updateTriedExplicitRelns(final int numRelns)
    '''
def updateGoodExplicitRelns():
    '''public static void updateGoodExplicitRelns(final int numRelns)
    '''
def reset():
    '''public static void reset()
    '''
def setError():
    '''public static void setError()
    '''
def getTriedObjects():
    '''public static int getTriedObjects()
    '''
