
import random

readFromfile = '/home/ec2-user/environment/text2twitter/readline'


lines = open(readFromfile).read().splitlines()
myline =random.choice(lines)
print(myline)