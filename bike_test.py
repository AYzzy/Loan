from Class_work.src.Bike.bike import Bike


import unittest

class TestBike(unittest.TestCase):

    def test_that_bike_is_off(self):
        bike = Bike()
        self.assertFalse(bike.power())

    def test_that_bike_is_on(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())

    def test_that_bike_can_be_off_when_is_on(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_when_bike_is_on_and_accelerate_bike_should_be_at_gear_one(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        bike.accelerate()
        self.assertEqual(bike.current_gear(), 1)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_when_bike_is_at_gear_one_the_acceleration_speed_is_1(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        bike.accelerate()
        self.assertEqual(bike.current_gear(), 1)
        bike.accelerate()
        self.assertEqual(bike.current_speed(), 2)
        bike.accelerate()
        self.assertEqual(bike.current_speed(), 3)
        bike.accelerate()
        self.assertEqual(bike.current_speed(), 4)
        bike.accelerate()
        self.assertEqual(bike.current_speed(), 5)

    def test_that_bike_can_accelerate_at_gear_one_and_acceleration_limit_is_20(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(20):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 1)
        self.assertEqual(bike.current_speed(), 20)
        self.assertNotEqual(bike.current_speed(), 1)
        bike.turn_off()
        self.assertFalse(bike.power())


    def test_that_when_bike_speed_is_21_the_gear_should_change_to_2(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 2)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_when_gear_is_2_speed_increment_is_2(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(22):
            bike.accelerate()
        self.assertEqual(bike.current_speed(), 24)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_gear_two_speed_limit_is_30(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(25):
            bike.accelerate()
        self.assertEqual(bike.current_speed(), 30)
        self.assertEqual(bike.current_gear(), 2)
        bike.accelerate()
        self.assertNotEqual(bike.current_gear(), 2)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_gear_when_speed_is_above_30_gear_should_change_to_3(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(26):
            bike.accelerate()
        self.assertEqual(bike.current_speed(), 33)
        self.assertEqual(bike.current_gear(), 3)
        bike.accelerate()
        self.assertEqual(bike.current_speed(), 36)
        self.assertEqual(bike.current_gear(), 3)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_when_bike_is_at_gear_3_speed_increment_is_3(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(26):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 3)
        bike.accelerate()
        self.assertEqual(bike.current_speed(), 36)
        bike.turn_off()
        self.assertFalse(bike.power())


    def test_that_when_bike_speed_is_above_40_gear_should_4(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(30):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 4)


    def test_that_when_bike_is_at_gear_4_speed_increment_is_4(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(30):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 4)
        self.assertEqual(bike.current_speed(), 46)
        bike.accelerate()
        self.assertEqual(bike.current_gear(), 4)
        self.assertEqual(bike.current_speed(), 50)

    def test_that_when_bike_is_off_you_can_accelerate(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.accelerate()
        self.assertEqual(bike.current_gear(), 0)


    def test_that_when_bike_can_decelerate(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(10):
            bike.accelerate()
        bike.decelerate()
        self.assertEqual(bike.current_speed(), 9)

    def test_that_when_bike_is_off_you_can_not_decelerate(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 0)
        self.assertEqual(bike.current_speed(), 0)

    def test_that_when_bike_is_at_gear_one_decelerate_must_be_1(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(10):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 1)
        self.assertEqual(bike.current_speed(), 10)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 1)
        self.assertEqual(bike.current_speed(), 9)

    def test_that_bike_cannot_decelerate_more_than_zero(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        bike.accelerate()
        bike.decelerate()
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 0)
        self.assertEqual(bike.current_speed(), 0)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_when_bike_is_at_gear_two_decelerate_must_be_2(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 2)
        self.assertEqual(bike.current_speed(), 22)
        bike.decelerate()
        self.assertEqual(bike.current_speed(), 20)

    def test_that_when_bike_can_decelerate_from_gear_two_to_gear_one(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(22):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 2)
        self.assertEqual(bike.current_speed(), 24)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 2)
        self.assertEqual(bike.current_speed(), 22)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 1)
        self.assertEqual(bike.current_speed(), 20)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 1)
        self.assertEqual(bike.current_speed(), 19)
        bike.turn_off()
        self.assertFalse(bike.power())


    def test_that_when_bike_is_at_gear_three_decelerate_must_be_3(self):
            bike = Bike()
            self.assertFalse(bike.power())
            bike.turn_on()
            self.assertTrue(bike.power())
            for _ in range(27):
                bike.accelerate()
            self.assertEqual(bike.current_gear(), 3)
            self.assertEqual(bike.current_speed(), 36)
            bike.decelerate()
            self.assertEqual(bike.current_speed(), 33)
            bike.turn_off()
            self.assertFalse(bike.power())


    def test_that_when_bike_can_decelerate_from_gear_three_to_gear_two(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(28):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 3)
        self.assertEqual(bike.current_speed(), 39)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 3)
        self.assertEqual(bike.current_speed(), 36)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 3)
        self.assertEqual(bike.current_speed(), 33)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 2)
        self.assertEqual(bike.current_speed(), 30)
        bike.turn_off()
        self.assertFalse(bike.power())

    def test_that_when_bike_is_at_gear_four_decelerate_must_be_4(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(30):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 4)
        self.assertEqual(bike.current_speed(), 46)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 4)
        self.assertEqual(bike.current_speed(), 42)

    def test_that_when_bike_can_decelerate_from_gear_four_to_gear_three(self):
        bike = Bike()
        self.assertFalse(bike.power())
        bike.turn_on()
        self.assertTrue(bike.power())
        for _ in range(30):
            bike.accelerate()
        self.assertEqual(bike.current_gear(), 4)
        self.assertEqual(bike.current_speed(), 46)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 4)
        self.assertEqual(bike.current_speed(), 42)
        bike.decelerate()
        self.assertEqual(bike.current_gear(), 3)
        self.assertEqual(bike.current_speed(), 38)
        bike.turn_off()
        self.assertFalse(bike.power())
