from simple_salesforce import Salesforce
import pandas as pd
import streamlit as st
import os

# Salesforce login credentials
username = st.secrets.salesforce.username
password = st.secrets.salesforce.password
security_token = st.secrets.salesforce.security_token

objects = 


sf = Salesforce(username=username, password=password, security_token=security_token)["Account", "Asset", "Contact", "Contract", "Clinical_Trainings__c", "Consumables__c", "Customer", "Lead", "Opportunity", "Event", "Campaign", "Product2", "Pricebook2", "Order", "OrderItem", "Quote", "OpportunityLineItem", "QuoteLineItem", "User", "Territory2", "Case"]

os.makedirs('SalesforceDocs', exist_ok=True)

# Process each specified object
for obj_name in objects:
    try:
        # Get the description of the object
        obj_desc = sf.__getattr__(obj_name).describe()
        
        # Markdown file path
        file_path = os.path.join('SalesforceDocs', f"{obj_name}.md")
        
        # Open the Markdown file for writing
        with open(file_path, 'w') as md_file:
            # Write the object name and label
            md_file.write(f"# {obj_desc['label']} ({obj_name})\n\n")
            md_file.write(f"**Description:** {obj_desc['labelPlural']}\n\n")
            
            # Create a table for fields
            md_file.write("## Fields\n")
            md_file.write("| API Name | Type | Formula | Help Text | Attributes |\n")
            md_file.write("| --- | --- | --- | --- | --- |\n")
            
            # Iterate through fields and fill in the table
            for field in obj_desc['fields']:
                formula = field.get('calculatedFormula', 'N/A')
                help_text = field.get('inlineHelpText', 'N/A')
                # Comma-separated attributes for better readability in plain Markdown
                attributes = "; ".join(f"{k}: {v}" for k, v in field.items() if k not in ['name', 'type', 'calculatedFormula', 'inlineHelpText'])
                md_file.write(f"| {field['name']} | {field['type']} | {formula} | {help_text} | {attributes} |\n")
    except Exception as e:
        print(f"Failed to process {obj_name}: {str(e)}")

print("Markdown files created successfully in the SalesforceDocs directory.")