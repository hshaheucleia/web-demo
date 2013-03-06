
import datetime

from utils.decorators import render_to
from django.shortcuts import get_object_or_404, redirect
from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from edu.models import University, Institute, Application, Stream
from edu.forms import SearchForm

@login_required
@render_to('edu/index.html')
def index(request):
    form = SearchForm()
    return {'form':form}

@login_required
@render_to('edu/search_results.html')   
def get_search_results(request):
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            institutes = Institute.objects.all()
            return {'institutes' : institutes,
                    'form' : form}
        else:
            return {'form':form,
                    'errors':form.errors.as_ul()
                    }
    else:
        form = SearchForm()
        return {'form':form}
    
@login_required
@render_to('edu/streams_list.html')
def get_streams_for_institute(request):
    inst_pk = request.GET.get('inst_pk', '')
    if inst_pk:
        institute = get_object_or_404(Institute,pk=inst_pk)
        return {'institute' : institute,
                'streams': institute.streams.all()
            }
    else:
        return { 'institute' : '', 'streams':''}
    
@login_required
def apply_for_institute(request):
    inst_pk = request.POST.get('inst_pk', '')
    selected_streams = request.POST.get('selected_streams', '')
    for stream_cd in selected_streams.split(','):
        appln_id = '1-EDU-'+ request.user.username + '-' + inst_pk + '-' + stream_cd
        application = Application.objects.create(appln_id=appln_id,user=request.user,
                                             institute=Institute.objects.get(pk=int(inst_pk)),
                                             stream=Stream.objects.get(stream_code=stream_cd.strip()),
                                             last_updated_by = request.user)

    response = {'status' : 'success' }
    return HttpResponse(simplejson.dumps(response))

@login_required
@render_to('edu/my_applications.html')
def my_applications(request):
    user = request.user
    print user.applications.all()
    applications = user.applications.all().exclude(is_deleted=1)
    return {'applications': applications}

@login_required
def delete_application(request):
    try:
        appln_id = request.POST['appln_id']
        application = get_object_or_404(Application,appln_id=appln_id)
        application.is_deleted = 1
        application.save()
        response = {'status' : 'success' }
        return HttpResponse(simplejson.dumps(response))
    except:
        response = {'status' : 'failed' }
        return HttpResponse(simplejson.dumps(response))