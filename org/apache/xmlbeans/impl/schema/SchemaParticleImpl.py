def setImmutable():
    '''public void setImmutable()
    '''
def hasTransitionRules():
    '''public boolean hasTransitionRules()
    '''
def hasTransitionNotes():
    '''public boolean hasTransitionNotes()
    '''
def setTransitionRules():
    '''public void setTransitionRules(final QNameSet start, final boolean isSkippable)
    '''
def setTransitionNotes():
    '''public void setTransitionNotes(final QNameSet excludeNext, final boolean isDeterministic)
    '''
def canStartWithElement():
    '''public boolean canStartWithElement(final QName name)
    '''
def acceptedStartNames():
    '''public QNameSet acceptedStartNames()
    '''
def getExcludeNextSet():
    '''public QNameSet getExcludeNextSet()
    '''
def isSkippable():
    '''public boolean isSkippable()
    '''
def isDeterministic():
    '''public boolean isDeterministic()
    '''
def getParticleType():
    '''public int getParticleType()
    '''
def setParticleType():
    '''public void setParticleType(final int pType)
    '''
def isSingleton():
    '''public boolean isSingleton()
    '''
def getMinOccurs():
    '''public BigInteger getMinOccurs()
    '''
def setMinOccurs():
    '''public void setMinOccurs(final BigInteger min)
    '''
def getIntMinOccurs():
    '''public int getIntMinOccurs()
    '''
def getMaxOccurs():
    '''public BigInteger getMaxOccurs()
    '''
def getIntMaxOccurs():
    '''public int getIntMaxOccurs()
    '''
def setMaxOccurs():
    '''public void setMaxOccurs(final BigInteger max)
    '''
def getParticleChildren():
    '''public SchemaParticle[] getParticleChildren()
    '''
def setParticleChildren():
    '''public void setParticleChildren(final SchemaParticle[] children)
    '''
def getParticleChild():
    '''public SchemaParticle getParticleChild(final int i)
    '''
def countOfParticleChild():
    '''public int countOfParticleChild()
    '''
def setWildcardSet():
    '''public void setWildcardSet(final QNameSet set)
    '''
def getWildcardSet():
    '''public QNameSet getWildcardSet()
    '''
def setWildcardProcess():
    '''public void setWildcardProcess(final int process)
    '''
def getWildcardProcess():
    '''public int getWildcardProcess()
    '''
def getName():
    '''public QName getName()
    '''
def setNameAndTypeRef():
    '''public void setNameAndTypeRef(final QName formname, final SchemaType.Ref typeref)
    '''
def isTypeResolved():
    '''public boolean isTypeResolved()
    '''
def resolveTypeRef():
    '''public void resolveTypeRef(final SchemaType.Ref typeref)
    '''
def isAttribute():
    '''public boolean isAttribute()
    '''
def getType():
    '''public SchemaType getType()
    '''
def getDefaultText():
    '''public String getDefaultText()
    '''
def isDefault():
    '''public boolean isDefault()
    '''
def isFixed():
    '''public boolean isFixed()
    '''
def setDefault():
    '''public void setDefault(final String deftext, final boolean isFixed, final XmlObject parseObject)
    '''
def isNillable():
    '''public boolean isNillable()
    '''
def setNillable():
    '''public void setNillable(final boolean nillable)
    '''
def getDefaultValue():
    '''public XmlAnySimpleType getDefaultValue()
    '''
def setDefaultValue():
    '''public void setDefaultValue(final XmlValueRef defaultRef)
    '''
def getUserData():
    '''public Object getUserData()
    '''
def setUserData():
    '''public void setUserData(final Object data)
    '''
