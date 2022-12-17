BL_SERVICE_UNAVAILABLE = "int  101"
BL_SERVICE_AVAILABLE = "int  102"
BL_RETRIEVED = "int  103"
BL_FAILED_RETRIEVED = "int  104"
BL_SET_SUCCEEDED = "int  105"
BL_SET_FAILED = "int  106"
BL_UPDATED = "int  107"
BL_OVERFLOWED = "int  108"
def ():
    '''returns BLEvent\n\n
    (final Object o, final int n)\n
    (final Object o, final int n, final int reasonCode)\n
    (final Object o, final int n, final BL bl)\n
    '''
def getBL():
    '''returns BL\n\n
    getBL()\n
    '''
def getReason():
    '''returns int\n\n
    getReason()\n
    '''
