BASE_URL='http://127.0.0.1:8000/'


def loginapi():
  return BASE_URL+'user/ManagerLogin/'
def pimapi():
  return BASE_URL+'user/ManagerDetail/'
def complaintAll():
  return BASE_URL+'user/ComplaintAll/'
def replycomplaint():
  return BASE_URL+'user/ComplaintListDetail/'
def suggestionAll():
  return BASE_URL+'user/SuggestionAll/'
def replysuggestion():
  return BASE_URL+'user/SuggestionListDetail/'
def carlimit():
  return BASE_URL+'user/Limit/'
def hotline():
  return BASE_URL+'user/Hotline/'
def hotlinedetail():
  return BASE_URL+'user/HotlineDetail/'
def warmnotice():
  return BASE_URL+'user/Warn/'
def picture():
  return BASE_URL+'user/Cover/'
def picDetail():
  return BASE_URL+'user/CoverDetail/'