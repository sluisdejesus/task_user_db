DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  -- delete the assignee from tasks
  duration INT,
  completed BOOLEAN
);


INSERT INTO tasks (description, assignee, duration, completed)
VALUES ('get milk', 'Zsolt', 5, false);
INSERT INTO tasks (description, assignee, duration, completed)
VALUES ('walk hedgehog', 'John', 15, True);
INSERT INTO tasks (description, assignee, duration, completed)
VALUES ('cook dinner', 'Juan', 30, false);