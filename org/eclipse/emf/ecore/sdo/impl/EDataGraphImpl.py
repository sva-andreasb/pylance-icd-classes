def isAdapterForType():
    '''returns boolean\n\n
    isAdapterForType(final Object type)\n
    '''
def notifyChanged():
    '''returns None\n\n
    notifyChanged(final Notification msg)\n
    notifyChanged(final Notification notification)\n
    '''
def getTarget():
    '''returns Notifier\n\n
    getTarget()\n
    '''
def setTarget():
    '''returns None\n\n
    setTarget(final Notifier newTarget)\n
    '''
def getResourceSet():
    '''returns ResourceSet\n\n
    getResourceSet()\n
    '''
def setResourceSetGen():
    '''returns None\n\n
    setResourceSetGen(final ResourceSet newResourceSet)\n
    '''
def setResourceSet():
    '''returns None\n\n
    setResourceSet(final ResourceSet newResourceSet)\n
    '''
def getRootResource():
    '''returns Resource\n\n
    getRootResource()\n
    '''
def getDataGraphResource():
    '''returns Resource\n\n
    getDataGraphResource()\n
    '''
def getEChangeSummary():
    '''returns EChangeSummary\n\n
    getEChangeSummary()\n
    '''
def basicSetEChangeSummary():
    '''returns NotificationChain\n\n
    basicSetEChangeSummary(final EChangeSummary newEChangeSummary, NotificationChain msgs)\n
    '''
def setEChangeSummary():
    '''returns None\n\n
    setEChangeSummary(final EChangeSummary newEChangeSummary)\n
    '''
def getERootObject():
    '''returns EObject\n\n
    getERootObject()\n
    '''
def setERootObjectGen():
    '''returns None\n\n
    setERootObjectGen(final EObject newERootObject)\n
    '''
def setERootObject():
    '''returns None\n\n
    setERootObject(final EObject newERootObject)\n
    '''
def getEClassifier():
    '''returns EClassifier\n\n
    getEClassifier(final String namespaceURI, final String typeName)\n
    '''
def getType():
    '''returns Type\n\n
    getType(final String namespaceURI, final String typeName)\n
    '''
def getEType():
    '''returns EType\n\n
    getEType(final String namespaceURI, final String typeName)\n
    '''
def createEObject():
    '''returns EObject\n\n
    createEObject(final EClass type)\n
    '''
def createEDataObject():
    '''returns EDataObject\n\n
    createEDataObject(final EType type)\n
    '''
def getRootObject():
    '''returns DataObject\n\n
    getRootObject()\n
    '''
def createRootObject():
    '''returns DataObject\n\n
    createRootObject(final String namespaceURI, final String typeName)\n
    createRootObject(final Type type)\n
    '''
def getChangeSummary():
    '''returns ChangeSummary\n\n
    getChangeSummary()\n
    '''
def getWriteReplacement():
    '''returns Object\n\n
    getWriteReplacement()\n
    getWriteReplacement(final EObject eObject)\n
    getWriteReplacement(final EObject eObject)\n
    '''
def writeReplace():
    '''returns Object\n\n
    writeReplace()\n
    '''
def eObjectForURIFragmentSegment():
    '''returns EObject\n\n
    eObjectForURIFragmentSegment(final String uriFragmentSegment)\n
    '''
def eInverseAdd():
    '''returns NotificationChain\n\n
    eInverseAdd(final InternalEObject otherEnd, final int featureID, final Class baseClass, NotificationChain msgs)\n
    '''
def eInverseRemove():
    '''returns NotificationChain\n\n
    eInverseRemove(final InternalEObject otherEnd, final int featureID, final Class baseClass, final NotificationChain msgs)\n
    '''
def eGet():
    '''returns Object\n\n
    eGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eSet():
    '''returns None\n\n
    eSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eUnset():
    '''returns None\n\n
    eUnset(final EStructuralFeature eFeature)\n
    '''
def eIsSet():
    '''returns boolean\n\n
    eIsSet(final EStructuralFeature eFeature)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def ():
    '''returns EDataObjectExternalizable\n\n
    ()\n
    (final EDataGraph eDataGraph)\n
    ()\n
    (final EDataGraph eDataGraph, final EObject eObject)\n
    '''
def writeExternal():
    '''returns None\n\n
    writeExternal(final ObjectOutput objectOutput)\n
    writeExternal(final ObjectOutput objectOutput)\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray()\n
    '''
def readExternal():
    '''returns None\n\n
    readExternal(final ObjectInput objectInput)\n
    readExternal(final ObjectInput objectInput)\n
    '''
