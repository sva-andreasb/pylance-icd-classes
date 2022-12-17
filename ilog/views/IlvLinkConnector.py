def ():
    '''returns IlvLinkConnector\n\n
    ()\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvLinkImage ilvLinkImage, final boolean b)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def attach():
    '''returns IlvLinkConnector\n\n
    attach(final IlvGraphic a, final boolean b)\n
    attach(final IlvLinkImage ilvLinkImage, final boolean c, final boolean b)\n
    attach(final IlvLinkImage ilvLinkImage, boolean b, final boolean b2, final boolean b3)\n
    '''
def detach():
    '''returns None\n\n
    detach(final boolean b)\n
    detach(final IlvLinkImage ilvLinkImage, final boolean b, final boolean b2)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    write(final IlvOutputStream ilvOutputStream, final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def read():
    '''returns None\n\n
    read(final IlvInputStream ilvInputStream, final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def disconnectLink():
    '''returns None\n\n
    disconnectLink(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def allowsConnectionPointMove():
    '''returns boolean\n\n
    allowsConnectionPointMove(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def linkRemoved():
    '''returns None\n\n
    linkRemoved(final IlvLinkImage ilvLinkImage)\n
    '''
def drawGhost():
    '''returns None\n\n
    drawGhost(final Graphics graphics, final IlvTransformer ilvTransformer, final Object o, final Object o2, final Object o3, final boolean b)\n
    '''
def supportsDrawGhost():
    '''returns boolean\n\n
    supportsDrawGhost()\n
    '''
