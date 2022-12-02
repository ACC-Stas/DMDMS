DELIMITER //  
CREATE TRIGGER date_check_examination_insert
BEFORE INSERT ON Examination
FOR EACH ROW
BEGIN

IF NEW.time IS NULL THEN SET NEW.time = NOW();
END IF;

IF NEW.time > NOW() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid examination time';
END IF;

END //

CREATE TRIGGER date_check_examination_update
BEFORE UPDATE ON Examination
FOR EACH ROW
BEGIN

IF NEW.time > NOW() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid examination time';
END IF;

END //


CREATE TRIGGER date_check_patient_insert
BEFORE INSERT ON Patient
FOR EACH ROW
BEGIN

IF NEW.registration_date IS NULL THEN SET NEW.registration_date = CURDATE();
END IF;

IF NEW.registration_date > CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid registration date';
END IF;

END //

CREATE TRIGGER date_check_patient_update
BEFORE UPDATE ON Patient
FOR EACH ROW
BEGIN

IF NEW.registration_date > CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid registration date';
END IF;

END //


CREATE TRIGGER date_check_invoice_insert
BEFORE INSERT ON Invoice
FOR EACH ROW
BEGIN

IF NEW.date_issue IS NULL THEN SET NEW.date_issue = CURDATE();
END IF;

IF NEW.date_issue > CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid date issue';
END IF;

IF NEW.date_paid IS NOT NULL AND NEW.date_paid > CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid date paid';
END IF;

IF NEW.date_paid IS NOT NULL AND NEW.date_paid < NEW.date_issue THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Date paid < date issue';
END IF;

END //

CREATE TRIGGER date_check_invoice_update
BEFORE UPDATE ON Invoice
FOR EACH ROW
BEGIN

IF NEW.date_issue > CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid date issue';
END IF;

IF NEW.date_paid IS NOT NULL AND NEW.date_paid > CURDATE() THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid date paid';
END IF;

END //
DELIMITER ;

