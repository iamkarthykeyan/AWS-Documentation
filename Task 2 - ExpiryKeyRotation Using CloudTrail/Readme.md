# Project Documentation

# Documentation: Configuration steps of Expiry Key Rotation setup  
  
## Overview:  
### This documentation outlines the steps to:  

1.	AWS CloudTrail: Monitors API calls for creating new access keys and  triggers the workflow.  
2.	Amazon EventBridge: Filters the CreateKey event from CloudTrail and  forwards it to a Lambda function.  
3.	Lambda Functions:  
•	Creation Lambda: Stores details about the created keys (source IP address, creation time, CloudTrail event, and access  key) in DynamoDB.  
•	Notification Lambda: Handles email notifications through Amazon 
SES when keys expire.  
4.	Amazon DynamoDB: Stores the access key details along with Time- to-Live (TTL) for automated expiration.  
5.	Amazon Simple Email Service (SES): Sends email notifications to the user when key expiration is near or triggered.  


Here is my Architecture :

 ![Architecture Image](./Architecture%20Model/architectureimage.png)

You can view the project documentation by clicking the link below:

[View the PDF Documentation](./docs/KARTHIKEYAN%20J%20-%20ExpiryKeyRotation%20using%20Cloudtrail%20with%20SES.pdf)
