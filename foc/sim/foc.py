import unittest
import math

class PidController():

    def __init__(self):
        self.pgain = 0
        self.igain = 0
        self.imax = 0
        self.imin = 0
        self.output_max = 0
        self.output_min = 0
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

    class Quantity:
        IA = 0
        IB = 1
        IC = 2
        ANGLE = 3

        def __init__(self):
            pass

    def __init__(self, sensor):
        self.ia = 0
        self.ib = 0
        self.ic = 0
        self.angle_rad = 0
        self.sensor = sensor

    def update(self):
        self.ia = sensor(Quantity.IA)

class Foc():

    def __init__(self, motor, iqreg, idreg):
        self.motor = motor
        self.iqreg = iqreg
        self.idreg = idreg
        self.current_sensor = None



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
    ia = motor.ia
    ib = motor.ib
    ic = motor.ic
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

    def mock_sensor(quantity):
        if(quantity == Motor.Quantity.IA):
            pass
        else:
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

    def test_foc(self):
        motor = Motor()
        iqreg = PidController()
        idreg = PidController()
        foc = Foc(motor, iqreg, idreg)

if __name__ == '__main__':
    unittest.main()
