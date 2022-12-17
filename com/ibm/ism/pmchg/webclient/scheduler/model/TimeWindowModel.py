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
