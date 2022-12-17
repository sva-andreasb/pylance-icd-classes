def ():
    '''returns LanguageMatcherData\n\n
    (final LocalePriorityList languagePriorityList)\n
    (final String languagePriorityListString)\n
    (final LocalePriorityList languagePriorityList, final LanguageMatcherData matcherData)\n
    (final String toMatch)\n
    (final Level level)\n
    ()\n
    '''
def match():
    '''returns double\n\n
    match(final ULocale desired, final ULocale desiredMax, final ULocale supported, final ULocale supportedMax)\n
    match(final ULocale a, final ULocale aMax, final ULocale b, final ULocale bMax)\n
    '''
def canonicalize():
    '''returns ULocale\n\n
    canonicalize(final ULocale ulocale)\n
    '''
def getBestMatch():
    '''returns ULocale\n\n
    getBestMatch(final LocalePriorityList languageList)\n
    getBestMatch(final String languageList)\n
    getBestMatch(final ULocale ulocale)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def getScript():
    '''returns String\n\n
    getScript()\n
    '''
def getRegion():
    '''returns String\n\n
    getRegion()\n
    '''
def cloneAsThawed():
    '''returns LanguageMatcherData\n\n
    cloneAsThawed()\n
    cloneAsThawed()\n
    '''
def freeze():
    '''returns LanguageMatcherData\n\n
    freeze()\n
    freeze()\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    isFrozen()\n
    '''
def addDistance():
    '''returns LanguageMatcherData\n\n
    addDistance(final String desired, final String supported, final int percent, final String comment)\n
    addDistance(final String desired, final String supported, final int percent, final boolean oneway)\n
    '''
