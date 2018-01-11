class MathDojo( object ):
    def __init__( self, result = 0 ):
        self.result = result

    def add( self, *args ):
        for item in args:
            if isinstance( item, list ):
                self.result += sum (item)
            else:
                self.result += item
        return self

    def subtract( self, *args ):
        for item in args:
            if isinstance( item, list ):
                self.result -= sum (item)
            else:
                self.result -= item
        return self

md = MathDojo()

# print md.add(2).add(2,5).subtract(3,2).result

print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result