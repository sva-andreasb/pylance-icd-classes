def ():
    '''returns Entry\n\n
    ()\n
    (final EStore eStore)\n
    (final EClass eClass)\n
    (final EClass eClass, final EStore eStore)\n
    (final InternalEObject owner, final EStructuralFeature eStructuralFeature, final EStore store)\n
    (final InternalEObject owner, final EStructuralFeature eStructuralFeature, final EStore store)\n
    ()\n
    (final InternalEObject eObject, final EStructuralFeature eStructuralFeature)\n
    '''
def dynamicGet():
    '''returns Object\n\n
    dynamicGet(final int dynamicFeatureID)\n
    dynamicGet(final int dynamicFeatureID)\n
    '''
def dynamicSet():
    '''returns None\n\n
    dynamicSet(final int dynamicFeatureID, final Object value)\n
    dynamicSet(final int dynamicFeatureID, final Object value)\n
    '''
def dynamicUnset():
    '''returns None\n\n
    dynamicUnset(final int dynamicFeatureID)\n
    dynamicUnset(final int dynamicFeatureID)\n
    '''
def eDynamicIsSet():
    '''returns boolean\n\n
    eDynamicIsSet(final EStructuralFeature eStructuralFeature)\n
    '''
def eContainer():
    '''returns EObject\n\n
    eContainer()\n
    '''
def eContainerFeatureID():
    '''returns int\n\n
    eContainerFeatureID()\n
    '''
def eStore():
    '''returns EStore\n\n
    eStore()\n
    '''
def eSetStore():
    '''returns None\n\n
    eSetStore(final EStore store)\n
    '''
def eDerivedStructuralFeatureID():
    '''returns int\n\n
    eDerivedStructuralFeatureID(final EStructuralFeature eStructuralFeature)\n
    '''
def getEClass():
    '''returns EClass\n\n
    getEClass()\n
    '''
def setEClass():
    '''returns None\n\n
    setEClass(final EClass eClass)\n
    '''
def getEProxyURI():
    '''returns URI\n\n
    getEProxyURI()\n
    '''
def setEProxyURI():
    '''returns None\n\n
    setEProxyURI(final URI eProxyURI)\n
    '''
def setEResource():
    '''returns None\n\n
    setEResource(final Resource.Internal eResource)\n
    '''
def getEContents():
    '''returns EList\n\n
    getEContents()\n
    '''
def setEContents():
    '''returns None\n\n
    setEContents(final EList eContents)\n
    '''
def getECrossReferences():
    '''returns EList\n\n
    getECrossReferences()\n
    '''
def setECrossReferences():
    '''returns None\n\n
    setECrossReferences(final EList eCrossReferences)\n
    '''
def hasSettings():
    '''returns boolean\n\n
    hasSettings()\n
    '''
def allocateSettings():
    '''returns None\n\n
    allocateSettings(final int maximumDynamicFeatureID)\n
    '''
def getEStructuralFeature():
    '''returns EStructuralFeature\n\n
    getEStructuralFeature()\n
    getEStructuralFeature()\n
    '''
def get():
    '''returns Object\n\n
    get(final InternalEObject eObject, final EStructuralFeature feature, final int index)\n
    '''
def set():
    '''returns Object\n\n
    set(final InternalEObject eObject, final EStructuralFeature feature, final int index, final Object value)\n
    '''
def add():
    '''returns None\n\n
    add(final InternalEObject eObject, final EStructuralFeature feature, final int index, final Object value)\n
    '''
def remove():
    '''returns Object\n\n
    remove(final InternalEObject eObject, final EStructuralFeature feature, final int index)\n
    '''
def move():
    '''returns Object\n\n
    move(final InternalEObject eObject, final EStructuralFeature feature, final int targetIndex, final int sourceIndex)\n
    '''
def clear():
    '''returns None\n\n
    clear(final InternalEObject eObject, final EStructuralFeature feature)\n
    '''
def isSet():
    '''returns boolean\n\n
    isSet(final InternalEObject eObject, final EStructuralFeature feature)\n
    '''
def unset():
    '''returns None\n\n
    unset(final InternalEObject eObject, final EStructuralFeature feature)\n
    '''
def size():
    '''returns int\n\n
    size(final InternalEObject eObject, final EStructuralFeature feature)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final InternalEObject eObject, final EStructuralFeature feature, final Object value)\n
    '''
def lastIndexOf():
    '''returns int\n\n
    lastIndexOf(final InternalEObject eObject, final EStructuralFeature feature, final Object value)\n
    '''
def toArray():
    '''returns Object[]\n\n
    toArray(final InternalEObject eObject, final EStructuralFeature feature)\n
    toArray(final InternalEObject eObject, final EStructuralFeature feature, final Object[] array)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final InternalEObject eObject, final EStructuralFeature feature)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final InternalEObject eObject, final EStructuralFeature feature, final Object value)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode(final InternalEObject eObject, final EStructuralFeature feature)\n
    hashCode()\n
    '''
def getContainer():
    '''returns InternalEObject\n\n
    getContainer(final InternalEObject eObject)\n
    '''
def getContainingFeature():
    '''returns EStructuralFeature\n\n
    getContainingFeature(final InternalEObject eObject)\n
    '''
def create():
    '''returns EObject\n\n
    create(final EClass eClass)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object that)\n
    '''
