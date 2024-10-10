import unittest
from Class_work.src.Television.television import Television


class MyTestCase(unittest.TestCase):

    def setUp(self):
        television = Television()


    def test_that_television_is_off(self):
        television = Television()
        self.assertFalse(television.power())


    def test_that_television_can_be_on(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())

    def test_that_television_can_be_on_and_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_television_have_default_channel_number_when_is_on(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_television_can_set_channel_number_when_is_on(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        television.set_channel(5)
        self.assertEqual(television.get_channel(), 5)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_television_can_not_set_channel_number_when_not_on(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        television.set_channel(90)
        self.assertEqual(television.get_channel(), 90)
        television.turn_off()
        self.assertFalse(television.power())
        television.set_channel(90)
        self.assertRaises(ValueError, television.get_channel)


    def test_that_television_can_not_set_channel_number_not_more_than_100(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        television.set_channel(90)
        self.assertEqual(television.get_channel(), 90)
        self.assertRaises(ValueError, television.set_channel, 101)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_televison_can_not_set_channel_not_less_than_1(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertRaises(ValueError, television.set_channel, 0)
        self.assertRaises(ValueError, television.set_channel, -1)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_televison_have_a_default_volume_of_when_turn_on(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_volume_can_be_change_to_any_number(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.set_volume(7)
        self.assertEqual(television.get_volume(), 7)
        television.set_volume(9)
        self.assertEqual(television.get_volume(), 9)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_volume_can_not_exceed_10(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertNotEqual(television.get_volume(), 10)
        self.assertEqual(television.get_volume(), 2)
        television.set_volume(10)
        self.assertEqual(television.get_volume(), 10)
        self.assertRaises(ValueError, television.set_volume, 11)
        television.set_volume(9)
        self.assertEqual(television.get_volume(), 9)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_volume_can_not_be_less_than_one(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.set_volume(9)
        self.assertEqual(television.get_volume(), 9)
        self.assertRaises(ValueError, television.set_volume, -1)
        television.set_volume(1)
        self.assertEqual(television.get_volume(), 1)
        self.assertRaises(ValueError, television.set_volume, -1)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_volume_can_not_be_set_when_televison_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())
        self.assertRaises(ValueError, television.set_volume, 9)


    def test_that_channel_can_be_up_by_one_step(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.channel_up()
        self.assertEqual(television.get_channel(), 2)
        television.channel_up()
        self.assertEqual(television.get_channel(), 3)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_channel_can_not_move_more_than_one_step(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.channel_up()
        self.assertEqual(television.get_channel(), 2)
        television.channel_up()
        self.assertNotEqual(television.get_channel(), 4)
        television.turn_off()
        self.assertFalse(television.power())

    def test_that_channel_can_not_pass_hundred(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.channel_up()
        self.assertEqual(television.get_channel(), 2)
        television.set_channel(99)
        self.assertEqual(television.get_channel(), 99)
        television.channel_up()
        self.assertEqual(television.get_channel(), 100)
        television.channel_up()
        self.assertEqual(television.get_channel(), 100)

    def test_channel_can_not_increase_when_tv_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.channel_up()
        self.assertRaises(ValueError, television.get_channel)

    def test_that_channel_can_go_backward(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.channel_up()
        self.assertEqual(television.get_channel(), 2)
        television.channel_down()
        self.assertEqual(television.get_channel(), 1)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_channel_can_not_go_back_beyond_1(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.channel_down()
        self.assertRaises(ValueError, television.channel_down)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_channel_down_will_not_work_tv_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertRaises(ValueError, television.channel_down)


    def test_that_volume_can_increase_by_one_step(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.volume_up()
        self.assertEqual(television.get_volume(), 3)
        television.turn_off()
        self.assertFalse(television.power())


    def test_that_volume_increase_will_not_pass_10(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.set_channel(10)
        self.assertEqual(television.get_channel(), 10)
        television.volume_up()
        television.volume_up()
        self.assertEqual(television.get_channel(), 10)
        television.turn_off()
        self.assertFalse(television.power())

    def test_that_volume_will_not_increase_when_tv_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())
        self.assertRaises(ValueError, television.volume_up)

    def test_that_volume_will_decrease_by_one_step(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.set_volume(8)
        self.assertEqual(television.get_volume(), 8)
        television.volume_down()
        self.assertEqual(television.get_volume(), 7)
        television.turn_off()
        self.assertFalse(television.power())

    def test_that_volume_will_not_decrease_less_than_1(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.volume_down()
        self.assertEqual(television.get_volume(), 1)

    def test_that_volume_will_will_not_decrease_when_tv_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television. turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())
        self.assertRaises(ValueError, television.volume_down)

    def test_that_tv_can_mute_volume_turns_0(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.mute()
        self.assertEqual(television.get_volume(), 0)
        television.turn_off()
        self.assertFalse(television.power())

    def test_that_mute_function_will_not_work_when_tv_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())
        self.assertRaises(ValueError, television.mute)


    def test_that_unmute_function_will_return_the_initial_state_of_the_volume(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.mute()
        self.assertEqual(television.get_volume(), 0)
        television.unmute()
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())

    def test_that_unmute_will_not_work_when_tv_is_off(self):
        television = Television()
        self.assertFalse(television.power())
        television.turn_on()
        self.assertTrue(television.power())
        self.assertEqual(television.get_channel(), 1)
        self.assertEqual(television.get_volume(), 2)
        television.turn_off()
        self.assertFalse(television.power())
        self.assertRaises(ValueError, television.unmute)

