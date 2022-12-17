PRICEBOOK_STATUS_LIST = "String  \"PLUSPPBSTATUS\""
def ():
    '''returns PlusPPriceBook\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    duplicate(final MboSetRemote mboSetRemote)\n
    '''
def revisePriceBook():
    '''returns PlusPPriceBookRemote\n\n
    revisePriceBook(final MboSetRemote mboSetRemote, final String val, final Date val2)\n
    '''
def toExternalPBStatus():
    '''returns String\n\n
    toExternalPBStatus(final String value)\n
    '''
def toInternalPriceBookStatus():
    '''returns String\n\n
    toInternalPriceBookStatus(final String value)\n
    '''
def getNewRevisionNumber():
    '''returns int\n\n
    getNewRevisionNumber()\n
    '''
def canRevise():
    '''returns boolean\n\n
    canRevise()\n
    '''
def isPendingRevision():
    '''returns boolean\n\n
    isPendingRevision(final MboRemote mboRemote)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def isRevision():
    '''returns boolean\n\n
    isRevision()\n
    '''
def setRevision():
    '''returns None\n\n
    setRevision(final boolean isRevision)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String s, final Date date, final String s2)\n
    changeStatus(final String status, final Date date, final Date date2, final String memo)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def validateEffectiveDateField():
    '''returns None\n\n
    validateEffectiveDateField(final Date date, final String s)\n
    '''
def validateEndDateField():
    '''returns None\n\n
    validateEndDateField(final Date date, final String anObject)\n
    '''
def getInternalType():
    '''returns String\n\n
    getInternalType()\n
    '''
def copyCraftsToRate():
    '''returns None\n\n
    copyCraftsToRate(final MboSetRemote mboSetRemote)\n
    '''
