## Automated JIRA Issue Creation
This project automates the process of creating issues in JIRA using the JIRA REST API. Instead of manually creating tasks, this script enables automatic issue creation, ensuring efficiency, consistency, and accuracy in project tracking.
## Features 
 Automates JIRA issue creation using REST API
 Supports dynamic issue assignment based on predefined rules
 Ensures consistency in issue creation, reducing human error
 Uses API authentication for secure and authorized access
  Enhances productivity by reducing manual effort
## How It Works ⚙️
Fetches Project Details: Retrieves all available projects to validate issue creation.
Automates Issue Creation: Creates new JIRA issues with predefined fields such as summary, description, issue type, and priority.
Assigns Issues: Automatically assigns issues to team members.
Formats Response: The response is formatted and displayed in JSON for better readability.
##  API Details
Method: POST
The request body includes:
Project Key – Defines where the issue will be created
Issue Type – Task, Bug, Story, etc.
Summary & Description – Describes the issue
Assignee ID – Assigns it to the right user
Priority Level – Sets importance (High, Medium, Low)

