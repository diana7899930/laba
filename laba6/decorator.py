def utf8_converter(func):   
def wrapper(*args, **kwargs):             

        new_args = []                         

        for value in args:
            if isinstance(value, str):       
                utf_text = value.encode("utf-8")   
                new_args.append(utf_text)         
            else:
                new_args.append(value)             

        new_kwargs = {}                      

      
        for key, value in kwargs.items():
            if isinstance(value, str):
                utf_text = value.encode("utf-8")
                new_kwargs[key] = utf_text
            else:
                new_kwargs[key] = value

        result = func(*new_args, **new_kwargs)
        return result

    return wrapper
