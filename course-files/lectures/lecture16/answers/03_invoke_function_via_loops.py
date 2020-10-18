# invoke the function you made in #2 to generate a 
# personalized message to everyone in the list.

def generate_email(name, amount, level, gift):
    print('''
    Dear ''' + name + ''',

    Thank you for donating $''' + str(amount) + ''' to the Southern Poverty Law Center. We really appreciate donors like
    you. Because of your support, you are eligible to become a ''' + level + '''-level supporter. As a token of
    our appreciation, please accept this ''' + gift + '''.

    We look forward to your continued sponsorship.

    Sincerely,

    SPLC
    ''')

people = [
    ['Tammy Spencer', '42022 Daniel Forest Apt. 201', 'Lake Amyhaven', 'Louisiana', 54479, 'Runner, broadcasting/film/video', 50, 'bronze', 'coffee mug'],
    ['Amy Meyer', '5558 Brown Street Apt. 718', 'Calebport', 'Wyoming', '96398', 'Administrator, charities/voluntary organisations', 250, 'gold', 'T-shirt'],
    ['Michael Gutierrez', '560 Rhonda Isle Apt. 851', 'West Dakotaside', 'South Carolina', '92315', 'Location manager', 150, 'silver', 'engraved pen'],
    ['Victoria Zhang', '9007 Rivera Highway Apt. 726', 'Andreafurt', 'Connecticut', '08533', 'Lecturer, further education', 50, 'bronze', 'coffee mug'],
    ['Dorothy Acevedo', '43878 Deleon Ranch Apt. 191', 'Emilystad', 'Vermont', '5721', 'Social worker', 50, 'bronze', 'coffee mug'],
    ['Richard Haley', '482 Robertson Plaza', 'West Kelly', 'Alabama', '65044', 'Fashion designer', 250, 'gold', 'T-shirt'],
    ['Christopher Jimenez MD', '5679 Pamela Wall Apt. 023', 'West Nathan', 'Delaware', '63181', 'Naval architect', 150, 'silver', 'engraved pen'],
    ['Paul Peterson', '415 Hernandez Islands Suite 379', 'Port Matthew', 'Utah', '99271', 'Publishing rights manager', 50, 'bronze', 'coffee mug'],
    ['Christine Lambert DDS', '043 Wright Key Suite 737', 'Port Lisa', 'Vermont', '84484', 'Technical author', 150, 'silver', 'engraved pen'],
    ['Robert Jones', '0816 Tyler Inlet', 'Courtneyberg', 'Nevada', '5095', 'Clinical psychologist', 250, 'gold', 'T-shirt'],
]

for person in people:
    generate_email(person[0], person[6], person[7], person[8])
