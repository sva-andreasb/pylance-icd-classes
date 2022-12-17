def ():
    '''returns Reorder\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def toExtString():
    '''returns String\n\n
    toExtString()\n
    '''
def processVendorAndCost():
    '''returns None\n\n
    processVendorAndCost(final boolean considerContract, final int allowanceDays)\n
    processVendorAndCost(final boolean considerContract, final int allowanceDays, final boolean recheckLeadTime)\n
    '''
def generatePRHeader():
    '''returns PRRemote\n\n
    generatePRHeader(final PRSetRemote prSet)\n
    '''
def generatePOHeader():
    '''returns PORemote\n\n
    generatePOHeader(final POSetRemote poSet)\n
    '''
def generatePRLine():
    '''returns None\n\n
    generatePRLine(final PRRemote pr, final boolean groupByVender)\n
    '''
def getInternalLineType():
    '''returns String\n\n
    getInternalLineType()\n
    '''
def generatePOLine():
    '''returns None\n\n
    generatePOLine(final PRRemote po, final boolean groupByVender)\n
    '''
def calculateReorderQtywithInventory():
    '''returns None\n\n
    calculateReorderQtywithInventory(final MboRemote inventoryMbo)\n
    '''
def setIgnoreReorderPoint():
    '''returns None\n\n
    setIgnoreReorderPoint(final boolean ignoreReorderPointParam)\n
    '''
