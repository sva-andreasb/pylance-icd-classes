COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomRecordType\n\n
    ()\n
    '''
def isNotApplicable():
    '''returns boolean\n\n
    isNotApplicable()\n
    '''
def setNotApplicable():
    '''returns None\n\n
    setNotApplicable(final boolean notApplicable)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String value)\n
    '''
def getFields():
    '''returns List<IloDomRecordField>\n\n
    getFields()\n
    '''
def getField():
    '''returns IloDomRecordField\n\n
    getField(final String name)\n
    '''
def checkRecord():
    '''returns boolean\n\n
    checkRecord(final IloDomRecord t)\n
    '''
def newRecord():
    '''returns IloDomRecord\n\n
    newRecord()\n
    newRecord(final IloDomRecord t)\n
    '''
def getPrimaryKey():
    '''returns List<IloDomRecordField>\n\n
    getPrimaryKey()\n
    '''
def newRecordKey():
    '''returns IloDomAbstractObjectKey\n\n
    newRecordKey(final IloDomRecord t)\n
    newRecordKey(final Object[] keyParts)\n
    '''
def newRecordFromKey():
    '''returns IloDomRecord\n\n
    newRecordFromKey(final IloDomAbstractObjectKey recordKey)\n
    '''
def recordToString():
    '''returns String\n\n
    recordToString(final IloDomRecord r)\n
    '''
