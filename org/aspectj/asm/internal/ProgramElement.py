def getModel():
'''public AsmManager getModel()
'''
pass
def ProgramElement():
'''public ProgramElement()
public ProgramElement(final AsmManager asm, final String name, final Kind kind, final List<IProgramElement> children)
public ProgramElement(final AsmManager asm, final String name, final Kind kind, final ISourceLocation sourceLocation, final int modifiers, final String comment, final List<IProgramElement> children)
'''
pass
def getRawModifiers():
'''public int getRawModifiers()
'''
pass
def getModifiers():
'''public List<Modifiers> getModifiers()
'''
pass
def getAccessibility():
'''public Accessibility getAccessibility()
'''
pass
def setDeclaringType():
'''public void setDeclaringType(final String t)
'''
pass
def getDeclaringType():
'''public String getDeclaringType()
'''
pass
def getPackageName():
'''public String getPackageName()
'''
pass
def getKind():
'''public Kind getKind()
'''
pass
def isCode():
'''public boolean isCode()
'''
pass
def getSourceLocation():
'''public ISourceLocation getSourceLocation()
'''
pass
def setSourceLocation():
'''public void setSourceLocation(final ISourceLocation sourceLocation)
'''
pass
def getMessage():
'''public IMessage getMessage()
'''
pass
def setMessage():
'''public void setMessage(final IMessage message)
'''
pass
def getParent():
'''public IProgramElement getParent()
'''
pass
def setParent():
'''public void setParent(final IProgramElement parent)
'''
pass
def isMemberKind():
'''public boolean isMemberKind()
'''
pass
def setRunnable():
'''public void setRunnable(final boolean value)
'''
pass
def isRunnable():
'''public boolean isRunnable()
'''
pass
def isImplementor():
'''public boolean isImplementor()
'''
pass
def setImplementor():
'''public void setImplementor(final boolean value)
'''
pass
def isOverrider():
'''public boolean isOverrider()
'''
pass
def setOverrider():
'''public void setOverrider(final boolean value)
'''
pass
def getFormalComment():
'''public String getFormalComment()
'''
pass
def toString():
'''public String toString()
'''
pass
def genAccessibility():
'''public static Accessibility genAccessibility(final int modifiers)
'''
pass
def getBytecodeName():
'''public String getBytecodeName()
'''
pass
def setBytecodeName():
'''public void setBytecodeName(final String s)
'''
pass
def setBytecodeSignature():
'''public void setBytecodeSignature(final String s)
'''
pass
def getBytecodeSignature():
'''public String getBytecodeSignature()
'''
pass
def getSourceSignature():
'''public String getSourceSignature()
'''
pass
def setSourceSignature():
'''public void setSourceSignature(final String string)
'''
pass
def setKind():
'''public void setKind(final Kind kind)
'''
pass
def setCorrespondingType():
'''public void setCorrespondingType(final String s)
'''
pass
def setParentTypes():
'''public void setParentTypes(final List<String> ps)
'''
pass
def getParentTypes():
'''public List<String> getParentTypes()
'''
pass
def setAnnotationType():
'''public void setAnnotationType(final String fullyQualifiedAnnotationType)
'''
pass
def setAnnotationRemover():
'''public void setAnnotationRemover(final boolean isRemover)
'''
pass
def getAnnotationType():
'''public String getAnnotationType()
'''
pass
def isAnnotationRemover():
'''public boolean isAnnotationRemover()
'''
pass
def getRemovedAnnotationTypes():
'''public String[] getRemovedAnnotationTypes()
'''
pass
def getCorrespondingType():
'''public String getCorrespondingType()
public String getCorrespondingType(final boolean getFullyQualifiedType)
'''
pass
def getCorrespondingTypeSignature():
'''public String getCorrespondingTypeSignature()
'''
pass
def nameToSignature():
'''public static String nameToSignature(final String name)
'''
pass
def trim():
'''public static String trim(final String fqname)
'''
pass
def getName():
'''public String getName()
'''
pass
def getChildren():
'''public List<IProgramElement> getChildren()
'''
pass
def setChildren():
'''public void setChildren(final List<IProgramElement> children)
'''
pass
def addChild():
'''public void addChild(final IProgramElement child)
public void addChild(final int position, final IProgramElement child)
'''
pass
def removeChild():
'''public boolean removeChild(final IProgramElement child)
'''
pass
def setName():
'''public void setName(final String string)
'''
pass
def walk():
'''public IProgramElement walk(final HierarchyWalker walker)
'''
pass
def toLongString():
'''public String toLongString()
'''
pass
def preProcess():
'''public void preProcess(final IProgramElement node)
'''
pass
def postProcess():
'''public void postProcess(final IProgramElement node)
'''
pass
def setModifiers():
'''public void setModifiers(final int i)
'''
pass
def addModifiers():
'''public void addModifiers(final Modifiers newModifier)
'''
pass
def toSignatureString():
'''public String toSignatureString()
public String toSignatureString(final boolean getFullyQualifiedArgTypes)
'''
pass
def toLinkLabelString():
'''public String toLinkLabelString()
public String toLinkLabelString(final boolean getFullyQualifiedArgTypes)
'''
pass
def toLabelString():
'''public String toLabelString()
public String toLabelString(final boolean getFullyQualifiedArgTypes)
'''
pass
def getHandleIdentifier():
'''public String getHandleIdentifier()
public String getHandleIdentifier(final boolean create)
'''
pass
def setHandleIdentifier():
'''public void setHandleIdentifier(final String handle)
'''
pass
def getParameterNames():
'''public List<String> getParameterNames()
'''
pass
def setParameterNames():
'''public void setParameterNames(final List<String> list)
'''
pass
def getParameterTypes():
'''public List<char[]> getParameterTypes()
'''
pass
def getParameterSignatures():
'''public List<char[]> getParameterSignatures()
'''
pass
def getParameterSignaturesSourceRefs():
'''public List<String> getParameterSignaturesSourceRefs()
'''
pass
def setParameterSignatures():
'''public void setParameterSignatures(final List<char[]> list, final List<String> sourceRefs)
'''
pass
def getDetails():
'''public String getDetails()
'''
pass
def setDetails():
'''public void setDetails(final String string)
'''
pass
def setFormalComment():
'''public void setFormalComment(final String txt)
'''
pass
def setExtraInfo():
'''public void setExtraInfo(final ExtraInformation info)
'''
pass
def getExtraInfo():
'''public ExtraInformation getExtraInfo()
'''
pass
def isAnnotationStyleDeclaration():
'''public boolean isAnnotationStyleDeclaration()
'''
pass
def setAnnotationStyleDeclaration():
'''public void setAnnotationStyleDeclaration(final boolean b)
'''
pass
def getDeclareParentsMap():
'''public Map<String, List<String>> getDeclareParentsMap()
'''
pass
def setDeclareParentsMap():
'''public void setDeclareParentsMap(final Map<String, List<String>> newmap)
'''
pass
def addFullyQualifiedName():
'''public void addFullyQualifiedName(final String fqname)
'''
pass
def getFullyQualifiedName():
'''public String getFullyQualifiedName()
'''
pass
