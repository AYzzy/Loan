from Class_work.src.Air_Conditioner.ac import AirConditioner

import unittest
class TestAirConditioner(unittest.TestCase):

    def test_that_ac_is_off(self):
        ac = AirConditioner()
        self.assertFalse(ac.power())

    def test_that_ac_is_on(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.power())

    def test_that_ac_is_on_and_can_be_off(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.power())
        ac.turn_off()
        self.assertFalse(ac.power())

    def test_that_ac_temperature_default_state_is_16(self):
        ac = AirConditioner()
        ac.turn_on()
        ac.turn_on()
        self.assertTrue(ac.power())
        self.assertEqual(ac.current_temperature(), 16)


    def test_that_ac_temperature_can_increased(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.power())
        ac.increase()
        self.assertEqual(ac.current_temperature(), 17)

    def test_that_ac_temperature_can_not_increased_beyond_30(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.power())
        for _ in range(14):
            ac.increase()
        self.assertEqual(ac.current_temperature(), 30)
        ac.increase()
        self.assertEqual(ac.current_temperature(), 30)

    def test_that_ac_temperature_can_not_increase_when_ac_is_off(self):
        ac = AirConditioner()
        self.assertFalse(ac.power())
        ac.increase()
        self.assertEqual(ac.current_temperature(), 0)


    def test_that_ac_temperature_can_decrease_when_ac_is_on(self):
        ac = AirConditioner()
        self.assertFalse(ac.power())
        ac.turn_on()
        self.assertTrue(ac.power())
        for _ in range(5):
            ac.increase()
        self.assertEqual(ac.current_temperature(), 21)
        ac.decrease()
        self.assertEqual(ac.current_temperature(), 20)
        ac.turn_off()
        self.assertFalse(ac.power())

    def test_that_ac_temperature_can_not_decrease_when_ac_is_off(self):
        ac = AirConditioner()
        self.assertFalse(ac.power())
        ac.decrease()
        self.assertEqual(ac.current_temperature(), 0)


    def test_that_ac_temperature_can_not_decrease_less_tha_16(self):
        ac = AirConditioner()
        self.assertFalse(ac.power())
        ac.turn_on()
        self.assertTrue(ac.power())
        self.assertEqual(ac.current_temperature(), 16)
        for _ in range(3):
            ac.increase()
        self.assertEqual(ac.current_temperature(), 19)
        ac.decrease()
        self.assertEqual(ac.current_temperature(), 18)
        ac.decrease()
        self.assertEqual(ac.current_temperature(), 17)
        ac.decrease()
        self.assertEqual(ac.current_temperature(), 16)
        ac.decrease()
        self.assertEqual(ac.current_temperature(), 16)
        ac.turn_off()
        self.assertFalse(ac.power())