# data_file = "majorcourses (1).unl"

# with open('fixed_input', 'w') as output:
#     output.write('{\n')
#     with open(data_file, 'r') as data:
#         for line in data.readlines():
#             line = line.replace("\n", "")
#             elems = line.split("|")
#             class_id = '"{}"'.format(elems[0])
#             output.write("  {}: ".format(class_id))
#             classes = ['"{}"'.format(elem) for elem in elems[1:]]
#             output.write("[{}], \n".format(', '.join(classes)))
#     output.write('}')



data_file = "majorcourses (1).unl"

with open('major_courses.json', 'w') as output:
    output.write('{\n')
    with open(data_file, 'r') as data:
        for line in data.readlines():
            line = line.replace("\n", "")
            elems = line.split("|")
            
            class_id = elems[0]
            major = elems[1]
            desc = elems[2]
            #Get department from class and from major
            temp_class = elems[0].split(" ")
            class_dept = temp_class[0]

            temp_dept = elems[1].split("-")
            major_dept = temp_dept[0]


            output.write('  "{}": {}\n'.format(class_id, "{"))
            output.write('    "class_dept":"{}",\n'.format(class_dept))
            output.write('    "major_dept":"{}",\n'.format(major_dept))
            output.write('    "major":"{}",\n'.format(major))
            output.write('    "description": "{}"\n'.format(desc))
            output.write('  },\n')
    output.write('}')
