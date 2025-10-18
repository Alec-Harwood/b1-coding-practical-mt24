#Generating the controller for the UUV

class PD_Controller:
    def __init__(self,kp: float, kd: float):

        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def compute_control(self, setpoint: float, measurement: float) -> float:
        error = setpoint - measurement
        difference = (error - self.previous_error)
        control_signal = self.kp * error + self.kd * difference
        self.previous_error = error
        return control_signal