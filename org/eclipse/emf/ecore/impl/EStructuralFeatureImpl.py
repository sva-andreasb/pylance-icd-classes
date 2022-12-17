CONTAINMENT_UNSETTABLE_DYNAMIC = "int  0"
CONTAINMENT_UNSETTABLE = "int  1"
CONTAINMENT_DYNAMIC = "int  2"
CONTAINMENT = "int  3"
CONTAINMENT_INVERSE_UNSETTABLE_DYNAMIC = "int  4"
CONTAINMENT_INVERSE_UNSETTABLE = "int  5"
CONTAINMENT_INVERSE_DYNAMIC = "int  6"
CONTAINMENT_INVERSE = "int  7"
DATA_UNIQUE_UNSETTABLE_DYNAMIC = "int  8"
DATA_UNIQUE_UNSETTABLE = "int  9"
DATA_UNIQUE_DYNAMIC = "int  10"
DATA_UNIQUE = "int  11"
DATA_UNSETTABLE_DYNAMIC = "int  12"
DATA_UNSETTABLE = "int  13"
DATA_DYNAMIC = "int  14"
DATA = "int  15"
EOBJECT_RESOLVE_UNSETTABLE_DYNAMIC = "int  16"
EOBJECT_RESOLVE_UNSETTABLE = "int  17"
EOBJECT_RESOLVE_DYNAMIC = "int  18"
EOBJECT_RESOLVE = "int  19"
EOBJECT_UNSETTABLE_DYNAMIC = "int  20"
EOBJECT_UNSETTABLE = "int  21"
EOBJECT_DYNAMIC = "int  22"
EOBJECT = "int  23"
MANY_INVERSE_RESOLVE_UNSETTABLE_DYNAMIC = "int  24"
MANY_INVERSE_RESOLVE_UNSETTABLE = "int  25"
MANY_INVERSE_RESOLVE_DYNAMIC = "int  26"
MANY_INVERSE_RESOLVE = "int  27"
MANY_INVERSE_UNSETTABLE_DYNAMIC = "int  28"
MANY_INVERSE_UNSETTABLE = "int  29"
MANY_INVERSE_DYNAMIC = "int  30"
MANY_INVERSE = "int  31"
INVERSE_RESOLVE_UNSETTABLE_DYNAMIC = "int  32"
INVERSE_RESOLVE_UNSETTABLE = "int  33"
INVERSE_RESOLVE_DYNAMIC = "int  34"
INVERSE_RESOLVE = "int  35"
INVERSE_UNSETTABLE_DYNAMIC = "int  36"
INVERSE_UNSETTABLE = "int  37"
INVERSE_DYNAMIC = "int  38"
INVERSE = "int  39"
FEATURE_MAP = "int  40"
EMAP = "int  41"
def getDefaultValue():
    '''returns Object\n\n
    getDefaultValue()\n
    '''
def setDefaultValue():
    '''returns None\n\n
    setDefaultValue(final Object newDefaultValue)\n
    '''
def setDefaultValueLiteral():
    '''returns None\n\n
    setDefaultValueLiteral(final String newDefaultValueLiteral)\n
    '''
def setDefaultValueLiteralGen():
    '''returns None\n\n
    setDefaultValueLiteralGen(final String newDefaultValueLiteral)\n
    '''
def isUnsettable():
    '''returns boolean\n\n
    isUnsettable()\n
    '''
def setUnsettable():
    '''returns None\n\n
    setUnsettable(final boolean newUnsettable)\n
    '''
def isDerived():
    '''returns boolean\n\n
    isDerived()\n
    '''
def setDerived():
    '''returns None\n\n
    setDerived(final boolean newDerived)\n
    '''
def getEContainingClass():
    '''returns EClass\n\n
    getEContainingClass()\n
    '''
def eGet():
    '''returns Object\n\n
    eGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eIsSet():
    '''returns boolean\n\n
    eIsSet(final EStructuralFeature eFeature)\n
    '''
def eSet():
    '''returns None\n\n
    eSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eUnset():
    '''returns None\n\n
    eUnset(final EStructuralFeature eFeature)\n
    '''
def isTransient():
    '''returns boolean\n\n
    isTransient()\n
    '''
def setTransient():
    '''returns None\n\n
    setTransient(final boolean newTransient)\n
    '''
def isVolatile():
    '''returns boolean\n\n
    isVolatile()\n
    '''
def setVolatile():
    '''returns None\n\n
    setVolatile(final boolean newVolatile)\n
    '''
def isChangeable():
    '''returns boolean\n\n
    isChangeable()\n
    '''
def setChangeable():
    '''returns None\n\n
    setChangeable(final boolean newChangeable)\n
    '''
def getDefaultValueLiteral():
    '''returns String\n\n
    getDefaultValueLiteral()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getFeatureID():
    '''returns int\n\n
    getFeatureID()\n
    '''
def setFeatureID():
    '''returns None\n\n
    setFeatureID(final int featureID)\n
    '''
def getContainerClass():
    '''returns Class\n\n
    getContainerClass()\n
    '''
def eInverseAdd():
    '''returns NotificationChain\n\n
    eInverseAdd(final InternalEObject otherEnd, final int featureID, final Class baseClass, NotificationChain msgs)\n
    '''
def eInverseRemove():
    '''returns NotificationChain\n\n
    eInverseRemove(final InternalEObject otherEnd, final int featureID, final Class baseClass, final NotificationChain msgs)\n
    '''
def eBasicRemoveFromContainer():
    '''returns NotificationChain\n\n
    eBasicRemoveFromContainer(final NotificationChain msgs)\n
    '''
def setContainerClass():
    '''returns None\n\n
    setContainerClass(final Class containerClass)\n
    '''
def getSettingDelegate():
    '''returns SettingDelegate\n\n
    getSettingDelegate()\n
    '''
def setSettingDelegate():
    '''returns None\n\n
    setSettingDelegate(final SettingDelegate settingDelegate)\n
    '''
def isFeatureMap():
    '''returns boolean\n\n
    isFeatureMap()\n
    '''
def getExtendedMetaData():
    '''returns EStructuralFeatureExtendedMetaData\n\n
    getExtendedMetaData()\n
    '''
def setExtendedMetaData():
    '''returns None\n\n
    setExtendedMetaData(final EStructuralFeatureExtendedMetaData eStructuralFeatureExtendedMetaData)\n
    '''
def ():
    '''returns SettingMany\n\n
    (final EStructuralFeature feature, final EStructuralFeature featureMapFeature)\n
    (final int style, final Class dataClass, final EStructuralFeature feature)\n
    (final int style, final EStructuralFeature feature)\n
    (final int style, final Class dataClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final int style, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final Object defaultValue, final Object intrinsicDefaultValue, final EStructuralFeature feature)\n
    (final EDataType eDataType, final Object defaultValue, final Object intrinsicDefaultValue, final EStructuralFeature feature)\n
    (final Class dataClass, final Object defaultValue, final Object intrinsicDefaultValue, final EStructuralFeature feature)\n
    (final Object defaultValue, final Object intrinsicDefaultValue, final EStructuralFeature feature)\n
    (final EDataType eDataType, final Object defaultValue, final Object intrinsicDefaultValue, final EStructuralFeature feature)\n
    (final Class dataClass, final Object defaultValue, final Object intrinsicDefaultValue, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EClass eClass, final EStructuralFeature feature, final EReference inverseFeature)\n
    (final EObject owner, final EStructuralFeature eStructuralFeature, final List list)\n
    '''
def dynamicSetting():
    '''returns Setting\n\n
    dynamicSetting(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicSetting(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicSetting(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    '''
def dynamicGet():
    '''returns Object\n\n
    dynamicGet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final boolean resolve)\n
    dynamicGet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final boolean resolve)\n
    dynamicGet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final boolean resolve)\n
    dynamicGet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final boolean resolve)\n
    dynamicGet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final boolean resolve)\n
    '''
def dynamicSet():
    '''returns None\n\n
    dynamicSet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final Object newValue)\n
    dynamicSet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final Object newValue)\n
    dynamicSet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final Object newValue)\n
    dynamicSet(final InternalEObject owner, final DynamicValueHolder settings, final int index, Object newValue)\n
    dynamicSet(final InternalEObject owner, final DynamicValueHolder settings, final int index, Object newValue)\n
    dynamicSet(final InternalEObject owner, final DynamicValueHolder settings, final int index, final Object newValue)\n
    '''
def dynamicUnset():
    '''returns None\n\n
    dynamicUnset(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicUnset(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicUnset(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicUnset(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicUnset(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicUnset(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    '''
def dynamicIsSet():
    '''returns boolean\n\n
    dynamicIsSet(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicIsSet(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicIsSet(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicIsSet(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicIsSet(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    dynamicIsSet(final InternalEObject owner, final DynamicValueHolder settings, final int index)\n
    '''
def dynamicInverseAdd():
    '''returns NotificationChain\n\n
    dynamicInverseAdd(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, final NotificationChain notifications)\n
    dynamicInverseAdd(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, final NotificationChain notifications)\n
    dynamicInverseAdd(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, final NotificationChain notifications)\n
    dynamicInverseAdd(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, NotificationChain notifications)\n
    dynamicInverseAdd(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, NotificationChain notifications)\n
    '''
def dynamicInverseRemove():
    '''returns NotificationChain\n\n
    dynamicInverseRemove(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, final NotificationChain notifications)\n
    dynamicInverseRemove(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, NotificationChain notifications)\n
    dynamicInverseRemove(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, final NotificationChain notifications)\n
    dynamicInverseRemove(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, NotificationChain notifications)\n
    dynamicInverseRemove(final InternalEObject owner, final DynamicValueHolder settings, final int index, final InternalEObject otherEnd, NotificationChain notifications)\n
    '''
def getEObject():
    '''returns EObject\n\n
    getEObject()\n
    getEObject()\n
    '''
def getEStructuralFeature():
    '''returns EStructuralFeature\n\n
    getEStructuralFeature()\n
    getEStructuralFeature()\n
    '''
def get():
    '''returns Object\n\n
    get(final boolean resolve)\n
    get(final boolean resolve)\n
    '''
def set():
    '''returns None\n\n
    set(final Object newValue)\n
    set(final Object newValue)\n
    '''
def isSet():
    '''returns boolean\n\n
    isSet()\n
    isSet()\n
    '''
def unset():
    '''returns None\n\n
    unset()\n
    unset()\n
    '''
