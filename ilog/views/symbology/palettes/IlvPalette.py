PALETTE_DESCRIPTION_FILE = "String  \"palette.xml\""
SMALLICON_SIZE = "int  24"
def ():
    '''returns IlvPalette\n\n
    ()\n
    (final ClassLoader classLoader)\n
    '''
def load():
    '''returns None\n\n
    load(final URL url)\n
    '''
def setName():
    '''returns None\n\n
    setName(final Locale locale, final String s)\n
    setName(final String s)\n
    '''
def getName():
    '''returns String\n\n
    getName(final Locale locale)\n
    getName()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final Locale locale, final String s)\n
    setDescription(final String s)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription(final Locale locale)\n
    getDescription()\n
    '''
def getIconURL():
    '''returns URL\n\n
    getIconURL()\n
    '''
def setIconURL():
    '''returns None\n\n
    setIconURL(final URL g)\n
    '''
def setIconResourceName():
    '''returns None\n\n
    setIconResourceName(final String name)\n
    '''
def getIconResourceName():
    '''returns String\n\n
    getIconResourceName()\n
    '''
def addCategory():
    '''returns IlvPaletteCategory\n\n
    addCategory(final IlvPaletteCategory ilvPaletteCategory, final String s)\n
    '''
def addSymbol():
    '''returns IlvPaletteSymbol\n\n
    addSymbol(final IlvPaletteCategory ilvPaletteCategory, final String s)\n
    '''
def replace():
    '''returns None\n\n
    replace(final IlvPaletteObject ilvPaletteObject, final IlvPaletteObject ilvPaletteObject2)\n
    '''
def getSymbol():
    '''returns IlvPaletteSymbol\n\n
    getSymbol(final String s)\n
    getSymbol(final String s, final String s2)\n
    '''
def getCategory():
    '''returns IlvPaletteCategory\n\n
    getCategory(final String s)\n
    '''
def getPaletteObject():
    '''returns IlvPaletteObject\n\n
    getPaletteObject(final String s)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getIcon():
    '''returns Icon\n\n
    getIcon()\n
    '''
def getSmallIcon():
    '''returns ImageIcon\n\n
    getSmallIcon()\n
    '''
def getRoot():
    '''returns IlvPaletteCategory\n\n
    getRoot()\n
    '''
def setRoot():
    '''returns None\n\n
    setRoot(final IlvPaletteCategory i)\n
    '''
def setRootCategory():
    '''returns IlvPaletteCategory\n\n
    setRootCategory(final String s)\n
    '''
def getChildren():
    '''returns Enumeration\n\n
    getChildren(final Object o)\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object o)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount(final Object o)\n
    '''
def isCategory():
    '''returns boolean\n\n
    isCategory(final Object o)\n
    '''
def addPaletteListener():
    '''returns None\n\n
    addPaletteListener(final PaletteListener l)\n
    '''
def removePaletteListener():
    '''returns None\n\n
    removePaletteListener(final PaletteListener l)\n
    '''
def getJarURL():
    '''returns URL\n\n
    getJarURL()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def setPackageName():
    '''returns None\n\n
    setPackageName(String string)\n
    '''
def getPaletteResourceName():
    '''returns String\n\n
    getPaletteResourceName()\n
    '''
def getPaletteURL():
    '''returns URL\n\n
    getPaletteURL()\n
    '''
def setDefaultLocale():
    '''returns None\n\n
    setDefaultLocale(final Locale n)\n
    '''
def getDefaultLocale():
    '''returns Locale\n\n
    getDefaultLocale()\n
    '''
def addValueSet():
    '''returns String\n\n
    addValueSet(final IlvPaletteSymbolParameterValueSet e, final boolean b)\n
    '''
def removeValueSet():
    '''returns None\n\n
    removeValueSet(final IlvPaletteSymbolParameterValueSet o)\n
    '''
def getValueSetCount():
    '''returns int\n\n
    getValueSetCount()\n
    '''
def getValueSet():
    '''returns IlvPaletteSymbolParameterValueSet\n\n
    getValueSet(final int index)\n
    getValueSet(final String anObject)\n
    '''
def getValueSets():
    '''returns IlvPaletteSymbolParameterValueSet[]\n\n
    getValueSets()\n
    '''
