from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from fbfriendsapp.models import *
from social_auth.models import *

from fbfriendsapp.serializers import LinkedinSerializer
from rest_framework import viewsets

def index(request):
	return render_to_response('home.html',
                          context_instance=RequestContext(request))

def register(request):
	if request.method == 'POST':
		email = request.POST['email']
		full_name = request.POST['full_name']
		password = request.POST['password']
		try:
			user = Register.objects.create_user(email,email,password)
			user.full_name = full_name
			user.save()
			return HttpResponse('success')
		except:
			return HttpResponse('user already exists')
	else:
		return render_to_response('register.html',
                          	context_instance=RequestContext(request))

def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				return redirect('/home/')
			else:
				print("The password is valid, but the account has been disabled!")
		else:
			return HttpResponse("The username and password were incorrect.")
	else:
		return redirect('/')

def home(request):
	# LinkedinUserFriendsData.objects.filter(linkedin_profile__user_id='fQ-sVxFTtT')
	# query_set = UserSocialAuth.objects.filter(user=request.user.id)
	try:
		user_id = LinkedinProfileData.objects.get(email=request.user.email).user_id
		query_set = LinkedinUserFriendsData.objects.filter(linkedin_profile__user_id=user_id)
		# data = query_set[0].extra_data
		pro = []
		for x in query_set:
			dat = {'im':x.photo_url,'full_name':x.full_name,'id':x.id}
			pro.append(dat)
		return render_to_response('logged_in.html',
								{'data':pro},
	                          	context_instance=RequestContext(request))
	except:
		return HttpResponse('Welocome home, use linkeden login to view your connections')

def save_profile(sender, **kwargs):
	instance = kwargs['instance']
	try:
		uid = instance.extra_data['id']
		try:
			LinkedinProfileData.objects.get(user_id=uid)
		except LinkedinProfileData.DoesNotExist:
			a = LinkedinProfileData()
			a.first_name = instance.extra_data['first_name']
			a.last_name = instance.extra_data['last_name']
			a.user_id = instance.extra_data['id']
			a.email = instance.extra_data['email_address']
			a.picture_url = instance.extra_data['picture-url']
			a.save()
			query_set = UserSocialAuth.objects.filter(uid=instance.extra_data['id'])
			data = query_set[0].extra_data
			for x in data['connections']['person']:
				b = LinkedinUserFriendsData()
				try:
					x['picture-url']
					b.linkedin_profile = a
					b.photo_url = x['picture-url']
					b.full_name = x['first-name']+' '+x['last-name']
					b.save()
				except:
					b.linkedin_profile = a
					b.photo_url = ''
					b.full_name = x['first-name']+' '+x['last-name']
					b.save()
				# print 'test',x['first-name']+' '+x['last-name']
				# b.photo_url = x['picture-url']
				
	except:
		uid = None
	
		
post_save.connect(save_profile, sender=UserSocialAuth)

def update(request):
	name = request.POST['name']
	uid = request.POST['id']
	a = LinkedinUserFriendsData.objects.get(id=uid)
	a.full_name = name
	a.save()
	return HttpResponse('success')

class LinkedinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LinkedinUserFriendsData.objects.all()
    serializer_class = LinkedinSerializer