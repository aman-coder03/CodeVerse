import random

def error_comedy_response(error_type):
    responses = {
        "loop": ["Your loop is more lost than a penguin in the desert!"],
        "syntax": ["Syntax error? Looks like your code tripped on a banana peel!"]
    }
    return random.choice(responses.get(error_type, ["Oops, something's off!"]))
