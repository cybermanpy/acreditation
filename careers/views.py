# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Career
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from careers.forms import FormSearch
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
# Librerias para requeridas para generar pdf
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch, landscape, portrait

# Create your views here.

def viewNational(request):
    title = 'Carreras de Grado Modelo Nacional'
    template = loader.get_template('view_careers.html')
    label = 'national'
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
            elif options == '2':
                careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
            elif options == '3':
                careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
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
    }
    return HttpResponse(template.render(context, request))

def viewPostponed(request):
    title = 'Carreras de Grado/Programas de posgrado postergados Modelo Nacional'
    template = loader.get_template('view_postponed.html')
    label = 'postponed'
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
            elif options == '2':
                careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
            elif options == '3':
                careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
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
    }
    return HttpResponse(template.render(context, request))

def viewNoReputable(request):
    title = 'Carreras de Grado/Programas de postgrado no acreditadas Modelo Nacional'
    template = loader.get_template('view_postponed.html')
    label = 'noreputable'
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
            elif options == '2':
                careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
            elif options == '3':
                careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
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
    }
    return HttpResponse(template.render(context, request))

def viewPosgrado(request):
    title = 'Programas de postgrado acreditados'
    template = loader.get_template('view_posgrado.html')
    label = 'posgrado'
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
            elif options == '2':
                careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
            elif options == '3':
                careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
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
    }
    return HttpResponse(template.render(context, request))

def viewArcusur(request):
    title = 'Carreras de grado acreditados - Modelo Arcusur'
    template = loader.get_template('view_careers.html')
    label = 'arcusur'
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
            elif options == '2':
                careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
            elif options == '3':
                careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
            context = {
                'careers': careers,
                'title': title,
                'form': form,
                'label': label,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listCareer = Career.objects.filter(fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
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
    }
    return HttpResponse(template.render(context, request))

def cleanner(request, link):
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if link == 'national':
        return redirect('/acreditation/model/national')
    elif link == 'arcusur':
        return redirect('/acreditation/model/arcusur')
    elif link == 'postponed':
        return redirect('/acreditation/postponed')
    elif link == 'noreputable':
        return redirect('/acreditation/no-reputable')
    elif link == 'posgrado':
        return redirect('/acreditation/posgrado')
    

def pdfNational(request):
    search = request.session['s_text']
    options = request.session['s_options']
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadasModeloNacional.pdf"'
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
        pagesize=landscape(letter))
    # Our container for 'Flowable' objects
    elements = []
    logo = "/var/www/html/acreditation/static/img/logoBlack.png"
    im = Image(logo, 3*inch, 1*inch)

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    title = styles['Heading1']
    title.alignment=TA_CENTER
    thead = styles["Normal"]
    thead.alignment=TA_CENTER
    tbody = styles["BodyText"]
    tbody.alignment=TA_LEFT
    styles.wordWrap = 'CJK'
    styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
    elements.append(im)

    if options == '':
        careers = Career.objects.filter(fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
    elif options == '1':
        careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
    elif options == '2':
        careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
    elif options == '3':
        careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')

    elements.append(Paragraph('Carreras Acreditadas - Modelo Nacional', title))

    # Need a place to store our table rows
    table_data = []
    table_data.append([
        Paragraph(str('Nro.'), thead),
        Paragraph(str('Carrera'), thead),
        Paragraph(str('Institución'), thead),
        Paragraph(str('Sede'), thead),
        Paragraph(str('Facultad'), thead),
        Paragraph(str('Resolución'), thead),
        Paragraph(str('Fecha'), thead),
        Paragraph(str('Periodo de Acreditación'), thead),
        ])
    for i, c in enumerate(careers):
        # Add a row to the table
        i=i+1
        table_data.append([
            Paragraph(str(i), tbody),
            Paragraph(str(c.fknamecareer.description), tbody),
            Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
            Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
            Paragraph(str(c.fkfaculty.fkname.name), tbody),
            Paragraph(str(c.fkresolution.number), tbody),
            Paragraph(str(c.fkresolution.start_date), tbody),
            Paragraph(str(c.fkresolution.end_date), tbody),
            ])
    
    # Create the table
    career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

    career_table.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    elements.append(career_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    response.write(buff.getvalue())
    buff.close()
    return response

def pdfArcusur(request):
    search = request.session['s_text']
    options = request.session['s_options']
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadasModeloArcusur.pdf"'
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
        pagesize=landscape(letter))
    # Our container for 'Flowable' objects
    elements = []
    logo = "/var/www/html/acreditation/static/img/logoBlack.png"
    im = Image(logo, 3*inch, 1*inch)

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    title = styles['Heading1']
    title.alignment=TA_CENTER
    thead = styles["Normal"]
    thead.alignment=TA_CENTER
    tbody = styles["BodyText"]
    tbody.alignment=TA_LEFT
    styles.wordWrap = 'CJK'
    styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
    elements.append(im)

    if options == '':
        careers = Career.objects.filter(fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
    elif options == '1':
        careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
    elif options == '2':
        careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
    elif options == '3':
        careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')

    elements.append(Paragraph('Carreras Acreditadas - Modelo ARCU-SUR', title))

    # Need a place to store our table rows
    table_data = []
    table_data.append([
        Paragraph(str('Nro.'), thead),
        Paragraph(str('Carrera'), thead),
        Paragraph(str('Institución'), thead),
        Paragraph(str('Sede'), thead),
        Paragraph(str('Facultad'), thead),
        Paragraph(str('Resolución'), thead),
        Paragraph(str('Fecha'), thead),
        Paragraph(str('Periodo de Acreditación'), thead),
        ])
    for i, c in enumerate(careers):
        # Add a row to the table
        i=i+1
        table_data.append([
            Paragraph(str(i), tbody),
            Paragraph(str(c.fknamecareer.description), tbody),
            Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
            Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
            Paragraph(str(c.fkfaculty.fkname.name), tbody),
            Paragraph(str(c.fkresolution.number), tbody),
            Paragraph(str(c.fkresolution.start_date), tbody),
            Paragraph(str(c.fkresolution.end_date), tbody),
            ])
    
    # Create the table
    career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

    career_table.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    elements.append(career_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    response.write(buff.getvalue())
    buff.close()
    return response

def pdfPostponed(request):
    search = request.session['s_text']
    options = request.session['s_options']
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="carrerasPostergadas.pdf"'
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
        pagesize=landscape(letter))
    # Our container for 'Flowable' objects
    elements = []
    logo = "/var/www/html/acreditation/static/img/logoBlack.png"
    im = Image(logo, 3*inch, 1*inch)

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    title = styles['Heading1']
    title.alignment=TA_CENTER
    thead = styles["Normal"]
    thead.alignment=TA_CENTER
    tbody = styles["BodyText"]
    tbody.alignment=TA_LEFT
    styles.wordWrap = 'CJK'
    styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
    elements.append(im)

    if options == '':
        careers = Career.objects.filter(fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
    elif options == '1':
        careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
    elif options == '2':
        careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')
    elif options == '3':
        careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Postergada', arcusur=False, posgrado=False).order_by('national')

    elements.append(Paragraph('Carreras Postergadas - Modelo Nacional', title))

    # Need a place to store our table rows
    table_data = []
    table_data.append([
        Paragraph(str('Nro.'), thead),
        Paragraph(str('Universidad/Institutos Superiores'), thead),
        Paragraph(str('Carrera/Programa'), thead),
        Paragraph(str('Sede'), thead),
        Paragraph(str('Resolución'), thead),
        ])
    for i, c in enumerate(careers):
        # Add a row to the table
        i=i+1
        table_data.append([
            Paragraph(str(i), tbody),
            Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
            Paragraph(str(c.fknamecareer.description), tbody),
            Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
            Paragraph(str(c.fkresolution.number), tbody),
            ])
    
    # Create the table
    career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

    career_table.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    elements.append(career_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    response.write(buff.getvalue())
    buff.close()
    return response

def pdfNoReputable(request):
    search = request.session['s_text']
    options = request.session['s_options']
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="carrerasNoAcreditadas.pdf"'
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
        pagesize=landscape(letter))
    # Our container for 'Flowable' objects
    elements = []
    logo = "/var/www/html/acreditation/static/img/logoBlack.png"
    im = Image(logo, 3*inch, 1*inch)

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    title = styles['Heading1']
    title.alignment=TA_CENTER
    thead = styles["Normal"]
    thead.alignment=TA_CENTER
    tbody = styles["BodyText"]
    tbody.alignment=TA_LEFT
    styles.wordWrap = 'CJK'
    styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
    elements.append(im)

    if options == '':
        careers = Career.objects.filter(fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
    elif options == '1':
        careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
    elif options == '2':
        careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')
    elif options == '3':
        careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='No acreditada', arcusur=False, posgrado=False).order_by('national')

    elements.append(Paragraph('Carreras No Acreditadas - Modelo Nacional', title))

    # Need a place to store our table rows
    table_data = []
    table_data.append([
        Paragraph(str('Nro.'), thead),
        Paragraph(str('Universidad/Institutos Superiores'), thead),
        Paragraph(str('Carrera/Programa'), thead),
        Paragraph(str('Sede'), thead),
        Paragraph(str('Resolución'), thead),
        ])
    for i, c in enumerate(careers):
        # Add a row to the table
        i=i+1
        table_data.append([
            Paragraph(str(i), tbody),
            Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
            Paragraph(str(c.fknamecareer.description), tbody),
            Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
            Paragraph(str(c.fkresolution.number), tbody),
            ])
    
    # Create the table
    career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

    career_table.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    elements.append(career_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    response.write(buff.getvalue())
    buff.close()
    return response

def pdfPosgrado(request):
    search = request.session['s_text']
    options = request.session['s_options']
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="posgradosAcreditados.pdf"'
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
        pagesize=landscape(letter))
    # Our container for 'Flowable' objects
    elements = []
    logo = "/var/www/html/acreditation/static/img/logoBlack.png"
    im = Image(logo, 3*inch, 1*inch)

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    title = styles['Heading1']
    title.alignment=TA_CENTER
    thead = styles["Normal"]
    thead.alignment=TA_CENTER
    tbody = styles["BodyText"]
    tbody.alignment=TA_LEFT
    styles.wordWrap = 'CJK'
    styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
    elements.append(im)

    if options == '':
        careers = Career.objects.filter(fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
    elif options == '1':
        careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
    elif options == '2':
        careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')
    elif options == '3':
        careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=True).order_by('national')

    elements.append(Paragraph('Programas de Posgrados Acreditados - Modelo Nacional', title))
    # Need a place to store our table rows
    table_data = []
    table_data.append([
        Paragraph(str('Nro.'), thead),
        Paragraph(str('Programa de Posgrado'), thead),
        Paragraph(str('Institución'), thead),
        Paragraph(str('Sede'), thead),
        Paragraph(str('Resolución'), thead),
        Paragraph(str('Fecha'), thead),
        Paragraph(str('Periodo de Acreditación'), thead),
        ])
    for i, c in enumerate(careers):
        # Add a row to the table
        i=i+1
        table_data.append([
            Paragraph(str(i), tbody),
            Paragraph(str(c.fknamecareer.description), tbody),
            Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
            Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
            Paragraph(str(c.fkresolution.number), tbody),
            Paragraph(str(c.fkresolution.start_date), tbody),
            Paragraph(str(c.fkresolution.end_date), tbody),
            ])
    
    # Create the table
    career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

    career_table.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    elements.append(career_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    response.write(buff.getvalue())
    buff.close()
    return response

# def renderPdf(request):
#     response = HttpResponse(content_type='aplication/pdf')
#     response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadas.pdf"'
#     buff = BytesIO()
#     doc = SimpleDocTemplate(buff,
#         rightMargin=72,
#         leftMargin=72,
#         topMargin=72,
#         bottomMargin=72,
#         pagesize=landscape(letter))
#     # Our container for 'Flowable' objects
#     elements = []
#     logo = "/var/www/html/acreditation/static/img/logoBlack.png"
#     im = Image(logo, 3*inch, 1*inch)

#     # A large collection of style sheets pre-made for us
#     styles = getSampleStyleSheet()
#     title = styles['Heading1']
#     title.alignment=TA_CENTER
#     thead = styles["Normal"]
#     thead.alignment=TA_CENTER
#     tbody = styles["BodyText"]
#     tbody.alignment=TA_LEFT
#     styles.wordWrap = 'CJK'
#     styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
#     elements.append(im)

#     careers = Career.objects.filter(fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
#     elements.append(Paragraph('Carreras de Grado Acreditadas Modelo Nacional', title))

#     # Need a place to store our table rows
#     table_data = []
#     table_data.append([
#         Paragraph(str('Nro.'), thead),
#         Paragraph(str('Carrera'), thead),
#         Paragraph(str('Institución'), thead),
#         Paragraph(str('Sede'), thead),
#         Paragraph(str('Facultad'), thead),
#         Paragraph(str('Resolución'), thead),
#         Paragraph(str('Fecha'), thead),
#         Paragraph(str('Periodo de Acreditación'), thead),
#         ])
#     for i, c in enumerate(careers):
#         # Add a row to the table
#         i=i+1
#         table_data.append([
#             Paragraph(str(i), tbody),
#             Paragraph(str(c.fknamecareer.description), tbody),
#             Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
#             Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
#             Paragraph(str(c.fkfaculty.fkname.name), tbody),
#             Paragraph(str(c.fkresolution.number), tbody),
#             Paragraph(str(c.fkresolution.start_date), tbody),
#             Paragraph(str(c.fkresolution.end_date), tbody),
#             ])
    
#     # Create the table
#     career_table = Table(table_data, colWidths=[doc.width/8.0]*8)
#     # career_table.setStyle(TableStyle([
#     #     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#     #     ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
#     #     ]))

#     career_table.setStyle(TableStyle(
#         [
#             ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
#             ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
#         ]
#     ))
#     elements.append(career_table)
#     doc.build(elements)

#     # Get the value of the BytesIO buffer and write it to the response.
#     response.write(buff.getvalue())
#     buff.close()
#     return response



# def pdfNational(request, search, options):
#     response = HttpResponse(content_type='aplication/pdf')
#     response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadasModeloNacional.pdf"'
#     buff = BytesIO()
#     doc = SimpleDocTemplate(buff,
#         rightMargin=72,
#         leftMargin=72,
#         topMargin=72,
#         bottomMargin=72,
#         pagesize=landscape(letter))
#     # Our container for 'Flowable' objects
#     elements = []
#     logo = "/var/www/html/acreditation/static/img/logoBlack.png"
#     im = Image(logo, 3*inch, 1*inch)

#     # A large collection of style sheets pre-made for us
#     styles = getSampleStyleSheet()
#     title = styles['Heading1']
#     title.alignment=TA_CENTER
#     thead = styles["Normal"]
#     thead.alignment=TA_CENTER
#     tbody = styles["BodyText"]
#     tbody.alignment=TA_LEFT
#     styles.wordWrap = 'CJK'
#     styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
#     elements.append(im)

#     if options == '0':
#         careers = Career.objects.filter(fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
#     elif options == '1':
#         careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
#     elif options == '2':
#         careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')
#     elif options == '3':
#         careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=False, posgrado=False).order_by('national')

#     elements.append(Paragraph('Carreras Acreditadas - Modelo Nacional', title))

#     # Need a place to store our table rows
#     table_data = []
#     table_data.append([
#         Paragraph(str('Nro.'), thead),
#         Paragraph(str('Carrera'), thead),
#         Paragraph(str('Institución'), thead),
#         Paragraph(str('Sede'), thead),
#         Paragraph(str('Facultad'), thead),
#         Paragraph(str('Resolución'), thead),
#         Paragraph(str('Fecha'), thead),
#         Paragraph(str('Periodo de Acreditación'), thead),
#         ])
#     for i, c in enumerate(careers):
#         # Add a row to the table
#         i=i+1
#         table_data.append([
#             Paragraph(str(i), tbody),
#             Paragraph(str(c.fknamecareer.description), tbody),
#             Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
#             Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
#             Paragraph(str(c.fkfaculty.fkname.name), tbody),
#             Paragraph(str(c.fkresolution.number), tbody),
#             Paragraph(str(c.fkresolution.start_date), tbody),
#             Paragraph(str(c.fkresolution.end_date), tbody),
#             ])
    
#     # Create the table
#     career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

#     career_table.setStyle(TableStyle(
#         [
#             ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
#             ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
#         ]
#     ))
#     elements.append(career_table)
#     doc.build(elements)

#     # Get the value of the BytesIO buffer and write it to the response.
#     response.write(buff.getvalue())
#     buff.close()
#     return response

# def pdfArcusur(request, search, options):
#     response = HttpResponse(content_type='aplication/pdf')
#     response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadasModeloArcusur.pdf"'
#     buff = BytesIO()
#     doc = SimpleDocTemplate(buff,
#         rightMargin=72,
#         leftMargin=72,
#         topMargin=72,
#         bottomMargin=72,
#         pagesize=landscape(letter))
#     # Our container for 'Flowable' objects
#     elements = []
#     logo = "/var/www/html/acreditation/static/img/logoBlack.png"
#     im = Image(logo, 3*inch, 1*inch)

#     # A large collection of style sheets pre-made for us
#     styles = getSampleStyleSheet()
#     title = styles['Heading1']
#     title.alignment=TA_CENTER
#     thead = styles["Normal"]
#     thead.alignment=TA_CENTER
#     tbody = styles["BodyText"]
#     tbody.alignment=TA_LEFT
#     styles.wordWrap = 'CJK'
#     styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
#     elements.append(im)

#     if options == '0':
#         careers = Career.objects.filter(fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
#     elif options == '1':
#         careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
#     elif options == '2':
#         careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')
#     elif options == '3':
#         careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada', arcusur=True, posgrado=False).order_by('national')

#     elements.append(Paragraph('Carreras Acreditadas - Modelo ARCU-SUR', title))

#     # Need a place to store our table rows
#     table_data = []
#     table_data.append([
#         Paragraph(str('Nro.'), thead),
#         Paragraph(str('Carrera'), thead),
#         Paragraph(str('Institución'), thead),
#         Paragraph(str('Sede'), thead),
#         Paragraph(str('Facultad'), thead),
#         Paragraph(str('Resolución'), thead),
#         Paragraph(str('Fecha'), thead),
#         Paragraph(str('Periodo de Acreditación'), thead),
#         ])
#     for i, c in enumerate(careers):
#         # Add a row to the table
#         i=i+1
#         table_data.append([
#             Paragraph(str(i), tbody),
#             Paragraph(str(c.fknamecareer.description), tbody),
#             Paragraph(str(c.fkfaculty.fkuniversity.name), tbody),
#             Paragraph(str(c.fkfaculty.fkcampus.name), tbody),
#             Paragraph(str(c.fkfaculty.fkname.name), tbody),
#             Paragraph(str(c.fkresolution.number), tbody),
#             Paragraph(str(c.fkresolution.start_date), tbody),
#             Paragraph(str(c.fkresolution.end_date), tbody),
#             ])
    
#     # Create the table
#     career_table = Table(table_data, colWidths=[doc.width/8.0]*8)

#     career_table.setStyle(TableStyle(
#         [
#             ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
#             ('LINEBELOW', (0, 0), (-1, 0), 0.25, colors.black),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
#         ]
#     ))
#     elements.append(career_table)
#     doc.build(elements)

#     # Get the value of the BytesIO buffer and write it to the response.
#     response.write(buff.getvalue())
#     buff.close()
#     return response

# def render(request, search, options):
#     title = 'test PDF'
#     template = loader.get_template('view_test.html')
#     context = {
#         'title': title,
#         'search': search,
#         'options': options,
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
#             search = request.POST['text']
#             careers = Career.objects.filter(fknamecareer__description__icontains=search, fkstatus__description='Acreditada').order_by('fknamecareer__description')
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
#     listCareer = Career.objects.filter(fkstatus__description='Acreditada').order_by('fknamecareer__description')
#     paginator = Paginator(listCareer, 10)
#     try:
#        page = int(request.GET.get('page', '1'))
#     except ValueError:
#        page = 1
#     try:
#        careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#        careers = paginator.page(paginator.num_pages)
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
#             search = request.POST['text']
#             careers = Career.objects.filter(fkfaculty__fkname__name__icontains=search, fkstatus__description='Acreditada').order_by('fkfaculty__fkuniversity__name')
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
#     listCareer = Career.objects.filter(fkstatus__description='Acreditada').order_by('fkfaculty__fkuniversity__name')
#     paginator = Paginator(listCareer, 10)
#     try:
#        page = int(request.GET.get('page', '1'))
#     except ValueError:
#        page = 1
#     try:
#        careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#        careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#         'label': label,
#         'link': link,
#     }
#     return HttpResponse(template.render(context, request))

# def viewPostponed(request):
#     title = 'Carreras de Grado / Programas de postgrado postergados Modelo Nacional'
#     template = loader.get_template('view_postponed.html')
#     label = 'Universidad'
#     link = '/acreditation/postponed'
#     if request.method == 'POST':
#         form = FormSearch(request.POST)
#         if form.is_valid():
#             search = request.POST['text']
#             careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='Postergada').order_by('national')
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
#     listCareer = Career.objects.filter(fkstatus__description='Postergada').order_by('national')
#     paginator = Paginator(listCareer, 10)
#     try:
#        page = int(request.GET.get('page', '1'))
#     except ValueError:
#        page = 1
#     try:
#        careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#        careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#         'label': label,
#         'link': link,
#     }
#     return HttpResponse(template.render(context, request))

# def viewNoReputable(request):
#     title = 'Carreras de Grado / Programas de postgrado no acreditadas Modelo Nacional'
#     template = loader.get_template('view_postponed.html')
#     label = 'Universidad'
#     link = '/acreditation/no-reputable'
#     if request.method == 'POST':
#         form = FormSearch(request.POST)
#         if form.is_valid():
#             search = request.POST['text']
#             careers = Career.objects.filter(fkfaculty__fkuniversity__name__icontains=search, fkstatus__description='No acreditada').order_by('national')
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
#     listCareer = Career.objects.filter(fkstatus__description='No acreditada').order_by('national')
#     paginator = Paginator(listCareer, 10)
#     try:
#        page = int(request.GET.get('page', '1'))
#     except ValueError:
#        page = 1
#     try:
#        careers = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#        careers = paginator.page(paginator.num_pages)
#     context = {
#         'careers': careers,
#         'title': title,
#         'form': form,
#         'label': label,
#         'link': link,
#     }
#     return HttpResponse(template.render(context, request))

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


# def renderPdf3(request):
#         response = HttpResponse(content_type='aplication/pdf')
#         response['Content-Disposition'] = 'attachment; filename="carrerasAcreditadas.pdf"'
#         buff = BytesIO()
#         doc = SimpleDocTemplate(buff,
#                                 rightMargin=72,
#                                 leftMargin=72,
#                                 topMargin=72,
#                                 bottomMargin=72,
#                                 pagesize=landscape(letter))
 
#         # Our container for 'Flowable' objects
#         elements = []
 
#         # A large collection of style sheets pre-made for us
#         styles = getSampleStyleSheet()
#         # styles = styles["BodyText"]
#         styles.wordWrap = 'CJK'
#         styles.add(ParagraphStyle(name='RightAlign', alignment=TA_JUSTIFY))
 
#         # Draw things on the PDF. Here's where the PDF generation happens.
#         # See the ReportLab documentation for the full list of functionality.
#         # users = User.objects.all()
#         careers = Career.objects.filter(fkstatus__description='Acreditada').order_by('national')
#         elements.append(Paragraph('Carreras de Grado Acreditadas Modelo Nacional', styles['Heading1']))
 
#         # Need a place to store our table rows
#         table_data = []
#         table_data.append(['Carrera', 'Institución', 'Sede', 'Facultad', 'Resolución', 'Fecha', 'Periodo de Acreditación'])
#         for i, c in enumerate(careers):
#             # Add a row to the table
#             table_data.append([c.fknamecareer.description, c.fkfaculty.fkuniversity.name, c.fkfaculty.fkcampus.name, c.fkfaculty.fkname.name, c.fkresolution.number, c.fkresolution.start_date, c.fkresolution.end_date])
#         # Create the table
#         career_table = Table(table_data, colWidths=[doc.width/7.0]*7)
#         career_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
#         elements.append(career_table)
#         doc.build(elements)
 
#         # Get the value of the BytesIO buffer and write it to the response.
#         response.write(buff.getvalue())
#         buff.close()
#         return response


# def renderPdf1(request):
#     doc = SimpleDocTemplate("carrerasAcreditadas.pdf", pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
#     doc.pagesize = landscape(letter)
#     elements = []
#     careers = Career.objects.filter(fkstatus__description='Acreditada').order_by('national')
#     data = []
#     data.append(['Carrera', 'Institución', 'Sede', 'Facultad'])
#     for i, c in enumerate(careers):
#         # Add a row to the table
#         data.append([c.fknamecareer.description, c.fkfaculty.fkuniversity.name, c.fkfaculty.fkcampus.name, c.fkfaculty.fkname.name])
#     # style = TableStyle([
#     #                     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#     #                     ('BOX', (0, 0), (-1, -1), 0.25, colors.black)])

#     style = TableStyle([
#                         ('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
#                         ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
#                         ('VALIGN', (0, 0), (0, -1), 'TOP'),
#                         ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
#                         ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
#                         ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
#                         ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
#                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
#                         ])
#     s = getSampleStyleSheet()
#     s = s["BodyText"]
#     s.wordWrap = 'CJK'
#     data2 = [[Paragraph(cell, s) for cell in row] for row in data]
#     t = Table(data2, colWidths=[doc.width/4.0]*4)
#     t.setStyle(style)
#     elements.append(style)
#     doc.build(elements)

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
