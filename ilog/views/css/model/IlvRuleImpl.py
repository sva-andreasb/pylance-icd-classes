def ():
    '''returns IlvRuleImpl\n\n
    (final Rule b)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final IlvNode ilvNode)\n
    '''
def getSelectors():
    '''returns IlvSelector[]\n\n
    getSelectors()\n
    '''
def getSelector():
    '''returns IlvSelector\n\n
    getSelector()\n
    '''
def setSelectors():
    '''returns None\n\n
    setSelectors(final IlvSelector[] c)\n
    '''
def setSelector():
    '''returns None\n\n
    setSelector(final IlvSelector d)\n
    '''
def getDeclarations():
    '''returns IlvCSSDeclaration[]\n\n
    getDeclarations()\n
    '''
def setDeclarations():
    '''returns None\n\n
    setDeclarations(final IlvCSSDeclaration[] array)\n
    '''
def getDeclarationValue():
    '''returns String\n\n
    getDeclarationValue(final String s)\n
    getDeclarationValue(final String s, final boolean b)\n
    '''
def getMetaDeclarationValue():
    '''returns String\n\n
    getMetaDeclarationValue(final String s)\n
    '''
def setMetaDeclaration():
    '''returns String\n\n
    setMetaDeclaration(final String s, final String value)\n
    setMetaDeclaration(final Declaration declaration)\n
    '''
def getDeclaration():
    '''returns IlvCSSDeclaration\n\n
    getDeclaration(final String s)\n
    '''
def getMetaDeclaration():
    '''returns IlvCSSDeclaration\n\n
    getMetaDeclaration(final String anObject)\n
    '''
def getMetadata():
    '''returns IlvCSSDeclaration[]\n\n
    getMetadata()\n
    '''
def setMetadata():
    '''returns None\n\n
    setMetadata(final IlvCSSDeclaration[] array)\n
    '''
def isConfigurationRule():
    '''returns boolean\n\n
    isConfigurationRule()\n
    '''
def setConfigurationRule():
    '''returns None\n\n
    setConfigurationRule(final boolean e)\n
    '''
def updateRule():
    '''returns None\n\n
    updateRule()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getSuffixSelectorString():
    '''returns String\n\n
    getSuffixSelectorString()\n
    '''
def getSelectorString():
    '''returns String\n\n
    getSelectorString()\n
    '''
def getSelectorsString():
    '''returns String\n\n
    getSelectorsString()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setEnabled():
    '''returns None\n\n
    setEnabled(final boolean b)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def setInheritedStatus():
    '''returns None\n\n
    setInheritedStatus(final int k)\n
    '''
def getInheritedStatus():
    '''returns int\n\n
    getInheritedStatus()\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
    '''
def setUsed():
    '''returns None\n\n
    setUsed(final boolean l)\n
    '''
def getRule():
    '''returns Rule\n\n
    getRule()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String j)\n
    '''
def printCSS():
    '''returns None\n\n
    printCSS(final PrintWriter printWriter)\n
    printCSS(final PrintWriter printWriter, final IlvCSSDocument ilvCSSDocument)\n
    '''
def compare():
    '''returns int\n\n
    compare(final IlvRule ilvRule)\n
    compare(final IlvRule ilvRule, final IlvRule ilvRule2)\n
    '''
def resetAttributes():
    '''returns None\n\n
    resetAttributes()\n
    '''
def resetPseudoClasses():
    '''returns None\n\n
    resetPseudoClasses()\n
    '''
def setPseudoClasses():
    '''returns None\n\n
    setPseudoClasses(final String[] pseudos)\n
    '''
def getPseudoClasses():
    '''returns String[]\n\n
    getPseudoClasses()\n
    '''
def getDisabledGroup():
    '''returns long\n\n
    getDisabledGroup()\n
    '''
def setDisabledGroup():
    '''returns None\n\n
    setDisabledGroup(final long disabledGroup)\n
    '''
def isDisabled():
    '''returns boolean\n\n
    isDisabled()\n
    '''
def getDOMImplementation():
    '''returns IlvCSSDOMImplementation\n\n
    getDOMImplementation()\n
    '''
def copy():
    '''returns IlvRule\n\n
    copy()\n
    '''
def createSameRule():
    '''returns IlvRule\n\n
    createSameRule()\n
    '''
def copyAttributes():
    '''returns None\n\n
    copyAttributes(final IlvRule ilvRule)\n
    '''
def setModified():
    '''returns None\n\n
    setModified(final boolean m)\n
    setModified(final String key)\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    isModified(final String key)\n
    '''
def setDeclaration():
    '''returns String\n\n
    setDeclaration(final String s, final String value)\n
    setDeclaration(final IlvCSSDeclaration ilvCSSDeclaration)\n
    '''
def isDeletable():
    '''returns boolean\n\n
    isDeletable()\n
    '''
def setDeletable():
    '''returns None\n\n
    setDeletable(final boolean n)\n
    '''
def removeDeclaration():
    '''returns None\n\n
    removeDeclaration(final String key)\n
    '''
def removeMetaDeclaration():
    '''returns None\n\n
    removeMetaDeclaration(final String anObject)\n
    '''
def setUnModified():
    '''returns None\n\n
    setUnModified(final String key)\n
    '''
def getOldValue():
    '''returns String\n\n
    getOldValue(final String key)\n
    '''
def resetModified():
    '''returns String\n\n
    resetModified(final String s)\n
    '''
def setDeclarationValue():
    '''returns String\n\n
    setDeclarationValue(final String s, final String value)\n
    '''
def updateWeights():
    '''returns None\n\n
    updateWeights()\n
    '''
def isIdentical():
    '''returns boolean\n\n
    isIdentical(final Object o)\n
    '''
def getPropertyNames():
    '''returns String[]\n\n
    getPropertyNames()\n
    '''
def isCompositeRule():
    '''returns boolean\n\n
    isCompositeRule()\n
    isCompositeRule(final IlvRuleModel ilvRuleModel)\n
    '''
def getChildPositionFromId():
    '''returns int\n\n
    getChildPositionFromId(final String anObject)\n
    '''
def getRulesForCompositeUNUSED():
    '''returns None\n\n
    getRulesForCompositeUNUSED(final IlvRuleModel ilvRuleModel, IlvRule[] allRules, final List<IlvRule> list)\n
    '''
def getAttachmentIdFromIndexUNUSED():
    '''returns String\n\n
    getAttachmentIdFromIndexUNUSED(final int i)\n
    '''
def getFirstAvailableIndex():
    '''returns int\n\n
    getFirstAvailableIndex()\n
    '''
def getCSSSelectors():
    '''returns IlvCSSSelector[]\n\n
    getCSSSelectors()\n
    '''
def getCSSDeclarations():
    '''returns IlvCSSDeclaration[]\n\n
    getCSSDeclarations()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    '''
def getDocumentPath():
    '''returns URL\n\n
    getDocumentPath()\n
    '''
