def ():
    '''returns IlvTiledLayer\n\n
    (final IlvRect ilvRect)\n
    (final IlvRect ilvRect, final IlvTileCache ilvTileCache, final int j)\n
    (final IlvRect ilvRect, final IlvTileCache ilvTileCache)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def setDebugView():
    '''returns None\n\n
    setDebugView(final IlvManagerView ilvManagerView)\n
    setDebugView(final IlvManagerView b, final Color c, final Color d, final Color e, final Color f)\n
    '''
def computeBBox():
    '''returns IlvRect\n\n
    computeBBox(final IlvTransformer ilvTransformer)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible(final IlvManagerView ilvManagerView)\n
    '''
def ignoreView():
    '''returns None\n\n
    ignoreView(final IlvManagerView ilvManagerView, final boolean b)\n
    '''
def isIgnoringView():
    '''returns boolean\n\n
    isIgnoringView(final IlvManagerView ilvManagerView)\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final IlvRect size)\n
    '''
def getSize():
    '''returns IlvRect\n\n
    getSize()\n
    '''
def setTileLoader():
    '''returns None\n\n
    setTileLoader(final IlvTileLoader tileLoader)\n
    '''
def fitTransformerToTile():
    '''returns None\n\n
    fitTransformerToTile(final IlvManagerView ilvManagerView, final int n, final int n2)\n
    fitTransformerToTile(final IlvManagerView ilvManagerView, final IlvFreeTile ilvFreeTile)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def layerInserted():
    '''returns None\n\n
    layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)\n
    '''
def layerRemoved():
    '''returns None\n\n
    layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)\n
    '''
def layerMoved():
    '''returns None\n\n
    layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)\n
    '''
def layerChanged():
    '''returns None\n\n
    layerChanged(final ManagerLayerEvent managerLayerEvent)\n
    '''
def tileChanged():
    '''returns None\n\n
    tileChanged(final TileEvent tileEvent)\n
    '''
