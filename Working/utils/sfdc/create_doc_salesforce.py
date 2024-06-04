import pandas as pd
import os

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the CSV file
csv_path = os.path.join(dir_path, 'Key Salesforce Object Field List.csv')

# Read the file into a DataFrame
field_list = pd.read_csv(csv_path)
#print(field_list)


def generate_markdown_for_object(object_name, data):
    """
    Generate markdown description for a given Salesforce object.
    
    Args:
    - object_name (str): Name of the Salesforce object.
    - data (pd.DataFrame): DataFrame containing the Salesforce objects and fields data.
    
    Returns:
    - str: Markdown formatted description of the object.
    """
    
    # Extracting all fields associated with the given object
    object_fields = data[data['Object'] == object_name]
    #print(object_fields)

    # Formatting the fields into the desired Markdown structure
    markdown_output = f"""
## Table: Salesforce.{object_name}
### (Stores {object_name.lower()} information)

This table contains information about {object_name.lower()}s in Salesforce.

"""

    for index, row in object_fields.iterrows():
        field_label = row['Field']
        api_name = row['API Name']
        attributes = row['Attributes']

        # Generate a generic description for the field based on its label
        description = f"Information related to the {field_label.lower()} of the {object_name.lower()}"

        # If the field has a specific attribute (like "Required"), add it to the description
        if pd.notna(attributes):
            description += f" [{attributes}]"

        markdown_output += f"- **{api_name}**: Text - {description}\n"
    
    return markdown_output

def create_markdown_file(object, content):
    filepath = os.path.join('SalesforceDocs', f"{object}.md")
    with open(filepath, "w") as mdfile:
        mdfile.write(content)
        
# Generate markdown descriptions for the specified objects
objects_list = ["Account", "Asset", "Contact", "Contract", "Clinical_Trainings__c", "Consumables__c", "Customer", "Lead", "Opportunity", "Event", "Campaign", "Product2", "Pricebook2", "Order", "OrderItem", "Quote", "OpportunityLineItem", "QuoteLineItem", "User", "Territory2", "Case"]

markdown_outputs = {}
for obj in objects_list:
    content = generate_markdown_for_object(obj, field_list)
    markdown_outputs[obj]=content
    file = create_markdown_file(obj, content)



