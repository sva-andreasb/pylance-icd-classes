def ():
    '''returns IlvPaletteManager\n\n
    ()\n
    (final IlvCSSCompatible ilvCSSCompatible)\n
    '''
def attach():
    '''returns None\n\n
    attach(final IlvCSSCompatible e)\n
    '''
def detach():
    '''returns None\n\n
    detach(final IlvCSSCompatible o)\n
    detach()\n
    '''
def getAttachComponents():
    '''returns IlvCSSCompatible[]\n\n
    getAttachComponents()\n
    '''
def isAttached():
    '''returns boolean\n\n
    isAttached(final IlvCSSCompatible o)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def add():
    '''returns None\n\n
    add(final IlvPalette e)\n
    '''
def remove():
    '''returns None\n\n
    remove(final IlvPalette ilvPalette)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def getPalette():
    '''returns IlvPalette\n\n
    getPalette(final String s)\n
    getPalette(final int index)\n
    '''
def getPaletteCount():
    '''returns int\n\n
    getPaletteCount()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPalette o)\n
    '''
def getPaletteWithSymbol():
    '''returns IlvPalette\n\n
    getPaletteWithSymbol(final String s, final String s2, final String s3)\n
    '''
def addPaletteManagerListener():
    '''returns None\n\n
    addPaletteManagerListener(final PaletteManagerListener l)\n
    '''
def removePaletteManagerListener():
    '''returns None\n\n
    removePaletteManagerListener(final PaletteManagerListener l)\n
    '''
def getPaletteIndex():
    '''returns int\n\n
    getPaletteIndex(final IlvPalette o)\n
    '''
def load():
    '''returns IlvPalette\n\n
    load(final URL url)\n
    load(final String s)\n
    '''
def save():
    '''returns None\n\n
    save(final IlvPalette ilvPalette, final File file)\n
    save(final IlvPalette ilvPalette, final File file, final boolean b, final boolean b2)\n
    '''
def getWorkingDirectory():
    '''returns File\n\n
    getWorkingDirectory()\n
    '''
def setWorkingDirectory():
    '''returns None\n\n
    setWorkingDirectory(final File file)\n
    '''
def setAndCreateWorkingDirectory():
    '''returns None\n\n
    setAndCreateWorkingDirectory(final File parent, String string)\n
    '''
def isPaletteReadOnly():
    '''returns boolean\n\n
    isPaletteReadOnly(final IlvPalette o)\n
    '''
def updateSymbolReferences():
    '''returns None\n\n
    updateSymbolReferences(final ArrayList list, final String s, final String str, final String str2)\n
    '''
def getPalettesToUpdate():
    '''returns ArrayList\n\n
    getPalettesToUpdate(final String s)\n
    '''
