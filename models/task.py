class Task:
    
    def __init__(self, description, user_id, duration, completed = False,  id = None, ):
        self.description = description
        self.user_id = user_id
        self.duration = duration
        self.completed = completed
        self.id = id
        
    def mark_complete(self):
        self.completed = True

   