# Write your code here
def process_data(string_data):
  result = {}
  for item in string_data:
    name, age, *courses = item.split(',')
    result[name] = {
      'age': int(age),
      'courses': courses
    } 
  return result

def average_age(data):
  total_age = 0
  num_students = 0
  for student in data.values():
    total_age += student["age"]
    num_students += 1
  return total_age / num_students

def courses(data):
  result = set()
  for student in data.values():
    result.update(student["courses"])
  return result
  
def most_common_courses(data):
  course_counts = {}
  for student in data.values():
    for course in student['courses']:
      if course not in course_counts.keys():
        course_counts[course] = 0
      course_counts[course] += 1
  max_count = max(course_counts.values())
  return{
    course
    for course in course_counts.keys()
    if course_counts[course] == max_count
  }
  print(course_counts)