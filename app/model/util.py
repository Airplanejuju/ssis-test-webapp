# Function to generate a code based on the selected college
def gencode_college(college):
    # Define mappings of preset codes for colleges and courses
    college_codes = {
        'College of Engineering': 'COE',
        'College of Arts and Social Sciences': 'CASS',
        'College of Economics and Business Administration': 'CEBA',
        'College of Education': 'CED',
        'College of Health Sciences': 'CHS',
        'College of Science and Mathematics': 'CSM',
        'College of Computer Studies': 'CCS'
    }

    return college_codes.get(college, 'COL')  # Default to 'COL' if not found

# Function to generate college based on the code
def generate_college(college):
    college_codes = {
        'COE': 'College of Engineering',
        'CASS': 'College of Arts and Social Sciences',
        'CEBA': 'College of Economics and Business Administration',
        'CED': 'College of Education',
        'CHS': 'College of Health Sciences',
        'CSM': 'College of Science and Mathematics',
        'CCS': 'College of Computer Studies'
    }

    return college_codes.get(college, 'COL')  # Default to 'COL' if not found

# Function to generate a code based on the selected course
def gencode_course(course):
    course_codes = {
        # College of Engineering
        'Bachelor of Science in Metallurgical Engineering' : 'BSMetE',
        'Bachelor of Science in Computer Engineering' : 'BSCpE',
        'Bachelor of Science in Electronics and Communication Engineering': 'BSECE',
        'Bachelor of Science in Mechanical Engineering' : 'BSME',
        'Bachelor of Science in Chemical Engineering': 'BSChE',
        'Bachelor of Science in Civil Engineering' : 'BSCE',
        'Bachelor of Science in Industrial Automation and Mechatronics' : 'BSIAM',
        'Bachelor of Science in Ceramics Engineering' : 'BSCerE',
        'Bachelor of Science in Mining Engineering' : 'BSMiningE',
        'Bachelor of Science in Electrical Engineering' : 'BSEE',
        'Bachelor of Science in Environmental Engineering' : 'BSEnvE',
        # College of Arts and Social Sciences
        'Bachelor of Arts in English Language Studies' : 'BAELS',
        'Bachelor of Arts in Literary and Culture Studies' : 'BALCS',
        'Bachelor of Arts in Filipino' : 'BAF',
        'Bachelor of Arts in History' : 'BAH',
        'Bachelor of Arts in Panitikan' : 'BAP',
        'Bachelor of Arts in Political Science' : 'BAPS',
        'Bachelor of Arts in Psychology' : 'BAPsy',
        'Bachelor of Arts in Sociology' : 'BASoc',
        'Bachelor of Science in Philosophy': 'BSPhil',
        'Bachelor of Science in Psychology': 'BSPsy',
        # College of Economics and Business Administration
        'Bachelor of Science in Accountancy': 'BSA',
        'Bachelor of Science in Economics': 'BSE',
        'Bachelor of Science in Business Administration major in Business Economics': 'BSBA-BE',
        'Bachelor of Science in Business Administration major in Marketing Management': 'BSBA-MM',
        'Bachelor of Science in Entrepreneurship': 'BSEnt',
        'Bachelor of Science in Hospitality Management': 'BSHM',
        # College of Education
        'Bachelor of Elementary Education – Language Education': 'BEEd-LE',
        'Bachelor of Elementary Education – Science and Mathematics': 'BEEd-SM',
        'Bachelor of Secondary Education – Biology': 'BSE-Bio',
        'Bachelor of Secondary Education – Chemistry': 'BSE-Chem',
        'Bachelor of Secondary Education – Physics': 'BSE-Physics',
        'Bachelor of Secondary Education – Mathematics': 'BSE-Math',
        'Bachelor of Physical Education': 'BPE',
        'Bachelor of Technology and Livelihood Education major in Home Economics': 'BTLE-HE',
        'Bachelor of Technology and Livelihood Education major in Industrial Arts': 'BTLE-IA',
        'Bachelor of Technical-Vocational Teacher Education major in Drafting Technology': 'BTVTE-DraftTech',
        # College of Health Sciences
        'Bachelor of Science in Nursing': 'BSN',
        # College of Science and Mathematics
        'Bachelor of Science in Physics': 'BSP',
        'Bachelor of Science in Chemistry': 'BSChem',
        'Bachelor of Science in Biology': 'BSBio',
        'Bachelor of Science in Statistics': 'BSStat',
        'Bachelor of Science in Mathematics': 'BSMath',
        # College of Computer Studies
        'Bachelor of Science in Computer Science': 'BSCS',
        'Bachelor of Science in Computer Application': 'BSCA',
        'Bachelor of Science in Information Technology': 'BSIT',
        'Bachelor of Science in Information System': 'BSIS'
    }
    
    return course_codes.get(course, 'COURSE')  # Default to 'COURSE' if not found

# Function to generate course based on code
def generate_course(course):
    course_codes = {
        # College of Engineering
        'BSMetE' : 'Bachelor of Science in Metallurgical Engineering',
        'BSCpE' : 'Bachelor of Science in Computer Engineering',
        'BSECE': 'Bachelor of Science in Electronics and Communication Engineering',
        'BSME' : 'Bachelor of Science in Mechanical Engineering',
        'BSChE': 'Bachelor of Science in Chemical Engineering',
        'BSCE' : 'Bachelor of Science in Civil Engineering',
        'BSIAM' : 'Bachelor of Science in Industrial Automation and Mechatronics',
        'BSCerE' : 'Bachelor of Science in Ceramics Engineering',
        'BSMiningE' : 'Bachelor of Science in Mining Engineering',
        'BSEE' : 'Bachelor of Science in Electrical Engineering',
        'BSEnvE' : 'Bachelor of Science in Environmental Engineering',
        # College of Arts and Social Sciences
        'BAELS' : 'Bachelor of Arts in English Language Studies',
        'BALCS' : 'Bachelor of Arts in Literary and Culture Studies',
        'BAF' : 'Bachelor of Arts in Filipino',
        'BAH' : 'Bachelor of Arts in History',
        'BAP' : 'Bachelor of Arts in Panitikan',
        'BAPS' : 'Bachelor of Arts in Political Science',
        'BAPsy' : 'Bachelor of Arts in Psychology',
        'BASoc' : 'Bachelor of Arts in Sociology',
        'BSPhil': 'Bachelor of Science in Philosophy',
        'BSPsy': 'Bachelor of Science in Psychology',
        # College of Economics and Business Administration
        'BSA': 'Bachelor of Science in Accountancy',
        'BSE': 'Bachelor of Science in Economics',
        'BSBA-BE': 'Bachelor of Science in Business Administration major in Business Economics',
        'BSBA-MM': 'Bachelor of Science in Business Administration major in Marketing Management',
        'BSEnt': 'Bachelor of Science in Entrepreneurship',
        'BSHM': 'Bachelor of Science in Hospitality Management',
        # College of Education
        'BEEd-LE': 'Bachelor of Elementary Education – Language Education',
        'BEEd-SM': 'Bachelor of Elementary Education – Science and Mathematics',
        'BSE-Bio': 'Bachelor of Secondary Education – Biology',
        'BSE-Chem': 'Bachelor of Secondary Education – Chemistry',
        'BSE-Physics': 'Bachelor of Secondary Education – Physics',
        'BSE-Math': 'Bachelor of Secondary Education – Mathematics',
        'BPE': 'Bachelor of Physical Education',
        'BTLE-HE': 'Bachelor of Technology and Livelihood Education major in Home Economics',
        'BTLE-IA': 'Bachelor of Technology and Livelihood Education major in Industrial Arts',
        'BTVTE-DraftTech': 'Bachelor of Technical-Vocational Teacher Education major in Drafting Technology',
        # College of Health Sciences
        'BSN': 'Bachelor of Science in Nursing',
        # College of Science and Mathematics
        'BSP': 'Bachelor of Science in Physics',
        'BSChem': 'Bachelor of Science in Chemistry',
        'BSBio': 'Bachelor of Science in Biology',
        'BSStat': 'Bachelor of Science in Statistics',
        'BSMath': 'Bachelor of Science in Mathematics',
        # College of Computer Studies
        'BSCS': 'Bachelor of Science in Computer Science',
        'BSCA': 'Bachelor of Science in Computer Application',
        'BSIT': 'Bachelor of Science in Information Technology',
        'BSIS': 'Bachelor of Science in Information System'
    }

    return course_codes.get(course, 'COURSE')  # Default to 'COURSE' if not found

# Function to generate college code based on the course code
def gencode_college_course(course):
    college_codes = {
        # College of Engineering
        'BSMetE' : 'COE',
        'BSCpE' : 'COE',
        'BSECE': 'COE',
        'BSME' : 'COE',
        'BSChE': 'COE',
        'BSCE' : 'COE',
        'BSIAM' : 'COE',
        'BSCerE' : 'COE',
        'BSMiningE' : 'COE',
        'BSEE' : 'COE',
        'BSEnvE' : 'COE',
        # College of Arts and Social Sciences
        'BAELS' : 'CASS',
        'BALCS' : 'CASS',
        'BAF' : 'CASS',
        'BAH' : 'CASS',
        'BAP' : 'CASS',
        'BAPS' : 'CASS',
        'BAPsy' : 'CASS',
        'BASoc' : 'CASS',
        'BSPhil': 'CASS',
        'BSPsy': 'CASS',
        # College of Economics and Business Administration
        'BSA': 'CEBA',
        'BSE': 'CEBA',
        'BSBA-BE': 'CEBA',
        'BSBA-MM': 'CEBA',
        'BSEnt': 'CEBA',
        'BSHM': 'CEBA',
        # College of Education
        'BEEd-LE': 'CED',
        'BEEd-SM': 'CED',
        'BSE-Bio': 'CED',
        'BSE-Chem': 'CED',
        'BSE-Physics': 'CED',
        'BSE-Math': 'CED',
        'BPE': 'CED',
        'BTLE-HE': 'CED',
        'BTLE-IA': 'CED',
        'BTVTE-DraftTech': 'CED',
        # College of Health Sciences
        'BSN': 'CHS',
        # College of Science and Mathematics
        'BSP': 'CSM',
        'BSChem': 'CSM',
        'BSBio': 'CSM',
        'BSStat': 'CSM',
        'BSMath': 'CSM',
        # College of Computer Studies
        'BSCS': 'CCS',
        'BSCA': 'CCS',
        'BSIT': 'CCS',
        'BSIS': 'CCS'
    }

    return college_codes.get(course, 'COL')  # Default to 'COL' if not found


