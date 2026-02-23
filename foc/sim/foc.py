import unittest
import math

class PidController():

    def __init__(self):
        self.pgain = 1
        self.igain = 1
        self.imax = 100
        self.imin = -100
        self.output_max = 10
        self.output_min = -10
        self.error = 0
        self.setpoint = 0
        self.iterm = 0

    def update(self, feedback):
        self.error = self.setpoint - feedback

        self.pterm = self.pgain * self.error

        self.iterm += self.igain * self.error

        if(self.iterm >= self.imax):
            self.iterm = self.imax
        elif(self.iterm <= self.imin):
            self.iterm = self.imin



class Motor():

    def __init__(self):
        self.ia = 0
        self.ib = 0
        self.ic = 0
        self.current_grabber = None

class Foc():

    def __init__(self, motor, iqreg, idreg):
        self.motor = motor
        self.iqreg = iqreg
        self.idreg = idreg
        self.current_sensor = None

    def update(self):
        pass


def clarke(ia, ib):
    ialpha = ia
    ibeta = (1/math.sqrt(3))*ia + (2/math.sqrt(3))*ib
    return ialpha, ibeta

def park(ialpha, ibeta, sinval, cosval):
    idirect = ialpha*cosval + ibeta * sinval
    iquad = -ialpha*sinval + ibeta*cosval
    return idirect, iquad

def inv_clarke(ialpha, ibeta):
    ialpha = ialpha
    ibeta = -0.5*ialpha + math.sqrt(3)/2*ibeta
    return ialpha, ibeta

def inv_park(idirect, iquad, sinval, cosval):
    ialpha = idirect*cosval - iquad*sinval
    ibeta = idirect*sinval + iquad*cosval
    return ialpha, ibeta

def foc(motor):
    angle_rad = motor.angle_rad

    vq = motor.iqreg.update()
    vd = motor.idreg.update()



class TestFoc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nothing(self):
        self.assertTrue(True)

    def fake_current_grabber(self):
        pass

        # ideally we deliver more current to iq and 0 to id
    def test_maths(self):
        ia = 2
        ib = 3
        ic = 3 # unnecessary
        ialpha, ibeta = clarke(ia, ib)
        print("\n")
        print(ialpha, ibeta)

        sinval = math.sin(1)
        cosval = math.cos(1)

        idirect, iquad = park(ialpha, ibeta, sinval, cosval)
        print("\n")
        print(idirect, iquad)

    def test_motor(self):
        motor = Motor()
        motor.current_grabber = self.fake_current_grabber
        motor.current_grabber()

    def test_foc(self):
        motor = Motor()
        motor.current_grabber = self.fake_current_grabber
        iqreg = PidController()
        idreg = PidController()
        foc = Foc(motor, iqreg, idreg)

if __name__ == '__main__':
    unittest.main()
