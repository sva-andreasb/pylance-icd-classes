STRUCTURE_CHANGED = "int  1"
GEOMETRY_CHANGED = "int  2"
NODE_ADDED = "int  4"
NODE_REMOVED = "int  8"
LINK_ADDED = "int  16"
LINK_REMOVED = "int  32"
NODE_GEOMETRY_CHANGED = "int  64"
LINK_GEOMETRY_CHANGED = "int  128"
ADJUSTMENT_END = "int  256"
def ():
    '''returns GraphModelEvent\n\n
    (final IlvGraphModel source)\n
    '''
def getGraphModel():
    '''returns IlvGraphModel\n\n
    getGraphModel()\n
    '''
def setNodeOrLink():
    '''returns None\n\n
    setNodeOrLink(final Object c)\n
    '''
def getNodeOrLink():
    '''returns Object\n\n
    getNodeOrLink()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int b)\n
    '''
