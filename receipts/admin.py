from django.contrib import admin
from .models import ExpenseCategory, Account, Receipt


@admin.register(ExpenseCategory)
class ExpenseCategory(admin.ModelAdmin):
    pass


@admin.register(Account)
class Account(admin.ModelAdmin):
    pass


@admin.register(Receipt)
class Receipt(admin.ModelAdmin):
    pass