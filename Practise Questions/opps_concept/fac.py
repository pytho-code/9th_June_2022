#self is to use class properties eg self.name which is variable of class 
class facultyclass:
        name=""
        email=""
        number=""
        subject=""
        city=""

        dict={}
        def createfaculty(self,name,email,number,sub,city):
            innerdict={}
            self.name=name
            self.email=email
            self.number=number
            self.subject=sub
            self.city=city

            innerdict['email']=self.email
            innerdict['number']=self.number
            innerdict['subject']=self.subject
            innerdict['city']=self.city

            self.dict[name]=innerdict
            print(self.dict)