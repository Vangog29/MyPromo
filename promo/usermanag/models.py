from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class ExtendedUser(AbstractUser):
    date_joined = None
    last_login = None
    groups = None
    user_permissions = None
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class House(models.Model):
    id_house = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200, verbose_name='Город', default="default title")
    street = models.CharField(max_length=200, verbose_name='Улица')
    house_number = models.CharField(max_length=200, verbose_name='Номер дома', default="default title")

    entrance = models.IntegerField(verbose_name='Количество подъездов')
    apartment_in_entracne = models.IntegerField(verbose_name='Квартир в подъезде')
    poll = models.BooleanField(verbose_name='Обход')

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


class Campaing(models.Model):
    id_campaign = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=200, verbose_name='Название кампании', unique=True)
    campaign_description = models.CharField(max_length=200, verbose_name='Описание кампании')

    class Meta:
        verbose_name = 'Кампания'
        verbose_name_plural = 'Кампании'


class Poll(models.Model):
    id_poll = models.AutoField(primary_key=True)
    door_open = models.BooleanField (verbose_name='Открыли дверь')
    date = models.DateField(verbose_name='Дата обхода')
    time = models.TimeField(verbose_name='Время обхода')
    reaction = models.CharField(max_length=400, verbose_name='Реакция')

    class Meta:
        verbose_name = 'Обход'
        verbose_name_plural = 'Обходы'


class PoolForm(models.Model):
    id_form = models.AutoField(primary_key=True)
    resp_name = models.CharField(max_length=200, verbose_name='Имя')
    resp_phone_number = models.CharField(max_length=200, verbose_name='Телефон')
    comment = models.CharField(max_length=400, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Протокол обходов'
        verbose_name_plural = 'Протоколы'

class CampaignData (models.Model):
    user_camp = models.ForeignKey('ExtendedUser',  blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    house_camp = models.ForeignKey('House', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Адрес')
    camp_num = models.ForeignKey('Campaing', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Кампания')
    poll_camp = models.ForeignKey('Poll', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Обход')
    poll_form_camp = models.ForeignKey('PoolForm',blank=True, null=True, on_delete=models.CASCADE, verbose_name='Форма обхода')
