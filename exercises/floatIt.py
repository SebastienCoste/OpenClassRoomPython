
def floatIt(floatting):
    splt = str(floatting).split(".")
    if len(splt) == 1:
        return floatting
    splt[1] = splt[1][:4]
    return '.'.join(splt)


print(floatIt(2))
print(floatIt(2.5))
print(floatIt(2.33333333))