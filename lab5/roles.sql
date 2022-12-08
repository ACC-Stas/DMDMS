CREATE ROLE 'Admin';
CREATE ROLE 'Manager';
CREATE ROLE 'Stuff';

GRANT SELECT ON DMDMS.* TO 'Admin' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.* TO 'Admin' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.* TO 'Admin' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.* TO 'Admin' WITH GRANT OPTION;
GRANT CREATE USER ON *.* TO 'Admin' WITH GRANT OPTION;
GRANT RELOAD ON *.* TO 'Admin' WITH GRANT OPTION;
GRANT SELECT ON mysql.user TO 'Admin' WITH GRANT OPTION;



GRANT SELECT ON DMDMS.Patient TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Examination TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Treatment TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Invoice TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.PatientCenter TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.StockItem TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.StockPharmacy TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Stuff TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Address TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.FullName TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Contact TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.CryogenicChamber TO 'Manager' WITH GRANT OPTION;
GRANT SELECT ON DMDMS.Center TO 'Manager' WITH GRANT OPTION;

GRANT INSERT ON DMDMS.Patient TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.Examination TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.Treatment TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.Invoice TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.PatientCenter TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.StockItem TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.StockPharmacy TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.Stuff TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.Address TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.FullName TO 'Manager' WITH GRANT OPTION;
GRANT INSERT ON DMDMS.Contact TO 'Manager' WITH GRANT OPTION;

GRANT UPDATE ON DMDMS.Patient TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.Examination TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.Treatment TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.Invoice TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.PatientCenter TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.StockItem TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.StockPharmacy TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.Stuff TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.Address TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.FullName TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.Contact TO 'Manager' WITH GRANT OPTION;
GRANT UPDATE ON DMDMS.CryogenicChamber TO 'Manager' WITH GRANT OPTION;

GRANT DELETE ON DMDMS.Patient TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.Examination TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.Treatment TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.Invoice TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.PatientCenter TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.StockItem TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.StockPharmacy TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.Stuff TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.Address TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.FullName TO 'Manager' WITH GRANT OPTION;
GRANT DELETE ON DMDMS.Contact TO 'Manager' WITH GRANT OPTION;

GRANT CREATE USER ON *.* TO 'Manager' WITH GRANT OPTION;
GRANT RELOAD ON *.* TO 'Manager' WITH GRANT OPTION;


GRANT SELECT ON DMDMS.Patient TO 'Stuff';
GRANT SELECT ON DMDMS.Invoice TO 'Stuff';
GRANT SELECT ON DMDMS.Examination TO 'Stuff';
GRANT SELECT ON DMDMS.Treatment TO 'Stuff';
GRANT SELECT ON DMDMS.StockPharmacy TO 'Stuff';
GRANT SELECT ON DMDMS.StockItem TO 'Stuff';
GRANT SELECT ON DMDMS.CryogenicChamber TO 'Stuff';
GRANT SELECT ON DMDMS.Contact TO 'Stuff';
GRANT SELECT ON DMDMS.FullName TO 'Stuff';
GRANT SELECT ON DMDMS.Address TO 'Stuff';
GRANT SELECT ON DMDMS.Center TO 'Stuff';

GRANT INSERT ON DMDMS.StockItem TO 'Stuff';
GRANT INSERT ON DMDMS.StockPharmacy TO 'Stuff';
GRANT INSERT ON DMDMS.Treatment TO 'Stuff';
GRANT INSERT ON DMDMS.Examination TO 'Stuff';
GRANT INSERT ON DMDMS.Invoice TO 'Stuff';

GRANT UPDATE ON DMDMS.StockItem TO 'Stuff';
GRANT UPDATE ON DMDMS.StockPharmacy TO 'Stuff';

GRANT DELETE ON DMDMS.StockItem TO 'Stuff';
GRANT DELETE ON DMDMS.StockPharmacy TO 'Stuff';
