from django.urls import path

from invoice import views



urlpatterns = [
    path('', views.InvoiceFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', views.InvoiceDetailView.as_view(), name='detail'),
    path('create/', views.InvoiceCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(), name='delete'),
]

## クラスベースビューの場合
##path(URL, views.クラス名.as_view(), name=URL名称)

# 関数ベースビューの場合
##path(URL, views.関数名, name=URL名称)

#<int:pk>とはURL のその部分を、その名前のパラメーターとしてビューに渡します。
# 次に、ビュー関数を次のように記述できます。
#def my_view(request, pk):
#    ...
#ビュー内でその変数を参照します。
#通常、モデルの主キーを参照するために使用されます。