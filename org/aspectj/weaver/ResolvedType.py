PARAMETERIZED_TYPE_IDENTIFIER = "String  \"P\""
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable()\n
    '''
def isMissing():
    '''returns boolean\n\n
    isMissing()\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getAnnotationOfType():
    '''returns AnnotationAJ\n\n
    getAnnotationOfType(final UnresolvedType ofType)\n
    '''
def getResolvedComponentType():
    '''returns ResolvedType\n\n
    getResolvedComponentType()\n
    '''
def getWorld():
    '''returns World\n\n
    getWorld()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def getFields():
    '''returns Iterator<ResolvedMember>\n\n
    getFields()\n
    '''
def get():
    '''returns Iterator<ResolvedMember>\n\n
    get(final ResolvedType o)\n
    get(final ResolvedType type)\n
    get(final ResolvedType o)\n
    get(final ResolvedType o)\n
    get(final ResolvedType o)\n
    get(final ResolvedType type)\n
    get(final ResolvedType o)\n
    get(final ResolvedType type)\n
    get(final ResolvedType type)\n
    '''
def getMethods():
    '''returns Iterator<ResolvedMember>\n\n
    getMethods(final boolean wantGenerics, final boolean wantDeclaredParents)\n
    '''
def getMethodsIncludingIntertypeDeclarations():
    '''returns Iterator<ResolvedMember>\n\n
    getMethodsIncludingIntertypeDeclarations(final boolean wantGenerics, final boolean wantDeclaredParents)\n
    '''
def getHierarchy():
    '''returns Iterator<ResolvedType>\n\n
    getHierarchy()\n
    getHierarchy(final boolean wantGenerics, final boolean wantDeclaredParents)\n
    '''
def getMethodsWithoutIterator():
    '''returns List<ResolvedMember>\n\n
    getMethodsWithoutIterator(final boolean includeITDs, final boolean allowMissing, final boolean genericsAware)\n
    '''
def getHierarchyWithoutIterator():
    '''returns List<ResolvedType>\n\n
    getHierarchyWithoutIterator(final boolean includeITDs, final boolean allowMissing, final boolean genericsAware)\n
    '''
def getResolvedTypeParameters():
    '''returns ResolvedType[]\n\n
    getResolvedTypeParameters()\n
    '''
def lookupField():
    '''returns ResolvedMember\n\n
    lookupField(final Member field)\n
    '''
def lookupMethod():
    '''returns ResolvedMember\n\n
    lookupMethod(final Member m)\n
    '''
def lookupMethodInITDs():
    '''returns ResolvedMember\n\n
    lookupMethodInITDs(final Member member)\n
    '''
def lookupResolvedMember():
    '''returns ResolvedMember\n\n
    lookupResolvedMember(final ResolvedMember aMember, final boolean allowMissing, final boolean eraseGenerics)\n
    '''
def getPointcuts():
    '''returns Iterator<ResolvedMember>\n\n
    getPointcuts()\n
    '''
def findPointcut():
    '''returns ResolvedPointcutDefinition\n\n
    findPointcut(final String name)\n
    '''
def collectCrosscuttingMembers():
    '''returns CrosscuttingMembers\n\n
    collectCrosscuttingMembers(final boolean shouldConcretizeIfNeeded)\n
    '''
def addParent():
    '''returns None\n\n
    addParent(final ResolvedType newParent)\n
    '''
def getPerClause():
    '''returns PerClause\n\n
    getPerClause()\n
    '''
def getDeclares():
    '''returns Collection<Declare>\n\n
    getDeclares()\n
    '''
def getTypeMungers():
    '''returns Collection<ConcreteTypeMunger>\n\n
    getTypeMungers()\n
    '''
def getPrivilegedAccesses():
    '''returns Collection<ResolvedMember>\n\n
    getPrivilegedAccesses()\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass()\n
    '''
def isAspect():
    '''returns boolean\n\n
    isAspect()\n
    '''
def isAnnotationStyleAspect():
    '''returns boolean\n\n
    isAnnotationStyleAspect()\n
    '''
def isEnum():
    '''returns boolean\n\n
    isEnum()\n
    '''
def isAnnotation():
    '''returns boolean\n\n
    isAnnotation()\n
    '''
def isAnonymous():
    '''returns boolean\n\n
    isAnonymous()\n
    '''
def isNested():
    '''returns boolean\n\n
    isNested()\n
    '''
def getOuterClass():
    '''returns ResolvedType\n\n
    getOuterClass()\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final AnnotationAJ annotationX)\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def canAnnotationTargetType():
    '''returns boolean\n\n
    canAnnotationTargetType()\n
    '''
def getAnnotationTargetKinds():
    '''returns AnnotationTargetKind[]\n\n
    getAnnotationTargetKinds()\n
    '''
def isAnnotationWithRuntimeRetention():
    '''returns boolean\n\n
    isAnnotationWithRuntimeRetention()\n
    '''
def isSynthetic():
    '''returns boolean\n\n
    isSynthetic()\n
    '''
def getDeclaredAdvice():
    '''returns List<ShadowMunger>\n\n
    getDeclaredAdvice()\n
    '''
def getDeclaredShadowMungers():
    '''returns List<ShadowMunger>\n\n
    getDeclaredShadowMungers()\n
    '''
def getDeclaredJavaFields():
    '''returns ResolvedMember[]\n\n
    getDeclaredJavaFields()\n
    '''
def getDeclaredJavaMethods():
    '''returns ResolvedMember[]\n\n
    getDeclaredJavaMethods()\n
    '''
def lookupMemberNoSupers():
    '''returns ResolvedMember\n\n
    lookupMemberNoSupers(final Member member)\n
    '''
def lookupMemberWithSupersAndITDs():
    '''returns ResolvedMember\n\n
    lookupMemberWithSupersAndITDs(final Member member)\n
    '''
def lookupDirectlyDeclaredMemberNoSupers():
    '''returns ResolvedMember\n\n
    lookupDirectlyDeclaredMemberNoSupers(final Member member)\n
    '''
def lookupMemberIncludingITDsOnInterfaces():
    '''returns ResolvedMember\n\n
    lookupMemberIncludingITDsOnInterfaces(final Member member)\n
    '''
def getInterTypeMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getInterTypeMungers()\n
    '''
def getInterTypeParentMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getInterTypeParentMungers()\n
    '''
def getInterTypeMungersIncludingSupers():
    '''returns List<ConcreteTypeMunger>\n\n
    getInterTypeMungersIncludingSupers()\n
    '''
def getInterTypeParentMungersIncludingSupers():
    '''returns List<ConcreteTypeMunger>\n\n
    getInterTypeParentMungersIncludingSupers()\n
    '''
def checkInterTypeMungers():
    '''returns None\n\n
    checkInterTypeMungers()\n
    '''
def getDeclaringType():
    '''returns ResolvedType\n\n
    getDeclaringType()\n
    '''
def discoverActualOccurrenceOfTypeInHierarchy():
    '''returns ResolvedType\n\n
    discoverActualOccurrenceOfTypeInHierarchy(final ResolvedType lookingFor)\n
    '''
def fillInAnyTypeParameters():
    '''returns ConcreteTypeMunger\n\n
    fillInAnyTypeParameters(ConcreteTypeMunger munger)\n
    '''
def addInterTypeMunger():
    '''returns None\n\n
    addInterTypeMunger(ConcreteTypeMunger munger, final boolean isDuringCompilation)\n
    '''
def checkLegalOverride():
    '''returns boolean\n\n
    checkLegalOverride(final ResolvedMember parent, final ResolvedMember child, final int transformerPosition, final ResolvedType aspectType)\n
    '''
def lookupSyntheticMember():
    '''returns ResolvedMember\n\n
    lookupSyntheticMember(final Member member)\n
    '''
def clearInterTypeMungers():
    '''returns None\n\n
    clearInterTypeMungers()\n
    '''
def isTopmostImplementor():
    '''returns boolean\n\n
    isTopmostImplementor(final ResolvedType interfaceType)\n
    '''
def getTopmostImplementor():
    '''returns ResolvedType\n\n
    getTopmostImplementor(final ResolvedType interfaceType)\n
    '''
def getExposedPointcuts():
    '''returns List<ResolvedMember>\n\n
    getExposedPointcuts()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def isExposedToWeaver():
    '''returns boolean\n\n
    isExposedToWeaver()\n
    '''
def getWeaverState():
    '''returns WeaverStateInfo\n\n
    getWeaverState()\n
    '''
def getGenericType():
    '''returns ReferenceType\n\n
    getGenericType()\n
    '''
def getRawType():
    '''returns ResolvedType\n\n
    getRawType()\n
    '''
def parameterizedWith():
    '''returns ResolvedType\n\n
    parameterizedWith(final UnresolvedType[] typeParameters)\n
    '''
def parameterize():
    '''returns UnresolvedType\n\n
    parameterize(final Map<String, UnresolvedType> typeBindings)\n
    '''
def isException():
    '''returns boolean\n\n
    isException()\n
    '''
def isCheckedException():
    '''returns boolean\n\n
    isCheckedException()\n
    '''
def needsNoConversionFrom():
    '''returns boolean\n\n
    needsNoConversionFrom(final ResolvedType o)\n
    needsNoConversionFrom(final ResolvedType other)\n
    '''
def getSignatureForAttribute():
    '''returns String\n\n
    getSignatureForAttribute()\n
    '''
def isParameterizedWithTypeVariable():
    '''returns boolean\n\n
    isParameterizedWithTypeVariable()\n
    '''
def setBinaryPath():
    '''returns None\n\n
    setBinaryPath(final String binaryPath)\n
    '''
def getBinaryPath():
    '''returns String\n\n
    getBinaryPath()\n
    '''
def ensureConsistent():
    '''returns None\n\n
    ensureConsistent()\n
    '''
def isInheritedAnnotation():
    '''returns boolean\n\n
    isInheritedAnnotation()\n
    '''
def tagAsTypeHierarchyComplete():
    '''returns None\n\n
    tagAsTypeHierarchyComplete()\n
    '''
def isTypeHierarchyComplete():
    '''returns boolean\n\n
    isTypeHierarchyComplete()\n
    '''
def getCompilerVersion():
    '''returns int\n\n
    getCompilerVersion()\n
    '''
def isPrimitiveArray():
    '''returns boolean\n\n
    isPrimitiveArray()\n
    '''
def isGroovyObject():
    '''returns boolean\n\n
    isGroovyObject()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def resolve():
    '''returns ResolvedType\n\n
    resolve(final World world)\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    getSourceContext()\n
    '''
def ():
    '''returns SuperClassWalker\n\n
    (final ResolvedType type, final SuperInterfaceWalker iwalker, final boolean genericsAware)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns ResolvedType\n\n
    next()\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    remove()\n
    '''
def push():
    '''returns None\n\n
    push(final ResolvedType ret)\n
    '''
