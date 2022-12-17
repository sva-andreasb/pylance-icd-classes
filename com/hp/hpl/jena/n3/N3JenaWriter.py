propWriterName = "String  \"http://jena.hpl.hp.com/n3/properties/writer\""
n3Writer = "String  \"N3\""
n3WriterPrettyPrinter = "String  \"N3-PP\""
n3WriterPlain = "String  \"N3-PLAIN\""
n3WriterTriples = "String  \"N3-TRIPLES\""
n3WriterTriplesAlt = "String  \"N3-TRIPLE\""
turtleWriter = "String  \"TURTLE\""
turtleWriterAlt1 = "String  \"Turtle\""
turtleWriterAlt2 = "String  \"TTL\""
def ():
    '''returns N3JenaWriter\n\n
    ()\n
    (final N3JenaWriterCommon w)\n
    '''
def write():
    '''returns None\n\n
    write(final Model model, final Writer out, final String base)\n
    write(final Model model, final OutputStream out, final String base)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String propName, final Object propValue)\n
    '''
def setErrorHandler():
    '''returns RDFErrorHandler\n\n
    setErrorHandler(final RDFErrorHandler errHandler)\n
    '''
