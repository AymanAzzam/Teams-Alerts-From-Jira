# Libraries
from jira import JIRA
import pymsteams
 
# Configurations
jira = JIRA('<jira-host-url>',token_auth='<your-personal-token>')
teams_message = pymsteams.connectorcard('<teams-webhook>')
message_section = pymsteams.cardsection()
 
 
# Get the needed info from Jira
issues = jira.search_issues('project=<jira-project-name> and status=open')
for issue in issues:
    num = issue.key
    link = "<the-custom-url-of-project>" + num
    message_section.addFact("Num: ", num) 
    message_section.addFact("URL: ", link)
 
# Send the message to Jira
if len(issues) > 0:
    message_section.addTitle()
    teams_message.text(str(len(issues)) + " New Alerts")
    teams_message.addSection(message_section)
    teams_message.send()
