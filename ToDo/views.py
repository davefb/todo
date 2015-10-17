from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect
from ToDo.models import ToDo, ToDoItem
from json import dumps

from django.core import serializers


def create(request,json=None,ignore=None):
    newlist = ToDo()
    newlist.save()

    if json is not None:
        return HttpResponse(dumps({"id":newlist.id}), content_type="application/json")
    else:
        return redirect('ToDo.views.list', id=newlist.id);

def list(request,id,json=None):
    result = ToDo.objects.all().filter(id=int(id))

    if len(result)<=0:
        raise  Http404("Cannot find list!");

    if json is not None:
        return HttpResponse(serializers.serialize('json', result[0].items.all()), content_type="application/json")
    else:
        t = result[0].items.all();
        context = {'items': t}
        return render(request, 'todo.html', context)

def add_item(request,id,json=None):
    result = ToDo.objects.get(id=int(id))

    if result is  None:
        return Http404()

    item = ToDoItem()
    item.item_text = request.GET["text"];
    result.items.add(item);
    result.save();
    item.save();

    return HttpResponse("{\"id\":\"%s\"}"%item.id, content_type="application/json")

def remove_item(request,id,itemid):
    result = ToDo.objects.get(id=int(id)).items.get(id=int(itemid))
    result.delete()

    return HttpResponse("{}", content_type="application/json")



