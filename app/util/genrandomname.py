#coding:utf8

import app.config.randomname as randomname
import random
malist = None;
mblist = None;
fmalist = None;
fmblist = None;
clist = None;
def genname(b_boy = True):
    if clist == None:
        clist = randomname.create_Randomname("C")
        malist = randomname.create_Randomname("MA")
        mblist = randomname.create_Randomname("MB")
        fmalist = randomname.create_Randomname("WA")
        fmblist = randomname.create_Randomname("WB")
    alist = [];
    blist = [];
    cl = clist.content
    if b_boy:
        alist = malist.content
        blist = mblist.content
    else:
        alist = fmalist.content
        blist = fmblist.content
    a = alist[random.randint(0,len(alist) - 1)]["content"];
    b = blist[random.randint(0,len(blist) - 1)]["content"];
    c = cl[random.randint(0,len(cl) - 1)]["content"];
    return a+c+b;
