
def bbb(cuvant):
    consoana = "qwrtzpsdfghjklyxcvbnm"
    vocala = "aeiuo"
    for i in consoana:
        for v in consoana:
            if len(cuvant) > 2:
                if cuvant[-3] == i and cuvant[-1] == v and cuvant[-2] != i:
                    cuvant = cuvant + cuvant[-1] + "ing"
                    return cuvant
    for i in cuvant:
        if cuvant[-2] == "i" and cuvant[-1] == "e":
            cuvant = cuvant[:-2] + "ying"
            return cuvant
    for i in cuvant[-2]:
        for i in cuvant[-1]:
            if i == "e":
                return cuvant + "ing"
    for i in cuvant[-1]:
        if i == "e":
            cuvant = cuvant[:-1] + "ing"
            return cuvant
    else:
        cuvant = cuvant + "ing"
        return cuvant


print(bbb("go"))
print(bbb("fuck"))
print(bbb("die"))
print(bbb("move"))
print(bbb("hug"))
print(bbb("see"))
# If the verb ends in e, drop the e and add -ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, replace ie with y and add -ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding -ing
# By default just add -ing
