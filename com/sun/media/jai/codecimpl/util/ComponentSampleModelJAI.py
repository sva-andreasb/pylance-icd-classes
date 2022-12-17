def ():
    '''returns ComponentSampleModelJAI\n\n
    (final int dataType, final int w, final int h, final int pixelStride, final int scanlineStride, final int[] bandOffsets)\n
    (final int dataType, final int w, final int h, final int pixelStride, final int scanlineStride, final int[] bankIndices, final int[] bandOffsets)\n
    '''
def createCompatibleSampleModel():
    '''returns SampleModel\n\n
    createCompatibleSampleModel(final int w, final int h)\n
    '''
def createSubsetSampleModel():
    '''returns SampleModel\n\n
    createSubsetSampleModel(final int[] bands)\n
    '''
def createDataBuffer():
    '''returns DataBuffer\n\n
    createDataBuffer()\n
    '''
def getDataElements():
    '''returns Object\n\n
    getDataElements(final int x, final int y, Object obj, final DataBuffer data)\n
    getDataElements(final int x, final int y, final int w, final int h, Object obj, final DataBuffer data)\n
    '''
def setDataElements():
    '''returns None\n\n
    setDataElements(final int x, final int y, final Object obj, final DataBuffer data)\n
    setDataElements(final int x, final int y, final int w, final int h, final Object obj, final DataBuffer data)\n
    '''
def setSample():
    '''returns None\n\n
    setSample(final int x, final int y, final int b, final float s, final DataBuffer data)\n
    setSample(final int x, final int y, final int b, final double s, final DataBuffer data)\n
    '''
def getSampleFloat():
    '''returns float\n\n
    getSampleFloat(final int x, final int y, final int b, final DataBuffer data)\n
    '''
def getSampleDouble():
    '''returns double\n\n
    getSampleDouble(final int x, final int y, final int b, final DataBuffer data)\n
    '''
def getPixels():
    '''returns double[]\n\n
    getPixels(final int x, final int y, final int w, final int h, final double[] dArray, final DataBuffer data)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
