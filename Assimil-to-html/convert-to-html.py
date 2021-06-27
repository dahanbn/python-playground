import csv

lesson_file = 'Assimil-to-html/Assimil-lecciones.csv'
lesson_dictionary_keys = ["soundfile",
                          "lesson-nr",
                          "sentence-nr",
                          "sentence-foreign",
                          "sentence-translated"]

exercise1_file = 'Assimil-to-html/Assimil-ejercicios1.csv'
exercise1_dictionary_keys = ["soundfile",
                             "lesson-nr",
                             "exercise-nr",
                             "exercise-foreign",
                             "exercise-translated"]

exercise2_file = 'Assimil-to-html/Assimil-ejercicios2.csv'
exercise2_dictionary_keys = ["exercise-foreign",
                             "exercise-translated"
                             "lesson-nr",
                             "exercise-nr"]

lessons = []
exercises1 = []
exercises2 = []


print(f"Parsing lesson file: {lesson_file}")
with open(lesson_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=lesson_dictionary_keys)
    for row in reader:
        lessons.append(row)

print(f"Parsing exercise 1 file: {exercise1_file}")
with open(exercise1_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=exercise1_dictionary_keys)
    for row in reader:
        exercises1.append(row)

print(f"Parsing exercise 2 file: {exercise2_file}")
with open(exercise2_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=exercise2_dictionary_keys)
    for row in reader:
        exercises2.append(row)

current_lesson_nr = "0"

course = {}

for row in lessons:
    # test for new lesson, each new lesson contains in the first line
    # with the sentence-nr 0a the lesson name in both languages

    # checking for a new lesson
    if row['lesson-nr'] != current_lesson_nr:
        current_lesson_nr = row['lesson-nr']
        # create a new dictionary for the new lesson
        course[current_lesson_nr] = {'lesson-nr': current_lesson_nr}
        # create an empty list of sentences
        course[current_lesson_nr]['sentences'] = []
    # addding lesson title    
    if row['sentence-nr'] == '0a':
        course[current_lesson_nr]['title-foreign'] = row['sentence-foreign']
        course[current_lesson_nr]['title-translated'] = row['sentence-translated']
    else:
        # adding lesson sentences
        sentence = {
            'sentence-nr': row['sentence-nr'],
            'sentence-foreign': row['sentence-foreign'],
            'sentence-translated': row['sentence-translated']
                }
        course[current_lesson_nr]['sentences'].append(sentence)


print(course['1'])

keys = list(course.keys())

keys.sort()


