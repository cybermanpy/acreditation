# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Career
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from careers.forms import FormSearch
# Librerias para requeridas para generar pdf
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch

# Create your views here.

def viewNational(request):
    title = 'Carreras de Grado Modelo Nacional'
    template = loader.get_template('view_careers.html')
    label = 'Universidad'
    link = '/acreditation/model/national'
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada').order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
                'link': link,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Acreditada').order_by('national')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
        'form': form,
        'label': label,
        'link': link,
    }
    return HttpResponse(template.render(context, request))

def viewCareer(request):
    title = 'Carreras de Grado Acreditadas por Carreras'
    template = loader.get_template('view_careers.html')
    label = 'Carrera'
    link = '/acreditation/career'
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada').order_by('fknamecareer__description')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
                'link': link,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Acreditada').order_by('fknamecareer__description')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
        'form': form,
        'label': label,
        'link': link,
    }
    return HttpResponse(template.render(context, request))

def viewUniversity(request):
    title = 'Carreras de Grado Acreditadas por Universidad'
    template = loader.get_template('view_careers.html')
    label = 'Facultad'
    link = '/acreditation/university'
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada').order_by('fkfaculty__fkuniversity__name')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
                'link': link,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Acreditada').order_by('fkfaculty__fkuniversity__name')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
        'form': form,
        'label': label,
        'link': link,
    }
    return HttpResponse(template.render(context, request))

def viewPostponed(request):
    title = 'Carreras de Grado / Programas de postgrado postergados Modelo Nacional'
    template = loader.get_template('view_postponed.html')
    label = 'Universidad'
    link = '/acreditation/postponed'
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Postergada').order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
                'link': link,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Postergada').order_by('national')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
        'form': form,
        'label': label,
        'link': link,
    }
    return HttpResponse(template.render(context, request))

def viewNoReputable(request):
    title = 'Carreras de Grado / Programas de postgrado no acreditadas Modelo Nacional'
    template = loader.get_template('view_postponed.html')
    label = 'Universidad'
    link = '/acreditation/no-reputable'
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='No acreditada').order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
                'link': link,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='No acreditada').order_by('national')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
        'form': form,
        'label': label,
        'link': link,
    }
    return HttpResponse(template.render(context, request))

# def renderPdf(request):
#     print "Genero el PDF"
#     response = HttpResponse(content_type='aplication/pdf')
#     response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadas.pdf"'
#     buff = BytesIO()
#     doc = SimpleDocTemplate(buff,
#         pagesize=letter,
#         rightMargin=72,
#         leftMargin=72,
#         topMargin=72,
#         bottomMargin=72,
#         )
#     careers = []
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name="ParagraphTitle", fontSize=8, alignment=TA_JUSTIFY, fontName="FreeSansBold"))
#     header = Paragraph("Listado de Carreras Acreditadas Modelo Nacional", styles['Heading1'])
#     careers.append(header)
#     headings = ('Nro.', 'Carrera', 'Institución', 'Sede', 'Facultad', 'Resolución', 'Fecha', 'Periodo de Acreditación')
#     allCareers = [(c.national, c.fknamecareer, c.fkfaculty.fkuniversity, c.fkfaculty.fkcampus, c.fkfaculty.fkname, c.fkresolution.number, c.fkresolution.start_date, c.fkresolution.end_date) for c in Career.objects.filter(fkstatus__description='Acreditada').order_by('national')]
#     print allCareers
#     t = Table([headings] + allCareers)
#     # t.setStyle(TableStyle(
#     #     [
#     #         ('GRID', (0, 8), (-1, -1), 0.25, colors.dodgerblue),
#     #         ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.darkblue),
#     #         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
#     #     ]
#     # ))
#     t.setStyle(TableStyle(
#         [
#             ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.dodgerblue),
#             ('BOX', (0, 0), (-1, -1), 0.5, colors.dodgerblue),
#             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
#         ]
#     ))
#     careers.append(t)
#     doc.build(careers)
#     response.write(buff.getvalue())
#     buff.close()
#     return response


def renderPdf(self):
        response = HttpResponse(content_type='aplication/pdf')
        response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadas.pdf"'
        buff = BytesIO()
        doc = SimpleDocTemplate(buff,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=letter)
 
        # Our container for 'Flowable' objects
        elements = []
 
        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
 
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # users = User.objects.all()
        careers = Career.objects.filter(fkstatus__description='Acreditada').order_by('national')
        elements.append(Paragraph('Carreras Acreditadas', styles['Heading1']))
 
        # Need a place to store our table rows
        table_data = []
        table_data.append(['Carrera', 'Institución', 'Sede', 'Facultad'])
        for i, u in enumerate(careers):
            # Add a row to the table
            table_data.append([u.fknamecareer, u.fkfaculty.fkuniversity, u.fkfaculty.fkcampus, u.fkfaculty.fkname])
        # Create the table
        user_table = Table(table_data, colWidths=[doc.width/4.0]*4)
        user_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
        elements.append(user_table)
        doc.build(elements)
 
        # Get the value of the BytesIO buffer and write it to the response.
        response.write(buff.getvalue())
        buff.close()
        return response
# def viewNational(request):
#     title = 'Carreras de Grado Modelo Nacional'
#     template = loader.get_template('view_careers.html')
#     label = 'Universidad'
#     link = '/acreditation/model/national'
#     if request.method == 'POST':
#         form = FormSearch(request.POST)
#         # u = request.POST['text']
#         # request.session['text'] = u
#         if form.is_valid():
#             u = request.POST['text']
#             # listCareer = Career.objects.filter(fkfaculty__fkuniversity=u)
#             # listCareer = Career.objects.filter(fkfaculty__fkuniversity__name__contains=request.session['text']).order_by('national')
#             listCareer = Career.objects.filter(fkfaculty__fkuniversity__name__contains=u).order_by('national')
#             paginator = Paginator(listCareer, 200)
#             try:
#                 page = int(request.GET.get('page', '1'))
#             except ValueError:
#                 page = 1
#             try:
#                 careers = paginator.page(page)
#             except (EmptyPage, InvalidPage):
#                 careers = paginator.page(paginator.num_pages)
#             context = {
#                 'careers': careers,
#                 'title': title,
#                 'form': form,
#                 'label': label,
#                 'link': link,
#             }
#             return HttpResponse(template.render(context, request))
#     else:
#         form = FormSearch()
#     listCareer = Career.objects.all().order_by('national')
#     paginator = Paginator(listCareer, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#         'label': label,
#         'link': link,
#         'var': var,
#     }
#     return HttpResponse(template.render(context, request))

# def viewCareer(request):
#     title = 'Carreras de Grado Acreditadas por Carreras'
#     template = loader.get_template('view_careers.html')
#     label = 'Carrera'
#     link = '/acreditation/career'
#     if request.method == 'POST':
#         form = FormSearch(request.POST)
#         if form.is_valid():
#             c = request.POST['text']
#             # listCareer = Career.objects.filter(fkfaculty__fkuniversity=u)
#             listCareer = Career.objects.filter(fknamecareer__description__contains=c).order_by('fknamecareer__description')
#             paginator = Paginator(listCareer, 200)
#             try:
#                 page = int(request.GET.get('page', '1'))
#             except ValueError:
#                 page = 1
#             try:
#                 careers = paginator.page(page)
#             except (EmptyPage, InvalidPage):
#                 careers = paginator.page(paginator.num_pages)
#             context = {
#                 'careers': careers,
#                 'title': title,
#                 'form': form,
#                 'label': label,
#                 'link': link,
#             }
#             return HttpResponse(template.render(context, request))
#     else:
#         form = FormSearch()
#     listCareer = Career.objects.all().order_by('fknamecareer__description')
#     paginator = Paginator(listCareer, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#         'label': label,
#         'link': link,
#     }
#     return HttpResponse(template.render(context, request))

# def viewUniversity(request):
#     title = 'Carreras de Grado Acreditadas por Universidad'
#     template = loader.get_template('view_careers.html')
#     label = 'Facultad'
#     link = '/acreditation/university'
#     if request.method == 'POST':
#         form = FormSearch(request.POST)
#         if form.is_valid():
#             u = request.POST['text']
#             # listCareer = Career.objects.filter(fkfaculty__fkuniversity=u)
#             listCareer = Career.objects.filter(fkfaculty__fkname__name__contains=u).order_by('fkfaculty__fkuniversity__name')
#             paginator = Paginator(listCareer, 200)
#             try:
#                 page = int(request.GET.get('page', '1'))
#             except ValueError:
#                 page = 1
#             try:
#                 careers = paginator.page(page)
#             except (EmptyPage, InvalidPage):
#                 careers = paginator.page(paginator.num_pages)
#             context = {
#                 'careers': careers,
#                 'title': title,
#                 'form': form,
#                 'label': label,
#                 'link': link,
#             }
#             return HttpResponse(template.render(context, request))
#     else:
#         form = FormSearch()
#     listCareer = Career.objects.all().order_by('fkfaculty__fkuniversity__name')
#     paginator = Paginator(listCareer, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#         'label': label,
#         'link': link,
#     }
#     return HttpResponse(template.render(context, request))

# def viewCareers(request):
#     title = 'Carreras Acreditadas Modelo Nacional'
#     careers = Career.objects.all().order_by('national')
#     template = loader.get_template('view_careers.html')
#     context = {
#         'careers': careers,
#         'title':  title,
#     }
#     return HttpResponse(template.render(context, request))

# def viewNational(request):
#     title = 'Carreras de Grado Modelo Nacional'
#     template = loader.get_template('view_careers.html')
#     form = FormUniversity()
#     listCareer = Career.objects.all().order_by('national')
#     paginator = Paginator(listCareer, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#     }
#     return HttpResponse(template.render(context, request))

# def viewCareer(request):
#     title = 'Carreras de Grado Acreditadas por Carreras'
#     template = loader.get_template('view_careers.html')
#     listCareer = Career.objects.all().order_by('fknamecareer__description')
#     paginator = Paginator(listCareer, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#     }
#     return HttpResponse(template.render(context, request))

# def viewUniversity(request):
#     title = 'Carreras de Grado Acreditadas por Universidad'
#     template = loader.get_template('view_careers.html')
#     listCareer = Career.objects.all().order_by('fkfaculty__fkuniversity__name')
#     paginator = Paginator(listCareer, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#     }
#     return HttpResponse(template.render(context, request))