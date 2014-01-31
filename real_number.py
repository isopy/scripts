def men_real(a):
    print "Calculating the actual number of women you've slept with: "
    return a / 2.0

def women_real(a):
    print "Calculating the actual number of men you've slept with: "
    return a * 2.0

print "Type M and press ENTER if you are male, Type F and press enter if you are female"
gender = raw_input("--> ")

print "How many people have you slept with?"  
partners = int(raw_input("--> "))

if gender in ("M", "m"):
    actual_women = men_real(partners)
    print "You've actually slept with %.1f women" % round(actual_women)

elif gender in ("F", "f"):
    actual_men = women_real(partners)
    print "You've actually slept with %.1f men" % round(actual_men)
