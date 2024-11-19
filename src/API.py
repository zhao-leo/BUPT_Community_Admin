# -*- coding: utf-8 -*-
import os

BASE_URL=os.getenv('BASE_URL')+'/'

def loginapi():
  return BASE_URL+'user/ManagerLogin/'
def pimapi():
  return BASE_URL+'user/ManagerDetail/'

def complaintAll():
  return BASE_URL+'user/ComplaintAll/'
def replycomplaint():
  return BASE_URL+'user/ComplaintListDetail/'
def complainttreat():
  return BASE_URL+'user/ComplaintTreat/'
def complainthandle():
  return BASE_URL+'user/ComplaintTreatWhich/'

def suggestionAll():
  return BASE_URL+'user/SuggestionAll/'
def replysuggestion():
  return BASE_URL+'user/SuggestionListDetail/'
def suggestiontreat():
  return BASE_URL+'user/SuggestionTreat/'
def suggestionhandle():
  return BASE_URL+'user/SuggestionTreatWhich/'

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
def handlenumber():
  return BASE_URL+'user/CountSum/'
def Icon():
  return BASE_URL+'docker_media/picture/favicon.ico'

def complaintHistory():
  return BASE_URL+'user/ComplaintHistory/'
def suggestionHistory():
  return BASE_URL+'user/SuggestionHistory/'
def singleComplaint():
  return BASE_URL+'user/ComplaintHistoryWhich/'
def singleSuggestion():
  return BASE_URL+'user/SuggestionHistoryWhich/'

def suggPicupload():
  return BASE_URL+'user/UpLoadSuggestionPicture/'

def compPicupload():
  return BASE_URL+'user/UpLoadComplaintPicture/'
  
