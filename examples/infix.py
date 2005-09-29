import sys
sys.path.append('src')
sys.path.append('../src')

try:
    from mathml.termparser import *
    from mathml.mathdom    import *
except ImportError:
    # Maybe we are still before installation?
    from mathdom    import MathDOM
    from termparser import *
    from xmlterm    import *

print "Please enter an infix term or leave empty to proceed with an example term."
try:
    term = raw_input('# ')
except EOFError:
    sys.exit(0)

if not term:
    term = ".1*pi+2*(1+3i)-5.6-6*-1/sin(-45*a.b) * CASE WHEN 3|12 THEN 1+3 ELSE e^(4*1) END + 1"
    term = "%(term)s = 1 or %(term)s > 5 and true" % {'term':term}


print "ORIGINAL:"
print term
print

try:
    try:
        doc = MathDOM.fromMathmlSax(term, TermSaxParser())
    except ParseException:
        doc = MathDOM.fromMathmlSax(term, BoolExpressionSaxParser())
except ParseException:
    print "The term is not parsable, neither as arithmetic term not as boolean expression."
    sys.exit(0)
    

print "MATHML:"
doc.toMathml(indent=True)
print

print "AST:"
tree = dom_to_tree(doc)
print tree
print

print "INFIX:"
print infixof(tree)
print

print "PREFIX  :"
print prefixof(tree)
print

print "POSTFIX:"
print postfixof(tree)
print