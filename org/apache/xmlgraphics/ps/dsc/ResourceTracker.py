def getDocumentSuppliedResources():
    '''returns Set\n\n
    getDocumentSuppliedResources()\n
    '''
def getDocumentNeededResources():
    '''returns Set\n\n
    getDocumentNeededResources()\n
    '''
def notifyStartNewPage():
    '''returns None\n\n
    notifyStartNewPage()\n
    '''
def registerSuppliedResource():
    '''returns None\n\n
    registerSuppliedResource(final PSResource res)\n
    '''
def registerNeededResource():
    '''returns None\n\n
    registerNeededResource(final PSResource res)\n
    '''
def notifyResourceUsageOnPage():
    '''returns None\n\n
    notifyResourceUsageOnPage(final PSResource res)\n
    notifyResourceUsageOnPage(final Collection resources)\n
    '''
def isResourceSupplied():
    '''returns boolean\n\n
    isResourceSupplied(final PSResource res)\n
    '''
def writeResources():
    '''returns None\n\n
    writeResources(final boolean pageLevel, final PSGenerator gen)\n
    '''
def writePageResources():
    '''returns None\n\n
    writePageResources(final PSGenerator gen)\n
    '''
def writeDocumentResources():
    '''returns None\n\n
    writeDocumentResources(final PSGenerator gen)\n
    '''
def declareInlined():
    '''returns None\n\n
    declareInlined(final PSResource res)\n
    '''
def getUsageCount():
    '''returns long\n\n
    getUsageCount(final PSResource res)\n
    '''
def inc():
    '''returns None\n\n
    inc()\n
    '''
def getCount():
    '''returns long\n\n
    getCount()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
