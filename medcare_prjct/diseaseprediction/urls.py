from django.urls import path
from diseaseprediction.views import *
from django.conf.urls.static import static



urlpatterns = [
    path('',home_diseaseprediction, name='home_diseaseprediction'), #done
    path('cataract/', predict_cataract, name='predict_cataract'),   #done
    path('ecg/', predict_ecg, name='predict_ecg'),                  #error in model
    path('mri/', predict_tumor, name='predict_tumor'),
    path('diabetes/', predict_diabetes, name='predict_diabetes'),   #done
    path('tuberculosis/', predict_tuberculosis, name='predict_tuberculosis'), #done
    path('stress_management/', predict_cataract, name='predict_stress'),
    path('aids/', predict_aids, name='predict_aids'),
    
    path('predict1/', gotoecg, name='gotoecg'),
    path('predict2/', gotocataract, name='gotocataract'),
    path('predict3/', gotostress, name='gotostress'),
    path('predict4/', gototubersulosis, name='gototubersulosis'),
    path('predict5/', gototumor, name='gototumor'),
    path('predict6/', gotodiabetes, name='gotodiabetes'),
    path('predict7/', gotoaids, name='gotoaids'),


    path('feedback_ecg/', feedback_ecg, name='feedback_ecg'),
    path('feedback_cataract/', feedback_cataract, name='feedback_cataract'),
    path('aboutUs/', about_us, name='about_us'),
    path('login/', login_u, name='login_u'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)