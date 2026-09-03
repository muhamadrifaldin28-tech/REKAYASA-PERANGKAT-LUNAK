from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Pelanggan
    path('pelanggan/', views.pelanggan_list, name='pelanggan_list'),
    path('pelanggan/hapus/<int:pk>/', views.pelanggan_hapus, name='pelanggan_hapus'),

    # Kasir
    path('kasir/', views.kasir_list, name='kasir_list'),
    path('kasir/hapus/<int:pk>/', views.kasir_hapus, name='kasir_hapus'),

    # Sistem Pembayaran
    path('sistem-pembayaran/', views.sistem_pembayaran_list, name='sistem_pembayaran_list'),
    path('sistem-pembayaran/hapus/<int:pk>/', views.sistem_pembayaran_hapus, name='sistem_pembayaran_hapus'),

    # Pilih Menu
    path('pilih-menu/', views.pilih_menu_list, name='pilih_menu_list'),
    path('pilih-menu/hapus/<int:pk>/', views.pilih_menu_hapus, name='pilih_menu_hapus'),

    # Pesan Makanan/Minuman
    path('pesan/', views.pesan_list, name='pesan_list'),
    path('pesan/hapus/<int:pk>/', views.pesan_hapus, name='pesan_hapus'),

    # Melakukan Pembayaran
    path('pembayaran/', views.pembayaran_list, name='pembayaran_list'),
    path('pembayaran/hapus/<int:pk>/', views.pembayaran_hapus, name='pembayaran_hapus'),

    # Validasi Pembayaran
    path('validasi/', views.validasi_list, name='validasi_list'),
    path('validasi/hapus/<int:pk>/', views.validasi_hapus, name='validasi_hapus'),

    # Menyiapkan Pesanan
    path('siapkan/', views.siapkan_list, name='siapkan_list'),
    path('siapkan/hapus/<int:pk>/', views.siapkan_hapus, name='siapkan_hapus'),

    # Mengantar Pesanan
    path('antar/', views.antar_list, name='antar_list'),
    path('antar/hapus/<int:pk>/', views.antar_hapus, name='antar_hapus'),

    # Menerima Pesanan
    path('terima/', views.terima_list, name='terima_list'),
    path('terima/hapus/<int:pk>/', views.terima_hapus, name='terima_hapus'),

    # Rancangan Sistem (ERD & Use Case)
    path('rancangan/', views.rancangan, name='rancangan'),
]
