# -------------------------------------------------
# 3. functions with no parameter and a return value
# -------------------------------------------------
# function definition:
def get_todays_date():
    from datetime import datetime
    return datetime.now().date()

# function call:
print('Today\'s date is', get_todays_date())