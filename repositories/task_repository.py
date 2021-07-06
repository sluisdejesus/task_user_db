from db.run_sql import run_sql
from models.task import Task

#Read in CRUD
def select_all():
#create sql statement
    tasks = []
    sql = 'SELECT * FROM tasks'

# execute sql statement
# get results
    results = run_sql(sql)
    for row in results:
        
        task = Task(
            row['description'], 
            row['user_id'], 
            row['duration'], 
            row['completed'], 
            row['id']
            )
        
        tasks.append(task)

#return results
    return tasks

#Create in CRUD
def save(task):
    sql = f"INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.description, task.user_id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

#read one
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        task = Task(result['description'], result['user_id'], result['duration'], result['completed'], result['id'])

    return task

#DELETE ALL
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

# DELETE ONE
def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE
def update(task):
    sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.user_id, task.duration, task.completed, task.id]
    run_sql(sql, values)