from django.shortcuts import render

# Create your views here.

# Views to docs
def commentDocs(request):
    return render(request, 'api_docs/comment_api/comment_doc.html')

def authDocs(request):
    return render(request, 'api_docs/auth_api/auth_doc.html')

# Views to hire consultant
def consultant(request):
    return render(request, 'api_docs/hire_consultant.html')

