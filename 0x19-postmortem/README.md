# Incident Report on site downtime 

### Issue Summary
On 12th May 2023 12:30 PM WAT, I noticed that the web-01 server hosting the static files for the AirBnB clone project was down. The system was still running as the load balancer was still using the web-02 to serve content.This increased the load and traffic that resulted in a downtime. The web-01 downtime was as a result not being able to connect to the server using its IP address.

### Timeline
- The issue was detected by 12:30PM WAT after deploying the static files on both servers
- The engineer noticed the deployment was not successful for the web-01. 
- Tries redeploying
- Edited nginx configuration files
- Escalated to a mentor
- Removing the files uploaded fixed the issue

### Root Cause and Resolution
The down time was linked to the unsuccessful deployment. To resolve this, I tried to redeploy the files again which further led to another error. I checked the nginx configuration file for both servers and found a discrepancy. I fixed it but the web-01 server was not connecting yet. I escalated to one of the mentors and the issue was fixed after removing the files uploaded for the unsuccessful deployment.

### Corrective and Preventive Measure
Error Logging will make failures easy to trace.

