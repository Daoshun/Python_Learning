#RegEx正则表达式  搜索字符串中是否含有所搜寻的词汇
import re
pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'
print(pattern1 in string)
print(pattern2 in string)
#灵活匹配
pattern3 = r'r[au]n'   #可以搜索a或u
print(re.search(pattern3,'dogs runs to cat'))
pattern4 = r'r[0-9A-Za-z]n'  #可以搜索中间0-9,a-z，A-Z的任意值
print(re.search(pattern4,'dogs runs to cat'))
#\d : 任何数字
#\D : 不是数字
#\s : 任何 white space, 如 [\t\n\r\f\v]
#\S : 不是 white space
#\w : 任何大小写字母, 数字和 “” [a-zA-Z0-9]
#\W : 不是 \w
#\b : 空白字符 (只在某个字的开头或结尾)
#\B : 空白字符 (不在某个字的开头或结尾)
#\\ : 匹配 \
#. : 匹配任何字符 (除了 \n)
#^ : 匹配开头
#$ : 匹配结尾
#? : 前面的字符可有可无
pattern5 = r'r[\w]n$'    #\w任何大小写字母，数字，和空格     $从结尾开始匹配，第一个是r4n
print(re.search(pattern5,'run rUn r4n'))
#re.search(r''^I'',string,flags=re.M)   flags=re.M  可以做到对每一行做单独处理
string1 = '''
dog runs to cat.
I run to dog.
'''
print(re.search(r'^I',string,flags=re.M))
string2 = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))                 # None
print(re.search(r"^I", string, flags=re.M))     # <_sre.SRE_Match object; span=(18, 19), match='I'>
