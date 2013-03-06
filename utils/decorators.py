# -*- coding: utf-8 -*-
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def render_to(template=None, mimetype="text/html", extra_context_func=None):
    """
    Decorator for Django views that sends returned dict to render_to_response
    function.

    Template name can be decorator parameter or TEMPLATE item in returned
    dictionary.  RequestContext always added as context instance.
    If view doesn't return dict then decorator simply returns output.

    Parameters:
     - template: template name to use
     - mimetype: content type to send in response headers

    Examples:
    # 1. Template name in decorator parameters

    @render_to('template.html')
    def foo(request):
        bar = Bar.object.all()
        return {'bar': bar}

    # equals to
    def foo(request):
        bar = Bar.object.all()
        return render_to_response('template.html',
                                  {'bar': bar},
                                  context_instance=RequestContext(request))


    # 2. Template name as TEMPLATE item value in return dictionary.
         if TEMPLATE is given then its value will have higher priority
         than render_to argument.

    @render_to()
    def foo(request, category):
        template_name = '%s.html' % category
        return {'bar': bar, 'TEMPLATE': template_name}

    #equals to
    def foo(request, category):
        template_name = '%s.html' % category
        return render_to_response(template_name,
                                  {'bar': bar},
                                  context_instance=RequestContext(request))

    @render_to('template.html', mimetype='application/json')
    def foo(request):
        return {'EXTRAS': {'id': 1}, 'user': user}

    #equals to
    def foo(request):
        fragment = render_to_string('template.html', {'user': user}, context_instance=RequestContext(request))
        return {'fragment': fragment, 'id': 1}
    """
    def renderer(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            output = function(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            tmpl = output.pop('TEMPLATE', template)
            if extra_context_func:
                extra_context = extra_context_func()
                if isinstance(extra_context, dict):
                    output.update(extra_context)
            return render_to_response(tmpl, output, context_instance=RequestContext(request), mimetype=mimetype)
        return wrapper
    return renderer


ROLE_PRIORITY = {'call-center': 0,
                 'dispatch': 10,
                 'supervisor': 50,
                 'admin': 100}

def required_role(role):
    '''Decorator to check logged-in user role meets the required role to view the page'''
    def decorate(view):
        @login_required
        def inner(request, *args, **kwargs):
            user = request.user
            user_role = user.get_profile().role
            if user_role == 'analytics':
                if request.path != '/analytics/':
                    return redirect('analytics_index')
                return view(request, *args, **kwargs)
            if user_role == 'map_page':
                if request.path != '/call_center/cab_availability_map/':
                    return redirect('call_center_cab_availability_map')
                return view(request, *args, **kwargs)
            if user_role == 'accountant':
                if request.path != '/finances/':
                    return redirect('finance_home')
                return view(request, *args, **kwargs)
            # if user is not super user and 
            # user role value is less than required role value, raise permission denied
            if (not user.is_superuser) and (ROLE_PRIORITY[user_role] < ROLE_PRIORITY[role]):
                return redirect('call_center_home')
            else:
                return view(request, *args, **kwargs)
        return inner
    return decorate


def require_meta_operator(view):
    '''Decorator to check that the logged-in user belongs to meta organization(aggregator-TFS)'''
    @login_required
    def inner(request, *args, **kwargs):
        user = request.user
        # if user organization is not meta operator redirect to call center
        if not user.organization.meta_operator:
            return redirect('call_center_home')
        else:
            return view(request, *args, **kwargs)
    return inner
