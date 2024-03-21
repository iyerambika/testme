def evaluate_policy(user_data, policy):
    result = {}
    for group, conditions in policy.items():
        group_result = True
        for rule in conditions:
            for match in rule["matches"]:
                feild_name = match["field"]
                value_name = match["value"]
            if feild_name in user_data and user_data[field_name] == value_name:
                continue
            else:
                group_result = False
                break
            if not group_result:
              break
        result[group] = group_result
    return result                     
user_data = {
    "data": {
        "workday": {
            "fieldA": "xxx"
        }
    }
}
policy = {
    "groupA": [
        {
            "matches": [{
                "field": "workday.fieldA",
                "value": "xxx"
            }]
        }
    ],
    "groupB": [
        {
            "matches": [{
                "field": "workday.fieldA",
                "value": "yyy"
            }]
        }
    ]
}

result = evaluate_policy(user_data, policy)
print(result["groupA"] == True)
print(result["groupB"] == False)