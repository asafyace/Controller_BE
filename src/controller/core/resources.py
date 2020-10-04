from import_export import resources
from .models import Server,Lab, Command

class ServerResource(resources.ModelResource):
    class Meta:
        model = Server

class LabResource(resources.ModelResource):
    class Meta:
        model = Lab

class CommandResource(resources.ModelResource):
    class Meta:
        model = Command