import unittest
import temp_tracker

class TestTempTracker(unittest.TestCase):

    def tearDown(self) -> None:
        temp_tracker.Temperatures=[];

    #Entering a too low temperature
    def test_temp_insert_lower(self):
        with self.assertRaises(ValueError) as context: 
            temp_tracker.insert(-1)
        self.assertTrue('Temperature wasnt between 0 and 110 F' in str(context.exception))

    #Entering a too high temperature
    def test_temp_insert_higher(self):
        with self.assertRaises(ValueError) as context: 
            temp_tracker.insert(120)
        self.assertTrue('Temperature wasnt between 0 and 110 F' in str(context.exception))

    #Entering a correct temperature on a border (0 and 110)
    def test_temp_insert_border(self):
        temp_tracker.insert(0)
        self.assertEqual(temp_tracker.Temperatures, [0],"Should be [0]")

    #Entering a correct temperature
    def test_temp_insert_correct(self):
        temp_tracker.insert(30)
        self.assertEqual(temp_tracker.Temperatures, [30],"Should be [30]")
    
    #Checking Max of temperatures when theres only one maximum
    def test_temp_max_single(self):
        temp_tracker.insert(30)
        temp_tracker.insert(40)
        self.assertEqual(temp_tracker.get_max(), 40,"Should be 40")

    #Checking Max of temperatures when theres two maximum
    def test_temp_max_multiple(self):
        temp_tracker.insert(30)
        temp_tracker.insert(40)
        temp_tracker.insert(40)
        self.assertEqual(temp_tracker.get_max(), 40,"Should be 40")
    
    #Checking Min of temperatures when theres only one minimum
    def test_temp_min_single(self):
        temp_tracker.insert(30)
        temp_tracker.insert(40)
        self.assertEqual(temp_tracker.get_min(), 30,"Should be 30")
    
    #Checking Min of temperatures when theres two minimum
    def test_temp_min_multiple(self):
        temp_tracker.insert(30)
        temp_tracker.insert(30)
        temp_tracker.insert(40)
        self.assertEqual(temp_tracker.get_min(), 30,"Should be 30")
    
    #Checking Mean of temperatures when the answer is a round
    def test_temp_mean_round(self):
        temp_tracker.insert(25)
        temp_tracker.insert(30)
        temp_tracker.insert(35)
        self.assertEqual(temp_tracker.get_mean(), 30,"Should be 30")

    #Checking Mean of temperatures when the answer is not round
    def test_temp_min_multiple(self):
        temp_tracker.insert(30)
        temp_tracker.insert(35)
        self.assertEqual(temp_tracker.get_mean(), 32.5,"Should be 32.5")

if __name__ == '__main__':
    unittest.main()