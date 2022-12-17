def ():
    '''returns IlvGroup\n\n
    (final String name)\n
    (final IlvGroup ilvGroup)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def copy():
    '''returns IlvGroupElement\n\n
    copy(final IlvGroup ilvGroup)\n
    copy()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getTopGroup():
    '''returns IlvGroup\n\n
    getTopGroup()\n
    '''
def addElement():
    '''returns None\n\n
    addElement(final IlvGroupElement ilvGroupElement)\n
    '''
def removeElement():
    '''returns None\n\n
    removeElement(final IlvGroupElement ilvGroupElement)\n
    '''
def getElements():
    '''returns Enumeration\n\n
    getElements()\n
    '''
def findElement():
    '''returns IlvGroupElement\n\n
    findElement(final String s)\n
    '''
def traverse():
    '''returns boolean\n\n
    traverse(final IlvGroupTraverser ilvGroupTraverser)\n
    '''
def addBehavior():
    '''returns None\n\n
    addBehavior(final IlvBehavior ilvBehavior)\n
    '''
def removeBehavior():
    '''returns None\n\n
    removeBehavior(final IlvBehavior ilvBehavior)\n
    '''
def swapBehaviors():
    '''returns None\n\n
    swapBehaviors(final IlvBehavior ilvBehavior, final IlvBehavior ilvBehavior2)\n
    '''
def getBehaviors():
    '''returns Enumeration\n\n
    getBehaviors()\n
    '''
def getValueNames():
    '''returns String[]\n\n
    getValueNames(final boolean b)\n
    '''
def isABehaviorValue():
    '''returns boolean\n\n
    isABehaviorValue(final String anObject, final boolean b)\n
    '''
def setPrivate():
    '''returns None\n\n
    setPrivate(String intern, final boolean b)\n
    '''
def isPrivate():
    '''returns boolean\n\n
    isPrivate(String intern)\n
    '''
def isOutput():
    '''returns boolean\n\n
    isOutput(String intern)\n
    '''
def renameValue():
    '''returns None\n\n
    renameValue(final String anObject, final String name)\n
    '''
def getGroupFrame():
    '''returns IlvGroupFrame\n\n
    getGroupFrame()\n
    '''
def getGroupBag():
    '''returns IlvGroupBag\n\n
    getGroupBag()\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe(IlvGroupElement element, String substring, String substring2)\n
    '''
def fromTypes():
    '''returns Class[]\n\n
    fromTypes()\n
    fromTypes()\n
    '''
def toTypes():
    '''returns Class[]\n\n
    toTypes()\n
    toTypes()\n
    '''
def convert():
    '''returns Object\n\n
    convert(final Object obj, final Class clazz)\n
    convert(final Object o, final Class clazz)\n
    '''
