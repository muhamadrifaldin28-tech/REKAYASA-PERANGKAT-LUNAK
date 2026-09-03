from django import forms
from .models import (
    Pelanggan, Kasir, SistemPembayaran,
    PilihMenu, PesanMakananMinuman, MelakukanPembayaran,
    ValidasiPembayaran, MenyiapkanPesanan, MengantarPesanan, MenerimaPesanan
)


class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = '__all__'


class KasirForm(forms.ModelForm):
    class Meta:
        model = Kasir
        fields = '__all__'


class SistemPembayaranForm(forms.ModelForm):
    class Meta:
        model = SistemPembayaran
        fields = '__all__'


class PilihMenuForm(forms.ModelForm):
    class Meta:
        model = PilihMenu
        fields = '__all__'


class PesanMakananMinumanForm(forms.ModelForm):
    class Meta:
        model = PesanMakananMinuman
        fields = '__all__'


class MelakukanPembayaranForm(forms.ModelForm):
    class Meta:
        model = MelakukanPembayaran
        fields = '__all__'


class ValidasiPembayaranForm(forms.ModelForm):
    class Meta:
        model = ValidasiPembayaran
        fields = '__all__'


class MenyiapkanPesananForm(forms.ModelForm):
    class Meta:
        model = MenyiapkanPesanan
        fields = '__all__'


class MengantarPesananForm(forms.ModelForm):
    class Meta:
        model = MengantarPesanan
        fields = '__all__'


class MenerimaPesananForm(forms.ModelForm):
    class Meta:
        model = MenerimaPesanan
        fields = '__all__'
