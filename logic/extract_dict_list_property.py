def extract_dict_list_property_logic(dict_list, property_name):
    """
    Extracts a specified property from a list of dictionaries.
    This function iterates over a list of dictionaries and extracts the value
    of a specified property from each dictionary that contains the property.
    The extracted properties are returned in a new list of dictionaries.
    Args:
        dict_list (list): A list of dictionaries from which to extract the property.
        property_name (str): The name of the property to extract from each dictionary.
    Returns:
        dict: A dictionary containing a single key 'extracted_properties' which maps
              to a list of dictionaries, each containing the specified property and its value.
    Example:
        >>> dict_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie'}]
        >>> property_name = 'age'
        >>> extract_dict_list_property_logic(dict_list, property_name)
        {'extracted_properties': [30, 25]}
    """
    
    # Go to terminal and make it a HTTP request     
    results = []
    
    # Iterate over the list of dictionaries
    for dictionary in dict_list:
        # Check if the property exists in the dictionary
        if property_name in dictionary:
            results.append(dictionary[property_name])
    return {'extracted_properties': results}


# ------------------------------------------------
# Our tasks
test_data = [
    
]


# 1.) Let us generate some testdata with proeprties: "name", "action", "timestamp" for a banking inspired application
# 2.) Go to terminal and make it a HTTP request     
