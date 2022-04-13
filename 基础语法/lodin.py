#创建一个功能

def londin(name=None,password=None):

    if name != None and password != None:
        if name == "zhang" and password =="123":
            return "登陆成功"
        else:
            return "账号/密码错误"
    else:
        return "账号/密码不能为空"


