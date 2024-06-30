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