COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomClassMapper\n\n
    ()\n
    '''
def getIndexing():
    '''returns IloDomClassIndexing\n\n
    getIndexing()\n
    '''
def setIndexing():
    '''returns None\n\n
    setIndexing(final IloDomClassIndexing indexing)\n
    '''
def isNotApplicable():
    '''returns boolean\n\n
    isNotApplicable()\n
    '''
def setNotApplicable():
    '''returns None\n\n
    setNotApplicable(final boolean notApplicable)\n
    '''
def getEClass():
    '''returns EClass\n\n
    getEClass()\n
    '''
def setEClass():
    '''returns None\n\n
    setEClass(final EClass eclass)\n
    '''
def getCrossReferenceFeatures():
    '''returns List<EReference>\n\n
    getCrossReferenceFeatures()\n
    '''
def getEntryMappers():
    '''returns List<IloDomClassEntryMapper>\n\n
    getEntryMappers()\n
    '''
def getType():
    '''returns IloDomRecordType\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final IloDomRecordType type)\n
    '''
def fromObjectModel():
    '''returns None\n\n
    fromObjectModel(final IloDomResourceImpl res, final IloDomObjectImpl o, IloDomRecord r)\n
    '''
def fromObjectModelForKey():
    '''returns None\n\n
    fromObjectModelForKey(final IloDomResourceImpl res, final IloDomObjectImpl o, IloDomRecord r)\n
    '''
def toObjectModel():
    '''returns EObject\n\n
    toObjectModel(final IloDomResourceImpl res, final IloDomRecord r)\n
    '''
def toObjectModelAt():
    '''returns EObject\n\n
    toObjectModelAt(final IloDomResourceImpl res, final IloDomRecord r, final int index)\n
    '''
def updateObjectModel():
    '''returns None\n\n
    updateObjectModel(final IloDomResourceImpl res, final IloDomObjectImpl obj, final IloDomRecord r, final int col)\n
    '''
def getMapperEntry():
    '''returns IloDomClassEntryMapper\n\n
    getMapperEntry(final EStructuralFeature f)\n
    getMapperEntry(final String name)\n
    '''
def clearObject():
    '''returns None\n\n
    clearObject(final EObject obj)\n
    '''
def clearObjectReference():
    '''returns None\n\n
    clearObjectReference(final EObject obj)\n
    '''
def updateObjectKey():
    '''returns IloDomAbstractObjectKey\n\n
    updateObjectKey(final IloDomResourceImpl res, final IloDomObjectImpl obj, final IloDomRecord r)\n
    updateObjectKey(final IloDomResourceImpl res, final IloDomObjectImpl obj, final IloDomRecord r, final IloDomAbstractObjectKey key)\n
    updateObjectKey(final IloDomResourceImpl res, final IloDomObjectImpl obj)\n
    '''
