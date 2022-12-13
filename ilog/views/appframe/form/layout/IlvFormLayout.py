DEFAUT_SIZE_MODE = "int  0"
PREFERRED_SIZE_MODE = "int  1"
MINIMUM_SIZE_MODE = "int  2"
MAXIMUM_SIZE_MODE = "int  4"
DEFAULT_BORDER_INSET = "int  3"
DEFAULT_INSET = "int  3"
PARENT_NAME = "String  \"${Parent}\""
def IlvFormLayout():
    '''public IlvFormLayout()
    '''
def setConstantValue():
    '''public void setConstantValue(final String s, final Number n)
    '''
def removeConstantValue():
    '''public Number removeConstantValue(final String s)
    '''
def getConstantValue():
    '''public Number getConstantValue(final String s)
    '''
def setGroup():
    '''public void setGroup(final Object f)
    '''
def getGroup():
    '''public Object getGroup()
    '''
def layout():
    '''public void layout(final Object group)
    '''
def calculateGroupSize():
    '''public IlvFormDimension calculateGroupSize(final Object group, final int n)
    '''
def addAttachment():
    '''public void addAttachment(final IlvAttachment ilvAttachment)
    public void addAttachment(final IlvControlAnchor ilvControlAnchor, final IlvControlAnchor ilvControlAnchor2, final Function function)
    '''
def getControlAnchor():
    '''public IlvControlAnchor getControlAnchor(final Object o, final String str)
    public IlvControlAnchor getControlAnchor(final String s, final String str)
    public IlvControlAnchor getControlAnchor(final String s, final Anchor anchor)
    '''
def leftOf():
    '''public IlvControlAnchor leftOf(final Object o)
    '''
def leadingOf():
    '''public IlvControlAnchor leadingOf(final Object o)
    '''
def rightOf():
    '''public IlvControlAnchor rightOf(final Object o)
    '''
def trailingOf():
    '''public IlvControlAnchor trailingOf(final Object o)
    '''
def topOf():
    '''public IlvControlAnchor topOf(final Object o)
    '''
def bottomOf():
    '''public IlvControlAnchor bottomOf(final Object o)
    '''
def widthOf():
    '''public IlvControlAnchor widthOf(final Object o)
    '''
def heightOf():
    '''public IlvControlAnchor heightOf(final Object o)
    '''
def extensibleRightOf():
    '''public IlvControlAnchor extensibleRightOf(final Object o)
    '''
def extensibleTrailingOf():
    '''public IlvControlAnchor extensibleTrailingOf(final Object o)
    '''
def extensibleBottomOf():
    '''public IlvControlAnchor extensibleBottomOf(final Object o)
    '''
def preferredHeightOf():
    '''public IlvControlAnchor preferredHeightOf(final Object o)
    '''
def preferredWidthOf():
    '''public IlvControlAnchor preferredWidthOf(final Object o)
    '''
def verticalCenterOf():
    '''public IlvControlAnchor verticalCenterOf(final Object o)
    '''
def horizontalCenterOf():
    '''public IlvControlAnchor horizontalCenterOf(final Object o)
    '''
def getComponentOrientation():
    '''public ComponentOrientation getComponentOrientation()
    '''
def toString():
    '''public String toString()
    public String toString()
    public String toString()
    '''
def setParentLayout():
    '''public void setParentLayout(final IlvFormLayout h)
    '''
def getParentLayout():
    '''public IlvFormLayout getParentLayout()
    '''
def GetAnchor():
    '''public static Anchor GetAnchor(final String s)
    '''
def GetAnchors():
    '''public static Collection GetAnchors()
    '''
def setComponentOrientation():
    '''public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    '''
def CreateFunction():
    '''public static Function CreateFunction(final String s, final float n)
    '''
def RegisterFunctionFactory():
    '''public static void RegisterFunctionFactory(final String s, final FunctionFactory functionFactory)
    '''
def create():
    '''public Function create(final float n)
    public Function create(final float n)
    public Function create(final float n)
    public Function create(final float n)
    public Function create(final float n)
    public Function create(final float n)
    '''
def ContainerSizeAttachment():
    '''public ContainerSizeAttachment(final IlvControlAnchor ilvControlAnchor)
    '''
def setMode():
    '''public void setMode(final int n)
    public void setMode(final int a)
    '''
def setSize():
    '''public void setSize(final float constant)
    '''
def ContainerSizeFunction():
    '''public ContainerSizeFunction()
    '''
def calcValue():
    '''public float calcValue(final float n, final float n2)
    public float calcValue(final float n, final float n2)
    public float calcValue(final float n, final float n2)
    public float calcValue(final float n, final float n2)
    public float calcValue(final float n, final float n2)
    public float calcValue(final float n, final float n2)
    public float calcValue(final float n, final float n2)
    '''
def calcInverseValue():
    '''public float calcInverseValue(final float n, final float n2)
    public float calcInverseValue(final float n, final float n2)
    public float calcInverseValue(final float n, final float n2)
    public float calcInverseValue(final float n, final float n2)
    public float calcInverseValue(final float n, final float n2)
    public float calcInverseValue(final float n, final float n2)
    public float calcInverseValue(final float n, final float n2)
    '''
def getDescription():
    '''public String getDescription(final String s, final String s2)
    public String getDescription(final String str, final String s)
    public String getDescription(final String s, final String s2)
    public String getDescription(final String s, final String s2)
    public String getDescription(final String s, final String s2)
    public String getDescription(final String str, final String str2)
    public String getDescription(final String str, final String str2)
    '''
def ConstantFunction():
    '''public ConstantFunction(final float a)
    '''
def getConstant():
    '''public float getConstant()
    '''
def setConstant():
    '''public void setConstant(final float a)
    '''
def PercentageFunction():
    '''public PercentageFunction(final float n)
    '''
def DivFunction():
    '''public DivFunction(final float divisor)
    '''
def MulFunction():
    '''public MulFunction(final float factor)
    '''
def SumFunction():
    '''public SumFunction(final float b)
    '''
def getSumParameter():
    '''public float getSumParameter()
    '''
