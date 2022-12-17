def getParent():
    '''returns IlvGroup\n\n
    getParent()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String s)\n
    '''
def getRelativePath():
    '''returns String\n\n
    getRelativePath(final IlvGroup obj)\n
    '''
def traverse():
    '''returns boolean\n\n
    traverse(final IlvGroupTraverser ilvGroupTraverser)\n
    traverse(final IlvGraphicElement ilvGraphicElement)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    boundingBox(final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    applyTransform(final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def move():
    '''returns None\n\n
    move(final float n, final float n2)\n
    '''
def getValueNames():
    '''returns String[]\n\n
    getValueNames(final boolean b)\n
    '''
def isOutput():
    '''returns boolean\n\n
    isOutput(final String s)\n
    '''
def subscribe():
    '''returns None\n\n
    subscribe(final IlvGroupElement ilvGroupElement, final String s, final String s2)\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe(final IlvGroupElement ilvGroupElement, final String s, final String s2)\n
    '''
