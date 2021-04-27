                            #### CSV ####

# During this course, you'll learn how to use the csv module provided by the Python Standard Library.
# However, for commercial projects, we recommend using an excellent library called PANDAS.

    # READING DATA FROM CSV #
# The Python Standard Library offers a module called csv that provides functions for reading and writing data in CSV format.
# Reading data is done using the reader object, while writing is done using the writer object.

    # THE READER OBJECT #
# The reader function returns an object that allows you to iterate over each line in the CSV file.
# To create it, we need to pass a file object to the reader function. 
# For this purpose, we can use a built-in function called open

# EXAMPLE:

import csv

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
print()
# output:
# ['Name', 'Phone']
# ['mother', '222-555-101']
# ['father', '222-555-102']
# ['wife', '222-555-103']
# ['mother-in-law', '222-555-104']

    # READING DATA PART-2 #
# Finally, we read each row using the for loop. Note that a single line is returned as a list of strings.
# However, more readable results can be obtained, e.g., by using the join method.

# EXAMPLE:

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(','.join(row))
print()

# output:
# Name, Phone
# mother, 222-555-101
# father, 222-555-102
# wife, 222-555-103
# mother-in-law, 222-555-104

# NOTE: The newline='' argument added to the open function protects us from incorrect interpretation of the 
    # newline character on different platforms.

    # READING DATA PART-3 #
# The csv module provides a more convenient way to read data, in which each line is mapped to an OrderedDict object.
# To achieve this, we must use the DictReader class in the way we show in the editor.

# EXAMPLE:

with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], ':', row['Phone'])
print()

# output:
# mother : 222-555-101
# father : 222-555-102
# wife : 222-555-103
# mother-in-law : 222-555-104


    # READING DATA PART-4 #
# Like the reader function, the DictReader class accepts a file object as an argument. It treats the first line of the file as a header 
    # from which to read the keys. If your file doesn't have a header, you must define it using the fieldnames argument.

# EXAMPLE:

with open('contacts.csv', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row['Name'], row['Phone'])
print()

# output:
# Name Phone
# mother 222-555-101
# father 222-555-102
# wife 222-555-103
# mother-in-law 222-555-104

# NOTE: If you define more column names than the values in the file, the missing values will be None.

