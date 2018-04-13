from django.shortcuts import render
from my_dbh import MyDBH

dbh = MyDBH()


def index(request):
    # show a widget and thing
    widget = dbh.get_widget('some widget')
    thing = dbh.get_thing('some thing')
    return render(request, 'index.html', {'widget': widget, 'thing': thing})
