import hfst

tr1 = hfst.regex('foo:bar')
tr2 = hfst.regex('bar:baz')
tr1.compose(tr2)
print(tr1)
