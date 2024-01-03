class TimeKeeper:
    def __init__(self, hours: int, minutes: int) -> None: # ->None -t magától odarakta
        """
        if hours < 0:
            raise ValueError("Hours must be positive")
        if minutes < 0:
            raise ValueError("Minutes must be positive")
        """
        assert hours >= 0, "Hours must be positive"
        assert minutes >= 0, "Minutes must be positive"
        
        if minutes > 60:
            hours += minutes // 60
            minutes = minutes % 60
        self.hours = hours
        self.minutes = minutes
    
    def add_time(self, given_hours: int, given_minutes: int) -> None:
        if self.minutes + given_minutes < 60:
            self.hours += given_hours
            self.minutes += given_minutes
        else:
            self.hours += ((self.minutes + given_minutes) // 60) + given_hours
            self.minutes = (self.minutes + given_minutes) % 60
    
    def __str__(self) -> str:
        # ez is jó, de
        if self.hours < 10:
            str_h = f"0{self.hours}"
        else:
            str_h = str(self.hours)
        if self.minutes < 10:
            str_m = f"0{self.minutes}"
        else:
            str_m = str(self.minutes)
        
        # ez szebb: Google: Python leading zeros
        # https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
        # int -> str
        # 1 -> "01"
        # 10 -> "10"
        str_h = f"{self.hours:02d}"
        str_m = f"{self.minutes:02d}"

        return str_h + ":" + str_m
    
    def __eq__(self, other) -> bool:
        if self.__str__() == other.__str__():
            return True
        else:
            return False


    


if __name__ == "__main__":
    time1 = TimeKeeper(-2, 30)
    time1.add_time(1, 45)
    print(time1)  # Kimenet: 04:15

    time2 = TimeKeeper(3, 50)
    time2.add_time(0, 25)
    print(time2)  # Kimenet: 04:15
    print(time1 == time2)  # Kimenet: True