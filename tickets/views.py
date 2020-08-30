from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ticketapi.serializers import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from tickets.models import Ticket, Category
import datetime
from django.utils.timezone import now
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    #res=[]
    serializer_class = TicketSerializer
    

    
    date_format = "%Y-%m-%d"
    #for i in queryset:
        
    '''#delta = datetime.now() - (str(i.created[:26])
     print(datetime.now(), str(i.created)[:26])
     #print( delta.total_seconds() / (60 * 60))
     #print(res)
     n=str(datetime.now())[:19]
     #print(n)
     c=str(i.created)[:19]
     #print(c)
     d,t=n.split()
     k,p=c.split()
     #print(d,t)
     unmarked=[]
     y,m,d=d.split("-")
     h,min,s=t.split(":")
     y1,m1,d1=k.split("-")
     h1,min1,s1=p.split(":")
     #print(y,m,d,y1,m1,d1)
     y=int(y)
     m=int(m)
     d=int(d)
     y1=int(y1)
     m1=int(m1)
     d1=int(d1)
     h1=int(h1)
     h=int(h1)
     min1=int(min1)
     min=int(min)
     s=int(s)
     s1=int(s1)
     timeinsec=abs(y-y1)*31536000 + abs(m1-m)*2628002 +abs(d-d1)*86400 +abs(h1-h)*3600 +abs(min1-min)*60 + abs(s-s1)
     if timeinsec>=8*3600:
        res.append(i)
     else:
         pass
    print("list of unmarked tickets")
    print(res)
    print("list of marked tickets")
    print(unmarked)
    for i in res:
        print(i)'''
    obj = Ticket.objects.get(ticket_id =2)
    financial_data = obj
    print(financial_data)
    k=(Ticket.objects.filter(ticket_id__in = ['3','1']))
    def k(request):
        return HttpResponse(k)
    


    




# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #print(queryset)

# Create your views here.
def k(request):
        return HttpResponse(Ticket.objects.filter(ticket_id__in = ['3','1']))

