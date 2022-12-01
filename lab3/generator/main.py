import random
import time
import string


def generate_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_number(length):
    result = []
    for i in range(length):
        number = random.randint(0, 9)
        result.append(str(number))

    return "".join(result)


def generate_fullname():
    result = []
    for i in range(3):
        size = random.randint(2, 12)
        result.append(generate_string(size))

    return f"(\'{result[0]}\', \'{result[1]}\', \'{result[2]}\'),"


def generate_email():
    email_type = generate_string(random.randint(0, 1))
    name = generate_string(random.randint(2, 15))
    region_type = generate_string(2)

    return f"{name}@{email_type}mail.{region_type}"


def generate_phone_number():
    body = generate_number(7)
    return f"+37529{body}"


def generate_contact():
    number = generate_phone_number()
    email = generate_email()
    return f"(\'{number}\', \'{email}\'),"


def generate_address():
    home = generate_number(2)
    street = generate_string(random.randint(2, 15))
    city = generate_string(random.randint(2, 15))

    return f"(\'{city}\', \'{street}\', \'{home}\'),"


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def generate_datetime(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)


def generate_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


def generate_patient():
    fullname_id = random.randint(1, 99)
    address_id = random.randint(1, 99)
    contact_id = random.randint(1, 99)
    sex = ['m', 'w'][random.randint(0, 1)]
    registration_date = generate_date("2020-11-25", "2022-11-25", random.random())

    return f"({fullname_id}, {address_id}, {contact_id}, \'{sex}\', \'{registration_date}\'),"


def generate_patient_center():
    patient_id = random.randint(1, 49)
    center_id = random.randint(1, 2)
    return f"({patient_id}, {center_id}),"


def generate_cryogenic_chamber():
    size = ['head', 'small', 'medium', 'large'][random.randint(0, 3)]
    status = ['occupied', 'free'][random.randint(0, 1)]
    if status == 'occupied':
        patient_id = random.randint(1, 49)
    else:
        patient_id = 'NULL'
    center_id = random.randint(1, 2)

    return f"(\'{size}\', \'{status}\', {patient_id}, {center_id}),"


def generate_stock_item():
    name = generate_string(random.randint(2, 49))
    description = generate_string(random.randint(5, 250))
    cost = generate_number(10)
    cost = cost[2:10] + "." + cost[0:2]
    quantity = generate_number(random.randint(1, 3))
    center_id = random.randint(1, 2)

    return f"(\'{name}\', \'{description}\', \'{cost}\', {quantity}, {center_id}),"


def generate_stock_pharmacy():
    name = generate_string(random.randint(2, 49))
    description = generate_string(random.randint(5, 250))
    dosage = generate_string(random.randint(5, 250))
    cost = generate_number(10)
    cost = cost[2:10] + "." + cost[0:2]
    on_prescription = ['yes', 'no'][random.randint(0, 1)]
    quantity = generate_number(random.randint(1, 3))
    center_id = random.randint(1, 2)

    return f"(\'{name}\', \'{description}\', \'{dosage}\', \'{on_prescription}\', \'{cost}\', {quantity}, {center_id}),"


def generate_stuff():
    fullname_id = random.randint(1, 99)
    address_id = random.randint(1, 99)
    contact_id = random.randint(1, 99)
    iin = generate_number(6)
    sex = ['m', 'w'][random.randint(0, 1)]
    position = generate_string(random.randint(5, 15))
    salary = generate_number(10)
    salary = salary[2:10] + "." + salary[0:2]
    center_id = random.randint(1, 2)
    role = ['Admin', 'Manager', 'Stuff'][random.randint(0, 2)]

    return f"({fullname_id}, {address_id}, {contact_id}, \'{iin}\', \'{sex}\', \'{position}\', \'{salary}\', " \
           f"{center_id}, \'{role}\'),"


def generate_examination():
    time_ = generate_datetime("2020-11-25 15:12:10", "2022-11-25 15:12:10", random.random())
    doctor_id = random.randint(1, 29)
    patient_id = random.randint(1, 49)
    results = generate_string(random.randint(4, 100))
    return f"(\'{time_}\', {doctor_id}, {patient_id}, \'{results}\'),"


def generate_invoice():
    cost = generate_number(10)
    cost = cost[2:10] + "." + cost[0:2]
    date_issue = generate_date("2020-11-25", "2022-11-25", random.random())
    paid = random.randint(0, 1)
    if paid == 0:
        date_paid = generate_date("2020-11-25", "2022-11-25", random.random())
        date_paid = "\'" + date_paid + "\'"
        payment_method = ['card', 'cash', 'check'][random.randint(0, 2)]
        payment_method = '\'' + payment_method + '\''
    else:
        date_paid, payment_method = "NULL", "NULL"

    return f"(\'{cost}\', \'{date_issue}\', {date_paid}, {payment_method}),"


def generate_treatment(idx):
    description = generate_string(random.randint(4, 100))
    doctor_id = random.randint(1, 29)
    invoice_id = idx
    examination_id = idx

    return f"(\'{description}\', {doctor_id}, {invoice_id}, {examination_id}),"


def main():
    for i in range(30):
        print(generate_treatment(i))


if __name__ == "__main__":
    main()
