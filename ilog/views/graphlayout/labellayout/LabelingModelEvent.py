STRUCTURE_CHANGED = "int  1"
GEOMETRY_CHANGED = "int  2"
LABEL_ADDED = "int  4"
LABEL_REMOVED = "int  8"
OBSTACLE_ADDED = "int  16"
OBSTACLE_REMOVED = "int  32"
LABEL_GEOMETRY_CHANGED = "int  64"
OBSTACLE_GEOMETRY_CHANGED = "int  128"
def ():
    '''returns LabelingModelEvent\n\n
    (final IlvLabelingModel source)\n
    '''
def getLabelingModel():
    '''returns IlvLabelingModel\n\n
    getLabelingModel()\n
    '''
def setObstacleOrLabel():
    '''returns None\n\n
    setObstacleOrLabel(final Object d)\n
    '''
def getObstacleOrLabel():
    '''returns Object\n\n
    getObstacleOrLabel()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int c)\n
    '''
