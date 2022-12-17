COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns TimeWindowModel\n\n
    (final String id, final TimeWindowSet root)\n
    '''
def addToRoot():
    '''returns None\n\n
    addToRoot(final TimeWindowSet set)\n
    '''
def computeTimeWindows():
    '''returns None\n\n
    computeTimeWindows()\n
    '''
def findSetbyIdPath():
    '''returns TimeWindowSet\n\n
    findSetbyIdPath(final String pathStr)\n
    findSetbyIdPath(final String[] path)\n
    '''
def getAvailableTimeWindows():
    '''returns Iterator<TimeWindow>\n\n
    getAvailableTimeWindows()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getRoot():
    '''returns TimeWindowSet\n\n
    getRoot()\n
    '''
def getTimeWindowSetsById():
    '''returns Iterator<TimeWindowSet>\n\n
    getTimeWindowSetsById(final String id)\n
    '''
def getUnavailableTimeWindows():
    '''returns Iterator<TimeWindow>\n\n
    getUnavailableTimeWindows()\n
    '''
def isAvailable():
    '''returns boolean\n\n
    isAvailable(final Date start, final Date end)\n
    '''
def resetDisabledFlag():
    '''returns None\n\n
    resetDisabledFlag()\n
    '''
def isDirty():
    '''returns boolean\n\n
    isDirty()\n
    '''
def setDirty():
    '''returns None\n\n
    setDirty(final boolean dirty)\n
    '''
def writeXml():
    '''returns None\n\n
    writeXml(final PrintWriter out)\n
    '''
