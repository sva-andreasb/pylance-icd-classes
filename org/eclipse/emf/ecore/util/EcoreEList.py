IS_SET = "int  1"
IS_UNSETTABLE = "int  2"
HAS_INSTANCE_CLASS = "int  4"
HAS_NAVIGABLE_INVERSE = "int  8"
HAS_MANY_INVERSE = "int  16"
IS_CONTAINMENT = "int  32"
IS_CONTAINER = "int  64"
IS_UNIQUE = "int  128"
IS_PRIMITIVE = "int  256"
IS_ENUM = "int  512"
IS_EOBJECT = "int  1024"
HAS_PROXIES = "int  2048"
def ():
    '''returns Dynamic\n\n
    (final Class dataClass, final InternalEObject owner)\n
    (final InternalEObject owner, final EStructuralFeature eStructuralFeature, final int size, final Object[] data)\n
    (final InternalEObject owner, final EStructuralFeature eStructuralFeature, final int size, final Object[] data)\n
    (final int kind, final Class dataClass, final InternalEObject owner)\n
    (final InternalEObject owner, final EStructuralFeature eStructuralFeature)\n
    (final int kind, final InternalEObject owner, final EStructuralFeature eStructuralFeature)\n
    (final int kind, final Class dataClass, final InternalEObject owner, final EStructuralFeature eStructuralFeature)\n
    '''
def getNotifier():
    '''returns Object\n\n
    getNotifier()\n
    '''
def getFeature():
    '''returns Object\n\n
    getFeature()\n
    '''
def getFeatureID():
    '''returns int\n\n
    getFeatureID()\n
    '''
def getEStructuralFeature():
    '''returns EStructuralFeature\n\n
    getEStructuralFeature()\n
    getEStructuralFeature()\n
    getEStructuralFeature()\n
    '''
def toArray():
    '''returns Object[]\n\n
    toArray()\n
    toArray(final Object[] array)\n
    '''
def basicList():
    '''returns List\n\n
    basicList()\n
    basicList()\n
    '''
def inverseAdd():
    '''returns NotificationChain\n\n
    inverseAdd(final Object object, final NotificationChain notifications)\n
    '''
def inverseRemove():
    '''returns NotificationChain\n\n
    inverseRemove(final Object object, final NotificationChain notifications)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Object object)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final Object object)\n
    '''
def lastIndexOf():
    '''returns int\n\n
    lastIndexOf(final Object object)\n
    '''
def basicIterator():
    '''returns Iterator\n\n
    basicIterator()\n
    basicIterator()\n
    '''
def basicListIterator():
    '''returns ListIterator\n\n
    basicListIterator()\n
    basicListIterator(final int index)\n
    basicListIterator()\n
    basicListIterator(final int index)\n
    '''
def getEObject():
    '''returns EObject\n\n
    getEObject()\n
    getEObject()\n
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
    isSet()\n
    '''
def unset():
    '''returns None\n\n
    unset()\n
    unset()\n
    unset()\n
    '''
def basicRemove():
    '''returns NotificationChain\n\n
    basicRemove(final Object object, final NotificationChain notifications)\n
    '''
def basicAdd():
    '''returns NotificationChain\n\n
    basicAdd(final Object object, final NotificationChain notifications)\n
    '''
