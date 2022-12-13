def getModel():
    '''public AsmManager getModel()
    '''
def ProgramElement():
    '''public ProgramElement()
    public ProgramElement(final AsmManager asm, final String name, final Kind kind, final List<IProgramElement> children)
    public ProgramElement(final AsmManager asm, final String name, final Kind kind, final ISourceLocation sourceLocation, final int modifiers, final String comment, final List<IProgramElement> children)
    '''
def getRawModifiers():
    '''public int getRawModifiers()
    '''
def getModifiers():
    '''public List<Modifiers> getModifiers()
    '''
def getAccessibility():
    '''public Accessibility getAccessibility()
    '''
def setDeclaringType():
    '''public void setDeclaringType(final String t)
    '''
def getDeclaringType():
    '''public String getDeclaringType()
    '''
def getPackageName():
    '''public String getPackageName()
    '''
def getKind():
    '''public Kind getKind()
    '''
def isCode():
    '''public boolean isCode()
    '''
def getSourceLocation():
    '''public ISourceLocation getSourceLocation()
    '''
def setSourceLocation():
    '''public void setSourceLocation(final ISourceLocation sourceLocation)
    '''
def getMessage():
    '''public IMessage getMessage()
    '''
def setMessage():
    '''public void setMessage(final IMessage message)
    '''
def getParent():
    '''public IProgramElement getParent()
    '''
def setParent():
    '''public void setParent(final IProgramElement parent)
    '''
def isMemberKind():
    '''public boolean isMemberKind()
    '''
def setRunnable():
    '''public void setRunnable(final boolean value)
    '''
def isRunnable():
    '''public boolean isRunnable()
    '''
def isImplementor():
    '''public boolean isImplementor()
    '''
def setImplementor():
    '''public void setImplementor(final boolean value)
    '''
def isOverrider():
    '''public boolean isOverrider()
    '''
def setOverrider():
    '''public void setOverrider(final boolean value)
    '''
def getFormalComment():
    '''public String getFormalComment()
    '''
def toString():
    '''public String toString()
    '''
def genAccessibility():
    '''public static Accessibility genAccessibility(final int modifiers)
    '''
def getBytecodeName():
    '''public String getBytecodeName()
    '''
def setBytecodeName():
    '''public void setBytecodeName(final String s)
    '''
def setBytecodeSignature():
    '''public void setBytecodeSignature(final String s)
    '''
def getBytecodeSignature():
    '''public String getBytecodeSignature()
    '''
def getSourceSignature():
    '''public String getSourceSignature()
    '''
def setSourceSignature():
    '''public void setSourceSignature(final String string)
    '''
def setKind():
    '''public void setKind(final Kind kind)
    '''
def setCorrespondingType():
    '''public void setCorrespondingType(final String s)
    '''
def setParentTypes():
    '''public void setParentTypes(final List<String> ps)
    '''
def getParentTypes():
    '''public List<String> getParentTypes()
    '''
def setAnnotationType():
    '''public void setAnnotationType(final String fullyQualifiedAnnotationType)
    '''
def setAnnotationRemover():
    '''public void setAnnotationRemover(final boolean isRemover)
    '''
def getAnnotationType():
    '''public String getAnnotationType()
    '''
def isAnnotationRemover():
    '''public boolean isAnnotationRemover()
    '''
def getRemovedAnnotationTypes():
    '''public String[] getRemovedAnnotationTypes()
    '''
def getCorrespondingType():
    '''public String getCorrespondingType()
    public String getCorrespondingType(final boolean getFullyQualifiedType)
    '''
def getCorrespondingTypeSignature():
    '''public String getCorrespondingTypeSignature()
    '''
def nameToSignature():
    '''public static String nameToSignature(final String name)
    '''
def trim():
    '''public static String trim(final String fqname)
    '''
def getName():
    '''public String getName()
    '''
def getChildren():
    '''public List<IProgramElement> getChildren()
    '''
def setChildren():
    '''public void setChildren(final List<IProgramElement> children)
    '''
def addChild():
    '''public void addChild(final IProgramElement child)
    public void addChild(final int position, final IProgramElement child)
    '''
def removeChild():
    '''public boolean removeChild(final IProgramElement child)
    '''
def setName():
    '''public void setName(final String string)
    '''
def walk():
    '''public IProgramElement walk(final HierarchyWalker walker)
    '''
def toLongString():
    '''public String toLongString()
    '''
def preProcess():
    '''public void preProcess(final IProgramElement node)
    '''
def postProcess():
    '''public void postProcess(final IProgramElement node)
    '''
def setModifiers():
    '''public void setModifiers(final int i)
    '''
def addModifiers():
    '''public void addModifiers(final Modifiers newModifier)
    '''
def toSignatureString():
    '''public String toSignatureString()
    public String toSignatureString(final boolean getFullyQualifiedArgTypes)
    '''
def toLinkLabelString():
    '''public String toLinkLabelString()
    public String toLinkLabelString(final boolean getFullyQualifiedArgTypes)
    '''
def toLabelString():
    '''public String toLabelString()
    public String toLabelString(final boolean getFullyQualifiedArgTypes)
    '''
def getHandleIdentifier():
    '''public String getHandleIdentifier()
    public String getHandleIdentifier(final boolean create)
    '''
def setHandleIdentifier():
    '''public void setHandleIdentifier(final String handle)
    '''
def getParameterNames():
    '''public List<String> getParameterNames()
    '''
def setParameterNames():
    '''public void setParameterNames(final List<String> list)
    '''
def getParameterTypes():
    '''public List<char[]> getParameterTypes()
    '''
def getParameterSignatures():
    '''public List<char[]> getParameterSignatures()
    '''
def getParameterSignaturesSourceRefs():
    '''public List<String> getParameterSignaturesSourceRefs()
    '''
def setParameterSignatures():
    '''public void setParameterSignatures(final List<char[]> list, final List<String> sourceRefs)
    '''
def getDetails():
    '''public String getDetails()
    '''
def setDetails():
    '''public void setDetails(final String string)
    '''
def setFormalComment():
    '''public void setFormalComment(final String txt)
    '''
def setExtraInfo():
    '''public void setExtraInfo(final ExtraInformation info)
    '''
def getExtraInfo():
    '''public ExtraInformation getExtraInfo()
    '''
def isAnnotationStyleDeclaration():
    '''public boolean isAnnotationStyleDeclaration()
    '''
def setAnnotationStyleDeclaration():
    '''public void setAnnotationStyleDeclaration(final boolean b)
    '''
def getDeclareParentsMap():
    '''public Map<String, List<String>> getDeclareParentsMap()
    '''
def setDeclareParentsMap():
    '''public void setDeclareParentsMap(final Map<String, List<String>> newmap)
    '''
def addFullyQualifiedName():
    '''public void addFullyQualifiedName(final String fqname)
    '''
def getFullyQualifiedName():
    '''public String getFullyQualifiedName()
    '''
