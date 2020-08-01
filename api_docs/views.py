from django.shortcuts import render

# Create your views here.

# Views to docs
def docs(request):
    return render(request, 'api_docs/api_doc_page.html')


