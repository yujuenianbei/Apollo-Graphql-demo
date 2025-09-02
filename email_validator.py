import re

def validate_email(email):
    """
    使用正则表达式验证电子邮件地址格式是否标准。

    参数:
    email (str): 待验证的电子邮件地址字符串。

    返回:
    bool: 如果格式正确返回 True，否则返回 False。
    """
    # 定义匹配标准电子邮件地址的正则表达式模式
    # ^ : 匹配字符串的开始
    # [a-zA-Z0-9._%+-]+ : 匹配用户名部分，允许字母、数字和常见特殊字符，至少一个
    # @ : 匹配 @ 符号
    # [a-zA-Z0-9.-]+ : 匹配域名部分，允许字母、数字、点和连字符，至少一个
    # \. : 匹配一个点 .
    # [a-zA-Z]{2,} : 匹配顶级域名，至少两个字母
    # $ : 匹配字符串的结束
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # 使用 re.match 进行匹配
    if re.match(pattern, email):
        return True
    else:
        return False

# 测试用例
test_emails = [
    "example@example.com",      # 有效
    "user.name+tag@domain.co.uk", # 有效
    "invalid.email@",           # 无效：缺少域名
    "@domain.com",              # 无效：缺少用户名
    "user@domain",              # 无效：缺少顶级域名
    "user@domain.c",            # 无效：顶级域名太短
    "user name@domain.com"      # 无效：用户名包含空格
]

print("电子邮件地址验证结果：")
for email in test_emails:
    result = validate_email(email)
    print(f"'{email}': {'有效' if result else '无效'}")