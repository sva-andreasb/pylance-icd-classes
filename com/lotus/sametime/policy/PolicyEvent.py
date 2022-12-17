POLICY_SERVICE_AVAILABLE = "int  5"
POLICY_SERVICE_UNAVAILABLE = "int  6"
def ():
    '''returns PolicyEvent\n\n
    (final Object o, final int n)\n
    (final Object o, final int n, final String[] pvId)\n
    (final Object o, final int n, final int reason)\n
    (final Object o, final int n, final PolicyValue[] pvList)\n
    (final Object o, final int n, final String[] pvId, final int reason)\n
    '''
def getQueryResult():
    '''returns PolicyValue[]\n\n
    getQueryResult()\n
    '''
def getReason():
    '''returns int\n\n
    getReason()\n
    '''
def getPViD():
    '''returns String[]\n\n
    getPViD()\n
    '''
