DELIMITER //

CREATE PROCEDURE get_clinics_contacts()
BEGIN

SELECT CONCAT_WS(' ', address.city, address.street, address.home) 'Address', contact.tel 'Clinic Number', CONCAT_WS(' ', fullname.first_name, fullname.middle_name, fullname.last_name) 'Manager Name'
FROM Center center INNER JOIN Stuff stuff ON center.id = stuff.center_id
                   INNER JOIN Address address ON center.address_id = address.id
                   INNER JOIN Contact contact ON center.contact_id = contact.id
                   INNER JOIN FullName fullname ON stuff.fullname_id = fullname.id
WHERE stuff.role = 'Manager'
ORDER BY center.id;

END //


CREATE PROCEDURE get_patients()
BEGIN

SELECT CONCAT_WS(' ', fullname.first_name, fullname.middle_name, fullname.last_name) 'Name',
       CONCAT_WS(' ', address.city, address.street, address.home) 'Address',
       contact.tel 'Number', contact.email 'Email'
FROM Patient patient INNER JOIN FullName fullname ON patient.fullname_id = fullname.id
                     INNER JOIN Address address ON patient.address_id = address.id
                     INNER JOIN Contact contact ON patient.contact_id = contact.id
ORDER BY fullname.first_name, fullname.middle_name, fullname.last_name;

END //


CREATE PROCEDURE get_patient_examinations(IN patient_id INT)
BEGIN

SELECT ex.time 'Time', ex.doctor_id 'Doctor id', ex.results 'Result'
FROM Examination ex
WHERE ex.patient_id = patient_id
ORDER BY ex.time DESC;

END //


CREATE PROCEDURE get_treatments(IN examination_id INT)
BEGIN

SELECT treatment.description 'Description', treatment.doctor_id 'Doctor Id'
FROM Treatment treatment
WHERE treatment.examination_id = examination_id;

END //


CREATE PROCEDURE get_patient_debt(IN patient_id INT)
BEGIN

SELECT invoice.cost 'Cost', invoice.date_issue 'Date Issue'
FROM Examination examination INNER JOIN Patient patient ON patient.id = examination.patient_id
                             INNER JOIN Treatment treatment ON examination.id = treatment.examination_id
                             INNER JOIN Invoice invoice ON invoice.id = treatment.invoice_id
WHERE patient.id = patient_id
ORDER BY invoice.date_issue DESC;

END //


CREATE PROCEDURE get_free_chambers(IN city VARCHAR(50))
BEGIN

SELECT chamber.size 'Size', CONCAT_WS(' ', address.city, address.street, address.home) 'Address', COUNT(chamber.id) 'Number'
FROM CryogenicChamber chamber INNER JOIN Center center ON center.id = chamber.center_id
                              INNER JOIN Address address ON address.id = center.address_id
WHERE chamber.status = 'free' AND address.city = city
GROUP BY chamber.size, address.city, address.street, address.home, center.id
ORDER BY center.id;

END //


CREATE PROCEDURE get_month_clinics_salary()
BEGIN

SELECT center.id 'Center Id', SUM(stuff.salary) 'Month salary sum'
FROM Center center INNER JOIN Stuff stuff ON center.id = stuff.center_id
GROUP BY center.id
ORDER BY center.id;

END //


CREATE PROCEDURE get_centers_patients_number()
BEGIN

SELECT center.id 'Center Id', COUNT(patient.id) 'Patients Number'
FROM Center center INNER JOIN PatientCenter ON PatientCenter.center_id = center.id
                   INNER JOIN Patient patient ON PatientCenter.patient_id = patient.id
GROUP BY center.id
ORDER BY center.id;

END //


CREATE PROCEDURE get_chambers()
BEGIN

SELECT center.id 'Center Id', chamber.size, COUNT(chamber.id)
FROM Center center INNER JOIN CryogenicChamber chamber ON center.id = chamber.center_id
GROUP BY center.id, chamber.size
ORDER BY center.id, chamber.size;

END //

DELIMITER ;
