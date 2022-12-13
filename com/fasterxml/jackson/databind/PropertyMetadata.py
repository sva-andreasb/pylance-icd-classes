def construct():
    '''public static PropertyMetadata construct(final Boolean req, final String desc, final Integer index, final String defaultValue)
    public static PropertyMetadata construct(final boolean req, final String desc, final Integer index, final String defaultValue)
    '''
def withDescription():
    '''public PropertyMetadata withDescription(final String desc)
    '''
def withMergeInfo():
    '''public PropertyMetadata withMergeInfo(final MergeInfo mergeInfo)
    '''
def withNulls():
    '''public PropertyMetadata withNulls(final Nulls valueNulls, final Nulls contentNulls)
    '''
def withDefaultValue():
    '''public PropertyMetadata withDefaultValue(String def)
    '''
def withIndex():
    '''public PropertyMetadata withIndex(final Integer index)
    '''
def withRequired():
    '''public PropertyMetadata withRequired(final Boolean b)
    '''
def getDescription():
    '''public String getDescription()
    '''
def getDefaultValue():
    '''public String getDefaultValue()
    '''
def hasDefaultValue():
    '''public boolean hasDefaultValue()
    '''
def isRequired():
    '''public boolean isRequired()
    '''
def getRequired():
    '''public Boolean getRequired()
    '''
def getIndex():
    '''public Integer getIndex()
    '''
def hasIndex():
    '''public boolean hasIndex()
    '''
def getMergeInfo():
    '''public MergeInfo getMergeInfo()
    '''
def getValueNulls():
    '''public Nulls getValueNulls()
    '''
def getContentNulls():
    '''public Nulls getContentNulls()
    '''
def createForDefaults():
    '''public static MergeInfo createForDefaults(final AnnotatedMember getter)
    '''
def createForTypeOverride():
    '''public static MergeInfo createForTypeOverride(final AnnotatedMember getter)
    '''
def createForPropertyOverride():
    '''public static MergeInfo createForPropertyOverride(final AnnotatedMember getter)
    '''
