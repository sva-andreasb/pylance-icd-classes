ICU_BUNDLE = "String  \"data/icudt44b\""
ICU_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b\""
ICU_COLLATION_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/coll\""
ICU_BRKITR_NAME = "String  \"/brkitr\""
ICU_BRKITR_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/brkitr\""
ICU_RBNF_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/rbnf\""
ICU_TRANSLIT_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/translit\""
ICU_LANG_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/lang\""
ICU_CURR_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/curr\""
ICU_REGION_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/region\""
ICU_ZONE_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/zone\""
FROM_FALLBACK = "int  1"
FROM_ROOT = "int  2"
FROM_DEFAULT = "int  3"
FROM_LOCALE = "int  4"
RES_BOGUS = "int  -1"
ALIAS = "int  3"
TABLE32 = "int  4"
TABLE16 = "int  5"
STRING_V2 = "int  6"
ARRAY16 = "int  9"
def setLoadingStatus():
    '''returns None\n\n
    setLoadingStatus(final int newStatus)\n
    setLoadingStatus(final String requestedLocale)\n
    '''
def getLoadingStatus():
    '''returns int\n\n
    getLoadingStatus()\n
    '''
def getResPath():
    '''returns String\n\n
    getResPath()\n
    '''
def getWithFallback():
    '''returns ICUResourceBundle\n\n
    getWithFallback(final String path)\n
    '''
def at():
    '''returns ICUResourceBundle\n\n
    at(final int index)\n
    at(final String key)\n
    '''
def findTopLevel():
    '''returns ICUResourceBundle\n\n
    findTopLevel(final int index)\n
    findTopLevel(final String aKey)\n
    '''
def findWithFallback():
    '''returns ICUResourceBundle\n\n
    findWithFallback(final String path)\n
    '''
def getStringWithFallback():
    '''returns String\n\n
    getStringWithFallback(final String path)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def run():
    '''returns List<String>\n\n
    run()\n
    '''
def visit():
    '''returns None\n\n
    visit(final String s)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    equals(final Object rhs)\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale()\n
    '''
def getParent():
    '''returns UResourceBundle\n\n
    getParent()\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def isAlias():
    '''returns boolean\n\n
    isAlias(final int index)\n
    isAlias()\n
    isAlias(final String k)\n
    '''
def getAliasPath():
    '''returns String\n\n
    getAliasPath(final int index)\n
    getAliasPath()\n
    getAliasPath(final String k)\n
    '''
def getKeysSafe():
    '''returns Enumeration<String>\n\n
    getKeysSafe()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
