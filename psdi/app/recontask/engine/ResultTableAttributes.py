TABLE_RECONLINK = "String  \"RECONLINK\""
TABLE_RECONRESULT = "String  \"RECONRESULT\""
def ():
    '''returns ResultTableAttributes\n\n
    (final String resultTableName)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String resultTableAttributeName, final String objectTableAttributeName)\n
    addAttribute(final String resultTableAttributeName, final String objectTableAttributeName, final boolean isInRootObject)\n
    '''
def getResultTableName():
    '''returns String\n\n
    getResultTableName()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getAttributeCount():
    '''returns int\n\n
    getAttributeCount()\n
    '''
def getResultTableAttributeName():
    '''returns String\n\n
    getResultTableAttributeName(final int index)\n
    '''
def getObjectTableAttributeName():
    '''returns String\n\n
    getObjectTableAttributeName(final int index)\n
    '''
def isObjectTableAttributeInRoot():
    '''returns boolean\n\n
    isObjectTableAttributeInRoot(final int index)\n
    '''
