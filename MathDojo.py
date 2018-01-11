class MathDojo( object ):
    def __init__( self, result = 0 ):
        self.result = result

    def add( self, *args ):
        self.result += sum( args )
        # print "add", sum (args)
        # print "current result", self.result
        return self

    def substract( self, *args ):
        self.result -= sum( args )
        # print "substract", sum(args)
        # print "current result", self.result
        return self

md = MathDojo()

print md.add(2).add(2,5).substract(3,2).result