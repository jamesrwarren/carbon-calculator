def validate(input):
    return input.strip().replace('<', '').replace('>', '').replace('\'', '\'\'')