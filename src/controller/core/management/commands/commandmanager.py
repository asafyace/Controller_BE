from django.core.management.base import BaseCommand, CommandError
from core.models import Server, Lab, User
import paramiko
from pypsexec.client import Client
from django.http import HttpResponse

class Command(BaseCommand):
    help = 'Checks connectivity to servers'

    def handle(self, *args, **options):

        while(True is True):
            Server_list = Server.objects.all()
            Users = User.objects.all()
            for Host in Server_list:
                command = Host.Lastcommand
                if((command != "" and Host.OS == "Linux")):
                    if(Host.runcommand == False):
                        usernamel = Users[0].user_name
                        passwordl = Users[0].password
                        port = 22
                        linuxhost = Host.IPAddress
                        print("Connecting to server " + Host.Hostname +
                              " and executing " + command)
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(
                            paramiko.AutoAddPolicy())
                        try:
                            ssh.connect(linuxhost, port, usernamel, passwordl)
                            stdin, stdout, stderr = ssh.exec_command(command)
                            errormes = stderr.readlines()
                            if (errormes != []):
                                Host.output = errormes
                            else:
                                Host.output = stdout.readlines()
                            Host.runcommand = True
                            Host.save()
                        except:
                            Host.output = "Cant connect to server"
                            Host.runcommand = True
                            Host.save()
                if((command != "" and Host.OS == "Windows")):
                    if(Host.runcommand == False):
                        windowshost = Host.IPAddress
                        labs = Lab.objects.all()
                        dbuser = Users[1].user_name
                        dblab = labs[0].labname
                        user = dblab+"\\"+dbuser
                        windowspass = Users[1].password
                        c = Client(windowshost, username=user,
                                   password=windowspass, encrypt=False)
                        try:
                            c.connect()
                            print("Running on " + Host.Hostname +
                                  " the command "+command)
                            c.create_service()
                            stdout, stderr, rc = c.run_executable(
                                "powershell.exe", arguments=command)
                            if (len(stderr) > 4):
                                Host.output = stderr
                            else:
                                Host.output = stdout
                            Host.runcommand = True
                            Host.save()
                            c.remove_service()
                            c.disconnect()
                        except:
                            Host.output = "Cant connect to server"
                            Host.runcommand = True
                            Host.save()
