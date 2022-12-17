def setChildPolicy():
    '''returns None\n\n
    setChildPolicy(final IlvLinkShapePolicy a)\n
    '''
def afterAdd():
    '''returns None\n\n
    afterAdd(final IlvLinkImage ilvLinkImage)\n
    '''
def beforeRemove():
    '''returns None\n\n
    beforeRemove(final IlvLinkImage ilvLinkImage)\n
    '''
def onInstall():
    '''returns None\n\n
    onInstall(final IlvLinkImage ilvLinkImage)\n
    '''
def onUninstall():
    '''returns None\n\n
    onUninstall(final IlvLinkImage ilvLinkImage)\n
    '''
def allowSetIntermediateLinkPoints():
    '''returns boolean\n\n
    allowSetIntermediateLinkPoints(final IlvLinkImage ilvLinkImage, final IlvPoint[] array, final int n, final int n2)\n
    '''
def afterSetIntermediateLinkPoints():
    '''returns None\n\n
    afterSetIntermediateLinkPoints(final IlvLinkImage ilvLinkImage)\n
    '''
def allowInsertPoint():
    '''returns boolean\n\n
    allowInsertPoint(final IlvLinkImage ilvLinkImage, final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def afterInsertPoint():
    '''returns None\n\n
    afterInsertPoint(final IlvLinkImage ilvLinkImage, final int n, final IlvTransformer ilvTransformer)\n
    '''
def allowRemovePoint():
    '''returns boolean\n\n
    allowRemovePoint(final IlvLinkImage ilvLinkImage, final int n, final IlvTransformer ilvTransformer)\n
    '''
def afterRemovePoint():
    '''returns None\n\n
    afterRemovePoint(final IlvLinkImage ilvLinkImage, final int n, final IlvTransformer ilvTransformer)\n
    '''
def allowMovePoint():
    '''returns boolean\n\n
    allowMovePoint(final IlvLinkImage ilvLinkImage, final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def afterMovePoint():
    '''returns None\n\n
    afterMovePoint(final IlvLinkImage ilvLinkImage, final int n, final IlvTransformer ilvTransformer)\n
    '''
def allowApplyTransform():
    '''returns boolean\n\n
    allowApplyTransform(final IlvLinkImage ilvLinkImage, final IlvTransformer ilvTransformer)\n
    '''
def afterApplyTransform():
    '''returns None\n\n
    afterApplyTransform(final IlvLinkImage ilvLinkImage, final IlvTransformer ilvTransformer)\n
    '''
def afterFromNodeMoved():
    '''returns None\n\n
    afterFromNodeMoved(final IlvLinkImage ilvLinkImage)\n
    '''
def afterToNodeMoved():
    '''returns None\n\n
    afterToNodeMoved(final IlvLinkImage ilvLinkImage)\n
    '''
def afterAny():
    '''returns None\n\n
    afterAny(final IlvLinkImage ilvLinkImage)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final IlvLinkImage ilvLinkImage, final IlvTransformer ilvTransformer)\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final IlvLinkImage ilvLinkImage, final int n, final IlvTransformer ilvTransformer)\n
    '''
