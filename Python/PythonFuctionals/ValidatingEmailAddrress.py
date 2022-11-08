Problem Link:

https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true


def fun(s):
    try:
        username,other=s.split("@")
        websitename,extension=other.split(".")
    except:
        return False
        
    username=username.replace("_","").replace("-","")
    if username.isalnum()==False:
        return False
    elif websitename.isalnum()==False:
        return False
    elif len(extension)>3:
        return False
    else:
        return True