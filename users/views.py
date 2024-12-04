from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from .models import UserChannelPreference
from dLearnex.top_extrac import func_1
from dLearnex.rec import get_channel_ids
from dLearnex.reccom import func_pred
# from dLearnex.new_embed_test1 import predict_score_for_new_user



chan_df="" #main dataframe for selected channels

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user = User.objects.create(
            username=username,
            password=make_password(password)  # Hash the password
        )
        user.save()
        return JsonResponse({'message': 'User registered successfully','user_id': user.id})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


from django.contrib.auth import authenticate, login

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)  # Save the user's session
            return JsonResponse({'message': 'Login successful','user id':user.id})
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
@csrf_exempt
def take_top(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        course_name = data.get('course_name')
        topic=data.get('topic')
        subtopic=data.get('subtopic')

        ans=func_1(course_name,topic,subtopic)
        chan_list=ans.channel.unique()
        # print(chan_list)

        # unique_channels_list = ans.tolist()
        df_dict = ans.to_dict(orient='records')
        chan_df=ans

        ids=get_channel_ids(chan_list)
        print(ids)

        
        print(request.user.id)
        dict={}


        for i,j in ids.items():
            
            dict[i]=func_pred(request.user.id, j)
        
        print(dict)


        # max_key = max(data, key=lambda k: dict[k][0][0])  # Extract the scalar value
        # max_score = dict[max_key][0][0]  # Get the highest score value

        best_chan_name = max(dict, key=lambda k: dict[k][0][0])
        print(best_chan_name)

        
        url_use = ans[ans['channel'] == best_chan_name]
        print(type(url_use['link']))

        url=url_use['link'].to_string(index=False)



        return JsonResponse({'best vid': url})



@login_required

def take_prefs(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ch_name = data.get('channel')
            ch_url = data.get('url')
            ch_score = data.get('score')

            # Save the preference in the database
            UserChannelPreference.objects.create(
                user=request.user,  # Automatically associate with the logged-in user
                channel_name=ch_name,
                channel_url=ch_url,
                channel_score=ch_score
            )

            return JsonResponse({'message': 'Preference saved successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# @login_required
# @csrf_exempt
# def take_prefs(request):
#     if(request.method == 'POST'):
#         data=json.loads(request.body)
#         ch_name=data.get('channel')
#         ch_url=data.get('url')
#         ch_score=data.get('score')
#         user=request.user
#         user_id=user.id

#         print(ch_name, ch_url, ch_score)
#         return JsonResponse({'message': [ch_name, ch_url, ch_score,user_id]})
    
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
@csrf_exempt
def show_pref(request):

    preferences = UserChannelPreference.objects.filter(user=request.user)
    for pref in preferences:
        print(pref.channel_name, pref.channel_url, pref.channel_score)

    return JsonResponse({'message':"displaying"})

from django.contrib.auth import logout

@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        logout(request)  # Clear the session
        return JsonResponse({'message': 'Logout successful'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)




@login_required
def protected_view(request):
    return JsonResponse({'message': 'This is a protected view'})



def home_view(request):
    return render(request, 'home.html',{})


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def get_user_data(request):
    user = request.user
    return JsonResponse({
        "username": user.username,
        "email": user.email,
        "date_joined": user.date_joined
    })

from django.http import JsonResponse

@login_required
def get_recommendations(request):
    # Dummy data - replace with your recommendation logic
    recommendations = [
        {"course_name": "Python for Beginners", "rating": 4.5},
        {"course_name": "Machine Learning 101", "rating": 4.8},
    ]
    ans=func_1('Python', 'Functions', 'Parameters')
    print(ans)
    return JsonResponse({"recommendations": recommendations})





