import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listneing...")
        r.pause_threshold = 1
        audio = r.listen(source,0,2)#listning har 2 second pe record hogi
        
    try:
        print ("recognising...")
        query = r.recognize_google(audio,language="en-in")
        print(f"you said: {query}")     
        
    except :
        return ""
    
    query = str(query)
    return query.lower()

#Listen()
    