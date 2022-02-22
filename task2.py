import  collections
class Markets():
	def __init__(self, name, area, categories):
		self.name = name
		self.area = area
		self.cat = categories
	def __str__(self):
		shop_str= ("Supermaket {0} has an area of {1} m2 and has the following categories: {2}".format( self.name, self.area, ",".join(self.cat)))
		return  shop_str
booze = Markets("Booze", 100, categories=["booze", "more booze"])
print(booze.__class__.__name__)
print(dir(booze))
print(booze.__class__.__eq__)
print(booze.__repr__())
print(booze)
class Classroom():
	def __init__(self, number, capacity, equipment):
		self.number = number
		self.capacity = capacity
		self.equipment = equipment
	def __str__(self):
		class_str= ("Classroom {0} has a capacity of {1} persons and has the following equipment: {2}.".format( self.number, self.capacity, ",".join(self.equipment)))
		return  class_str
	def is_larger(self, other_classroom):
		return  self.capacity > other_classroom.capacity
	def equipment_differences(self, other_classroom):
		diff_list = []
		for eq in self.equipment:
			if eq not in other_classroom.equipment:
				diff_list.append(eq)
		return  diff_list
classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
print(classroom_016.is_larger(classroom_007))
print(classroom_016.equipment_differences(classroom_007))
class AcademicBuilding():
	def __init__(self, address, classrooms):
		self.address = address
		self.classrooms = classrooms
	def __str__(self):
		lines = []
		#lassroom_map = (map(, self.classrooms))
		lines.append(self.address)
		for classroom in self.classrooms:
			lines.append(classroom.__str__())
		all_rooms = "\n".join(lines)
		return all_rooms
	def total_equipment(self):
		all_eq = []
		for classroom in classrooms:
			all_eq += classroom.equipment
			
		occurances = collections.Counter(all_eq)
		all_occ_view = occurances.items()
		all_occ_list = list(all_occ_view)
		all_occ_list.sort()
		return  all_occ_list
classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
b = AcademicBuilding("a", classrooms)
print(building)
for i in building.classrooms:
		print(i)
x= [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
x.sort()
print(x)
print(building.total_equipment())
