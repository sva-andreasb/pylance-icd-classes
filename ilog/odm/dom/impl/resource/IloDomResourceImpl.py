COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
FORMAT_OPTION = "String  \"FORMAT\""
FORMAT_CRF = "String  \"CRF\""
ENTITIES_OPTION = "String  \"ENTITIES\""
OBJECTS_OPTION = "String  \"OBJECTS\""
def ():
    '''returns IloDomFactoryAdapter\n\n
    ()\n
    (final IloDomModelManager<?> modelManager, final String modelid)\n
    (final IloDomModelManager<?> modelManager, final String modelid, final IloDomFactory factory)\n
    (final EFactory defaultFactory)\n
    '''
def getProxies():
    '''returns Collection<IloDomObjectImpl>\n\n
    getProxies()\n
    '''
def getFactory():
    '''returns IloDomFactory\n\n
    getFactory()\n
    '''
def getConfiguration():
    '''returns IloDomConfiguration\n\n
    getConfiguration()\n
    '''
def getEPackage():
    '''returns EPackage\n\n
    getEPackage()\n
    '''
def getEFactory():
    '''returns EFactory\n\n
    getEFactory()\n
    '''
def getModelId():
    '''returns String\n\n
    getModelId()\n
    '''
def getECollectorClass():
    '''returns EClass\n\n
    getECollectorClass()\n
    '''
def updateRowidMap():
    '''returns None\n\n
    updateRowidMap(final IloDomRowKey key, final IloDomObjectImpl obj)\n
    '''
def getObjectByRowid():
    '''returns IloDomObjectImpl\n\n
    getObjectByRowid(final IloDomRecordType recordType, final long rowid)\n
    '''
def getProxyById():
    '''returns IloDomObjectImpl\n\n
    getProxyById(final IloDomObjectKey id)\n
    '''
def setProxyById():
    '''returns None\n\n
    setProxyById(final IloDomObjectImpl obj)\n
    '''
def removeFromRowidMap():
    '''returns None\n\n
    removeFromRowidMap(final EObject eObject)\n
    '''
def attached():
    '''returns None\n\n
    attached(final EObject eObject)\n
    '''
def detached():
    '''returns None\n\n
    detached(final EObject eObject)\n
    '''
def getEClass():
    '''returns EClass\n\n
    getEClass(final Class<? extends IloDomObject> entity)\n
    '''
def createEObject():
    '''returns EObject\n\n
    createEObject(final Class<? extends IloDomObject> entity)\n
    '''
def propagateObjectKeyChange():
    '''returns None\n\n
    propagateObjectKeyChange(final IloDomObjectImpl source, final EStructuralFeature feature)\n
    propagateObjectKeyChange(final IloDomObjectImpl obj)\n
    '''
def setPropagateKeyChangeOnly():
    '''returns None\n\n
    setPropagateKeyChangeOnly(final boolean propagateKeyChangeOnly)\n
    '''
def createEObjectAt():
    '''returns EObject\n\n
    createEObjectAt(final Class<? extends IloDomObject> entity, final int index)\n
    '''
def ensureCapacity():
    '''returns None\n\n
    ensureCapacity(final Class<? extends IloDomObject> entity, final int size)\n
    '''
def addEObjectAt():
    '''returns None\n\n
    addEObjectAt(final EObject obj, final int index)\n
    '''
def createObject():
    '''returns EObject\n\n
    createObject(final Class<? extends IloDomObject> entity)\n
    '''
def createObjectAt():
    '''returns EObject\n\n
    createObjectAt(final Class<? extends IloDomObject> entity, final int index)\n
    '''
def getCollectorFeature():
    '''returns EReference\n\n
    getCollectorFeature(final Class<? extends IloDomObject> entity)\n
    '''
def getEObjectAt():
    '''returns EObject\n\n
    getEObjectAt(final Class<? extends IloDomObject> entity, final int index)\n
    '''
def checkRefCount():
    '''returns None\n\n
    checkRefCount(final IloDomObjectImpl obj)\n
    '''
def startObjectInit():
    '''returns None\n\n
    startObjectInit()\n
    '''
def stopObjectInit():
    '''returns None\n\n
    stopObjectInit()\n
    '''
def setRecordID():
    '''returns None\n\n
    setRecordID(final IloDomObjectImpl obj, final IloDomAbstractObjectKey id)\n
    '''
def getID():
    '''returns String\n\n
    getID(final EObject eObject)\n
    '''
def setID():
    '''returns None\n\n
    setID(final EObject eObject, final String id)\n
    '''
def getEObjectByID():
    '''returns EObject\n\n
    getEObjectByID(final String uriFragment)\n
    '''
def deleteContent():
    '''returns None\n\n
    deleteContent()\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll()\n
    '''
def createECollector():
    '''returns None\n\n
    createECollector()\n
    '''
def getECollector():
    '''returns EObject\n\n
    getECollector()\n
    '''
def getCollector():
    '''returns IloDomCollector\n\n
    getCollector()\n
    '''
def getEEntityObjects():
    '''returns List<IloDomObjectImpl>\n\n
    getEEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def getDomClass():
    '''returns IloDomEntityClass\n\n
    getDomClass(final Class<? extends IloDomObject> entity)\n
    '''
def nullifyReferences():
    '''returns None\n\n
    nullifyReferences(final IloDomObjectImpl obj)\n
    nullifyReferences(final Collection<IloDomObjectImpl> objs, final EClass eclass)\n
    '''
def replaceReferences():
    '''returns None\n\n
    replaceReferences(final IloDomObjectImpl obj, final IloDomObjectImpl newobj)\n
    '''
def touchReferences():
    '''returns None\n\n
    touchReferences(final IloDomObjectImpl obj)\n
    '''
def nullifyReferencesWithNotification():
    '''returns List<Notification>\n\n
    nullifyReferencesWithNotification(final List<IloDomObject> objs, final EClass eclass)\n
    '''
def listUnresolvedReferences():
    '''returns List<IloDomUnresolvedReference>\n\n
    listUnresolvedReferences(final Collection<IloDomObjectImpl> proxies, final Collection<Class<? extends IloDomObject>> scope)\n
    '''
def getReferencePaths():
    '''returns List<List<EStructuralFeature>>\n\n
    getReferencePaths(final EStructuralFeature feature)\n
    '''
def getColumnFromPath():
    '''returns String\n\n
    getColumnFromPath(final List<EStructuralFeature> path)\n
    '''
def load():
    '''returns None\n\n
    load(final Map<?, ?> options)\n
    '''
def save():
    '''returns None\n\n
    save(final Map<?, ?> options)\n
    '''
def doLoad():
    '''returns None\n\n
    doLoad(final InputStream inputStream, final Map<?, ?> options)\n
    '''
def doSave():
    '''returns None\n\n
    doSave(final OutputStream outputStream, final Map<?, ?> options)\n
    '''
def getSchema():
    '''returns IloDomSchema\n\n
    getSchema()\n
    '''
def deleteEntityObjectsAndReferences():
    '''returns None\n\n
    deleteEntityObjectsAndReferences(final Class<? extends IloDomObject> entity)\n
    '''
def deleteEntityObjects():
    '''returns None\n\n
    deleteEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def getObjectByKey():
    '''returns IloDomObjectImpl\n\n
    getObjectByKey(final Class<? extends IloDomObject> entity, final Object[] keyParts)\n
    getObjectByKey(final IloDomObjectKey key)\n
    '''
def shuttingDown():
    '''returns None\n\n
    shuttingDown()\n
    '''
def indexEntity():
    '''returns None\n\n
    indexEntity(final Class<? extends IloDomObject> entity)\n
    '''
def deindexEntity():
    '''returns None\n\n
    deindexEntity(final Class<? extends IloDomObject> entity)\n
    '''
def isEntityIndexed():
    '''returns boolean\n\n
    isEntityIndexed(final Class<? extends IloDomObject> entity)\n
    '''
def createObjectKey():
    '''returns IloDomObjectKey\n\n
    createObjectKey(final Class<? extends IloDomObject> entity, final Object[] keyParts)\n
    '''
def isApplicable():
    '''returns boolean\n\n
    isApplicable(final Class<? extends IloDomObject> entity)\n
    '''
def deleteObject():
    '''returns None\n\n
    deleteObject(final IloDomObject obj)\n
    '''
def deleteObjectAndReferences():
    '''returns None\n\n
    deleteObjectAndReferences(final IloDomObject obj)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def activateStringCache():
    '''returns None\n\n
    activateStringCache()\n
    activateStringCache(final int maxLength)\n
    '''
def deactivateStringCache():
    '''returns None\n\n
    deactivateStringCache()\n
    '''
def isStringCacheActivated():
    '''returns boolean\n\n
    isStringCacheActivated()\n
    '''
def getFromStringCache():
    '''returns String\n\n
    getFromStringCache(final String s)\n
    '''
def clearStringCache():
    '''returns None\n\n
    clearStringCache()\n
    '''
def resetStringCacheHits():
    '''returns None\n\n
    resetStringCacheHits()\n
    '''
def reportCacheHits():
    '''returns None\n\n
    reportCacheHits()\n
    '''
def getNotificationFactory():
    '''returns IloDomNotificationFactory\n\n
    getNotificationFactory()\n
    '''
def getModel():
    '''returns IloDomModel\n\n
    getModel()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Class<? extends IloDomObject> o1, final Class<? extends IloDomObject> o2)\n
    '''
def create():
    '''returns EObject\n\n
    create(final EClass eClass)\n
    '''
def notifyChanged():
    '''returns None\n\n
    notifyChanged(final Notification notification)\n
    notifyChanged(final Notification notification)\n
    '''
def notifyCollectorChanged():
    '''returns None\n\n
    notifyCollectorChanged(final IloDomObjectImpl collector, final Notification notification)\n
    '''
def notifyObjectChanged():
    '''returns None\n\n
    notifyObjectChanged(final IloDomObjectImpl source, final Notification notification)\n
    '''
def getTarget():
    '''returns Notifier\n\n
    getTarget()\n
    getTarget()\n
    '''
def setTarget():
    '''returns None\n\n
    setTarget(final Notifier newTarget)\n
    setTarget(final Notifier newTarget)\n
    '''
def isAdapterForType():
    '''returns boolean\n\n
    isAdapterForType(final Object type)\n
    isAdapterForType(final Object type)\n
    '''
def put():
    '''returns IloDomObjectImpl\n\n
    put(final IloDomAbstractObjectKey key, final IloDomObjectImpl obj)\n
    '''
def get():
    '''returns IloDomObjectImpl\n\n
    get(final IloDomAbstractObjectKey key)\n
    '''
def remove():
    '''returns IloDomObjectImpl\n\n
    remove(final IloDomAbstractObjectKey key)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    clear(final Object entry)\n
    '''
def getNotifications():
    '''returns List<Notification>\n\n
    getNotifications()\n
    '''
