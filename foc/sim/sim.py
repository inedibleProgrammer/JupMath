import unittest


class Timer:
    COUNT_UP = 0
    COUNT_DOWN = 1
    
    def __init__(self):
        self.cnt = 0
        self.arr = 0
        self.ccr1 = 0
        self.ccr2 = 0
        self.ccr3 = 0
        self.count_dir = self.COUNT_UP
        self.oc1ref = 1
        self.oc2ref = 1
        self.oc3ref = 1
        self.oc1 = self.oc1ref
        self.oc2 = self.oc2ref
        self.oc3 = self.oc3ref
        self.oc1n = 0
        self.oc2n = 0
        self.oc3n = 0

    def count(self):
        if(self.count_dir == self.COUNT_UP):
            self.cnt = self.cnt + 1
            if(self.cnt == self.arr):
                self.count_dir = self.COUNT_DOWN

            if(self.cnt < self.ccr1):
                self.oc1ref = 1
            else:
                self.oc1ref = 0

        elif(self.count_dir == self.COUNT_DOWN):
            self.cnt = self.cnt - 1
            if(self.cnt == 0):
                self.count_dir = self.COUNT_UP

            if(self.cnt > self.ccr1):
                self.oc1ref = 0
            else:
                self.oc1ref = 1

        else:
            # some kind of bug
            print("huge bug")
            pass

        # TODO: add deadtime insertion, where BOTH oc1 and oc1n go to
        # 0, then wait for the deadtime, then both are given their
        # values
        self.oc1 = self.oc1ref
        self.oc2 = self.oc2ref
        self.oc3 = self.oc3ref
        self.oc1n = int(not self.oc1)
        self.oc2n = int(not self.oc1)
        self.oc3n = int(not self.oc1)





class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()

    def test_first(self):
        self.assertTrue(self.timer.cnt == 0)
        self.assertTrue(1==1)

    def test_timer_counts_to_arr_and_back_down(self):
        self.timer.arr = 4200
        self.timer.cnt = 4199

        self.timer.count() # 4200
        self.assertTrue(self.timer.cnt == 4200)

        self.timer.count() # 4199
        self.assertTrue(self.timer.cnt == 4199)

        self.timer.count() # 4198
        self.assertTrue(self.timer.cnt == 4198)

    def test_pwm(self):
        # This turned into just some timer math

        # a regular sine wave has a period from [0, 2*pi)
        # in discrete degrees, that would be like [0, 359]
        fpwm = 100
        fclk = 72E6
        ratio = fclk/fpwm
        # print("\n" + str(ratio)) # 720
        prescaler = 719
        ftimer = fclk/(prescaler + 1)
        arr = ftimer/fpwm - 1
        # print("\n" + str(arr)) # 999

    def test_pwm_2(self):
        # This demonstrates following the timing diagram in the
        # reference manual for center aligned pwm
        self.timer.arr = 8
        self.timer.ccr1 = 4

        for i in range(0, 3):
            self.assertTrue(self.timer.oc1ref == 1)
            self.timer.count()
            self.assertTrue(self.timer.oc1ref == 1)

        self.assertTrue(self.timer.cnt == 3)

        for i in range(0, 8):
            self.timer.count()
            self.assertTrue(self.timer.oc1ref == 0)

        self.assertTrue(self.timer.cnt == 5)

        # breakpoint()
        for i in range(0, 3):
            self.timer.count()
            self.assertTrue(self.timer.oc1ref == 1)

    def test_pwm_3(self):
        # I want to figure out when the timer triggers the ADC

if __name__ == '__main__':
    unittest.main()


