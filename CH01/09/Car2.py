class Car2:
    """차를 나타내기 위한 간단한 시도"""

    def __init__(self, make, model, year):
        """차를 설명하는 데 사용할 속성을 초기화."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """잘 정리된 설명적인 이름을 반환."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """차의 마일리지를 보여주는 문장을 출력."""
        print(f"이 차는 {self.odometer_reading} 마일 주행했습니다.")

    def update_odometer(self, mileage):
        """
        지정된 값을 주행기록계로 설정.
        주행기록계를 되감으려고 시도하면 변경을 거부.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행기록계를 되감을 수 없습니다!")

    def increment_odometer(self, miles):
        """지정된 양을 주행기록계에 추가."""
        self.odometer_reading += miles
    
my_used_car = Car2('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()