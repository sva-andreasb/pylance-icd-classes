def ():
    '''returns IlvTransformedGraphic\n\n
    (final IlvGraphic ilvGraphic, final IlvTransformer transformer, final boolean b)\n
    (final IlvTransformedGraphic ilvTransformedGraphic)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer()\n
    '''
def setTransformer():
    '''returns None\n\n
    setTransformer(final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def inside():
    '''returns boolean\n\n
    inside(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def move():
    '''returns None\n\n
    move(final float n, final float n2)\n
    move(final IlvPoint ilvPoint)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(final IlvRect ilvRect)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final IlvPoint ilvPoint, double degreesToRadians)\n
    '''
def scale():
    '''returns None\n\n
    scale(final double n, final double n2)\n
    '''
def resize():
    '''returns None\n\n
    resize(final float n, final float n2)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
