def ():
    '''returns BaseTag\n\n
    (final BaseTag parent, final String name)\n
    '''
def getRootTag():
    '''returns RootTag\n\n
    getRootTag()\n
    '''
def isRootTag():
    '''returns boolean\n\n
    isRootTag()\n
    '''
def isGroupTag():
    '''returns boolean\n\n
    isGroupTag()\n
    '''
def isFileTag():
    '''returns boolean\n\n
    isFileTag()\n
    '''
def isExportFileTag():
    '''returns boolean\n\n
    isExportFileTag()\n
    '''
def isImportFileTag():
    '''returns boolean\n\n
    isImportFileTag()\n
    '''
def getParent():
    '''returns BaseTag\n\n
    getParent()\n
    '''
def getChildren():
    '''returns List<BaseTag>\n\n
    getChildren()\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final BaseTag child)\n
    '''
def addOption():
    '''returns None\n\n
    addOption(final Option option)\n
    '''
def getReplacementsInfo():
    '''returns ReplacementsInfo\n\n
    getReplacementsInfo()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getSummary():
    '''returns String\n\n
    getSummary()\n
    '''
def setSummary():
    '''returns None\n\n
    setSummary(final String summary)\n
    '''
def getIsSelected():
    '''returns boolean\n\n
    getIsSelected()\n
    '''
def setIsSelected():
    '''returns None\n\n
    setIsSelected()\n
    setIsSelected(final boolean isSelected)\n
    '''
def setNotSelected():
    '''returns None\n\n
    setNotSelected()\n
    '''
def getHasError():
    '''returns boolean\n\n
    getHasError()\n
    '''
def setHasError():
    '''returns None\n\n
    setHasError(final boolean hasError)\n
    '''
def getMessages():
    '''returns List<Message>\n\n
    getMessages()\n
    '''
def addMessage():
    '''returns None\n\n
    addMessage(final Message mesg)\n
    '''
def accept():
    '''returns None\n\n
    accept(final BaseTagVisitor visitor)\n
    accept(final BaseTagVisitor visitor, final boolean recurse)\n
    '''
def acceptReverse():
    '''returns None\n\n
    acceptReverse(final BaseTagVisitor visitor)\n
    '''
