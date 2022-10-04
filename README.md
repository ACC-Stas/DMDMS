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
    - Создание и храние записей, содержащих информацию о медицинских центрах DMDMS и их сотрудниках. (Admin)
    - Создание и храние записей, содержащих информацию о пациентах. (Admin, Manager)
    - Создание и храние записей, содержащих сведения о типах лечения. (Admin, Manager, Stuff)
    - Создание и храние записей, содержащих сведения о проведённых обследованиях. (Admin, Manager, Stuff)
    - Создание и храние записей, содержащих сведения о счетах за лечение. (Admin, Manager, Stuff)
    - Создание и храние записей, содержащих сведения о запасах в каждой из клиник. (Admin, Manager, Stuff)
    - Создание и храние записей, содержащих сведения о криогенных камерах. (Admin, Manager, Stuff)

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

