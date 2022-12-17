COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns FixedTimeWindowSet\n\n
    (final String id, final String name, final String description, final boolean unavailable)\n
    (final String description, final boolean unavailable)\n
    '''
def addTimeWindow():
    '''returns None\n\n
    addTimeWindow(final Date startTime, final Date endTime)\n
    '''
def computeTimeWindows():
    '''returns None\n\n
    computeTimeWindows()\n
    '''
def clearChildren():
    '''returns None\n\n
    clearChildren()\n
    '''
def findFirstChildById():
    '''returns TimeWindowSet\n\n
    findFirstChildById(final String id)\n
    '''
def fetchTimeWindowSetsById():
    '''returns None\n\n
    fetchTimeWindowSetsById(final List<TimeWindowSet> list, final String id)\n
    '''
def getChildrenIterator():
    '''returns Iterator<TimeWindowSet>\n\n
    getChildrenIterator()\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def getChildAt():
    '''returns TimeWindowSet\n\n
    getChildAt(final int index)\n
    '''
def resetDisabledFlag():
    '''returns None\n\n
    resetDisabledFlag()\n
    '''
def writeXml():
    '''returns None\n\n
    writeXml(final PrintWriter out)\n
    '''
