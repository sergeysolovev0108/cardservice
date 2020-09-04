from django.contrib import admin
from .models import *
from django import forms


class SexAdminForm(forms.ModelForm):
    class Meta:
        model = Sex
        fields = ('gender',)


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    form = SexAdminForm
    save_as = True
    list_display = ('gender', 'id')
    search_fields = ('gender',)


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'name', 'fathers_name', 'passport_number',
                  'phone', 'sex',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    save_as = True
    list_display = ('last_name', 'name', 'fathers_name', 'passport_number',
                    'phone', 'sex', 'get_card_number')
    search_fields = ('last_name', 'passport_number', 'phone',)
    list_display_links = ('last_name', 'get_card_number')

    def get_card_number(self, obj):
        user = User.objects.get(pk=obj.id)
        card = user.clubcard_set.all()
        for i in card:
            return i.card_number


class CardStatusAdminForm(forms.ModelForm):
    class Meta:
        model = CardStatus
        fields = ('title',)


@admin.register(CardStatus)
class CardStatusAdmin(admin.ModelAdmin):
    form = CardStatusAdminForm
    save_as = True
    list_display = ('title', 'id')


class CardCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = CardCategory
        fields = ('name',)


@admin.register(CardCategory)
class CardCategoryAdmin(admin.ModelAdmin):
    form = CardCategoryAdminForm
    save_as = True
    list_display = ('name', 'id')
    search_fields = ('name',)


class ActivateDateAdminForm(forms.ModelForm):
    class Meta:
        model = ActiveDate
        fields = ('title', 'value', 'price',)


@admin.register(ActiveDate)
class ActivateDateAdmin(admin.ModelAdmin):
    form = ActivateDateAdminForm
    save_as = True
    list_display = ('title', 'value', 'price', 'id')
    search_fields = ('title', 'value', 'price',)


class ClubCardAdminForm(forms.ModelForm):
    class Meta:
        model = ClubCard
        fields = ('user', 'balance', 'status',
                  'category', 'active_date', 'freeze_time')


@admin.register(ClubCard)
class ClubCardAdmin(admin.ModelAdmin):
    form = ClubCardAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'card_number', 'user', 'create_date', 'end_date', 'balance', 'status',
                    'category', 'active_date', 'freeze_time')
    search_fields = ('card_number', 'user__last_name', 'status__title',
                     'category__name',)
    list_display_links = ('card_number', 'user',)
