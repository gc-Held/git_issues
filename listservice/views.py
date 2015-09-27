from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import github3
from github import Github

from datetime import datetime
import json

@api_view(['GET'])
@csrf_exempt
def get_issues_list(request,user,repo, format=None):
	if request.method == 'GET':
		
		count_dict = {}   #response object with individual count
		count_dict["day"] = 0
		count_dict["week"] = 0
		count_dict["longer"] = 0
		
		today = datetime.now()
		github = github3.login("gc-Held", "gokul@1131011") # user credentials
		repo = github3.repository(user, repo)   #opens the repository 
		open_issues = [i for i in repo.iter_issues()] # lists all the issues
		count_dict["total"] = len(open_issues)
		for i in open_issues:
			
			if i.pull_request == None:	#filters all pull requests
				created_at  = i.created_at.replace(tzinfo=None) #makes the datetime naive if TZ
				dt = today - created_at
				if dt.days == 0:
					count_dict["day"]+=1
				elif dt.days > 0 and dt.days < 7:
					count_dict["week"]+=1
				else:
					count_dict["longer"]+=1
			else:
				count_dict["total"]-=1
		
		return Response(count_dict)
