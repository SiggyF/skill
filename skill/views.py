from pyramid.view import view_config
import pyramid.response
import models
import PIL
import cStringIO
import random
import numpy as np
@view_config(route_name='home', renderer='main.html')
def my_view(request):

    return {'project': 'skill'}


@view_config(route_name='experiment', renderer='experiment.html')
def experiment(request):
    df = models.getdata()
    case = request.matchdict.get('case')
    data = df[df.case == case]
    return {
        'project': 'skill',
        'case': case,
        'df' : data
    }
@view_config(route_name='image')
def image(request):
    df = models.getdata()
    row = df.ix[int(request.matchdict.get('id'))]
    path = row['path']
    img = PIL.Image.open(path)
    converted_file = cStringIO.StringIO()
    if 'thumbnail' in request.params:
        img.thumbnail((256,256))
    img.save(converted_file, format='png')
    converted_file.seek(0)
    response = pyramid.response.Response(body_file=converted_file, request=request, content_type='image/png')
    return response

@view_config(route_name="detail", renderer='detail.html')
def detail(request):
    case = request.matchdict.get('case')
    period = request.matchdict.get('period')
    quantity = request.matchdict.get('quantity')
    df = models.getdata()
    df = df[np.logical_and(df.case==case, df.period==period, df.quantity==quantity)]
    return {
        'case': case,
        'period': period,
        'quantity': quantity,
        'df': df
        }

