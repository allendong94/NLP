def search(grammar_dict_log, matched_rules, temp):
    for key, value in grammar_dict_log.items():
        for list_of_rhs in value:
            if temp == list_of_rhs[0]:
                matched_rules.append([key, list_of_rhs[-1]])
    return matched_rules