import re
import random
class RuleBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later","thanks","thank you","ok thank you")
    random_questions = (
        "why are you here?\n",
        "how can I help you?\n",
        "what do you want to know about the MCA department?\n",
    )
    
    def _init_(self):
        self.alien = {
            'describe_MCA_department_intent': r'.(MCA department|department of MCA|department intent|department|vision|vision of department).',
            'admission_process': r'.(admission process|admission|apply|admission criteria|enrollment|enroll).',
            'about_syllabus': r'.(syllabus|curriculum|subjects|outline|program|modules).',
            'about_courses': r'.(courses|Courses|courses detail|).',
            'eligibility_criteria': r'.(eligibility criteria|eligibility|Eligibility|Eligibility Criteria).',
            'teaching_Staff': r'.(teaching staff|faculty|staff member|teachers|Teachers|Teaching Staff).',
            'fee_structure': r'.(Fee|fee|fee structure|Fee Structure|Fee structure).',
            'contact': r'.(contact|Contact detail|Location|location|area|visit|Visit|Area).'
        }
    
    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am Rule-Bot.can I help you?\n")
        if will_help in self.negative_responses:
            print("OK, have a nice day! :)")
            return
        self.chat()
    
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("OK, have a nice day! :)")
                return True
    
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
    
    def match_reply(self, reply):
        for key, value in self.alien.items():
            intent = key
            regex_pattern = value
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'describe_MCA_department_intent':
                return self.describe_MCA_department_intent()
            elif found_match and intent == 'admission_process':
                return self.admission_process()
            elif found_match and intent == 'about_syllabus':
                return self.about_syllabus()
            elif found_match and intent == 'about_courses':
                return self.about_courses()
            elif found_match and intent == 'eligibility_criteria':
                return self.eligibility_criteria()
            elif found_match and intent == 'teaching_Staff':
                return self.teaching_Staff()
            elif found_match and intent == 'fee_structure':
                return self.fee_structure()
            elif found_match and intent == 'contact':
                return self.contact()
        if not found_match:
            return self.no_match_intent()
    
    def describe_MCA_department_intent(self):
        responses = (
            "After getting approval from AICTE the university started MCA from the session 2007-08. It is the first AICTE approved department of Jharkhand State.\n\n"

         +"The mission statement of the University Department of Computer Applications is:\n\n"

         +"To become the prime custodian of all information resources on current and traditional knowledge systems in science and technology in the country and to promote communication in science to diverse constituents at all levels, using the most appropriate technologies for more information please visit VBU official website(www.vbu.ac.in)\n"
        )
        return (responses)
    
    def admission_process(self):
        responses = (
            "Following instruction will help you in admission process in our department\n"
            +"step 1:You have to fill the form firstly for this you have to pay 1000 rs\n"
            +"step 2:At the given date you have to pass the entrance test and according to your rank you will get the college top 60 students will get our department\n"
        )
        return (responses)
    
    def about_syllabus(self):
        responses = (
            "MCA 1st semester:\n"
            +"=>Fundamentals of Computers\n"
            +"=>Data Structure through C\n"
            +"=>Operating System Concepts\n"
            +"=>Database management system\n"
            +"=>Computer Organization & Architecture\n"
            +"=>Management Information System\n"
             "MCA 2nd semester:\n"
            +"=>Advance java Programming\n"
            +"=>Design and analysis of Algorithm\n"
            +"=>Data Communication & Computer Networks\n"
            +"=>Discrete mathematics\n"
            +"=>Software Engineering\n"
             "MCA 3rd semester:\n"
            +"=>Data Warehouseing & Data Mining\n"
            +"=>Compiler Design\n"
            +"=>Programming in Python\n"
            +"=>Soft computing\n"
            +"=>Financial Accounting\n"
             "MCA 4th semester:\n"
            +"=>Computer Graphics\n"
            +"=>Operation Research\n"
        )
        return (responses)
    def about_courses(self):
        responses = ("=>Bachelor Of Computer Application\n=>Master Of Computer Application"
        )
        return (responses)
    def eligibility_criteria(self):
        responses = (
            "All Applicants must posses a general education diploma(12 year school leaving certificate) having cs background or having maths background for admission in BCA and for taking admission in MCA student must completed BCA degree or must be graduated in mathematics\n"
        )
        return (responses)
    def teaching_Staff(self):
        responses = (
            "All teaching staff of MCA department are:\n\n"
            +"Dr. Santosh kumar Srivastava\n"
            +"Ph.D.(computer Applications),M.Phil(C.S.),MCA\n"
            +"Area of Specialization-Wireless Network, Mathematical Modeling,Network Security\n"
            +"...............................................................................\n\n"
            
            +"Sunil kumar Rajwar\n"
            +"Ph.D.(computer Applications),MCA,UGC NET\n"
            +"Area of Specialization-Network Security,soft computing, Macine Learning\n"
            +"...............................................................................\n\n"
            +"Dr.Santosh kumar Singh\n"
            +"Ph.D.(computer Applications),Ph.D(Computer Science),MCA, M.phil(Computer Science)\n"
            +"Area of Specialization-Network Security,soft computing, Macine Learning\n"
            +"...............................................................................\n\n"
            +"Prabhat kumar\n"
            +"Ph.D.(computer Applications),MCA,UGC NET\n"
            +"Area of Specialization-compiler design,Theory of Computation,Computerized Financial Accounting\n"
            +"...............................................................................\n\n"
           +"Rahul Prasad\n"
            +"M.Tech,MCA\n"
            +"Area of Specialization-OOPS,Data structure,DBMS\n"
            +"...............................................................................\n\n"
            +"Manisha Baxla\n"
            +"B.TECH(Computer Science)\n"
            +"Area of Specialization-Operating System,Software Engineering\n"
            +"...............................................................................\n\n"
        )
        return (responses)
    def fee_structure(self):
        responses = (
            "Fee Structure for MCA and BCA courses:\n"
            +"BCA=> 15000.00 per semester(6 semester)\n"
            +"Mca=> 28000.00 per semester(4 semester)\n"
        )
        return (responses)
    def contact(self):
        responses = (
            "\nFor admission or other details, you can contact\n\n"
            +"Phone no.: (06546)261920\n"
            +"E-mail id: vbumca@gmail.com\n"
            +"Department Of Computer Applications\nVinoba Bhave University,sindur,Hazaribagh-825301\nFax:(06546)264279"
        )
        return (responses)
    def no_match_intent(self):
        responses = (
            "I'm sorry, I didn't understand what you're asking. Could you please rephrase the question?\n",
            "I'm not sure what you're looking for. Would you like me to direct you to the university's official website?\n"
        )
        return random.choice(responses)
studentBot=RuleBot()
studentBot.greet()