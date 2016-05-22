class A(object):
    def foo(self):
        print 'A'
        print 'end A'
class B(A):
    def foo(self):
        print 'B'
        print 'and'
        super(B, self).foo()
        print 'end B'
class C(A):
    def foo(self):
        print 'C'
        print 'and'
        super(C, self).foo()
        print 'end C'
class D(B,C):
    def foo(self):
        print 'D'
        print 'AND'
        super(D, self).foo()
        print 'end D'

d = D()
d.foo()