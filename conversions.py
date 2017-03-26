def convertCelsiusToKelvin(c):
    K = c + 273.15
    return K

def convertCelsiusToFahrenheit(c):
    F = (c * 1.8) + 32
    return F

def convertFahrenheitToKelvin(f):
    K = (f + 459.67) * (0.5555555555555556)
    return round(K, 3)

def convertFahrenheitToCelcius(f):
    C = (f - 32) * (0.5555555555555556)
    return round(C, 3)

def convertKelvinToFahrenheit(k):
    F = k * 1.8 - 459.67
    return round(F, 2)

def convertKelvinToCelcius(k):
    C = k - 273.15
    return C