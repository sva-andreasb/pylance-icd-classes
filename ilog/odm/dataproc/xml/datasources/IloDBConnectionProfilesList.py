COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDBConnectionProfilesList\n\n
    (final QName qname)\n
    '''
def getDBConnections():
    '''returns List<IloDBConnectionProfileImpl>\n\n
    getDBConnections()\n
    '''
def getDBConnection():
    '''returns IloDBConnectionProfileImpl\n\n
    getDBConnection(final String id)\n
    '''
def addDBConnection():
    '''returns IloDBConnectionProfileImpl\n\n
    addDBConnection(String id)\n
    '''
def removeDBConnection():
    '''returns None\n\n
    removeDBConnection(final IloDBConnectionProfileImpl c)\n
    '''
def isDuplicateId():
    '''returns boolean\n\n
    isDuplicateId(final IloDBConnectionProfileImpl c)\n
    '''
