class Worker:
    title = ''
    pay = ''
    def set_title(self, title):
         self.title = title
    def set_pay(self, pay):
        self.pay = pay

class TeamMember:
    project = ''
    def set_project(self, project):
        self.project = project
 
class TeamLeader(TeamMember, Worker):
    def set_exp(self,exp):
        self.experience = exp
    def details(self):
        print(f"\nTitle : {self.title}")
        print(f"\nPay : {self.pay}")
        print(f"\nProject : {self.project}")
        print(f"\nExperience : {self.experience} years")
