# DMDMS. Кононович Станислав Владимирович, 053501

Тема разрабатываемого проекта: **Частный медицинский центр**.

## Описание предметной области

### Медицинский центр
DMDMS располагает рядом центров по всей территории Республики. Информация о центре: идентификационный номер, адрес, номер телефона регистратуры, номер факса. Каждая клиника имеет менеджера и персонал: уборщики, врачи-консультанты, медсёстры, секретари. 

### Персонал
Данные персонала: идентификационный номер (уникальный для DMDMS), ФИО, телефонный номер, электронная почта, адрес, пол, ИИН (идентификационный номер физического лица, указан в паспорте гражданина Республики или виде на жительство в Республике), занимаемая должность, текущая месячная зарплата.

### Пациенты
Данные пациента: идентификационный номер (уникальный для DMDMS), ФИО, телефонный номер, электронная почта, адрес, пол, дата регистрации.

### Осмотры
Результаты каждого осмотра записываются: идентификационный номер осмотра, дата и время, данные врача, данные пациента, текстовое описание результатов осмотра (заключение). Может быть выписано лечение.

### Лечение
В ходе осмотра может потребоваться оперативное вмешательство (лечение). Данные: осмотр (в ходе которого потребовалось лечение), список использованных препаратов (описание лечения), цена и ответственный за лечение врач. 

### Криогенные камеры
Каждая клиника располагает некоторым количеством камер. В случае летального исхода или его неотвратимой угрозы, пациент будет помещен в одну из камер при наличии места. Данные: номер камеры, размер (Head, Small, Medium, Large), статус (занята / свободна), идентификационный номер пациента (если занята).

### Счета
Данные: номер счёта, дата выставления, ФИО пациента, адрес пациента, детали лечения, дата оплаты (если проведена), способ оплаты (чек, наличные, карта).

### Хирургические, нехирургические и фармацевтические запасы
Для каждой клиники ведётся учёт лекарственных средств и оборудования. 
Данные: идентификационный номер объекта, дата приобретения, стоимость приобретения, наименование, дата истечения срока годности, дата использования, цель использования.

## Функциональные требования к проекту

1. Обязательные требования:
    - Авторизация пользователя.
    - Управление пользователями (CRUD).
    - Система ролей (Admin, Manager, Stuff).
    - Журналирование действий пользователя.
  
2. Функции создания записей и их изменения:  
    i. Admin: CRUD Center, Stuff, Patient, Examination, Treatment, Invoice, StockItem, StockPharmacy, CryogenicChamber  
    ii. Manager: CRUD Patient, Examination, Treatment, Invoice, StockItem, StockPharmacy, RU CryogenicChamber  
    iii. Stuff: CR Treatment, Examination, Invoice, CRUD StockItem, StockPharmacy, R CryogenicChamber  

3. Должны быть реализованы следующие запросы к базе данных:
    - Предоставить отчет с указанием имени менеджера, адреса клиники и номера телефона для каждой клиники, упорядоченных по номеру центра.
    - Предоставить отчет, в котором перечислены имена пациентов и информация о них.
    - Предоставить отчет всех осмотров данного пациента.
    - Предоставить отчет о деталях лечения, предоставленного пациенту, на основе результатов данного обследования.
    - Предоставить детали неоплаченного счета для данного пациента.
    - Предоставить подробную информацию о криогенных камерах, доступных в определённом городе/Республике, упорядоченных по номеру центра.
    - Предоставить отчет, в котором указана общая месячная заработная плата персонала каждой клиники, упорядоченная по номеру центра.
    - Указать максимальную, минимальную и среднюю стоимость лечения.
    - Предоставить общее количество пациентов в каждом центре, упорядочить по номеру центра.
    - Перечислить количество криогенны камер каждого типа в каждом центре, упорядочить по номеру центра.
    - Предоставить отчет с перечнем фармацевтических средств, которые необходимо заказать в каждом центре, упорядочить по номеру центра.

# Database design, pt.1: Not normalized

## Attributes

| Entity  | Attributes  |
|:------------- |:--------------- |
| Center        | id, address (street, city, state), tel, fax |
| Staff         | id, name (first_name, middle_name, last_name), address (street, city, state), tel, email, IIN, sex, position, salary|
| Patient       | id, name (first_name, middle_name, last_name), address (street, city, state), tel, email, sex, registration_date|
| Examination   | id, date and time, doctor_id, patient_id, results, treatment_id|
| Treatment     | id, description, doctor_id, cost        |
| СryogenicСhamber | id, size, status, patient_id        |
| Invoice          | id, date_issue, date_paid, payment_method, treatment_id       |
| StockItem        | id, name, description, cost, quantity       |
| StockPharmacy    | id, name, description, dosage, method_admin, cost, quantity        |

## Entities

### Center

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| street | VARCHAR(50) | NO ||NULL||
| city | VARCHAR(50) | NO ||NULL||
| home | VARCHAR(50) | NO ||NULL||
| tel | CHAR(13) | NO ||NULL||
| fax | VARCHAR(50) | NO ||NULL||

### Staff

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int    | NO | PRI | NULL | AUTO_INCREMENT |
| first_name  | VARCHAR(50) | NO ||NULL||
| middle_name | VARCHAR(50) | NO ||""||
| last_name   | VARCHAR(50) | NO ||NULL||
| street | VARCHAR(50) | NO ||NULL||
| city | VARCHAR(50) | NO ||NULL||
| home | VARCHAR(50) | NO ||NULL||
| sex | ENUM('M', 'W') | NO ||NULL||
| tel | CHAR(13) | NO ||NULL||
| email | VARCHAR(50) | NO ||NULL||
| iin | CHAR(6) | NO ||NULL||
| position | VARCHAR(50) | NO ||NULL||
| salary | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| center_id | INT | NO | MUL |NULL| |
| role | ENUM("Admin", "Manager", "Stuff") | NO ||NULL||

Position can be enum.

### Patient

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int    | NO | PRI | NULL | AUTO_INCREMENT |
| first_name  | VARCHAR(50) | NO ||NULL||
| middle_name | VARCHAR(50) | NO ||""||
| last_name   | VARCHAR(50) | NO ||NULL||
| street | VARCHAR(50) | NO ||NULL||
| city | VARCHAR(50) | NO ||NULL||
| home | VARCHAR(50) | NO ||NULL||
| sex | ENUM('M', 'W') | NO ||NULL||
| tel | CHAR(13) | NO ||NULL||
| email | VARCHAR(50) | NO ||NULL||
| iin | CHAR(6) | NO ||NULL||
| registration_date | DATE | NO | |NULL| |
| center_id | INT | NO | MUL |NULL| |


### Examination

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| time | DATETIME | NO ||NULL||
| doctor_id | int | NO |MUL|NULL||
| patient_id | int | NO |MUL|NULL||
| results | TEXT | NO ||NULL||
| treatment_id | int | NO |MUL|NULL||
| invoice_id | int | NO |MUL|NULL||

### Treatment

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| description | TEXT | NO ||NULL||
| doctor_id | INT | NO |MUL|NULL||
| cost | DECIMAL(10, 2) | NO ||NULL| POSITIVE |

### СryogenicСhamber

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| size | ENUM('HEAD', 'SMALL', 'MEDIUM', 'LARGE') | NO ||NULL||
| status | ENUM('OCCUPIED', 'FREE') | NO ||NULL||
| patient_id | int | YES |MUL|NULL||

### Invoice

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| date_issue | DATE | NO ||NULL||
| date_paid | DATE | YES ||NULL||
| payment_method | ENUM('CARD', 'CASH', 'CHECK') | NO ||NULL||

### StockItem

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| name | VARCHAR(50) | NO ||NULL||
| description | TEXT | NO ||NULL||
| cost | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| quantity | INT | NO | MUL |NULL| POSITIVE |
| center_id | INT | NO | MUL |NULL|  |



### StockPharmacy

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| name | VARCHAR(50) | NO ||NULL||
| description | TEXT | NO ||NULL||
| dosage | TEXT | NO ||NULL||
| on_prescription | ENUM('YES', 'NO') | NO ||NULL||
| cost | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| quantity | INT | NO | MUL |NULL| POSITIVE |
| center_id | INT | NO | MUL |NULL|  |

## Database Information Scheme 

![Database Information Model](https://user-images.githubusercontent.com/79222536/193947014-9942b2fa-3543-4628-8c82-be297c7cb6d2.png)

# Database design, pt.2: Normalized

### Center

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| address_id | INT | NO | MUL |NULL| UNIQUE |
| contact_id | INT | NO | MUL |NULL| UNIQUE |

### Staff

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int    | NO | PRI | NULL | AUTO_INCREMENT |
| fullname_id  | INT | NO | MUL |NULL||
| address_id | INT | NO | MUL |NULL||
| contact_id | INT | NO | MUL |NULL| UNIQUE |
| sex | ENUM('M', 'W') | NO ||NULL||
| iin | CHAR(6) | NO ||NULL| UNIQUE |
| position | VARCHAR(50) | NO ||NULL||
| salary | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| center_id | INT | NO | MUL |NULL| |
| role | ENUM("Admin", "Manager", "Stuff") | NO ||NULL||

Position can be enum.

### Patient

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int    | NO | PRI | NULL | AUTO_INCREMENT |
| fullname_id  | int | NO | MUL |NULL||
| address_id | int | NO | MUL |NULL||
| contact_id  | int | NO | MUL |NULL| UNIQUE |
| sex | ENUM('M', 'W') | NO ||NULL||
| registration_date | DATE | NO | |NULL| CHECK(registration_date <= CURRENT_DATE)|


### Examination

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| time | DATETIME | NO ||NULL| CHECK(time <= CURRENT_TIME)|
| doctor_id | int | NO |MUL|NULL||
| patient_id | int | NO |MUL|NULL||
| results | TEXT | NO ||NULL||

### Treatment

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| description | TEXT | NO ||NULL||
| doctor_id | INT | NO |MUL|NULL||
| invoice_id | int | NO |MUL|NULL| UNIQUE |
| examination_id | int | NO |MUL|NULL||

### СryogenicСhamber

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| size | ENUM('HEAD', 'SMALL', 'MEDIUM', 'LARGE') | NO ||NULL||
| status | ENUM('OCCUPIED', 'FREE') | NO ||NULL||
| patient_id | int | YES | MUL |NULL| UNIQUE |
| center_id | INT | NO | MUL |NULL|  |

### Invoice

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| date_issue | DATE | NO ||NULL| CHECK(date_paid <= CURRENT_DATE)|
| date_paid | DATE | YES ||NULL| CHECK(date_paid <= CURRENT_DATE)|
| cost | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| payment_method | ENUM('CARD', 'CASH', 'CHECK') | YES ||NULL||

### StockItem

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| name | VARCHAR(50) | NO ||NULL| UNIQUE |
| description | TEXT | NO ||NULL||
| cost | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| quantity | INT | NO | MUL |NULL| POSITIVE |
| center_id | INT | NO | MUL |NULL|  |



### StockPharmacy

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| name | VARCHAR(50) | NO ||NULL| UNIQUE |
| description | TEXT | NO ||NULL||
| dosage | TEXT | NO ||NULL||
| on_prescription | ENUM('YES', 'NO') | NO ||NULL||
| cost | DECIMAL(10, 2) | NO ||NULL| POSITIVE |
| quantity | INT | NO | MUL |NULL| POSITIVE |
| center_id | INT | NO | MUL |NULL| |

### Address

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| city | VARCHAR(50) | NO ||NULL||
| street | VARCHAR(50) | NO ||NULL||
| home | VARCHAR(50) | NO ||NULL||

### Fullname

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| first_name  | VARCHAR(50) | NO ||NULL||
| middle_name | VARCHAR(50) | NO ||""||
| last_name   | VARCHAR(50) | NO ||NULL||

### Contact

| Field         | Type            | Null            | Key             | Default         | Extra           |
|:------------- |:--------------- |:--------------- |:--------------- |:--------------- |:--------------- |
| id | int  | NO | PRI | NULL | AUTO_INCREMENT |
| tel | CHAR(13) | NO ||NULL||
| email | VARCHAR(50) | NO ||NULL||
| fax | VARCHAR(50) | YES ||NULL||

## Logical Database Schema 

![Logical Database Schema](https://user-images.githubusercontent.com/79222536/199508369-49fdb5b7-8f60-4555-afc7-9cb776831443.png)
![Logical Database Schema (2)](https://user-images.githubusercontent.com/79222536/199528428-48a4332e-45c5-467b-9e37-81c17c06b9d1.png)
