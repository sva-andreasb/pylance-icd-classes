RESERVED = "int  -1"
def ():
    '''returns StructuredDataId\n\n
    (final String name)\n
    (final String name, final int maxLength)\n
    (final String name, final String[] required, final String[] optional)\n
    (final String name, final String[] required, final String[] optional, int maxLength)\n
    (final String name, final int enterpriseNumber, final String[] required, final String[] optional)\n
    (final String name, final int enterpriseNumber, final String[] required, final String[] optional, final int maxLength)\n
    '''
def makeId():
    '''returns StructuredDataId\n\n
    makeId(final StructuredDataId id)\n
    makeId(final String defaultId, final int anEnterpriseNumber)\n
    '''
def getRequired():
    '''returns String[]\n\n
    getRequired()\n
    '''
def getOptional():
    '''returns String[]\n\n
    getOptional()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getEnterpriseNumber():
    '''returns int\n\n
    getEnterpriseNumber()\n
    '''
def isReserved():
    '''returns boolean\n\n
    isReserved()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def formatTo():
    '''returns None\n\n
    formatTo(final StringBuilder buffer)\n
    '''
