def ():
    '''returns Linked\n\n
    (final MapperConfig<?> config, final AnnotationIntrospector ai, final boolean forSerialization, final PropertyName internalName)\n
    (final Linked<T> first)\n
    (final T v, final Linked<T> n, final PropertyName name, boolean explName, final boolean visible, final boolean ignored)\n
    '''
def withName():
    '''returns POJOPropertyBuilder\n\n
    withName(final PropertyName newName)\n
    '''
def withSimpleName():
    '''returns POJOPropertyBuilder\n\n
    withSimpleName(final String newSimpleName)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final POJOPropertyBuilder other)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getFullName():
    '''returns PropertyName\n\n
    getFullName()\n
    '''
def hasName():
    '''returns boolean\n\n
    hasName(final PropertyName name)\n
    '''
def getInternalName():
    '''returns String\n\n
    getInternalName()\n
    '''
def getWrapperName():
    '''returns PropertyName\n\n
    getWrapperName()\n
    '''
def isExplicitlyIncluded():
    '''returns boolean\n\n
    isExplicitlyIncluded()\n
    '''
def isExplicitlyNamed():
    '''returns boolean\n\n
    isExplicitlyNamed()\n
    '''
def getMetadata():
    '''returns PropertyMetadata\n\n
    getMetadata()\n
    '''
def getPrimaryType():
    '''returns JavaType\n\n
    getPrimaryType()\n
    '''
def hasGetter():
    '''returns boolean\n\n
    hasGetter()\n
    '''
def hasSetter():
    '''returns boolean\n\n
    hasSetter()\n
    '''
def hasField():
    '''returns boolean\n\n
    hasField()\n
    '''
def hasConstructorParameter():
    '''returns boolean\n\n
    hasConstructorParameter()\n
    '''
def couldDeserialize():
    '''returns boolean\n\n
    couldDeserialize()\n
    '''
def couldSerialize():
    '''returns boolean\n\n
    couldSerialize()\n
    '''
def getGetter():
    '''returns AnnotatedMethod\n\n
    getGetter()\n
    '''
def getSetter():
    '''returns AnnotatedMethod\n\n
    getSetter()\n
    '''
def getField():
    '''returns AnnotatedField\n\n
    getField()\n
    '''
def getConstructorParameter():
    '''returns AnnotatedParameter\n\n
    getConstructorParameter()\n
    '''
def getConstructorParameters():
    '''returns Iterator<AnnotatedParameter>\n\n
    getConstructorParameters()\n
    '''
def getPrimaryMember():
    '''returns AnnotatedMember\n\n
    getPrimaryMember()\n
    '''
def isTypeId():
    '''returns boolean\n\n
    isTypeId()\n
    '''
def withMember():
    '''returns ObjectIdInfo\n\n
    withMember(final AnnotatedMember member)\n
    withMember(final AnnotatedMember member)\n
    withMember(final AnnotatedMember member)\n
    withMember(final AnnotatedMember member)\n
    withMember(final AnnotatedMember member)\n
    withMember(final AnnotatedMember member)\n
    '''
def findObjectIdInfo():
    '''returns ObjectIdInfo\n\n
    findObjectIdInfo()\n
    '''
def addField():
    '''returns None\n\n
    addField(final AnnotatedField a, final PropertyName name, final boolean explName, final boolean visible, final boolean ignored)\n
    '''
def addCtor():
    '''returns None\n\n
    addCtor(final AnnotatedParameter a, final PropertyName name, final boolean explName, final boolean visible, final boolean ignored)\n
    '''
def addGetter():
    '''returns None\n\n
    addGetter(final AnnotatedMethod a, final PropertyName name, final boolean explName, final boolean visible, final boolean ignored)\n
    '''
def addSetter():
    '''returns None\n\n
    addSetter(final AnnotatedMethod a, final PropertyName name, final boolean explName, final boolean visible, final boolean ignored)\n
    '''
def addAll():
    '''returns None\n\n
    addAll(final POJOPropertyBuilder src)\n
    '''
def removeIgnored():
    '''returns None\n\n
    removeIgnored()\n
    '''
def removeConstructors():
    '''returns None\n\n
    removeConstructors()\n
    '''
def trimByVisibility():
    '''returns Linked<T>\n\n
    trimByVisibility()\n
    trimByVisibility()\n
    '''
def mergeAnnotations():
    '''returns None\n\n
    mergeAnnotations(final boolean forSerialization)\n
    '''
def anyVisible():
    '''returns boolean\n\n
    anyVisible()\n
    '''
def anyIgnorals():
    '''returns boolean\n\n
    anyIgnorals()\n
    '''
def findExplicitNames():
    '''returns Set<PropertyName>\n\n
    findExplicitNames()\n
    '''
def explode():
    '''returns Collection<POJOPropertyBuilder>\n\n
    explode(final Collection<PropertyName> newNames)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns T\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def withoutNext():
    '''returns Linked<T>\n\n
    withoutNext()\n
    '''
def withValue():
    '''returns Linked<T>\n\n
    withValue(final T newValue)\n
    '''
def withNext():
    '''returns Linked<T>\n\n
    withNext(final Linked<T> newNext)\n
    '''
def withoutIgnored():
    '''returns Linked<T>\n\n
    withoutIgnored()\n
    '''
def withoutNonVisible():
    '''returns Linked<T>\n\n
    withoutNonVisible()\n
    '''
