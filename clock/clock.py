class Clock:
    def __init__(self, hour, minute):
        self.minute=(hour*60+minute)%(24*60)

    def __repr__(self):
        return f'{self.minute//60:02d}:{self.minute%60:02d}'

    def __eq__(self, other):
        return self.minute==other.minute

    def __add__(self, minutes):
        return Clock(0,self.minute+minutes)

 
