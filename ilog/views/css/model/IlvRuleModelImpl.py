def ():
    '''returns IlvRuleModelImpl\n\n
    (final IlvRuleModelStrategy a)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def getWrappedRule():
    '''returns IlvRule\n\n
    getWrappedRule(final Rule rule)\n
    '''
def createRule():
    '''returns IlvRule\n\n
    createRule(final Rule rule)\n
    '''
def buildTree():
    '''returns None\n\n
    buildTree()\n
    '''
def getRootRules():
    '''returns IlvRule[]\n\n
    getRootRules(final boolean b)\n
    getRootRules(final boolean b, final boolean b2)\n
    '''
def getRootRule():
    '''returns IlvRule\n\n
    getRootRule()\n
    '''
def getConfig():
    '''returns IlvConfigNode\n\n
    getConfig()\n
    '''
def updateInheritanceIcons():
    '''returns None\n\n
    updateInheritanceIcons(final IlvRule ilvRule)\n
    '''
def resetOldIcons():
    '''returns None\n\n
    resetOldIcons(final IlvNode ilvNode)\n
    '''
def getParentRules():
    '''returns IlvRule[]\n\n
    getParentRules(final IlvRule ilvRule)\n
    getParentRules(final IlvRule ilvRule, final boolean b)\n
    '''
def getParentRule():
    '''returns IlvRule\n\n
    getParentRule(final IlvRule ilvRule)\n
    '''
def getRelatedRules():
    '''returns ArrayList<IlvRule>\n\n
    getRelatedRules(final IlvRule e)\n
    '''
def getMatchingObjects():
    '''returns Object[]\n\n
    getMatchingObjects(final IlvRule ilvRule)\n
    '''
def getAdditionalRules():
    '''returns IlvRule[]\n\n
    getAdditionalRules(final IlvRule ilvRule, final IlvRule[] array, HashSet<IlvRule> set, final boolean b)\n
    getAdditionalRules(final IlvRule[] array)\n
    '''
def getRuleWithDeclaration():
    '''returns IlvRule\n\n
    getRuleWithDeclaration(final IlvRule ilvRule, final String s)\n
    '''
def getSameRule():
    '''returns IlvRule\n\n
    getSameRule(final IlvRule ilvRule, final boolean b, final boolean b2)\n
    '''
def getRulesFromIdAsList():
    '''returns Collection<IlvRule>\n\n
    getRulesFromIdAsList(final RulesSubset rulesSubset, final String key)\n
    '''
def getRulesFromId():
    '''returns IlvRule[]\n\n
    getRulesFromId(final RulesSubset rulesSubset, final String s)\n
    '''
def getToplevelRule():
    '''returns IlvRule\n\n
    getToplevelRule(IlvRule ilvRule)\n
    '''
def getDeclarationValue():
    '''returns String\n\n
    getDeclarationValue(final IlvRule ilvRule, final String s)\n
    getDeclarationValue(final IlvRule ilvRule, final String s, final boolean b)\n
    '''
def setDeclarationValueAndUpdateUnusedSharpRules():
    '''returns None\n\n
    setDeclarationValueAndUpdateUnusedSharpRules(final IlvRule ilvRule, final String s, final String s2)\n
    '''
def removeDeclarationAndUpdateUnusedSharpRules():
    '''returns None\n\n
    removeDeclarationAndUpdateUnusedSharpRules(final IlvRule ilvRule, final String s)\n
    '''
def setDeclarationValue():
    '''returns None\n\n
    setDeclarationValue(final IlvRule ilvRule, final String modified, final String s)\n
    '''
def removeDeclaration():
    '''returns None\n\n
    removeDeclaration(final IlvRule ilvRule, final String s)\n
    '''
def removeMetaDeclaration():
    '''returns None\n\n
    removeMetaDeclaration(final IlvRule ilvRule, final String s)\n
    '''
def setSelector():
    '''returns None\n\n
    setSelector(final IlvRule obj, final IlvSelector[] selectors)\n
    setSelector(final IlvRule obj, final IlvSelector selector)\n
    '''
def getLayoutId():
    '''returns String\n\n
    getLayoutId(final IlvRule ilvRule)\n
    '''
def getTopCompositeRule():
    '''returns IlvRule\n\n
    getTopCompositeRule(final IlvRule ilvRule)\n
    '''
def getAttachmentIdFromIndex():
    '''returns String\n\n
    getAttachmentIdFromIndex(final int i, final IlvRule ilvRule)\n
    '''
def getDecoAvailableId():
    '''returns String\n\n
    getDecoAvailableId()\n
    '''
def getAttachmentAvailableId():
    '''returns String\n\n
    getAttachmentAvailableId()\n
    '''
def makeBeanFromRule():
    '''returns Object\n\n
    makeBeanFromRule(final IlvRule ilvRule)\n
    '''
def getMoreSpecificRules():
    '''returns Collection<IlvRule>\n\n
    getMoreSpecificRules(final IlvRule ilvRule, final boolean b)\n
    '''
def withoutOverridingRules():
    '''returns IlvRule[]\n\n
    withoutOverridingRules(final IlvRule ilvRule)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener listener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener listener)\n
    '''
def addStyleChangeListener():
    '''returns None\n\n
    addStyleChangeListener(final CSSChangeListener cssChangeListener)\n
    '''
def removeStyleChangeListener():
    '''returns None\n\n
    removeStyleChangeListener(final CSSChangeListener cssChangeListener)\n
    '''
def getMatchedRules():
    '''returns IlvRule[]\n\n
    getMatchedRules(final Object o)\n
    '''
def getSharpRules():
    '''returns HashSet<IlvRule>\n\n
    getSharpRules(final Collection<IlvRule> collection)\n
    getSharpRules(final IlvRule[] array)\n
    '''
def getSharpRuleUsageMap():
    '''returns SharpRuleUsageMap\n\n
    getSharpRuleUsageMap(final Collection<IlvRule> collection)\n
    getSharpRuleUsageMap(final IlvRule[] array)\n
    '''
def getSharpRuleUsageCount():
    '''returns int\n\n
    getSharpRuleUsageCount(final String s)\n
    '''
def removeSharpRule():
    '''returns None\n\n
    removeSharpRule(final String s)\n
    '''
def collectSharpRules():
    '''returns None\n\n
    collectSharpRules(final IlvRule ilvRule, final ArrayList<IlvRule> list)\n
    '''
def removeRulesUsingAttributeName():
    '''returns None\n\n
    removeRulesUsingAttributeName(final String s)\n
    '''
def getRulesUsingAttributeName():
    '''returns List<IlvRule>\n\n
    getRulesUsingAttributeName(final String s)\n
    '''
def getDeclarationsUsingAttributeName():
    '''returns List<IlvCSSDeclaration>\n\n
    getDeclarationsUsingAttributeName(final String s)\n
    '''
def removeDeclarationsUsingAttributeName():
    '''returns None\n\n
    removeDeclarationsUsingAttributeName(final String s)\n
    '''
def addRule():
    '''returns None\n\n
    addRule(final IlvRule ilvRule)\n
    '''
def removeRule():
    '''returns None\n\n
    removeRule(final IlvRule ilvRule)\n
    '''
def revalidateRules():
    '''returns None\n\n
    revalidateRules(final boolean b)\n
    '''
def setDebugMode():
    '''returns None\n\n
    setDebugMode(final boolean k)\n
    '''
def getRule():
    '''returns IlvRule\n\n
    getRule(final String str, final boolean b, final boolean b2)\n
    '''
def setAdjusting():
    '''returns None\n\n
    setAdjusting(final boolean b)\n
    '''
def isAdjusting():
    '''returns boolean\n\n
    isAdjusting()\n
    '''
def markUsed():
    '''returns None\n\n
    markUsed(final String s)\n
    '''
def markUnused():
    '''returns None\n\n
    markUnused(final String key)\n
    '''
def getUsageCount():
    '''returns int\n\n
    getUsageCount(final String key)\n
    '''
