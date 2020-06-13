# remove special character
import re
def preprocessing(remark):

    remark = re.sub(r'\\s', '', remark)#\s
    remark = re.sub(r'\\n', '', remark)#\n
    remark = re.sub(r'\\u', '', remark)#\u
    remark = re.sub('\(', '', remark)#(
    remark = re.sub('\（', '', remark)#(
    remark = re.sub('\）', '', remark)#)
    remark = re.sub('\,\)', '', remark)#,)
    remark = re.sub('\'', '', remark)#"
    remark = re.sub('、', '', remark)#、
    remark = re.sub('。', '', remark)#。
    remark = re.sub('※', '', remark)#※
    remark = re.sub('！', '', remark)#！

    return remark
