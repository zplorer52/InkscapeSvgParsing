from lxml import etree
    
def getellipseAttrib(treesSvgfile, id, attrib='@*', namespaces={'n': "http://www.w3.org/2000/svg"}):
    """
    :param treesSvgfile: lxml.etree.parse('.svg')
    :param id: ['id14K5_Q1_4-8']
    :param attrib: '@*', '@style', '@cx', '@cy', '@rx', '@ry'
    :param namespaces: {'n': "http://www.w3.org/2000/svg"}
    :return: list of attribute values
    """
    sttr = "//n:ellipse[@id='"+id +"']"+'/'+attrib
    ec = treesSvgfile.xpath(sttr, namespaces=namespaces)
    return ec

# Generalized version
def getAttrib(ptree, object, id, attrib='@*', namespaces={'n': "http://www.w3.org/2000/svg"}):
    sttr = "//n:"+object+"[@id='" + id + "']" + '/' + attrib
    ec = ptree.xpath(sttr, namespaces=namespaces)
    return ec
    
ifilename = "HVTurboV2.svg"
with open( ifilename, 'r') as infile:
    tree = etree.parse(infile) 

# print(getellipseAttrib(tree, 'id14K5_Q1_4-8'))
# print(getAttrib(tree,'text', 'text4487-8-3-0'))
print(getAttrib(tree,'tspan', 'tspan8261'))
