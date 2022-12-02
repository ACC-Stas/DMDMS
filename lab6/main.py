from windows.Enter import Enter
from windows.ListWindow import ListWindow
from windows.CRUDWindow import CRUDWindow
from windows.CreateUser import CreateUser


address_CRUD = CRUDWindow('Address',
                          select_columns=['id', 'city', 'street', 'home'],
                          delete_column='id',
                          insert_columns=['city', 'street', 'home'],
                          update_columns=['city', 'street', 'home', 'id'],
                          help_desc='Address')

fullname_CRUD = CRUDWindow('FullName',
                           select_columns=['id', 'first_name', 'middle_name', 'last_name'],
                           delete_column='id',
                           insert_columns=['first_name', 'middle_name', 'last_name'],
                           update_columns=['first_name', 'middle_name', 'last_name', 'id'],
                           help_desc='FullName')

contact_CRUD = CRUDWindow('Contact',
                          select_columns=['id', 'tel', 'email'],
                          delete_column='id',
                          insert_columns=['tel', 'email'],
                          update_columns=['tel', 'email', 'id'],
                          help_desc='Contact')

center_CRUD = CRUDWindow('Center',
                         select_columns=['id', 'address_id', 'contact_id'],
                         delete_column='id',
                         insert_columns=['address_id', 'contact_id'],
                         update_columns=['address_id', 'contact_id', 'id'],
                         help_desc='Center')

patient_center_CRUD = CRUDWindow('PatientCenter',
                                 select_columns=['center_id', 'patient_id'],
                                 insert_columns=['center_id', 'patient_id'],
                                 help_desc='PatientCenter')

stuff_CRUD = CRUDWindow('Stuff',
                        select_columns=['id', 'fullname_id', 'address_id', 'contact_id', 'iin', 'sex', 'position',
                                        'salary', 'center_id', 'role'],
                        delete_column='id',
                        insert_columns=['fullname_id', 'address_id', 'contact_id', 'iin', 'sex', 'position',
                                        'salary', 'center_id', 'role'],
                        update_columns=['fullname_id', 'address_id', 'contact_id', 'iin', 'sex', 'position',
                                        'salary', 'center_id', 'role', 'id'],
                        help_desc='Stuff')

patient_CRUD = CRUDWindow('Patient',
                          select_columns=['id', 'fullname_id', 'address_id', 'contact_id', 'sex', 'registration_date'],
                          delete_column='id',
                          insert_columns=['fullname_id', 'address_id', 'contact_id', 'sex', 'registration_date'],
                          update_columns=['fullname_id', 'address_id', 'contact_id', 'sex', 'registration_date', 'id'],
                          help_desc='Patient')

chamber_CRUD = CRUDWindow('CryogenicChamber',
                          select_columns=['id', 'size', 'status', 'patient_id', 'center_id'],
                          delete_column='id',
                          insert_columns=['size', 'status', 'patient_id', 'center_id'],
                          update_columns=['size', 'status', 'patient_id', 'center_id', 'id'],
                          help_desc='CryogenicChamber')

stock_item_CRUD = CRUDWindow('StockItem',
                             select_columns=['id', 'name', 'description', 'cost', 'quantity', 'center_id'],
                             delete_column='id',
                             insert_columns=['name', 'description', 'cost', 'quantity', 'center_id'],
                             update_columns=['name', 'description', 'cost', 'quantity', 'center_id', 'id'],
                             help_desc='StockItem')

stock_pharmacy_CRUD = CRUDWindow('StockPharmacy',
                                 select_columns=['id', 'name', 'description', 'dosage', 'on_prescription', 'cost',
                                                 'quantity', 'center_id'],
                                 delete_column='id',
                                 insert_columns=['name', 'description', 'dosage', 'on_prescription', 'cost',
                                                 'quantity', 'center_id'],
                                 update_columns=['name', 'description', 'dosage', 'on_prescription', 'cost',
                                                 'quantity', 'center_id', 'id'],
                                 help_desc='StockPharmacy')

examination_CRUD = CRUDWindow('Examination',
                              select_columns=['id', 'time', 'doctor_id', 'patient_id', 'results'],
                              delete_column='id',
                              insert_columns=['time', 'doctor_id', 'patient_id', 'results'],
                              update_columns=['time', 'doctor_id', 'patient_id', 'results', 'id'],
                              help_desc='Examination')


treatment_CRUD = CRUDWindow('Treatment',
                            select_columns=['id', 'description', 'doctor_id', 'invoice_id', 'examination_id'],
                            delete_column='id',
                            insert_columns=['description', 'doctor_id', 'invoice_id', 'examination_id'],
                            update_columns=['description', 'doctor_id', 'invoice_id', 'examination_id', 'id'],
                            help_desc='Treatment')


invoice_CRUD = CRUDWindow('Invoice',
                          select_columns=['id', 'cost', 'date_issue', 'date_paid', 'payment_method'],
                          delete_column='id',
                          insert_columns=['cost', 'date_issue', 'date_paid', 'payment_method'],
                          update_columns=['cost', 'date_issue', 'date_paid', 'payment_method', 'id'],
                          help_desc='Invoice')

user_creator = CreateUser()

windows_dict = {'Address': address_CRUD,
                'FullName': fullname_CRUD,
                'Contact': contact_CRUD,
                'Center': center_CRUD,
                'PatientCenter': patient_center_CRUD,
                'Patient': patient_CRUD,
                'CryogenicChamber': chamber_CRUD,
                'Stuff': stuff_CRUD,
                'StockItem': stock_item_CRUD,
                'StockPharmacy': stock_pharmacy_CRUD,
                'Examination': examination_CRUD,
                'Treatment': treatment_CRUD,
                'Invoice': invoice_CRUD,
                'CreateUser': user_creator,
                }

main_window = ListWindow('Main', windows=windows_dict)
enter_window = Enter(main_window, "Дарова Бандиты")
main_window.set_parent(enter_window)

for value in windows_dict.values():
    value.set_parent(main_window)

enter_window.run()
