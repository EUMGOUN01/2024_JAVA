class Car2:
    """차를 나타내는 간단한 시도"""

    def __init__(self, make, model, year):
        """차량을 설명"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """차량의 잘 정리된 설명적인 이름을 반환."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """차량의 주행 거리를 출력."""
        print(f"이 차는 {self.odometer_reading} 마일 주행했습니다.")
        
    def update_odometer(self, mileage):
        """주행 거리를 지정된 값으로 업데이트."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행 거리를 되감을 수 없습니다!")
    
    def increment_odometer(self, miles):
        """주행 거리에 지정된 양을 추가."""
        self.odometer_reading += miles

class Battery:
    """전기 자동차의 배터리를 모델링"""
    
    def __init__(self, battery_size=75):
        """배터리의 속성을 초기화."""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력."""
        print(f"이 차는 {self.battery_size}-kWh 배터리를 가지고 있습니다.")

    def get_range(self):
        """이 배터리가 제공하는 주행 가능 거리에 관한 문장을 출력."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"이 차는 전기를 완전히 충전했을 때 약 {range} 마일 갈 수 있습니다.")


class ElectricCar(Car2):
    """전기 자동차의 특성."""
    
    def __init__(self, make, model, year):
        """
        상위 클래스의 속성을 초기화한 후, 전기 자동차에 특화된 속성을 초기화.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력."""
        print(f"이 차는 {self.battery_size}-kWh 배터리를 가지고 있습니다.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()