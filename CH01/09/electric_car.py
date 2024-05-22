class Car2:
    """차를 나타내기 위한 간단한 시도"""

    def __init__(self, make, model, year):
        """차량을 설명하는 데 사용할 속성을 초기화."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """잘 정리된 설명적인 이름을 반환."""
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

class ElectricCar(Car2):
    """전기 자동차의 특징."""
    
    def __init__(self, make, model, year):
        """
        상위 클래스의 속성을 초기화한 후, 전기 자동차에 특화된 속성을 초기.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력."""
        print(f"이 차는 {self.battery_size}-kWh 배터리를 가지고 있습니다.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()