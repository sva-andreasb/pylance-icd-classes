INDEXED = "int  0"
FREE = "int  1"
LEFT_COLUMN_INDEX = "int  0"
RIGHT_COLUMN_INDEX = "int  1"
UPPER_ROW_INDEX = "int  2"
LOWER_ROW_INDEX = "int  3"
def ():
    '''returns IlvTileController\n\n
    (final IlvManager f, final IlvRect ilvRect)\n
    (final IlvManager ilvManager, final IlvRect ilvRect, final IlvTileCache c)\n
    (final IlvManager f)\n
    (final IlvManager ilvManager, final IlvTileCache c)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def setLockFilter():
    '''returns None\n\n
    setLockFilter(final IlvTileLockFilter n)\n
    '''
def getLockFilter():
    '''returns IlvTileLockFilter\n\n
    getLockFilter()\n
    '''
def setPrintingErrors():
    '''returns None\n\n
    setPrintingErrors(final boolean i)\n
    '''
def isPrintingErrors():
    '''returns boolean\n\n
    isPrintingErrors()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final IlvRect ilvRect)\n
    '''
def getSize():
    '''returns IlvRect\n\n
    getSize()\n
    '''
def getTileIndexes():
    '''returns int[]\n\n
    getTileIndexes(final IlvRect ilvRect)\n
    '''
def getTileOrigin():
    '''returns IlvRect\n\n
    getTileOrigin()\n
    '''
def tileBBox():
    '''returns None\n\n
    tileBBox(final int n, final int n2, final IlvRect ilvRect)\n
    '''
def getTile():
    '''returns IlvTile\n\n
    getTile(final int n, final int n2)\n
    '''
def lockTile():
    '''returns None\n\n
    lockTile(final int n, final int n2, final Object o)\n
    lockTile(final IlvTile ilvTile, final Object o)\n
    '''
def getIntersectingTiles():
    '''returns Collection\n\n
    getIntersectingTiles(final IlvRect ilvRect)\n
    '''
def getTiles():
    '''returns Collection\n\n
    getTiles()\n
    '''
def addTile():
    '''returns None\n\n
    addTile(final IlvFreeTile e)\n
    '''
def getCache():
    '''returns IlvTileCache\n\n
    getCache()\n
    '''
def ignoreView():
    '''returns None\n\n
    ignoreView(final IlvManagerView ilvManagerView, final boolean b)\n
    '''
def isIgnoringView():
    '''returns boolean\n\n
    isIgnoringView(final IlvManagerView o)\n
    '''
def unlockTiles():
    '''returns None\n\n
    unlockTiles(final Object o)\n
    '''
def unlockTile():
    '''returns boolean\n\n
    unlockTile(final int n, final int n2, final Object o)\n
    '''
def updateView():
    '''returns None\n\n
    updateView(final IlvManagerView ilvManagerView)\n
    '''
def getLayer():
    '''returns IlvTiledLayer\n\n
    getLayer()\n
    '''
def addTileListener():
    '''returns None\n\n
    addTileListener(final TileListener obj)\n
    '''
def removeTileListener():
    '''returns None\n\n
    removeTileListener(final TileListener obj)\n
    '''
def setTileLoader():
    '''returns None\n\n
    setTileLoader(final IlvTileLoader b)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def isUnlockFilteredTiles():
    '''returns boolean\n\n
    isUnlockFilteredTiles()\n
    '''
def setUnlockFilteredTiles():
    '''returns None\n\n
    setUnlockFilteredTiles(final boolean s)\n
    '''
def removeAllFreeTiles():
    '''returns None\n\n
    removeAllFreeTiles()\n
    '''
