from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Pelanggan, Kasir, SistemPembayaran,
    PilihMenu, PesanMakananMinuman, MelakukanPembayaran,
    ValidasiPembayaran, MenyiapkanPesanan, MengantarPesanan, MenerimaPesanan
)
from .forms import (
    PelangganForm, KasirForm, SistemPembayaranForm,
    PilihMenuForm, PesanMakananMinumanForm, MelakukanPembayaranForm,
    ValidasiPembayaranForm, MenyiapkanPesananForm, MengantarPesananForm,
    MenerimaPesananForm
)


def index(request):
    """Halaman utama: menampilkan menu ke semua modul aktivitas."""
    menu = [
        {'nama': 'Pelanggan', 'url': 'pelanggan_list'},
        {'nama': 'Kasir', 'url': 'kasir_list'},
        {'nama': 'Sistem Pembayaran', 'url': 'sistem_pembayaran_list'},
        {'nama': 'Pilih Menu', 'url': 'pilih_menu_list'},
        {'nama': 'Pesan Makanan/Minuman', 'url': 'pesan_list'},
        {'nama': 'Melakukan Pembayaran', 'url': 'pembayaran_list'},
        {'nama': 'Validasi Pembayaran', 'url': 'validasi_list'},
        {'nama': 'Menyiapkan Pesanan', 'url': 'siapkan_list'},
        {'nama': 'Mengantar Pesanan', 'url': 'antar_list'},
        {'nama': 'Menerima Pesanan', 'url': 'terima_list'},
    ]
    return render(request, 'pembayaran/index.html', {'menu': menu})


def _crud_view(request, model, form_class, judul, list_url_name, hapus_url_name):
    """
    Fungsi generik untuk menampilkan daftar data + form tambah data.
    Dipakai ulang oleh semua view di bawah supaya kode tidak berulang
    dan konsisten dengan tabel yang ada di models.py.
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_url_name)
    else:
        form = form_class()

    queryset = model.objects.all().order_by('-id')
    field_names = list(form_class.base_fields.keys())

    rows = []
    for obj in queryset:
        values = [getattr(obj, name) for name in field_names]
        rows.append({'pk': obj.pk, 'values': values})

    context = {
        'judul': judul,
        'headers': [form_class.base_fields[name].label or name for name in field_names],
        'rows': rows,
        'form': form,
        'list_url_name': list_url_name,
        'hapus_url_name': hapus_url_name,
    }
    return render(request, 'pembayaran/crud.html', context)


def _hapus_view(request, model, pk, list_url_name):
    """Fungsi generik untuk menghapus satu baris data berdasarkan id."""
    item = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect(list_url_name)


# ---------------- Pelanggan ----------------
def pelanggan_list(request):
    return _crud_view(request, Pelanggan, PelangganForm, 'Data Pelanggan', 'pelanggan_list', 'pelanggan_hapus')


def pelanggan_hapus(request, pk):
    return _hapus_view(request, Pelanggan, pk, 'pelanggan_list')


# ---------------- Kasir ----------------
def kasir_list(request):
    return _crud_view(request, Kasir, KasirForm, 'Data Kasir', 'kasir_list', 'kasir_hapus')


def kasir_hapus(request, pk):
    return _hapus_view(request, Kasir, pk, 'kasir_list')


# ---------------- Sistem Pembayaran ----------------
def sistem_pembayaran_list(request):
    return _crud_view(request, SistemPembayaran, SistemPembayaranForm, 'Data Sistem Pembayaran', 'sistem_pembayaran_list', 'sistem_pembayaran_hapus')


def sistem_pembayaran_hapus(request, pk):
    return _hapus_view(request, SistemPembayaran, pk, 'sistem_pembayaran_list')


# ---------------- Pilih Menu ----------------
def pilih_menu_list(request):
    return _crud_view(request, PilihMenu, PilihMenuForm, 'Aktivitas: Pilih Menu', 'pilih_menu_list', 'pilih_menu_hapus')


def pilih_menu_hapus(request, pk):
    return _hapus_view(request, PilihMenu, pk, 'pilih_menu_list')


# ---------------- Pesan Makanan/Minuman ----------------
def pesan_list(request):
    return _crud_view(request, PesanMakananMinuman, PesanMakananMinumanForm, 'Aktivitas: Pesan Makanan/Minuman', 'pesan_list', 'pesan_hapus')


def pesan_hapus(request, pk):
    return _hapus_view(request, PesanMakananMinuman, pk, 'pesan_list')


# ---------------- Melakukan Pembayaran ----------------
def pembayaran_list(request):
    return _crud_view(request, MelakukanPembayaran, MelakukanPembayaranForm, 'Aktivitas: Melakukan Pembayaran', 'pembayaran_list', 'pembayaran_hapus')


def pembayaran_hapus(request, pk):
    return _hapus_view(request, MelakukanPembayaran, pk, 'pembayaran_list')


# ---------------- Validasi Pembayaran ----------------
def validasi_list(request):
    return _crud_view(request, ValidasiPembayaran, ValidasiPembayaranForm, 'Aktivitas: Validasi Pembayaran', 'validasi_list', 'validasi_hapus')


def validasi_hapus(request, pk):
    return _hapus_view(request, ValidasiPembayaran, pk, 'validasi_list')


# ---------------- Menyiapkan Pesanan ----------------
def siapkan_list(request):
    return _crud_view(request, MenyiapkanPesanan, MenyiapkanPesananForm, 'Aktivitas: Menyiapkan Pesanan', 'siapkan_list', 'siapkan_hapus')


def siapkan_hapus(request, pk):
    return _hapus_view(request, MenyiapkanPesanan, pk, 'siapkan_list')


# ---------------- Mengantar Pesanan ----------------
def antar_list(request):
    return _crud_view(request, MengantarPesanan, MengantarPesananForm, 'Aktivitas: Mengantar Pesanan', 'antar_list', 'antar_hapus')


def antar_hapus(request, pk):
    return _hapus_view(request, MengantarPesanan, pk, 'antar_list')


# ---------------- Menerima Pesanan ----------------
def terima_list(request):
    return _crud_view(request, MenerimaPesanan, MenerimaPesananForm, 'Aktivitas: Menerima Pesanan', 'terima_list', 'terima_hapus')


def terima_hapus(request, pk):
    return _hapus_view(request, MenerimaPesanan, pk, 'terima_list')


# ---------------- Rancangan Sistem (ERD & Use Case) ----------------
def rancangan(request):
    """Menampilkan dokumentasi rancangan sistem: ERD dan Use Case Diagram."""
    return render(request, 'pembayaran/rancangan.html')
