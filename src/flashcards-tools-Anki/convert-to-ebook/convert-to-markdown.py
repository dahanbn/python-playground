import csv

lesson_file = './Anki-input/Assimil-lecciones.csv'
lesson_dictionary_keys = ["soundfile",
                          "lesson-nr",
                          "sentence-nr",
                          "sentence-foreign",
                          "sentence-translated"]

exercise1_file = './Anki-input/Assimil-ejercicios1.csv'
exercise1_dictionary_keys = ["soundfile",
                             "lesson-nr",
                             "exercise-nr",
                             "exercise-foreign",
                             "exercise-translated"]

exercise2_file = './Anki-input/Assimil-ejercicios2.csv'
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

# setting lesson title for revision lessons
# revision_lesson_foreign = ""

# italian
# revision_lesson_foreign = ""

# spanish
revision_lesson_foreign = "Revisión y notas"

# revision_lesson_translated is always the same
revision_lesson_translated = "Wiederholung und Anmerkungen"

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
        course[current_lesson_nr]['lesson-foreign'] = row['sentence-foreign']
        course[current_lesson_nr]['lesson-translated'] = row['sentence-translated']
    elif row['sentence-nr'] == '0':
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

for row in exercises1:
    pass


sorted_lessons = []

# convert keys from str to int for proper lesson sorting
for key in course.keys():
    sorted_lessons.append(int(key))

sorted_lessons.sort()

for lesson in sorted_lessons:
    # first convert lesson back to string because that's the dictionary key
    lesson_key = str(lesson)
    # setting variables for special contents
    lesson_nr = lesson_key
    lesson_foreign = course.get(lesson_key).get('lesson-foreign')
    lesson_translated = course.get(lesson_key).get('lesson-translated')
    title_foreign = course.get(lesson_key).get('title-foreign')
    title_translated = course.get(lesson_key).get('title-translated')
    print(f"{lesson_foreign} - {lesson_translated}")
    print(f"{title_foreign} - {title_translated}")
