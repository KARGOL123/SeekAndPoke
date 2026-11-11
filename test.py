syntaxes = ''
c = 'bomba         s'
syntaxCount = 1
for i in range(syntaxCount):
    if i < syntaxCount - 1:
        syntaxes = syntaxes + c.split(None)[i + 1] + ','
    else:
        syntaxes = syntaxes + c.split(None)[i + 1]

print(syntaxes)