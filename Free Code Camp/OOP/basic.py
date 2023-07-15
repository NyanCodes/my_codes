import numpy as np

class Scientist:

    # Create a constructor 
    def __init__(self, reading_speed, writing_speed):
        self.reading_speed = reading_speed
        self.writing_speed = writing_speed

    # Add additional methods 
    def read_paper(self, paper_length):
        return int(paper_length / self.reading_speed)

    def write_paper(self, paper_length):
        return int(paper_length / self.writing_speed)


# this class inherits from the Scientist class
class Phd(Scientist):

    # this overwrites the super clss
    def __init__(self, reading_speed, writing_speed, perc_funding_time_left):

        # call the constructor class of super to set the common variables
        super().__init__(reading_speed, writing_speed)

        # add variable only import for PHD
        self.perc_funding_time_left = perc_funding_time_left

    # additional function just for test, I have no idea what the function does
    def calculate_existential_angst(self, in_pandemic=False):
        if in_pandemic:
            return np.inf - self.perc_funding_time_left
        else:
            return 100 - self.perc_funding_time_left


# Use the pass keyword when you do not want 
# to add any other properties or methods to the class.

nyan = Scientist(reading_speed=2, writing_speed=3)
myo = Scientist(reading_speed=3, writing_speed=0.5)

han = Phd(reading_speed=0.5, writing_speed=0.6, perc_funding_time_left=3)

print(myo.writing_speed)
print(myo.write_paper(paper_length=100))
