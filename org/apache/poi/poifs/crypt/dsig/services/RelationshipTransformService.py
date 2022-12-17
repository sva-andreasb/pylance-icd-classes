TRANSFORM_URI = "String  \"http://schemas.openxmlformats.org/package/2006/RelationshipTransform\""
def ():
    '''returns RelationshipTransformParameterSpec\n\n
    ()\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final TransformParameterSpec params)\n
    init(final XMLStructure parent, final XMLCryptoContext context)\n
    '''
def marshalParams():
    '''returns None\n\n
    marshalParams(final XMLStructure parent, final XMLCryptoContext context)\n
    '''
def getParameterSpec():
    '''returns AlgorithmParameterSpec\n\n
    getParameterSpec()\n
    '''
def transform():
    '''returns Data\n\n
    transform(final Data data, final XMLCryptoContext context)\n
    transform(final Data data, final XMLCryptoContext context, final OutputStream os)\n
    '''
def isFeatureSupported():
    '''returns boolean\n\n
    isFeatureSupported(final String feature)\n
    '''
def addRelationshipReference():
    '''returns None\n\n
    addRelationshipReference(final String relationshipId)\n
    '''
def hasSourceIds():
    '''returns boolean\n\n
    hasSourceIds()\n
    '''
