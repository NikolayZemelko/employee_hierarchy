

## [Employees-hierarchy-app.onrender.com](https://employees-hierarchy-app.onrender.com/)
### Task:

Create a web page that will display the employee hierarchy in tree form.

### Information about each employee must be stored in a database and contain the following data:

* _FULL NAME;_
* _Job title;_
* _Employment date;_
* _Salary amount;_
* _Each employee has 1 boss;_
* _The database must contain at least 50,000 employees and 5 levels_
hierarchies.
* Don't forget to display the employee's position.

### Additional requirements:

- [x] Create the database using Django/Flask migrations.
- [x] Use DB seeder for Django ORM / Flask-SQLAlchemy to seed the database.
- [x] Use Twitter Bootstrap to create basic styling for your page.
- [x] Create another page and display a list of employees with all the information available about the employee from the database and the ability to sort by any field.
- [x] Add the ability to search for employees by any field for the page created in task 4.
- [ ] Add the ability to sort (and search if you completed task No5) by any field without reloading the page, for example using ajax.
- [x] Using standard Django/Flask functions, authenticate the user for the registered user-only section of the website.
- [x] Move the functionality developed in tasks 4, 5 and 6 (using ajax requests) to a section available only to registered users.
- [ ] In the section available only to registered users, implement the remaining CRUD operations for employee records. Please note that all fields related to users must be editable, including the boss of each employee.
- [ ] Make it possible to upload a photo of an employee and display it on the page where you can edit information about the employee. Add an additional column with a thumbnail photo of the employee on the list of all employees page.
- [ ] Implement the ability to redistribute employees in case of a change in boss (a bonus may be that you can do this using the built-in mechanisms/paradigms offered by Django ORM / Flask-SQLAlchemy ORM).
- [ ] Implement lazy loading for the employee tree. For example, show the first two levels of the hierarchy by default and load the next 2 levels or the entire tree branch when you click on a second-level employee.
- [ ] Implement the ability to change an employee's boss using drag-n-drop directly in the employee tree.

### Installation:

To start demo you need installed `postgres` or installed `docker-compose`

### Running:

#### With Poetry:
1. Install dependencies use `poetry install`
2. Run app with `make start`

#### With Docker-Compose:
1. Use command `make docker-start`

#### Usage:
    