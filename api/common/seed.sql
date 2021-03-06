\connect postgres

DROP DATABASE IF EXISTS project_management;

CREATE DATABASE project_management;

\connect project_management

CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255 ) NOT NULL
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cost MONEY NOT NULL,
    company_id INT NOT NULL REFERENCES company (id) ON DELETE CASCADE,
    parent_project_id INT REFERENCES project (id) ON DELETE CASCADE
);

CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    company_id INT NOT NULL REFERENCES company (id) ON DELETE CASCADE
);

CREATE TABLE employee_project (
    employee_id INT NOT NULL REFERENCES employee (id) ON DELETE CASCADE,
    project_id INT NOT NULL REFERENCES project (id) ON DELETE CASCADE
);
