def ():
    '''returns FeatureMapEObjectImpl\n\n
    (final InternalEObject owner, final int featureID)\n
    (final InternalEObject owner, final EStructuralFeature eStructuralFeature)\n
    ()\n
    (final int index)\n
    (final EStructuralFeature eStructuralFeature, final FeatureMap.Internal featureMap)\n
    (final EStructuralFeature eStructuralFeature, final FeatureMap.Internal featureMap)\n
    ()\n
    '''
def getEStructuralFeature():
    '''returns EStructuralFeature\n\n
    getEStructuralFeature()\n
    getEStructuralFeature(final int index)\n
    '''
def resolveProxy():
    '''returns Object\n\n
    resolveProxy(final EStructuralFeature feature, final int entryIndex, final int index, final Object object)\n
    '''
def getModCount():
    '''returns int\n\n
    getModCount()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final int index)\n
    '''
def setValue():
    '''returns Object\n\n
    setValue(final int index, final Object value)\n
    '''
def shadowAdd():
    '''returns NotificationChain\n\n
    shadowAdd(final Object object, NotificationChain notifications)\n
    '''
def inverseAdd():
    '''returns NotificationChain\n\n
    inverseAdd(final Object object, NotificationChain notifications)\n
    '''
def shadowRemove():
    '''returns NotificationChain\n\n
    shadowRemove(final Object object, NotificationChain notifications)\n
    '''
def inverseRemove():
    '''returns NotificationChain\n\n
    inverseRemove(final Object object, NotificationChain notifications)\n
    '''
def shadowSet():
    '''returns NotificationChain\n\n
    shadowSet(final Object oldObject, final Object newObject, NotificationChain notifications)\n
    '''
def inverseTouch():
    '''returns NotificationChain\n\n
    inverseTouch(final Object object, NotificationChain notifications)\n
    '''
def move():
    '''returns Object\n\n
    move(final int targetIndex, final int sourceIndex)\n
    move(final EStructuralFeature feature, final int index, final Object object)\n
    move(final EStructuralFeature feature, final int targetIndex, final int sourceIndex)\n
    '''
def set():
    '''returns Object\n\n
    set(final int index, final Object object)\n
    set(final EStructuralFeature feature, final Object object)\n
    set(final EStructuralFeature feature, final int index, final Object object)\n
    '''
def doSet():
    '''returns Object\n\n
    doSet(final int index, final Object object)\n
    '''
def add():
    '''returns None\n\n
    add(final Object object)\n
    add(final int index, final Object object)\n
    add(final int index, final EStructuralFeature feature, final Object object)\n
    add(final EStructuralFeature feature, final Object object)\n
    add(final EStructuralFeature feature, final int index, final Object object)\n
    add(final Object value)\n
    add(final EStructuralFeature eStructuralFeature, final Object value)\n
    '''
def doAdd():
    '''returns None\n\n
    doAdd(final int index, final Object object)\n
    '''
def addAll():
    '''returns boolean\n\n
    addAll(final Collection collection)\n
    addAll(final int index, final Collection collection)\n
    addAll(final int index, final EStructuralFeature feature, final Collection collection)\n
    addAll(final EStructuralFeature feature, final Collection collection)\n
    addAll(final EStructuralFeature feature, final int index, final Collection collection)\n
    '''
def doAddAll():
    '''returns boolean\n\n
    doAddAll(final Collection collection)\n
    doAddAll(final int index, final Collection collection)\n
    '''
def size():
    '''returns int\n\n
    size(final EStructuralFeature feature)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final EStructuralFeature feature)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final EStructuralFeature feature, final Object object)\n
    '''
def containsAll():
    '''returns boolean\n\n
    containsAll(final EStructuralFeature feature, final Collection collection)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final EStructuralFeature feature, final Object object)\n
    '''
def lastIndexOf():
    '''returns int\n\n
    lastIndexOf(final EStructuralFeature feature, final Object object)\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator(final EStructuralFeature feature)\n
    '''
def listIterator():
    '''returns ListIterator\n\n
    listIterator(final EStructuralFeature feature)\n
    listIterator(final EStructuralFeature feature, final int index)\n
    '''
def valueListIterator():
    '''returns ValueListIterator\n\n
    valueListIterator()\n
    valueListIterator(final int index)\n
    '''
def list():
    '''returns EList\n\n
    list(final EStructuralFeature feature)\n
    '''
def setting():
    '''returns Setting\n\n
    setting(final EStructuralFeature feature)\n
    '''
def basicList():
    '''returns List\n\n
    basicList(final EStructuralFeature feature)\n
    '''
def basicIterator():
    '''returns Iterator\n\n
    basicIterator(final EStructuralFeature feature)\n
    '''
def basicListIterator():
    '''returns ListIterator\n\n
    basicListIterator(final EStructuralFeature feature)\n
    basicListIterator(final EStructuralFeature feature, final int index)\n
    '''
def toArray():
    '''returns Object[]\n\n
    toArray(final EStructuralFeature feature)\n
    toArray(final EStructuralFeature feature, final Object[] array)\n
    '''
def addUnique():
    '''returns None\n\n
    addUnique(final EStructuralFeature feature, final Object object)\n
    addUnique(final EStructuralFeature feature, final int index, final Object object)\n
    '''
def basicAdd():
    '''returns NotificationChain\n\n
    basicAdd(final EStructuralFeature feature, final Object object, NotificationChain notifications)\n
    '''
def remove():
    '''returns Object\n\n
    remove(final EStructuralFeature feature, final Object object)\n
    remove(final EStructuralFeature feature, final int index)\n
    '''
def removeAll():
    '''returns boolean\n\n
    removeAll(final EStructuralFeature feature, final Collection collection)\n
    '''
def basicRemove():
    '''returns NotificationChain\n\n
    basicRemove(final EStructuralFeature feature, final Object object, NotificationChain notifications)\n
    basicRemove(final Object object, NotificationChain notifications)\n
    '''
def retainAll():
    '''returns boolean\n\n
    retainAll(final EStructuralFeature feature, final Collection collection)\n
    '''
def clear():
    '''returns None\n\n
    clear(final EStructuralFeature feature)\n
    '''
def get():
    '''returns Object\n\n
    get(final EStructuralFeature feature, final boolean resolve)\n
    get(final EStructuralFeature feature, final int index, final boolean resolve)\n
    '''
def setUnique():
    '''returns Object\n\n
    setUnique(final EStructuralFeature feature, final int index, final Object object)\n
    '''
def isSet():
    '''returns boolean\n\n
    isSet(final EStructuralFeature feature)\n
    '''
def unset():
    '''returns None\n\n
    unset(final EStructuralFeature feature)\n
    '''
def feature():
    '''returns EStructuralFeature\n\n
    feature()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def previous():
    '''returns Object\n\n
    previous()\n
    '''
def eDynamicGet():
    '''returns Object\n\n
    eDynamicGet(final EStructuralFeature eFeature, final boolean resolve)\n
    '''
def eDynamicSet():
    '''returns None\n\n
    eDynamicSet(final EStructuralFeature eFeature, final Object newValue)\n
    '''
def eDynamicUnset():
    '''returns None\n\n
    eDynamicUnset(final EStructuralFeature eFeature)\n
    '''
def eDynamicIsSet():
    '''returns boolean\n\n
    eDynamicIsSet(final EStructuralFeature eFeature)\n
    '''
def eDynamicInverseAdd():
    '''returns NotificationChain\n\n
    eDynamicInverseAdd(final InternalEObject otherEnd, final int featureID, final Class inverseClass, NotificationChain notifications)\n
    '''
def eDynamicInverseRemove():
    '''returns NotificationChain\n\n
    eDynamicInverseRemove(final InternalEObject otherEnd, final int featureID, final Class inverseClass, final NotificationChain notifications)\n
    '''
def featureMap():
    '''returns FeatureMap\n\n
    featureMap()\n
    '''
def eNotify():
    '''returns None\n\n
    eNotify(final Notification notification)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
