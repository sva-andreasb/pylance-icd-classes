def eURIFragmentSegment():
    '''returns String\n\n
    eURIFragmentSegment(EStructuralFeature eStructuralFeature, final EObject eObject)\n
    '''
def eObjectForURIFragmentSegment():
    '''returns EObject\n\n
    eObjectForURIFragmentSegment(final String uriFragmentSegment)\n
    '''
def eContains():
    '''returns boolean\n\n
    eContains(final EObject eObject)\n
    '''
def eContainer():
    '''returns EObject\n\n
    eContainer()\n
    '''
def eContainerFeatureID():
    '''returns int\n\n
    eContainerFeatureID()\n
    '''
def eContents():
    '''returns EList\n\n
    eContents()\n
    '''
def eCrossReferences():
    '''returns EList\n\n
    eCrossReferences()\n
    '''
def eAllContents():
    '''returns TreeIterator\n\n
    eAllContents()\n
    '''
def getChildren():
    '''returns Iterator\n\n
    getChildren(final Object object)\n
    '''
def eContainmentFeature():
    '''returns EReference\n\n
    eContainmentFeature()\n
    '''
def eContainingFeature():
    '''returns EStructuralFeature\n\n
    eContainingFeature()\n
    '''
def eResource():
    '''returns Resource\n\n
    eResource()\n
    '''
def eSetResource():
    '''returns NotificationChain\n\n
    eSetResource(final Resource.Internal resource, NotificationChain notifications)\n
    '''
def eGet():
    '''returns Object\n\n
    eGet(final EStructuralFeature eFeature)\n
    eGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eDynamicGet():
    '''returns Object\n\n
    eDynamicGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eOpenGet():
    '''returns Object\n\n
    eOpenGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eSet():
    '''returns None\n\n
    eSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eDynamicSet():
    '''returns None\n\n
    eDynamicSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eOpenSet():
    '''returns None\n\n
    eOpenSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eUnset():
    '''returns None\n\n
    eUnset(final EStructuralFeature eFeature)\n
    '''
def eDynamicUnset():
    '''returns None\n\n
    eDynamicUnset(final EStructuralFeature eFeature)\n
    '''
def eOpenUnset():
    '''returns None\n\n
    eOpenUnset(final EStructuralFeature eFeature)\n
    '''
def eIsSet():
    '''returns boolean\n\n
    eIsSet(final EStructuralFeature eFeature)\n
    '''
def eDynamicIsSet():
    '''returns boolean\n\n
    eDynamicIsSet(final EStructuralFeature eFeature)\n
    '''
def eOpenIsSet():
    '''returns boolean\n\n
    eOpenIsSet(final EStructuralFeature eFeature)\n
    '''
def eBasicSetContainer():
    '''returns NotificationChain\n\n
    eBasicSetContainer(final InternalEObject newContainer, final int newContainerFeatureID, NotificationChain msgs)\n
    '''
def eBasicRemoveFromContainer():
    '''returns NotificationChain\n\n
    eBasicRemoveFromContainer(final NotificationChain msgs)\n
    '''
def eDynamicBasicRemoveFromContainer():
    '''returns NotificationChain\n\n
    eDynamicBasicRemoveFromContainer(final NotificationChain msgs)\n
    '''
def eInverseAdd():
    '''returns NotificationChain\n\n
    eInverseAdd(final InternalEObject otherEnd, final int featureID, final Class baseClass, NotificationChain msgs)\n
    '''
def eDynamicInverseAdd():
    '''returns NotificationChain\n\n
    eDynamicInverseAdd(final InternalEObject otherEnd, final int featureID, final Class inverseClass, final NotificationChain msgs)\n
    '''
def eInverseRemove():
    '''returns NotificationChain\n\n
    eInverseRemove(final InternalEObject otherEnd, final int featureID, final Class baseClass, final NotificationChain msgs)\n
    '''
def eDynamicInverseRemove():
    '''returns NotificationChain\n\n
    eDynamicInverseRemove(final InternalEObject otherEnd, final int featureID, final Class inverseClass, final NotificationChain msgs)\n
    '''
def eProxyURI():
    '''returns URI\n\n
    eProxyURI()\n
    '''
def eSetProxyURI():
    '''returns None\n\n
    eSetProxyURI(final URI uri)\n
    '''
def eResolveProxy():
    '''returns EObject\n\n
    eResolveProxy(final InternalEObject proxy)\n
    '''
def eIsProxy():
    '''returns boolean\n\n
    eIsProxy()\n
    '''
def eBaseStructuralFeatureID():
    '''returns int\n\n
    eBaseStructuralFeatureID(final int derivedFeatureID, final Class baseClass)\n
    '''
def eDerivedStructuralFeatureID():
    '''returns int\n\n
    eDerivedStructuralFeatureID(final int baseFeatureID, final Class baseClass)\n
    eDerivedStructuralFeatureID(final EStructuralFeature eStructuralFeature)\n
    '''
def eClass():
    '''returns EClass\n\n
    eClass()\n
    '''
def eSetClass():
    '''returns None\n\n
    eSetClass(final EClass eClass)\n
    '''
def getEObject():
    '''returns EObject\n\n
    getEObject()\n
    '''
def getEStructuralFeature():
    '''returns EStructuralFeature\n\n
    getEStructuralFeature()\n
    '''
def get():
    '''returns Object\n\n
    get(final boolean resolve)\n
    '''
def set():
    '''returns None\n\n
    set(final Object newValue)\n
    '''
def isSet():
    '''returns boolean\n\n
    isSet()\n
    '''
def unset():
    '''returns None\n\n
    unset()\n
    '''
def eStore():
    '''returns EStore\n\n
    eStore()\n
    '''
def eSetStore():
    '''returns None\n\n
    eSetStore(final EStore store)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
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
    allocateSettings(final int dynamicFeatureCount)\n
    '''
def dynamicGet():
    '''returns Object\n\n
    dynamicGet(final int dynamicFeatureID)\n
    '''
def dynamicSet():
    '''returns None\n\n
    dynamicSet(final int dynamicFeatureID, final Object value)\n
    '''
def dynamicUnset():
    '''returns None\n\n
    dynamicUnset(final int dynamicFeatureID)\n
    '''
