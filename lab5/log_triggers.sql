DELIMITER //
CREATE TRIGGER patient_insert_log
BEFORE INSERT ON Patient
FOR EACH ROW
BEGIN

INSERT INTO Logs
(username, operation, tablename, description)
VALUES
((SELECT USER()), 'INSERT', 'Patient', CONCAT_WS(' ', NEW.id, NEW.fullname_id, NEW.address_id, NEW.contact_id, NEW.sex, NEW.registration_date));

END //

CREATE TRIGGER patient_update_log
BEFORE UPDATE ON Patient
FOR EACH ROW
BEGIN

INSERT INTO Logs
(username, operation, tablename, description)
VALUES
((SELECT USER()), 'UPDATE', 'Patient', CONCAT_WS(' ', NEW.id, NEW.fullname_id, NEW.address_id, NEW.contact_id, NEW.sex, NEW.registration_date));

END //

CREATE TRIGGER patient_delete_log
BEFORE DELETE ON Patient
FOR EACH ROW
BEGIN

INSERT INTO Logs
(username, operation, tablename, description)
VALUES
((SELECT USER()), 'DELETE', 'Patient', CONCAT_WS(' ', OLD.id, OLD.fullname_id, OLD.address_id, OLD.contact_id, OLD.sex, OLD.registration_date));

END //



CREATE TRIGGER center_insert_log
BEFORE INSERT ON Center
FOR EACH ROW
BEGIN

INSERT INTO Logs
(username, operation, tablename, description)
VALUES
((SELECT USER()), 'INSERT', 'Center', CONCAT_WS(' ', NEW.id, NEW.address_id, NEW.contact_id));

END //

CREATE TRIGGER center_update_log
BEFORE UPdATE ON Center
FOR EACH ROW
BEGIN

INSERT INTO Logs
(username, operation, tablename, description)
VALUES
((SELECT USER()), 'UPDATE', 'Center', CONCAT_WS(' ', NEW.id, NEW.address_id, NEW.contact_id));

END //

CREATE TRIGGER center_delete_log
BEFORE DELETE ON Center
FOR EACH ROW
BEGIN

INSERT INTO Logs
(username, operation, tablename, description)
VALUES
((SELECT USER()), 'DELETE', 'Center', CONCAT_WS(' ', OLD.id, OLD.address_id, OLD.contact_id));

END //



DELIMITER ;

