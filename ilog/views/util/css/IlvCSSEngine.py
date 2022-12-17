PSEUDOCLASS_PREFIX = "String  \"__PSEUDO__\""
ANY_PROPERTIES = "String  \"__ANY_PROPERTIES\""
ANY_PSEUDOCLASSES = "String  \"__ANY_PSEUDOCLASSES\""
ANY = "String  \"__ANY\""
MATCHING_OK = "int  1"
MATCHING_FAILED = "int  0"
MATCHING_DEFERRED = "int  -1"
def rulesChanged():
    '''returns None\n\n
    rulesChanged(final RuleSetEvent ruleSetEvent)\n
    '''
def getRulesState():
    '''returns Object\n\n
    getRulesState()\n
    '''
def getAttributeHandler():
    '''returns AttributeHandler\n\n
    getAttributeHandler()\n
    '''
def setAttributeHandler():
    '''returns None\n\n
    setAttributeHandler(final AttributeHandler m)\n
    '''
def getCSSClassHandler():
    '''returns CSSClassHandler\n\n
    getCSSClassHandler()\n
    '''
def setCSSClassHandler():
    '''returns None\n\n
    setCSSClassHandler(final CSSClassHandler n)\n
    '''
def setApplicableRuleListFactory():
    '''returns None\n\n
    setApplicableRuleListFactory(ApplicableRuleListFactory o)\n
    '''
def ():
    '''returns ApplicableRule\n\n
    (final IlvCSSDOMImplementation ilvCSSDOMImplementation, final DeclarationValueHandler declarationValueHandler, final ApplicableRuleListFactory applicableRuleListFactory)\n
    (final Rule a, final int b)\n
    '''
def applyCSStoModel():
    '''returns MatchingResult\n\n
    applyCSStoModel(final IlvCSSModel ilvCSSModel, final Object o)\n
    applyCSStoModel(final IlvCSSModel ilvCSSModel, final Object o, final IlvCSSModel ilvCSSModel2)\n
    '''
def getPossiblyApplicableEnabledRules():
    '''returns Collection<Rule>\n\n
    getPossiblyApplicableEnabledRules(final String s, final String s2)\n
    getPossiblyApplicableEnabledRules(final String key, final String key2, final String s, final IlvCSSModel ilvCSSModel)\n
    '''
def getUsedPseudoClasses():
    '''returns Set<String>\n\n
    getUsedPseudoClasses()\n
    '''
def usesPseudoClass():
    '''returns boolean\n\n
    usesPseudoClass(final String key)\n
    '''
def usesModelAttributesInSelector():
    '''returns boolean\n\n
    usesModelAttributesInSelector(final Rule rule, final Set<String> set)\n
    '''
def hasHierarchicalSelectors():
    '''returns boolean\n\n
    hasHierarchicalSelectors()\n
    '''
def getCurrentRule():
    '''returns Rule\n\n
    getCurrentRule()\n
    '''
def getModel():
    '''returns IlvCSSModel\n\n
    getModel()\n
    '''
def getRoot():
    '''returns Object\n\n
    getRoot()\n
    '''
def getEngine():
    '''returns IlvCSSEngine\n\n
    getEngine()\n
    '''
def findDeclarations():
    '''returns IlvApplicableDeclarationCollection\n\n
    findDeclarations(final Object o, final String[] array)\n
    '''
def update():
    '''returns None\n\n
    update(final IlvCSSModel d, final Object o, final IlvCSSModel ilvCSSModel)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def remove():
    '''returns None\n\n
    remove(final Object o)\n
    '''
def keySet():
    '''returns Set<Object>\n\n
    keySet()\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object o)\n
    '''
def getRules():
    '''returns Rule[]\n\n
    getRules(final Object o)\n
    '''
def getObjects():
    '''returns ArrayList<Object>\n\n
    getObjects(final Rule rule)\n
    '''
def print():
    '''returns None\n\n
    print(final Object o, final PrintStream printStream)\n
    print(final PrintStream printStream)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getPseudos():
    '''returns String[]\n\n
    getPseudos()\n
    '''
def getDeclarations():
    '''returns Declaration[]\n\n
    getDeclarations()\n
    '''
def compare():
    '''returns int\n\n
    compare(final ApplicableRule applicableRule, final ApplicableRule applicableRule2)\n
    '''
def createApplicableRuleList():
    '''returns IlvApplicableRuleList\n\n
    createApplicableRuleList(final ApplicableRule applicableRule)\n
    '''
def computeAttributeNameValue():
    '''returns Object\n\n
    computeAttributeNameValue(final IlvCSSModel ilvCSSModel, final Object o, final String s)\n
    '''
def evaluateAttributeSelector():
    '''returns int\n\n
    evaluateAttributeSelector(final IlvCSSModel ilvCSSModel, final Object o, final AttributeSelector attributeSelector)\n
    '''
def usesModelAttributes():
    '''returns boolean\n\n
    usesModelAttributes(final Set<String> set, final AttributeSelector attributeSelector)\n
    '''
def collectUsedAttributeNames():
    '''returns None\n\n
    collectUsedAttributeNames(final AttributeSelector attributeSelector, final Set<String> set, final Set<String> set2)\n
    '''
