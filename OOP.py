class Car_character(object):
    def __init__(self):
        print(' Car classified')

    def what_is_the_car(self):
        print('Passenger car')

    def fuel_type(self):
        print('Gasoline')


class Car(Car_character):                          # car is object
        # Class Object Attribute ( определяется без self.
        # (что то наподобии Видов у флоры и фауны(есть много разных животных:  львы, тигры и тд
        # но все они относятся к виду млекопитающих)))
    classification = 'sedan'

    def __init__(self, brand, country):     # Brand, Country is arguments (arguments(своего рода характеристики
        Car_character.__init__()
        self.brand = brand                  # объекта )
        self.country = country              # def __init__ is method (methods  это функции которые позволяют
                                            # провoдить операции над атрибутами


my_choice = Car('Ford', 'USA')

my_choice.brand
my_choice.country               # выводы атрибутов на экран
my_choice.classification


'''Second example'''


class Circle(object):
    # class object attribute
    pi = 3.14

    def __init__(self, radius=1, perimeter=6.5):
        self.radius = radius
        self.perimeter = perimeter

    def area(self): #radius**2 * pi
        return (self.radius**2) * Circle.pi

    def set_radius(self, new_radius):
        '''
        This radius  takes in radius and resets the current radius of the circle
        '''
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def perimeter(self):
        # circle perimeter is equal 2pi*radius
        return 2 * Circle.pi * self.radius

    def get_perimeter(self):
        return self.perimeter


c = Circle(100)

