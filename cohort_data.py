"""Functions to parse a file containing student data."""

def load_data(filename):
    """Open the file and tokenize the data to return a dictionary of each person
    
    Helper function to reuse throughout the document so as to avoid repeting tokenizing the data."""

    persons = []
    with open(filename) as cohort_data:
        for line in cohort_data:
            person_data = line.strip().split("|")
            person = {
                'firstname': person_data[0],
                'lastname': person_data[1],
                'fullname': "{} {}".format(person_data[0], person_data[1]),
                'house': person_data[2],
                'advisor': person_data[3],
                'cohort': person_data[4],
            }
            persons.append(person)
        return persons

def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    persons = load_data(filename)
    houses = set()
    for person in persons:
        if person["cohort"] != "G" and person["cohort"] != "I": 
            houses.add(person["house"])
    return houses

def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    persons = load_data(filename)

    for person in persons:

        if person["cohort"] != 'I' and person["cohort"] != 'G' and cohort == 'All':
            students.append(person["fullname"])
        elif person["cohort"] != 'I' and person["cohort"] != 'G' and cohort == person["cohort"]:
            students.append(person["fullname"])

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    persons = load_data(filename)

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for person in persons: 
        if person["house"] == "Gryffindor":
            gryffindor.append(person["fullname"])
        elif person["house"] == "Dumbledore's Army":
            dumbledores_army.append(person["fullname"])
        elif person["house"] == "Hufflepuff":
            hufflepuff.append(person["fullname"])
        elif person["house"] == "Ravenclaw":
            ravenclaw.append(person["fullname"])
        elif person["house"] == "Slytherin":
            slytherin.append(person["fullname"])
        elif person["cohort"] == "G":
            ghosts.append(person["fullname"])
        elif person["cohort"] == "I":
            instructors.append(person["fullname"])

    full_roster = [sorted(dumbledores_army), 
                   sorted(gryffindor), 
                   sorted(hufflepuff), 
                   sorted(ravenclaw), 
                   sorted(slytherin), 
                   sorted(ghosts), 
                   sorted(instructors)]
    
    return full_roster


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    persons = load_data(filename)
    for person in persons:
        all_data.append((person["fullname"], person["house"], person["advisor"], person["cohort"]))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    persons = load_data(filename)
    
    for person in persons:
        if person["fullname"] == name:
            return person["cohort"]

    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    persons = load_data(filename)
    all_lastnames = []

    for person in persons:
        all_lastnames.append(person["lastname"]) # gives a list of all last names 
    
    lastn_dict = {}

    for lname in all_lastnames:
        lastn_dict[lname] = all_lastnames.count(lname) # fills a dictionary with all last names pointing to the number of instances
    
    duplicates = set()
    
    for lname in lastn_dict: # finds only duplicate names and adds them to a set
        if lastn_dict[lname] > 1:
            duplicates.add(lname)

    return duplicates
    

def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    persons = load_data(filename)

    # find the target person's data 
    for person in persons:
        if name == person["fullname"]:
            target_cohort = person["cohort"]
            target_house = person["house"]
            break
    
    housemates = set()
    for person in persons:
        if person["house"] == target_house and person["cohort"] == target_cohort:
            housemates.add(person["fullname"])

    housemates.remove(name)

    return housemates



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
