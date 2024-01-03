

if __name__ == "__main__":
    # Assertion
    a = 1
    b = 1
    
    # Continue only if a == b
    """
    if a != b:
        print("sdfsdfsd")
        exit()
    """

    assert a == b, "a nem egyenlo b-vel"
        
    print(84)
    
    # Errors, try-except
    # https://docs.python.org/3/library/exceptions.html
    try:
        f = open("foo.csv", "r")
        
        #...
        a = 2
        a /= "a"
        
        f.close()
        
    except FileNotFoundError:
        print("macska")
    except TypeError:
        print("kutyaaaaaaaa")
    
        
    print("kutya0")
    
    
    # raise
    if 1 == 2:
        raise ValueError("blabla")
    
    # try, raise
    try:
        # do something...
        
        raise ValueError("hiba")
    
    except ValueError as e:
        # do something else
        print(f"hiba: {e}")
    
    
    
    try:
        # 100 sor
        a = 1
        
        b = 2
    except FileNotFoundError as e:
        print(e)
    except TypeError as e:
        print(e)        
    except Exception as e: 
        print(e)
        
        
    

    
    
    
    
    
    
    