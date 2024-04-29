class Students:
    def __init__(im, name, age, group, average_mark):
        im.name = name
        im.age = age
        im.group = group
        im.average_mark = average_mark

        im.sch_grade_max = 5
        im.sch_threshold = 4
        im.sch_low = 4000
        im.sch_high = 6000
    
    def get_name(im):
        return im.name

    def get_age(im):
        return im.age

    def __str__(im):
        return "Name: " + str(im.get_name()) + ", age: " + str(im.get_age()) + ", scholarship: " + str(im.get_scholarship())
    
    def get_scholarship(im):
        if im.average_mark == im.sch_grade_max:
            return im.sch_high
        elif im.average_mark > im.sch_threshold:
            return im.sch_low
        else:
            return 0
        
    def compare_scholarship(im, obj):
        return im.get_scholarship() > obj.get_scholarship()
		
class Aspirants(Students):
    def __init__(im, name, age, group, average_mark, thesis):
        super().__init__(name, age, group, average_mark)
        im.thesis = thesis
        im.sch_low = 6000
        im.sch_high = 8000

    def __str__(im):
        return super().__str__() + ", thesis: " + str(im.thesis)
		
st1 = Students("Максим", 34, 1049, 5)
print(st1)

st1.average_mark = 4.5
print(st1)

st1.average_mark = 4
print(st1)

st2 = Aspirants("Виталий", 45, 1043, 5, "Влияние русских народных музыкальных кнопочных инструментов на развитие религиозно-философской мысли России конца ХVIII начала ХХ века")
print(st2)

st2.average_mark = 4.5
print(st1.compare_scholarship(st2))
print(st2)

st2.average_mark = 4
print(st2)