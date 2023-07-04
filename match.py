def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(400))

def http_error_short(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
        
print(http_error_short(403))