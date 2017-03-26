import conversions
import unittest

class KnownValues(unittest.TestCase):
    knownValuesC2K = ((300.0, 573.15), (100.0, 373.15), (0, 273.15), (200.0, 473.15), (98.0, 371.15))
    knownValuesC2F = ((98.0, 208.4), (0, 32.0), (100.0, 212.0), (32.0, 89.6), (200.0, 392.0))
    knownValuesF2C = ((208.4, 98.0), (32.0, 0), (212.0, 100.0), (89.6, 32.0), (392.0, 200.0))
    knownValuesF2K = ((200.0, 366.483), (32.0, 273.15), (0, 255.372), (100.0, 310.928), (55.0, 285.928))
    knownValuesK2F = ((366.0, 199.13), (273, 31.73), (255, -0.67), (310, 98.33), (285, 53.33))
    knownValuesK2C = ((573.15, 300.0), (373.15, 100.0), (273.15, 0.0), (473.15, 200.0), (371.15, 98.0))


    def testCToK(self):
        """should produce known result with know input"""
        for input, output in self.knownValuesC2K:
            result = conversions.convertCelsiusToKelvin(input)
            self.assertEqual(output, result, msg = 'Test converting {}C to Kelvin. Result {}. Expected {}'.format(input, result, output))

    def testCToF(self):
        """should produce known result with know input"""
        for input, output in self.knownValuesC2F:
            result = conversions.convertCelsiusToFahrenheit(input)
            self.assertEqual(output, result, msg = 'Test converting {}C to Fahrenheit. Result {}. Expected {}'.format(input, result, output))

    def testKToF(self):
        """should produce known result with know input"""
        for input, output in self.knownValuesK2F:
            result = conversions.convertKelvinToFahrenheit(input)
            self.assertEqual(output, result, msg = 'Test converting {}K to Fahrenheit. Result {}. Expected {}'.format(input, result, output))

    def testKToC(self):
        """should produce known result with know input"""
        for input, output in self.knownValuesK2C:
            result = conversions.convertKelvinToCelcius(input)
            self.assertEqual(output, result, msg = 'Test converting {}K to Celsius. Result {}. Expected {}'.format(input, result, output))

    def testFToK(self):
        """should produce known result with know input"""
        for input, output in self.knownValuesF2K:
            result = conversions.convertFahrenheitToKelvin(input)
            self.assertEqual(output, result, msg = 'Test converting {}F to Kelvin. Result {}. Expected {}'.format(input, result, output))

    def testFToC(self):
        """should produce known result with know input"""
        for input, output in self.knownValuesF2C:
            result = conversions.convertFahrenheitToCelcius(input)
            self.assertEqual(output, result, msg = 'Test converting {}F to Celsius. Result {}. Expected {}'.format(input, result, output))



if __name__ == "__main__":
    unittest.main()