from django.views import View
from django.shortcuts import render
from .models import Server
from .resources import ServerResource
from tablib import Dataset
from django.http import HttpResponse
from django.http import Http404


class HomeView(View):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            server_resource = ServerResource()
            dataset = Dataset()
            new_servers = request.FILES['file']
            imported_data = dataset.load(new_servers.read())
            result = server_resource.import_data(
                dataset, dry_run=True)  # Test the data import
            if (not result.has_errors()) and (not result.has_validation_errors()):
                server_resource.import_data(
                    dataset, dry_run=False)  # Actually import now
                return HttpResponse("Success imported server data")
        raise Http404("import did not succeed")
