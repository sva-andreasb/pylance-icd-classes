def XDGFShape():
    '''public XDGFShape(final ShapeSheetType shapeSheet, final XDGFBaseContents parentPage, final XDGFDocument document)
    public XDGFShape(final XDGFShape parent, final ShapeSheetType shapeSheet, final XDGFBaseContents parentPage, final XDGFDocument document)
    '''
def toString():
    '''public String toString()
    '''
def getXmlObject():
    '''public ShapeSheetType getXmlObject()
    '''
def getID():
    '''public long getID()
    '''
def getType():
    '''public String getType()
    '''
def getTextAsString():
    '''public String getTextAsString()
    '''
def hasText():
    '''public boolean hasText()
    '''
def getCell():
    '''public XDGFCell getCell(final String cellName)
    '''
def getGeometryByIdx():
    '''public GeometrySection getGeometryByIdx(final long idx)
    '''
def getShapes():
    '''public List<XDGFShape> getShapes()
    '''
def getName():
    '''public String getName()
    '''
def getShapeType():
    '''public String getShapeType()
    '''
def getSymbolName():
    '''public String getSymbolName()
    '''
def getMasterShape():
    '''public XDGFShape getMasterShape()
    '''
def getParentShape():
    '''public XDGFShape getParentShape()
    '''
def getTopmostParentShape():
    '''public XDGFShape getTopmostParentShape()
    '''
def hasMaster():
    '''public boolean hasMaster()
    '''
def hasMasterShape():
    '''public boolean hasMasterShape()
    '''
def hasParent():
    '''public boolean hasParent()
    '''
def hasShapes():
    '''public boolean hasShapes()
    '''
def isTopmost():
    '''public boolean isTopmost()
    '''
def isShape1D():
    '''public boolean isShape1D()
    '''
def isDeleted():
    '''public boolean isDeleted()
    '''
def getText():
    '''public XDGFText getText()
    '''
def getPinX():
    '''public Double getPinX()
    '''
def getPinY():
    '''public Double getPinY()
    '''
def getWidth():
    '''public Double getWidth()
    '''
def getHeight():
    '''public Double getHeight()
    '''
def getLocPinX():
    '''public Double getLocPinX()
    '''
def getLocPinY():
    '''public Double getLocPinY()
    '''
def getBeginX():
    '''public Double getBeginX()
    '''
def getBeginY():
    '''public Double getBeginY()
    '''
def getEndX():
    '''public Double getEndX()
    '''
def getEndY():
    '''public Double getEndY()
    '''
def getAngle():
    '''public Double getAngle()
    '''
def getFlipX():
    '''public Boolean getFlipX()
    '''
def getFlipY():
    '''public Boolean getFlipY()
    '''
def getTxtPinX():
    '''public Double getTxtPinX()
    '''
def getTxtPinY():
    '''public Double getTxtPinY()
    '''
def getTxtLocPinX():
    '''public Double getTxtLocPinX()
    '''
def getTxtLocPinY():
    '''public Double getTxtLocPinY()
    '''
def getTxtAngle():
    '''public Double getTxtAngle()
    '''
def getTxtWidth():
    '''public Double getTxtWidth()
    '''
def getTxtHeight():
    '''public Double getTxtHeight()
    '''
def getLineCap():
    '''public Integer getLineCap()
    '''
def getLineColor():
    '''public Color getLineColor()
    '''
def getLinePattern():
    '''public Integer getLinePattern()
    '''
def getLineWeight():
    '''public Double getLineWeight()
    '''
def getFontColor():
    '''public Color getFontColor()
    '''
def getFontSize():
    '''public Double getFontSize()
    '''
def getStroke():
    '''public Stroke getStroke()
    '''
def getGeometrySections():
    '''public Iterable<GeometrySection> getGeometrySections()
    '''
def hasGeometry():
    '''public boolean hasGeometry()
    '''
def visitShapes():
    '''public void visitShapes(final ShapeVisitor visitor, AffineTransform tr, final int level)
    public void visitShapes(final ShapeVisitor visitor, final int level)
    '''
