from django.shortcuts import render

# Create your views here.
def about(request):
    about_content = {'about': 'Based in Mombasa, Kenya, a family owned swahili restaurant. Offering moderate prices, making it a popular place for a meal any time of the day.'}
    return render(request, 'about.html', about_content)