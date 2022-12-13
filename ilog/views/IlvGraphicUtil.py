COMPATIBLE_SMOOTHNESS = "float  -1.0f"
AUTO_SMOOTHNESS = "float  -2.0f"
def GetArrowSize():
    '''public static float GetArrowSize(final IlvLinkImage ilvLinkImage, final float n, final IlvTransformer ilvTransformer)
    '''
def DrawPolyline():
    '''public static void DrawPolyline(final Graphics graphics, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final float[] array2, final IlvTransformer ilvTransformer)
    public static void DrawPolyline(final Graphics graphics, final IlvPoint[] array, final int n, float width, int c, int d, float[] a, final IlvTransformer ilvTransformer, final boolean b)
    '''
def isPrinting():
    '''public static boolean isPrinting(final Graphics graphics)
    '''
def PointInPolyline():
    '''public static boolean PointInPolyline(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final IlvTransformer ilvTransformer)
    '''
def PolylineBBox():
    '''public static IlvRect PolylineBBox(final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final IlvTransformer ilvTransformer)
    '''
def DrawBezier():
    '''public static void DrawBezier(final Graphics graphics, final IlvPoint[] array, final int n, final boolean b, final float n2, final float n3, final int n4, final int n5, final float[] array2, final IlvTransformer ilvTransformer, final boolean b2)
    public static void DrawBezier(final Graphics graphics, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final float[] array2, final IlvTransformer ilvTransformer)
    public static void DrawBezier(final Graphics graphics, final IlvPoint[] array, final int n, float width, int c, int d, float[] a, IlvTransformer ilvTransformer, final boolean b)
    '''
def BezierBoundingBox():
    '''public static void BezierBoundingBox(final IlvRect ilvRect, final IlvPoint[] array, final int n, final boolean b, final float n2, final float n3, final int n4, final int n5, final IlvTransformer ilvTransformer)
    public static void BezierBoundingBox(final IlvRect ilvRect, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final IlvTransformer ilvTransformer)
    '''
def PointInBezier():
    '''public static boolean PointInBezier(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final boolean b, final float n2, final float n3, final int n4, final int n5, final IlvTransformer ilvTransformer)
    public static boolean PointInBezier(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final IlvTransformer ilvTransformer)
    '''
def DrawClosedBezier():
    '''public static void DrawClosedBezier(final Graphics graphics, final IlvPoint[] array, final int n, final boolean b, final float n2, final float n3, final int n4, final int n5, final float[] array2, final IlvTransformer ilvTransformer)
    public static void DrawClosedBezier(final Graphics graphics, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final float[] array2, final IlvTransformer ilvTransformer)
    '''
def ClosedBezierBoundingBox():
    '''public static void ClosedBezierBoundingBox(final IlvRect ilvRect, final IlvPoint[] array, final int n, final boolean b, final float n2, final float n3, final int n4, final int n5, final IlvTransformer ilvTransformer)
    public static void ClosedBezierBoundingBox(final IlvRect ilvRect, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final IlvTransformer ilvTransformer)
    '''
def PointInClosedBezier():
    '''public static boolean PointInClosedBezier(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final boolean b, final float n2, final float n3, final int n4, final int n5, final IlvTransformer ilvTransformer)
    public static boolean PointInClosedBezier(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final float n2, final int n3, final int n4, final IlvTransformer ilvTransformer)
    '''
def FillBezier():
    '''public static void FillBezier(final Graphics graphics, final IlvPoint[] array, final int n, final boolean b, final float n2, final IlvTransformer ilvTransformer)
    public static void FillBezier(final Graphics graphics, final IlvPoint[] array, final int n, final IlvTransformer ilvTransformer)
    '''
def PointInFilledBezier():
    '''public static boolean PointInFilledBezier(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final boolean b, final float n2, final IlvTransformer ilvTransformer)
    public static boolean PointInFilledBezier(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final IlvTransformer ilvTransformer)
    '''
def GetSmoothSpline():
    '''public static IlvPoint[] GetSmoothSpline(final IlvPoint[] array, final int n, final float n2, final boolean b, IlvPoint[] array2)
    '''
def GetSmoothSplineHandlesFromBends():
    '''public static IlvPoint[] GetSmoothSplineHandlesFromBends(final IlvPoint[] array, final int n, final float n2, final boolean b, IlvPoint[] a)
    '''
def GetSmoothSplineHandleFromBend():
    '''public static IlvPoint GetSmoothSplineHandleFromBend(final int n, final IlvPoint[] array, final int n2, final float n3, final boolean b)
    '''
def GetSmoothSplineBendFromHandle():
    '''public static IlvPoint GetSmoothSplineBendFromHandle(final int n, final IlvPoint ilvPoint, final IlvPoint[] array, final int n2, final float n3, final boolean b)
    '''
def GetAutoSmoothSpline():
    '''public static IlvPoint[] GetAutoSmoothSpline(final IlvPoint[] array, final int n, final boolean b, IlvPoint[] array2, int[] a, final int[] array3)
    '''
def FillPolygon():
    '''public static void FillPolygon(final Graphics graphics, final IlvPoint[] array, final int n, final IlvTransformer ilvTransformer)
    '''
def DrawPolygon():
    '''public static void DrawPolygon(final Graphics graphics, final IlvPoint[] array, final int n, final IlvTransformer ilvTransformer)
    '''
def PointInPolygon():
    '''public static boolean PointInPolygon(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final IlvTransformer ilvTransformer)
    public static boolean PointInPolygon(final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final IlvTransformer ilvTransformer, final boolean b)
    '''
def FillOutlinedPolygon():
    '''public static void FillOutlinedPolygon(final Graphics graphics, final IlvPoint[] array, final int n, final Color color, final Color color2, final IlvTransformer ilvTransformer)
    '''
def DrawString():
    '''public static void DrawString(final Graphics graphics, final String str, final int n, final int n2, final boolean b)
    public static void DrawString(final IlvGraphic ilvGraphic, final Graphics graphics, final String s, final int n, final int n2, final boolean b)
    '''
def GetStringBounds():
    '''public static IlvRect GetStringBounds(final String s, final Font font, final boolean isAntiAliased)
    public static IlvRect GetStringBounds(final IlvGraphic ilvGraphic, final String s, final Font font, final boolean b)
    '''
def GetFontDescent():
    '''public static float GetFontDescent(final String str, final Font font, final boolean isAntiAliased)
    '''
def StartAntiAliasing():
    '''public static void StartAntiAliasing(final Graphics graphics)
    '''
def StopAntiAliasing():
    '''public static void StopAntiAliasing(final Graphics graphics)
    '''
def GetAlpha():
    '''public static int GetAlpha(final Color color)
    '''
def MakeColor():
    '''public static Color MakeColor(final int r, final int g, final int b, final int a)
    public static Color MakeColor(final int rgba)
    '''
def PointInShape():
    '''public static boolean PointInShape(final IlvPoint ilvPoint, final Shape shape)
    '''
def RectBBox():
    '''public static IlvRect RectBBox(final IlvRect ilvRect, final IlvTransformer ilvTransformer)
    '''
def DrawImage():
    '''public static void DrawImage(final Graphics graphics, final IlvRect ilvRect, final Image image, final IlvTransformer ilvTransformer, final ImageObserver imageObserver, final boolean b)
    '''
def DrawRenderedImage():
    '''public static void DrawRenderedImage(final Graphics graphics, final IlvRect ilvRect, final RenderedImage renderedImage, final IlvTransformer ilvTransformer, final boolean b)
    '''
def AddClip():
    '''public static Shape AddClip(final Graphics graphics, final Shape shape)
    '''
def CreateTransformedShape():
    '''public static Shape CreateTransformedShape(final Shape pSrc, final IlvTransformer ilvTransformer)
    '''
def SetJViews60LineStyleMode():
    '''public static void SetJViews60LineStyleMode(final boolean o)
    '''
def IsJViews60LineStyleMode():
    '''public static boolean IsJViews60LineStyleMode()
    '''
def GetPolyPoints():
    '''public static final IlvPoint[] GetPolyPoints(final IlvPolyPointsInterface ilvPolyPointsInterface, final IlvTransformer ilvTransformer)
    '''
def startBidiChange():
    '''public static IlvGraphicVector startBidiChange(final IlvGraphicBag ilvGraphicBag)
    '''
def stopBidiChange():
    '''public static void stopBidiChange(final IlvGraphicBag ilvGraphicBag, final IlvGraphicVector ilvGraphicVector, final boolean b)
    '''
