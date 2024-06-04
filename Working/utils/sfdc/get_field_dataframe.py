from simple_salesforce import Salesforce
import pandas as pd
import streamlit as st

# Salesforce login credentials
username = st.secrets.salesforce.username
password = st.secrets.salesforce.password
security_token = st.secrets.salesforce.security_token

objects = ["Account", "Asset", "Contact", "Contract", "Clinical_Trainings__c", "Consumables__c", "Customer", "Lead", "Opportunity", "Event", "Campaign", "Product2", "Pricebook2", "Order", "OrderItem", "Quote", "OpportunityLineItem", "QuoteLineItem", "User", "Territory2", "Case"]


sf = Salesforce(username=username, password=password, security_token=security_token)

# List to hold all field records
all_fields = []

# Process each specified object
for obj_name in objects:
    try:
        # Use the correct method to describe the sobject
        obj_desc = sf.__getattr__(obj_name).describe()

        # Collect field details
        for field in obj_desc['fields']:
            field_details = {
                'Object': obj_desc['name'],
                'Field': field['label'],
                'API Name': field['name'],
                'Type': field['type'],
                'Formula': field.get('calculatedFormula', 'N/A'),  # Not all fields will have a formula
                'Help Text': field.get('inlineHelpText', 'N/A'),
                'Attributes': {k: v for k, v in field.items() if k not in ['name', 'type', 'calculatedFormula', 'inlineHelpText']}
            }
            all_fields.append(field_details)
    except Exception as e:
        print(f"Failed to process {obj_name}: {str(e)}")

# Convert list of dictionaries to DataFrame
df_fields = pd.DataFrame(all_fields)

# Show the DataFrame
print(df_fields)
df_fields.to_csv("Key Salesforce Object Field List.csv")

