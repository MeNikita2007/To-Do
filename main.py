class ToDo:
    def __init__(self):
        self.issue = {}
        self.count = 0
        
    def add_issue(self, issue, clock, complete):
        self.issue[issue] = [clock, complete]
        self.count += 1
        
    def delete_issue(self, issue):
        self.issue.pop(issue)
        self.count -= 1
        
    def get_count(self):
        return self.count
    
    def change_issue(self, issue):
        temp = self.issue.get(issue)
        temp[1] = True
        self.issue.update({issue:temp})
        
    def show(self):
        nums = 1
        for key,value in self.issue.items():
            print(f'{nums}.{key} time: {value[0]} {'Complete'if value[1] else 'Not Complete'}')
            nums += 1
            
            

todo = ToDo()
todo.add_issue('Breakfast', '07:30', True)
todo.add_issue('Cleaning', 'Never', False)
todo.add_issue('Pokormit_kota', '16:00', False)
todo.show()
todo.change_issue('Pokormit_kota')
todo.show()