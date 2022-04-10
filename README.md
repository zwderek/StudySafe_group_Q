# StudySafe Group Q
This project consists of deliver two small pilot MVPs as a step towards HKU reopening its teaching venues safely.  
If the pilot study proves successful, full-scale versions will be developed.  
  
  
## StudySafe Core
A service that provides a RESTful API for maintaining records of thetimes at which members of HKU enter and exit
enclosed public venues such as classrooms and lecture theatres on campus.  
The purpose is to allow the COVID Task Force to identify HKU “close contacts” of any member who tests positive for the SARS-CoV-2 virus.  
  
  
## StudySafe Trace
Given details of an infected member of HKU, and a date of diagnosis or onset of symptoms, it will consume your StudySafe 
Core API to obtain close contacts of that member and the venues the member visited while infectious.
