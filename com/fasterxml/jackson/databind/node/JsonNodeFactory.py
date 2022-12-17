def ():
    '''returns JsonNodeFactory\n\n
    (final boolean bigDecimalExact)\n
    '''
def booleanNode():
    '''returns BooleanNode\n\n
    booleanNode(final boolean v)\n
    '''
def nullNode():
    '''returns NullNode\n\n
    nullNode()\n
    '''
def numberNode():
    '''returns ValueNode\n\n
    numberNode(final byte v)\n
    numberNode(final Byte value)\n
    numberNode(final short v)\n
    numberNode(final Short value)\n
    numberNode(final int v)\n
    numberNode(final Integer value)\n
    numberNode(final long v)\n
    numberNode(final Long v)\n
    numberNode(final BigInteger v)\n
    numberNode(final float v)\n
    numberNode(final Float value)\n
    numberNode(final double v)\n
    numberNode(final Double value)\n
    numberNode(final BigDecimal v)\n
    '''
def textNode():
    '''returns TextNode\n\n
    textNode(final String text)\n
    '''
def binaryNode():
    '''returns BinaryNode\n\n
    binaryNode(final byte[] data)\n
    binaryNode(final byte[] data, final int offset, final int length)\n
    '''
def arrayNode():
    '''returns ArrayNode\n\n
    arrayNode()\n
    arrayNode(final int capacity)\n
    '''
def objectNode():
    '''returns ObjectNode\n\n
    objectNode()\n
    '''
def pojoNode():
    '''returns ValueNode\n\n
    pojoNode(final Object pojo)\n
    '''
def rawValueNode():
    '''returns ValueNode\n\n
    rawValueNode(final RawValue value)\n
    '''
