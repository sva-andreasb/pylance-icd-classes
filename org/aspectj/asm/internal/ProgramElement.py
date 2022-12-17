def getModel():
    '''returns AsmManager\n\n
    getModel()\n
    '''
def ():
    '''returns ProgramElement\n\n
    ()\n
    (final AsmManager asm, final String name, final Kind kind, final List<IProgramElement> children)\n
    (final AsmManager asm, final String name, final Kind kind, final ISourceLocation sourceLocation, final int modifiers, final String comment, final List<IProgramElement> children)\n
    '''
def getRawModifiers():
    '''returns int\n\n
    getRawModifiers()\n
    '''
def getModifiers():
    '''returns List<Modifiers>\n\n
    getModifiers()\n
    '''
def getAccessibility():
    '''returns Accessibility\n\n
    getAccessibility()\n
    '''
def setDeclaringType():
    '''returns None\n\n
    setDeclaringType(final String t)\n
    '''
def getDeclaringType():
    '''returns String\n\n
    getDeclaringType()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def getKind():
    '''returns Kind\n\n
    getKind()\n
    '''
def isCode():
    '''returns boolean\n\n
    isCode()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def setSourceLocation():
    '''returns None\n\n
    setSourceLocation(final ISourceLocation sourceLocation)\n
    '''
def getMessage():
    '''returns IMessage\n\n
    getMessage()\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final IMessage message)\n
    '''
def getParent():
    '''returns IProgramElement\n\n
    getParent()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final IProgramElement parent)\n
    '''
def isMemberKind():
    '''returns boolean\n\n
    isMemberKind()\n
    '''
def setRunnable():
    '''returns None\n\n
    setRunnable(final boolean value)\n
    '''
def isRunnable():
    '''returns boolean\n\n
    isRunnable()\n
    '''
def isImplementor():
    '''returns boolean\n\n
    isImplementor()\n
    '''
def setImplementor():
    '''returns None\n\n
    setImplementor(final boolean value)\n
    '''
def isOverrider():
    '''returns boolean\n\n
    isOverrider()\n
    '''
def setOverrider():
    '''returns None\n\n
    setOverrider(final boolean value)\n
    '''
def getFormalComment():
    '''returns String\n\n
    getFormalComment()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getBytecodeName():
    '''returns String\n\n
    getBytecodeName()\n
    '''
def setBytecodeName():
    '''returns None\n\n
    setBytecodeName(final String s)\n
    '''
def setBytecodeSignature():
    '''returns None\n\n
    setBytecodeSignature(final String s)\n
    '''
def getBytecodeSignature():
    '''returns String\n\n
    getBytecodeSignature()\n
    '''
def getSourceSignature():
    '''returns String\n\n
    getSourceSignature()\n
    '''
def setSourceSignature():
    '''returns None\n\n
    setSourceSignature(final String string)\n
    '''
def setKind():
    '''returns None\n\n
    setKind(final Kind kind)\n
    '''
def setCorrespondingType():
    '''returns None\n\n
    setCorrespondingType(final String s)\n
    '''
def setParentTypes():
    '''returns None\n\n
    setParentTypes(final List<String> ps)\n
    '''
def getParentTypes():
    '''returns List<String>\n\n
    getParentTypes()\n
    '''
def setAnnotationType():
    '''returns None\n\n
    setAnnotationType(final String fullyQualifiedAnnotationType)\n
    '''
def setAnnotationRemover():
    '''returns None\n\n
    setAnnotationRemover(final boolean isRemover)\n
    '''
def getAnnotationType():
    '''returns String\n\n
    getAnnotationType()\n
    '''
def isAnnotationRemover():
    '''returns boolean\n\n
    isAnnotationRemover()\n
    '''
def getRemovedAnnotationTypes():
    '''returns String[]\n\n
    getRemovedAnnotationTypes()\n
    '''
def getCorrespondingType():
    '''returns String\n\n
    getCorrespondingType()\n
    getCorrespondingType(final boolean getFullyQualifiedType)\n
    '''
def getCorrespondingTypeSignature():
    '''returns String\n\n
    getCorrespondingTypeSignature()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getChildren():
    '''returns List<IProgramElement>\n\n
    getChildren()\n
    '''
def setChildren():
    '''returns None\n\n
    setChildren(final List<IProgramElement> children)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final IProgramElement child)\n
    addChild(final int position, final IProgramElement child)\n
    '''
def removeChild():
    '''returns boolean\n\n
    removeChild(final IProgramElement child)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String string)\n
    '''
def walk():
    '''returns IProgramElement\n\n
    walk(final HierarchyWalker walker)\n
    '''
def toLongString():
    '''returns String\n\n
    toLongString()\n
    '''
def preProcess():
    '''returns None\n\n
    preProcess(final IProgramElement node)\n
    '''
def postProcess():
    '''returns None\n\n
    postProcess(final IProgramElement node)\n
    '''
def setModifiers():
    '''returns None\n\n
    setModifiers(final int i)\n
    '''
def addModifiers():
    '''returns None\n\n
    addModifiers(final Modifiers newModifier)\n
    '''
def toSignatureString():
    '''returns String\n\n
    toSignatureString()\n
    toSignatureString(final boolean getFullyQualifiedArgTypes)\n
    '''
def toLinkLabelString():
    '''returns String\n\n
    toLinkLabelString()\n
    toLinkLabelString(final boolean getFullyQualifiedArgTypes)\n
    '''
def toLabelString():
    '''returns String\n\n
    toLabelString()\n
    toLabelString(final boolean getFullyQualifiedArgTypes)\n
    '''
def getHandleIdentifier():
    '''returns String\n\n
    getHandleIdentifier()\n
    getHandleIdentifier(final boolean create)\n
    '''
def setHandleIdentifier():
    '''returns None\n\n
    setHandleIdentifier(final String handle)\n
    '''
def getParameterNames():
    '''returns List<String>\n\n
    getParameterNames()\n
    '''
def setParameterNames():
    '''returns None\n\n
    setParameterNames(final List<String> list)\n
    '''
def getParameterTypes():
    '''returns List<char[]>\n\n
    getParameterTypes()\n
    '''
def getParameterSignatures():
    '''returns List<char[]>\n\n
    getParameterSignatures()\n
    '''
def getParameterSignaturesSourceRefs():
    '''returns List<String>\n\n
    getParameterSignaturesSourceRefs()\n
    '''
def setParameterSignatures():
    '''returns None\n\n
    setParameterSignatures(final List<char[]> list, final List<String> sourceRefs)\n
    '''
def getDetails():
    '''returns String\n\n
    getDetails()\n
    '''
def setDetails():
    '''returns None\n\n
    setDetails(final String string)\n
    '''
def setFormalComment():
    '''returns None\n\n
    setFormalComment(final String txt)\n
    '''
def setExtraInfo():
    '''returns None\n\n
    setExtraInfo(final ExtraInformation info)\n
    '''
def getExtraInfo():
    '''returns ExtraInformation\n\n
    getExtraInfo()\n
    '''
def isAnnotationStyleDeclaration():
    '''returns boolean\n\n
    isAnnotationStyleDeclaration()\n
    '''
def setAnnotationStyleDeclaration():
    '''returns None\n\n
    setAnnotationStyleDeclaration(final boolean b)\n
    '''
def setDeclareParentsMap():
    '''returns None\n\n
    setDeclareParentsMap(final Map<String, List<String>> newmap)\n
    '''
def addFullyQualifiedName():
    '''returns None\n\n
    addFullyQualifiedName(final String fqname)\n
    '''
def getFullyQualifiedName():
    '''returns String\n\n
    getFullyQualifiedName()\n
    '''
