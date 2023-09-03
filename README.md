# Teams-Alerts-From-Jira
This project is used to send notification messages on Teams channel based on Jira tickets

## Pre-Requisites
1. Automation Server
2. Jira-python installed on the ECS
  - Reference: https://jira.readthedocs.io/installation.html
3. Channel on Teams

## General Idea
1. The Automation Server communicate with Jira to check if there is any open ticket and not assigned to anyone
2. Jira Reply to the Automation server with the needed info
3. The Automation Server process the given data 
4. The Automation Server sends a message to teams channel if needed

## Steps
We will split the steps into small sub-steps as following

1. Jira Steps
2. Teams Steps
3. Automation Scripts

### Jira Steps
1. Create a personal token on Jira
  - Go to your profile
  - Select **Personal Access Tokens**
  - Click **Create Token**
  - Enter a **Token Name**
  - Disable the **Automatic expiry**
  - Click **Create**
  - Copy the personal token and paste it in a save place to use it later

### Teams Steps
1. Create Incoming Webhook on Your channel
  - Open your channel
  - Select Connectors from the dropdown menu
  - Search for **Incoming Webhook** and select Add
  - Select Configure and fill the data
  - Copy and save the unique webhook URL present in the dialog. The URL maps to the channel and you can use it to send information to Team
  - Select Done
  - Reference: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet

### Automation Scripts
We have two automation scripts and one command to run them
1. **jira_teams.py**
2. **cron.py**
  - It runs the **jira_teams.py** script then sleep 1 minute and run it again then sleep 1 minute .... forever till you kill this process
