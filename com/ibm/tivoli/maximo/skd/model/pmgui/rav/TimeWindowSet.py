COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
ID_PATH_DELIMITER = "String  \">\""
def ():
    '''returns TimeWindowSet\n\n
    (final String id, final String name, final String description, final boolean unavailable)\n
    (final String description, final boolean unavailable)\n
    '''
def clearProperty():
    '''returns None\n\n
    clearProperty(final String name)\n
    '''
def clearProperties():
    '''returns None\n\n
    clearProperties()\n
    '''
def clearTimeWindows():
    '''returns None\n\n
    clearTimeWindows()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def getIconImageString():
    '''returns String\n\n
    getIconImageString()\n
    '''
def getIdPath():
    '''returns String[]\n\n
    getIdPath()\n
    '''
def getIdPathString():
    '''returns String\n\n
    getIdPathString()\n
    '''
def getObjectPath():
    '''returns TimeWindowSet[]\n\n
    getObjectPath()\n
    '''
def getParent():
    '''returns TimeWindowSet\n\n
    getParent()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def getTimeWindowAt():
    '''returns TimeWindow\n\n
    getTimeWindowAt(final int index)\n
    '''
def getTimeWindowCount():
    '''returns int\n\n
    getTimeWindowCount()\n
    '''
def getTimeWindowIterator():
    '''returns Iterator<TimeWindow>\n\n
    getTimeWindowIterator()\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String name)\n
    '''
def invert():
    '''returns List<TimeWindow>\n\n
    invert()\n
    '''
def isAncestorDisabled():
    '''returns boolean\n\n
    isAncestorDisabled()\n
    '''
def isAvailable():
    '''returns boolean\n\n
    isAvailable()\n
    '''
def isChildrenHidden():
    '''returns boolean\n\n
    isChildrenHidden()\n
    '''
def isDisabled():
    '''returns boolean\n\n
    isDisabled()\n
    '''
def isMerged():
    '''returns boolean\n\n
    isMerged()\n
    '''
def isSorted():
    '''returns boolean\n\n
    isSorted()\n
    '''
def isUnavailable():
    '''returns boolean\n\n
    isUnavailable()\n
    '''
def isZeroDurationTWsAllowed():
    '''returns boolean\n\n
    isZeroDurationTWsAllowed()\n
    '''
def locateTimeWindow():
    '''returns int\n\n
    locateTimeWindow(final Date time)\n
    '''
def merge():
    '''returns None\n\n
    merge()\n
    '''
def removeFromParent():
    '''returns None\n\n
    removeFromParent()\n
    '''
def setChildrenHidden():
    '''returns None\n\n
    setChildrenHidden(final boolean hidden)\n
    '''
def setDisabled():
    '''returns None\n\n
    setDisabled(final boolean disabled)\n
    '''
def setIconImageString():
    '''returns None\n\n
    setIconImageString(final String image)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final Object value)\n
    '''
def setZeroDurationTWsAllowed():
    '''returns None\n\n
    setZeroDurationTWsAllowed(final boolean allowed)\n
    '''
def sort():
    '''returns None\n\n
    sort()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
