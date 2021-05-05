from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import sentiment
from .Sentiment_mod import sentiment_check
from .forms import attrition_form


def resu(request):
    try:
        var = sentiment.objects.values_list(), # this gives a tuple with all the row data from the database.
        vip = var[0] # list of tuples

        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        for tup in var[0]:
            for i in range(0, 6):
                if i == 1:
                    temp = sentiment_check(str(tup[i]))
                    l1.append(temp[0])
                if i == 2:
                    temp1 = sentiment_check(str(tup[i]))
                    l2.append(temp1[0])
                if i == 3:
                    temp2 = sentiment_check(str(tup[i]))
                    l3.append(temp2[0])
                if i == 4:
                    temp3 = sentiment_check(str(tup[i]))
                    l4.append(temp3[0])
                if i == 5:
                    temp4 = sentiment_check(str(tup[i]))
                    l5.append(temp4[0])

        # calculation on the sentiments
        pos1 = l1.count('pos')
        senti1 = ''
        if float(pos1/len(l1)) > 0.5:
            senti1 = 'Sentiment towards this aspect is positive'
        elif float(pos1/len(l1)) == 0.5:
            senti1 = 'Sentiment towards this aspect is neutral'
        else:
            senti1 = 'Sentiment towards this aspect is negative'

        pos2 = l2.count('pos')
        senti2 = ''
        if float(pos2/len(l2)) > 0.5:
            senti2 = 'Sentiment towards this aspect is positive'
        elif float(pos2/len(l2)) == 0.5:
            senti2 = 'Sentiment towards this aspect is neutral'
        else:
            senti2 = 'Sentiment towards this aspect is negative'

        pos3 = l3.count('pos')
        senti3 = ''
        if float(pos3/len(l3)) > 0.5:
            senti3 = 'Sentiment towards this aspect is positive'
        elif float(pos3/len(l3)) == 0.5:
            senti3 = 'Sentiment towards this aspect is neutral'
        else:
            senti3 = 'Sentiment towards this aspect is negative'

        pos4 = l4.count('pos')
        senti4 = ''
        if float(pos4/len(l4)) > 0.5:
            senti4 = 'Sentiment towards this aspect is positive'
        elif float(pos4/len(l4)) == 0.5:
            senti4 = 'Sentiment towards this aspect is neutral'
        else:
            senti4 = 'Sentiment towards this aspect is negative'

        pos5 = l5.count('pos')
        senti5 = ''
        if float(pos5/len(l5)) > 0.5:
            senti5 = 'Sentiment towards this aspect is positive'
        elif float(pos5/len(l5)) == 0.5:
            senti5 = 'Sentiment towards this aspect is neutral'
        else:
            senti5 = 'Sentiment towards this aspect is negative'

        user_ = request.user.username
        con = {'ques1': senti1,
               'ques2': senti2,
               'ques3 ': senti3,
               'ques4': senti4,
               'ques5': senti5,
               'usernames': user_}

    except:
        print("Error Occurred")
        con = {}

    return render(request, 'result.html', con)


def homepage(request):
    """

    :param request:
    :return:
    """
    user_ = request.user.username
    if user_ != None:
        dic = {"username": user_}
        return render(request, 'web4.html', dic)
    else:
        return render(request, 'web4.html')



def loginpage(request):
    if request.method == 'POST':

        check_loginid = request.POST['login_id']
        check_password = request.POST['password']
        user = auth.authenticate(request, username=check_loginid, password=check_password)
        auth.login(request, user)
        return redirect('homepage')
    else:
        print("Error in Login") # all of errors to be replaced with error pages.

    return render(request, 'login_page.html')


def logout_(request):
    if request.method == "POST":
        logout(request)

    return render(request, 'page4.html')



def ask_ques(request):
    if request.method == 'POST':
        if request.POST.get('question_button'):
            ques1 = request.POST['ques1']
            ques2 = request.POST['ques2']
            ques3 = request.POST['ques3']
            ques4 = request.POST['ques4']
            ques5 = request.POST['ques5']
            # print(ques1)

            var = sentiment(sentiment1=ques1, sentiment2=ques2, sentiment3=ques3,
                            sentiment4=ques4, sentiment5=ques5)
            var.save()
            return redirect('homepage')
        else:
            print('Not Working')
    else:
        print('Not Working')

    return render(request, 'formpage.html')


@login_required
def upload_file(request):
    user_ = request.user.username
    if request.method == "POST":
        forms = attrition_form(request.POST, request.FILES)
        if forms.is_valid():
            changed = forms.save(commit=False)
            changed.user_name = str(user_)
            forms.save()
            return redirect('homepage')
        else:
            print(forms.errors)
    else:
        forms = attrition_form()

    return render(request, 'forpage3.html', {'form': forms, 'username': user_})


def homing(request):
    return render(request, 'index.html')








