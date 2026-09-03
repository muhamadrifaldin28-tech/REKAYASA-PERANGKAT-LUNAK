from django.contrib import admin
from .models import (
    Pelanggan, Kasir, SistemPembayaran,
    PilihMenu, PesanMakananMinuman, MelakukanPembayaran,
    ValidasiPembayaran, MenyiapkanPesanan, MengantarPesanan, MenerimaPesanan
)

admin.site.register(Pelanggan)
admin.site.register(Kasir)
admin.site.register(SistemPembayaran)
admin.site.register(PilihMenu)
admin.site.register(PesanMakananMinuman)
admin.site.register(MelakukanPembayaran)
admin.site.register(ValidasiPembayaran)
admin.site.register(MenyiapkanPesanan)
admin.site.register(MengantarPesanan)
admin.site.register(MenerimaPesanan)