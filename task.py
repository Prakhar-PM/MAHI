#function
import datetime

from main import Say
#2 types

#1 - non-input
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)
    
def NonInputExecution(query):
    
    query = str(query)
    
    if "time" in query:
        Time()
        
    elif "date" in query:
        Date()         
#2 - input
#eg - google search ,wikipedia

    
    
def InputExecution(tag,query):
    if wikipedia in tag:
        name = str(query).replace("","")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)