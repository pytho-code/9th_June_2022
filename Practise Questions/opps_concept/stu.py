class studentclass:
        name=""
        email=""
        city=""
        marks=""
        contact=""
        fees=""
        subject=""

        dict={}
        def createstudent(self,stuname,stuemail,stucity,stumarks,stucontact,stufees,stusub):
            innerdict={}
            self.name=stuname
            self.email=stuemail
            self.city=stucity
            self.marks=stumarks
            self.contact=stucontact  
            self.fees=stufees
            self.subject=stusub

            innerdict['email']=self.email
            innerdict['city']=self.city
            innerdict['marks']=self.marks
            innerdict['contact']=self.contact
            innerdict['fees']=self.fees
            innerdict['subject']=self.subject

            self.dict[stuname]=innerdict
            print(self.dict)

