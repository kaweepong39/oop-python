class Testexam:

  def __init__(self, pretest, posttest):
    self.pretest = pretest
    self.posttest = posttest
    self.total = pretest + posttest

  def __str__(self):
    # ponit = vars(self)
    # print(ponit)
    # list comprehension
    # ponit =["{:10}:{}".format(k,v) for k, v in ponit.items() ]
    # return "\n".join(ponit)
    
    attr = ("pretest", "posttest", "total")
    ponit = ["{:10}:{}".format(a,getattr(self,a)) for a in attr]
    return "\n".join(ponit)


      
