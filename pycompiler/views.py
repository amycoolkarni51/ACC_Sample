from django.shortcuts import render
from django.http import HttpResponse
import subprocess

HELLO_WORLD = """
print('Hello World!')
"""

# Create your views here.
def editor(request):
    # Endpoint for client's visit
    if request.method == 'GET':
        return render(request, 'editor_py.html', { 'code': HELLO_WORLD, 'output': '' })
    
    # Endpoint to execute the program sent thru POST
    elif request.method == 'POST':
        code_area_data = request.POST['codearea']
        output = ""

        try:
            # the contents of the code area are written to a file on the server
            with open('files/py_code.py', 'w') as file:
                file.write(code_area_data)
            
            # run the python program
            result = subprocess.run(['python3', 'files/py_code.py'], capture_output=True, text=True, timeout=10)

            # output is set to either stderr or stdout
            if result.returncode == 1:
                output = result.stderr
            elif result.returncode == 0:
                output = result.stdout

        # in case any other exception occurs in the subprocess, client will be notified
        except subprocess.CalledProcessError as e:
            output = str(e)
        except subprocess.TimeoutExpired as e:
            output = 'TIME LIMIT EXCEEDED'

        return render(request, 'editor_py.html', { 'code': code_area_data, 'output': output })
