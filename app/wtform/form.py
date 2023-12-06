from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField#, IntegerField
from wtforms.validators import DataRequired, Length

class StudentForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired(message='Please input your ID.'),Length(min=9, max=9)])
       
    firstname = StringField('FirstName', validators=[DataRequired(message='Please input your first name.'), 
                            Length(min=1, max=45)])
    lastname = StringField('LastName', validators=[DataRequired(message='Please input your last name.'), 
                            Length(min=1, max=45)])
    
    gender_choices = [('', '-- Please select --', {'disabled': True}),('F','Female'),('M','Male'),('Other','Other'),('Prefer not to say','Prefer not to say')]
    gender = SelectField('Gender', choices=gender_choices, validators=[DataRequired()], default='')

    college_choices = [('', '-- Please select --', {'disabled': True}),('College of Engineering','College of Engineering'),('College of Arts and Social Sciences','College of Arts and Social Sciences'),
                        ('College of Economics and Business Administration','College of Economics and Business Administration'),('College of Education','College of Education'),
                        ('College of Health Sciences','College of Health Sciences'),('College of Science and Mathematics','College of Science and Mathematics'),
                        ('College of Computer Studies', 'College of Computer Studies')]
    college = SelectField('College', choices=college_choices, validators=[DataRequired()], default='')
    
    # The course choices will be dynamically updated based on the selected college
    course = SelectField('Course', choices=[], validators=[DataRequired()])

    year_choices = [('', '-- Please select --', {'disabled': True}),('1','1st Year'),('2','2nd Year'),('3','3rd Year'),('4','4th Year')]
    year = SelectField('Year', choices=year_choices, validators=[DataRequired()], default='')

    photo = FileField('Upload Photo')

    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    college_choices = [('', '-- Please select --', {'disabled': True}),('College of Engineering','College of Engineering'),('College of Arts and Social Sciences','College of Arts and Social Sciences'),
                        ('College of Economics and Business Administration','College of Economics and Business Administration'),('College of Education','College of Education'),
                        ('College of Health Sciences','College of Health Sciences'),('College of Science and Mathematics','College of Science and Mathematics'),
                        ('College of Computer Studies', 'College of Computer Studies')]
    college = SelectField('College', choices=college_choices, validators=[DataRequired()], default='')

    # The course choices will be dynamically updated based on the selected college
    course = SelectField('Course', choices=[], validators=[DataRequired()], default='')

    submit = SubmitField('Submit')

class CollegeForm(FlaskForm):
    college_choices = [('', '-- Please select --', {'disabled': True}),('College of Engineering','College of Engineering'),('College of Arts and Social Sciences','College of Arts and Social Sciences'),
                        ('College of Economics and Business Administration','College of Economics and Business Administration'),('College of Education','College of Education'),
                        ('College of Health Sciences','College of Health Sciences'),('College of Science and Mathematics','College of Science and Mathematics'),
                        ('College of Computer Studies', 'College of Computer Studies')]
    college = SelectField('College', choices=college_choices, validators=[DataRequired()], default='')

    submit = SubmitField('Submit')