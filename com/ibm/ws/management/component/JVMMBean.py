SYSTEM_DUMP_EXT = "String  \"dmp\""
HEAP_DUMP_EXT = "String  \"phd\""
def ():
    '''returns DumpFileNameFilter\n\n
    ()\n
    (final String type)\n
    '''
def getTotalMemory():
    '''returns String\n\n
    getTotalMemory()\n
    '''
def setVerbose():
    '''returns None\n\n
    setVerbose(final boolean verbose, final String processType)\n
    setVerbose(final boolean verbose)\n
    '''
def isVerbose():
    '''returns boolean\n\n
    isVerbose()\n
    '''
def getFreeMemory():
    '''returns String\n\n
    getFreeMemory()\n
    '''
def getJavaVendor():
    '''returns String\n\n
    getJavaVendor()\n
    '''
def getJavaVersion():
    '''returns String\n\n
    getJavaVersion()\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String key)\n
    '''
def getIPAddress():
    '''returns String\n\n
    getIPAddress(final String hostname)\n
    '''
def getCurrentTimeInMillis():
    '''returns long\n\n
    getCurrentTimeInMillis()\n
    '''
def getJVMNode():
    '''returns String\n\n
    getJVMNode()\n
    '''
def dumpThreads():
    '''returns None\n\n
    dumpThreads()\n
    '''
def setMaxDumpsOnDisk():
    '''returns None\n\n
    setMaxDumpsOnDisk(final Integer max)\n
    '''
def getMaxDumpsOnDisk():
    '''returns Integer\n\n
    getMaxDumpsOnDisk()\n
    '''
def getMaxMemory():
    '''returns String\n\n
    getMaxMemory()\n
    '''
def setMaxSystemDumpsOnDisk():
    '''returns None\n\n
    setMaxSystemDumpsOnDisk(final Integer max)\n
    '''
def getMaxSystemDumpsOnDisk():
    '''returns Integer\n\n
    getMaxSystemDumpsOnDisk()\n
    '''
def generateHeapDump():
    '''returns String[]\n\n
    generateHeapDump()\n
    generateHeapDump(final String stoken)\n
    '''
def generateHeapDumps():
    '''returns String[]\n\n
    generateHeapDumps()\n
    '''
def generateSystemDump():
    '''returns String\n\n
    generateSystemDump()\n
    generateSystemDump(final String stoken)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File dir, final String name)\n
    '''
