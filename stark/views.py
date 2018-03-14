# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response, redirect
from models import Project, Worker, DatabaseForm
from graphs.chart import chart
from database.PythonCQL import CassandraDB
from django.utils import timezone
import json





class TestPageView(TemplateView):
    template_name = "test.html"


class HomePageView(TemplateView):
    template_name = "main.html"




class LoginFormControl(TemplateView):
    template_name = "registration/login.html"



class VerilerPageView(TemplateView):
    template_name = "veriler.html"

    def get(self, request, *args, **kwargs):
        i = chart()
        j= CassandraDB()
        dataPoints, x, y1, y2 = i.datas()
        j.connect()
        d = j.select()


        return render(request, 'veriler.html',  { 'ch':dataPoints, 'cd': d['IoT Cihaz 1']} )



class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        # we will pass this context object into the
        # template so that we can access the data
        # list in the template
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'data.html', context)

