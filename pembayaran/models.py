from django.db import models

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Kasir(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class SistemPembayaran(models.Model):
    nama = models.CharField(max_length=100, default="Sistem Pembayaran")

    def __str__(self):
        return self.nama


class PilihMenu(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)


class PesanMakananMinuman(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)


class MelakukanPembayaran(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    kasir = models.ForeignKey(Kasir, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)


class ValidasiPembayaran(models.Model):
    kasir = models.ForeignKey(Kasir, on_delete=models.CASCADE)
    sistem_pembayaran = models.ForeignKey(SistemPembayaran, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)


class MenyiapkanPesanan(models.Model):
    kasir = models.ForeignKey(Kasir, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)


class MengantarPesanan(models.Model):
    kasir = models.ForeignKey(Kasir, on_delete=models.CASCADE)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)


class MenerimaPesanan(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, blank=True)