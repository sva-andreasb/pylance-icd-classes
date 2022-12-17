def ():
    '''returns BaseFontParameters\n\n
    ()\n
    (final String fontName)\n
    '''
def awtToPdf():
    '''returns BaseFont\n\n
    awtToPdf(final Font font)\n
    '''
def pdfToAwt():
    '''returns Font\n\n
    pdfToAwt(final BaseFont font, final int size)\n
    '''
def putName():
    '''returns None\n\n
    putName(final String awtName, final BaseFontParameters parameters)\n
    '''
def putAlias():
    '''returns None\n\n
    putAlias(final String alias, final String awtName)\n
    '''
def getBaseFontParameters():
    '''returns BaseFontParameters\n\n
    getBaseFontParameters(final String name)\n
    '''
def insertNames():
    '''returns None\n\n
    insertNames(final Object[] allNames, final String path)\n
    '''
def insertDirectory():
    '''returns int\n\n
    insertDirectory(final String dir)\n
    '''
def getMapper():
    '''returns HashMap\n\n
    getMapper()\n
    '''
def getAliases():
    '''returns HashMap\n\n
    getAliases()\n
    '''
