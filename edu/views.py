
import datetime
import uuid

from django.db.models import Q
from utils.decorators import render_to, require_complete_profile
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from edu.models import University, Institute, Application, Stream, INACTIVE, Exam
from edu.forms import SearchForm


@require_complete_profile
@render_to('edu/index.html')
def index(request):
    form = SearchForm()
    return {'form':form}


@require_complete_profile
@render_to('edu/search_results.html')   
def get_search_results(request):
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q'].strip()
            data = form.cleaned_data
            print "q is %s" % q
            if q:
                institutes = Institute.objects.exclude(status=INACTIVE) \
                                                .filter(Q(name__icontains=1) |
                                                        Q(cur_pin__icontains=q) |
                                                        Q(cur_state__icontains=q))                               
            else:
                institutes = Institute.objects.exclude(status=INACTIVE)
            
            user = request.user
            applied_institutes = user.applications.exclude(is_deleted=1).values_list('institute',flat=True)
            
            return {'institutes' : institutes,
                    'form' : form,
                    'applied_institutes' : applied_institutes
                    }
        else:
            return {'form':form,
                    'errors':form.errors.as_ul()
                    }
    else:
        form = SearchForm()
        return {'form':form}
    
    
@require_complete_profile
@render_to('edu/streams_list.html')
def get_streams_for_institute(request):
    inst_pk = request.GET.get('inst_pk', '')
    if inst_pk:
        institute = get_object_or_404(Institute,pk=inst_pk)
        
        user = request.user
        applied_streams = user.applications.exclude(is_deleted=1).filter(institute=institute).values_list('stream__stream_code',flat=True)
        
        return {'status': 'success',
                'institute' : institute,
                'streams': institute.streams.all(),
                'applied_streams' : applied_streams
            }
    else:
        return { 'status': 'error'}


@require_complete_profile
def apply_for_institute(request):
    inst_pk = request.POST.get('inst_pk', '')
    selected_streams = request.POST.get('selected_streams', '')
    status = 'success'
    for stream_cd in selected_streams.split(','):
        appln_id = request.user.username + "-" + str(uuid.uuid4())[24:]
        print stream_cd
        try:
            is_application_exist = Application.objects.filter(institute=Institute.objects.get(pk=int(inst_pk)),
                                                              user=request.user,
                                                              is_deleted=False,
                                                              is_active=True,
                                                              stream=Stream.objects.get(stream_code=stream_cd.strip())).exists()
            if not is_application_exist:
                application = Application.objects.create(appln_id=appln_id,user=request.user,
                                                 institute=Institute.objects.get(pk=int(inst_pk)),
                                                 stream=Stream.objects.get(stream_code=stream_cd.strip()),
                                                 last_updated_by = request.user)
        except Exception as e:
            print e
            status = 'error'
            
            
    response = {'status' : status }
    return HttpResponse(simplejson.dumps(response))

@require_complete_profile
@render_to('edu/my_applications.html')
def my_applications(request):
    user = request.user
    applications = user.applications.all().exclude(is_deleted=1)
    return {'applications': applications}


@require_complete_profile
def delete_application(request):
    try:
        appln_id = request.POST['appln_id']
        application = get_object_or_404(Application,appln_id=appln_id)
        application.is_deleted = 1
        application.save()
        response = {'status' : 'success' }
        return HttpResponse(simplejson.dumps(response))
    except:
        response = {'status' : 'error' }
        return HttpResponse(simplejson.dumps(response))


@render_to('edu/about_institute.html')
def get_institute_info(request):
    inst_pk = request.GET.get('inst_pk', '')
    if inst_pk:
        institute = get_object_or_404(Institute,pk=inst_pk)
        return {'status': 'success',
                'name': institute.name,
                'info' : institute.about_info}
    else:
        return { 'status': 'error'}
    
def save_applications_priority(request):
    try:
        pref_data = simplejson.loads(request.body)
        user = request.user
        applications = user.applications.all().select_for_update().exclude(is_deleted=1)
        for pref in pref_data:
            if pref['applicationID']:
                priority_val = int(pref['appPriority'])
                appln = applications.filter(appln_id=pref['applicationID']).update(priority_number=priority_val)
        
        response = {'status' : 'success' }
        print response
        return HttpResponse(simplejson.dumps(response))
    except Exception as e:
        print e
        response = {'status' : 'error' }
        return HttpResponse(simplejson.dumps(response))
    
def autocomplete_suggestion(request):
    return HttpResponse(simplejson.dumps(list(Institute.objects.values_list('name',flat=True))))
    
    
