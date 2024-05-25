from django.urls import path
from harajat.views import kirimlar_views, chiqimlar_views
urlpatterns = [
    path('chiqimlar/create/', chiqimlar_views.ChiqimlarCreate.as_view(), name='chiqimlar-create'),
    path('chiqimlar/<int:pk>/update/', chiqimlar_views.ChiqimlarUpdate.as_view(), name='chiqimlar-update'),
    path('chiqimlar/<int:pk>/delete/', chiqimlar_views.ChiqimlarDelete.as_view(), name='chiqimlar-delete'),
    path('chiqimlar/', chiqimlar_views.ChiqimlarList.as_view(), name='chiqimlar'),
    path('chiqimlar/<int:pk>/', chiqimlar_views.ChiqimlarDetail.as_view(), name='chiqimlar-detail'),
    path('bugungi_chiqimlar/', chiqimlar_views.KunlikChiqimlarList.as_view(), name='bugungi-chiqimlar'),
    path('bugungi_chiqimlar/umumiy/', chiqimlar_views.KunlikChiqimlarUmumiy.as_view(), name='bugungi-chiqimlar-umumiy'),
    path('oylik_chiqimlar/', chiqimlar_views.OylikChiqimlarList.as_view(), name='oylik-chiqimlar'),
    path('oylik_chiqimlar/umumiy/', chiqimlar_views.OylikChiqimlarUmumiy.as_view(), name='oylik-chiqimlar'),
    path('kirimlar/create/', kirimlar_views.KirimlarCreate.as_view(), name='kirimlar-create'),
    path('kirimlar/<int:pk>/update/', kirimlar_views.KirimlarUpdate.as_view(), name='kirimlar-update'),
    path('kirimlar/<int:pk>/delete/', kirimlar_views.KirimlarDelete.as_view(), name='kirimlar-delete'),
    path('kirimlar/', kirimlar_views.KirimlarList.as_view(), name='kirimlar'),
    path('kirimlar/<int:pk>/', kirimlar_views.KirimlarDetail.as_view(), name='kirimlar-detail'),
    path('bugungi_kirimlar/', kirimlar_views.BugungiKirimlar.as_view(), name='bugungi-kirimlar'),
    path('bugungi_kirimlar/umumiy/', kirimlar_views.KunlikKirimlarUmumiy.as_view(), name='bugungi-kirimlat-umumiy'),
    path('oylik_kirimlar/', kirimlar_views.OylikKirimlar.as_view(), name='oylik-kirimlar'),
    path('oylik_kirimlar/umumiy/', kirimlar_views.OylikKirimlarSum.as_view(), name='oylik-kirimlar-umumiy'),

]