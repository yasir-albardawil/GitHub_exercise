class Udacian:
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

        print('Name: ' + self.name)
        print('City: ' + self.city)
        print('Enrollment: ' + self.enrollment)
        print('Nanodegree: ' + self.nanodegree)
        print('Status: ' + self.status)
        
Udacian('name', 'city', 'enrollment', 'nanodegree', 'status')


