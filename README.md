# Teams-Alerts-From-Jira
This project is used to send notification messages on Teams channel based on the status of Jira tickets

Confluence Page: https://ayman-azzam.atlassian.net/wiki/spaces/~712020f9f917cdb4b94d0e812d7cdfbabf1081/pages/589825/Teams+Alerts+from+Jira

## Pre-Requisites
1. Automation Server
2. Jira-python installed on the Automation Server
    - Reference: https://jira.readthedocs.io/installation.html
3. Channel on Teams

## General Idea
1. The Automation Server communicate with Jira to check if there is any open tickets
2. Jira Reply to the Automation server with the needed info
3. The Automation Server process the given data 
4. The Automation Server sends a message to teams channel if needed

## Steps
We will split the steps into small sub-steps as following

1. Jira Steps
2. Teams Steps
3. Automation Scripts

### Jira Steps
Create a personal token on Jira
  1. Go to your profile
  2. Select **Personal Access Tokens**
  3. Click **Create Token**
  4. Enter a **Token Name**
  5. Disable the **Automatic expiry**
  6. Click **Create**
  7. Copy the personal token and paste it in a save place to use it later

### Teams Steps
Create Incoming Webhook on Your channel
  1. Open your channel
  2. Select Connectors from the dropdown menu
  3. Search for **Incoming Webhook** and select Add
  4. Select Configure and fill the data
  5. Copy and save the unique webhook URL present in the dialog. The URL maps to the channel and you can use it to send information to Team
  6. Select Done
  7. Reference: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet

### Automation Scripts
We have two automation scripts and one command to run them
1. **jira_teams.py**
2. **cron.sh**
    - This script act as a cron job that runs the **jira_teams.py** script then sleep 1 minute and run it again then sleep 1 minute .... forever till you kill this process
    - I faced an issue related to mail server When I tried to use the **crontab** instead of this script
        - I will investigate in it later when I get more knowledge about mail servers
