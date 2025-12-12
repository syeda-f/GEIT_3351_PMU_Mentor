
#dummy database
session_requests = [
    {"sessionID":MS2025-12, "mentor":"nuhaak@pmu.edu.sa", "mentee":"202300994@pmu.edu.sa", "status": "pending", "start": None, "end": None, "mins": "", "feedback": "Good session"},
    {"sessionID":MS2025-90, "mentor":"wasana@pmu.edu.sa", "mentee":"202300288@pmu.edu.sa", "status": "accepted", "start": "13:00 18-12-2025", "end": "14:00 18-12-2025", "mins": "60 minutes", "feedback": "Bad mentor"},
    {"sessionID":MS2025-21, "mentor":"saraha@pmu.edu.sa", "mentee":"202301587@pmu.edu.sa", "status": "declined", "start": "8:00 4-1-2026", "end": "10:00 4-1-2026", "mins": "120 minutes", "feedback": "Very supportive mentor"},
]


def getRequest(sessionID):
    for req in session_requests:
        if req["sessionID"] == sessionID:
            return req
    return None

def viewSessionRequest(sessionID):
    req = getRequest(sessionID)
    if req is not None:
        return req
    else:
        return "No session found with this ID"

def updateStatus(sessionID, status):
    req = getRequest(sessionID)
    if req is not None:
        req["status"] = status
        return True
    else:
        return False

def acceptRequest(sessionID):
    req = getRequest(sessionID)
    if req is not None:
        if req["status"] == "accepted":
            return "Request already accepted"
        else:
            if updateStatus(sessionID, "accepted") is True:
                return "Request accepted"
    return "Request not found"

def updateShcedule(sessionID, startTime, endTime):
    req = getRequest(sessionID)
    if req is not None:
        req["start"] = startTime 
        req["end"] = endTime
        return True
    else:
        return False

def scheduleSession(sessionID, startTime, endTime):
    if updateShcedule(sessionID, startTime, endTime) is True:
        return "Session scheduled"
    else:
        return "Session is not found"

def recordSessionTime(sessionID, meetingMinutes):
    req = getRequest(sessionID)
    if req is not None:
        req["mins"] = meetingMinutes
        return True
    else:
        return False

def recordMinutes(sessionID, meetingMinutes):
    if recordSessionTime(sessionID, meetingMinutes) is True:
        return "Meeting minutes saved"
    else:
        return "No meeting minutes"

def declineRequest(sessionID):
    req = getRequest(sessionID)
    if req is not None:
        if req["status"] == "declined":
            return "Request already declined"
        else:
            if updateStatus(sessionID, "declined") is True:
                return "Request declined"
    return "Request not found"

def getFeedback(sessionID):
    req = getRequest(sessionID)
    if req is not None:
        return req["feedback"]
    else:
        return "Session ID not found"

def viewFeedback(sessionID):
    return getFeedback(sessionID)

def main(): 
    print()
    for session in session_requests:
        print("Session ID:", session["sessionID"])
        print("  Status:", session["status"])
        print("  Mentor:", session["mentor"])
        print("  Mentee:", session["mentee"])
        print("  Time:", session["start"], "to", session["end"])
        print("  Minutes:", session["mins"])
        print("  Feedback:", session["feedback"])
        print()

    print("Test viewSessionRequest:")
    print("   Look for session MS2025-12: ")
    print("   Result:", viewSessionRequest("MS2025-12"))
    print("   Look for non-existent session MS2025-999:")
    print("   Result:", viewSessionRequest("MS2025-999"))
    
    print()
    print("Test acceptRequest:")
    print("   Before accepting [Status of MS2025-12]: ", getRequest("MS2025-12")["status"])
    print("   Accept request MS2025-12:", acceptRequest("MS2025-12"))
    print("   After accepting [Status of MS2025-12]: ", getRequest("MS2025-12")["status"])
    
    print()
    print("Test declineRequest:")
    print("   Before declining [Status of MS2025-21]: ", getRequest("MS2025-21")["status"])
    print("   Decline request MS2025-21:", declineRequest("MS2025-21"))
    print("   After declining [Status of MS2025-21]: ", getRequest("MS2025-21")["status"])
    
    print()
    print("Test scheduleSession:")
    print("   Schedule session MS2025-12: ", scheduleSession("MS2025-12", "14:30", "15:30"))
    print("   New schedule [Start time:", getRequest("MS2025-12")["start"], "End time]:", getRequest("MS2025-12")["end"])
    
    print()
    print("Test recordMinutes:")
    print("   Record minutes for MS2025-12: ", recordMinutes("MS2025-12", "60 minutes of Python"))
    print("   New minutes: ", getRequest("MS2025-12")["mins"])
    
    print()
    print("Test getFeedback and viewFeedback functions:")
    print("   getFeedback for MS2025-90: ", getFeedback("MS2025-21"))
    print("   viewFeedback for MS2025-90: ", viewFeedback("MS2025-21"))
    
    print()
    print("Test error cases:")
    print("   Accept non-existent session MS2025-55: ", acceptRequest("MS2025-555"))
    print("   Schedule non-existent session MS2025-29: ", scheduleSession("MS2025-777", "10:00", "11:00"))
    
if __name__ == "__main__":
    main()
