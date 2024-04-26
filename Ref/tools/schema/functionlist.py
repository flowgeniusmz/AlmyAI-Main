import json
import tools.executable as functions


# Define the available functions
functionslist = [
        {
            "name": "internet_search",
            "description": "Search the internet",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        },
        {
            "name": "create_record",
            "description": "Inserts/Updates records into the database",
            "parameters": {
                "type": "object",
                "properties": {
                    "sObjectType": {"type": "string"},
                    "records": {"type": "string"},
                    "operation": {"type": "string"}
                },
                "required": ["sObjectType", "records", "operation"]
            }
        },
        {
            "name": "get_sobject_fields",
            "description": "Get fields metadata for a SObject. Do not use when asked to get a list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sobject": {"type": "string"}
                },
                "required": ["sobject"]
            }
        },
        {
            "name": "extract_webpage_info",
            "description": "find information in webpage",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                    "target_info": {"type": "string"}
                },
                "required": ["url"]
            }
        },
        {
        "name": "run_soql_agent_tool",
        "description": "Executes a SOQL query and returns JSON results.",
        "parameters": {
            "type": "object",
            "properties": {
                "sql": {"type": "string"}
                },
            "required": ["sql"]
            }
        },
        {
        "name": "schedule_meeting_tool",
        "description": "Please schedule a meeting.",
        "parameters": {
            "type": "object",
            "properties": {
            "attendee": {
                "type": "string",
                "description": "Attendee for the meeting"
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting"
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting"
            }
            }
        }
        },
        {
        "name": "stock_info_tool",
        "description": "Retrieve information about a stock ticker or list of tickers.",
        "parameters": {
            "type": "object",
            "properties": {
            "tickers": {
                "type": "array",
                "items": {
                "type": "string"
                },
                "description": "The stock ticker or list of tickers to retrieve information for."
            },
            "action": {
                "type": "string",
                "description": "The type of information to retrieve. Can be one of 'info', 'history', 'actions', 'dividends', 'splits', 'income_stmt', 'balance_sheet', 'cashflow', 'major_holders', 'institutional_holders', 'mutual_funds', 'options', 'news'."
            }
            },
            "required": ["tickers", "action"]
        }
        },
        {
        "name": "almy_get_opportunity_id",
        "description": "Get ID of an Opportunity linked to set account.",
        "parameters": {
            "type": "object",
            "properties": {
                "opportunity_name": {
                    "type": "string",
                    "description": "opportunity to query"
                    }
                    },
            "required": ["opportunity_name"]
            }
        },
        {
            "name": "almy_add_product_into_opportunity",
            "description": "Get Add Salesforce Product into Opportunity.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"},
                    "quantity": {"type": "integer"},
                    "opportunity_id": {"type": "string"},
                    "pricebook_name": {"type": "string"},
                    "custom_total_price": {"type": "string"}
                },
                "required": ["product_name", "quantity"]
            }
        },
        {
            "name": "almy_create_new_opportunity",
            "description": "Get Create Salesforce Opportunity object.",
            "parameters": {
                "type": "object",
                "properties": {
                    "close_date": {"type":"string"},
                    "opportunity_name": {"type":"string"},
                    "stage_name": {"type":"string"},
                    "account_name": {"type":["string", "null"]}
                },
                "required": ["close_date", "opportunity_name", "stage_name"]
            }
        },
        {
            "name": "almy_create_salesforce_object",
            "description": "Get Create Salesforce object by type and data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "object_type": {"type": "string"},
                    "object_data": {"type": "string"}
                },
                "required": ["object_type", "object_data"]
            }
        },
        {
            "name": "almy_describe_salesforce_object",
            "description": "Get Get Salesforce object description by type.",
            "parameters": {
                "type": "object",
                "properties": {
                    "object_type": {"type": "string"}
                },
                "required": ["object_type"]
            }
        },
        {
            "name": "almy_get_salesforce_object_by_id",
            "description": "Get Salesforce object by id and type.",
            "parameters": {
                "type": "object",
                "properties": {
                    "object_type": {"type": "string"},
                    "object_id": {"type": "string"}
                },
                "required": ["object_type", "object_id"]
            }
        },
        {
            "name": "almy_salesforce_query",
            "description": "Get Perform SQL query and return result as dict or Table. As table should be always FALSE",
            "parameters": {
                "type": "object",
                "properties": {
                    "sql_string": {"type": "string"},
                    "as_table": {"type": "boolean"}
                },
                "required": ["sql_string", "as_table"]
            }
        },
        {
            "name": "almy_salesforce_query_result_as_table",
            "description": "Get Shorthand for Salesforce Query ${sql_string} as_table=${True}.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sql_string": {"type": "string"}
                },
                "required": ["sql_string"]
            }
        },
        {
            "name": "almy_create_new_lead",
            "description": "Create a new lead in salesforce",
            "parameters": {
                "type": "object", 
                "properties": {
                    "phone": {"type": "string"},
                    "firstname": {"type": "string"},
                    "lastname": {"type": "string"},
                    "email": {"type": "string"}, 
                    "company": {"type": "string"},
                    "postal": {"type": "string"},
                    "state": {"type": "string"}
                },
                "required": ["phone", "firstname", "lastname", "email", "company", "postal", "state"]
            }
        }
    ]

available_functions_list = {
    "internet_search": functions.internet_search,
    "create_record": functions.create_record,
    "get_sobject_fields": functions.get_sobject_fields,
    "extract_webpage_info": functions.extract_webpage_info,
    "run_soql_agent_tool": functions.run_soql_agent_tool,
    "schedule_meeting_tool": functions.schedule_meeting_tool,
    "stock_info_tool": functions.stock_info_tool,
    "almy_get_opportunity_id": functions.AlmySalesforce().almy_get_opportunity_id,
    "almy_create_new_opportunity": functions.AlmySalesforce().almy_create_new_opportunity,
    "almy_add_product_into_opportunity": functions.AlmySalesforce().almy_add_product_into_opportunity,
    "almy_create_salesforce_object": functions.AlmySalesforce().almy_create_salesforce_object,
    "almy_describe_salesforce_object": functions.AlmySalesforce().almy_describe_salesforce_object,
    "almy_salesforce_query": functions.AlmySalesforce().almy_salesforce_query,
    "almy_create_new_lead": functions.AlmySalesforce().almy_create_new_lead,
    "almy_salesforce_query_results_as_table": functions.AlmySalesforce().almy_salesforce_query_result_as_table
}