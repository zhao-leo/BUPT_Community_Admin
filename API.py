# -*- coding: utf-8 -*-
import os

#BASE_URL=os.getenv('BASE_URL')+'/'
BASE_URL='http://49.232.6.217:8001/'


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
  return BASE_URL+'user/LimitDetailNew/'
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
def frequency():
  return BASE_URL+'user/Frequency/'
def addadmin():
  return BASE_URL+'user/ManagerAdd/'
def excel():
  return BASE_URL+'user/GetExcelNew/'
def background():
  return BASE_URL+'user/Background/'