from django.shortcuts import render

# Create your views here.
import folium #위도와 경도를 잡아와야해

def home(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start= 10)#lat_long위도경도 지정 및 얼만큼의 사이즈인지 알려줌
    mf = mf._repr_html_() #한글로 바꿔주는 방법
    first = 'hwasa'
    result = {'mapfolium':mf, 'f01':first} #변수로 딕셔너리형태로 해서 넘겨주려고 준비
    return render(request, template_name='maps/home.html',context=result)