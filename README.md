# PMU Mentor
## Peer Mentorship Application

Code snippets from a platfrom designed specifically to support and adhere to the needs of PMU students. 
It is a collaborative space where more experienced students, referred to as mentors, can offer their guidance, support, and knowledge to less experienced students, referred to as mentees. This application aims to help the mentees in their studies and prepare them for the competitive job market.

## Features
- **Account Creation**
- **Login**
- **View Study Sessions Requests**

## Prerequisites
Python 3.x must be installed on your system
- To check if Python is installed, open your terminal/command prompt and type `python --version` or `python3 --version`

## Usage Guide
1. Navigation: The program uses a numbered menu system. Enter the number corresponding to the option you want (1: Create Account & 2: Login)
2. Inputs: Follow the on-screen prompts

## Example Workflow (View session requests)
```Session ID: MS2025-12
  Status: pending
  Mentor: 202300308@pmu.edu.sa
  Mentee: 202300994@pmu.edu.sa
  Time: None to None
  Minutes: 
  Feedback: Good session

Session ID: MS2025-90
  Status: accepted
  Mentor: 202301446@pmu.edu.sa
  Mentee: 202300288@pmu.edu.sa
  Time: 13:00 18-12-2025 to 14:00 18-12-2025
  Minutes: 60 minutes
  Feedback: Bad mentor

Session ID: MS2025-21
  Status: declined
  Mentor: 202300316@pmu.edu.sa
  Mentee: 202300481@pmu.edu.sa
  Time: 8:00 4-1-2026 to 10:00 4-1-2026
  Minutes: 120 minutes
  Feedback: Very supportive mentor

Test viewSessionRequest:
   Look for session MS2025-12: 
   Result: {'sessionID': 'MS2025-12', 'mentor': '202300308@pmu.edu.sa', 'mentee': '202300994@pmu.edu.sa', 'status': 'pending', 'start': None, 'end': None, 'mins': '', 'feedback': 'Good session'}
   Look for non-existent session MS2025-999:
   Result: No session found with this ID

Test acceptRequest:
   Before accepting [Status of MS2025-12]:  pending
   Accept request MS2025-12: Request accepted
   After accepting [Status of MS2025-12]:  accepted

Test declineRequest:
   Before declining [Status of MS2025-21]:  declined
   Decline request MS2025-21: Request already declined
   After declining [Status of MS2025-21]:  declined

Test scheduleSession:
   Schedule session MS2025-12:  Session scheduled
   New schedule [Start time: 14:30 End time]: 15:30

Test recordMinutes:
   Record minutes for MS2025-12:  Meeting minutes saved
   New minutes:  60 minutes of Python

Test getFeedback and viewFeedback:
   getFeedback for MS2025-90:  Very supportive mentor
   viewFeedback for MS2025-90:  Very supportive mentor

Test error cases:
   Accept non-existent session MS2025-55:  Request not found
   Schedule non-existent session MS2025-29:  Session is not found```
   
## References
1. [w3schools](https://www.w3schools.com/python/python_dictionaries.asp) : used to comprehend and apply the knowledge of Python dictionaries
