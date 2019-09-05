from django.contrib import admin

from .models import Fop, FopRecord, Uo, UoRecord, Founder


@admin.register(FopRecord)
class FopRecordAdmin(admin.ModelAdmin):
    list_filter = ('stan', )


@admin.register(Fop)
class FopAdmin(admin.ModelAdmin):
    pass


class FounderInline(admin.TabularInline):
    model = Founder


@admin.register(UoRecord)
class UoRecordAdmin(admin.ModelAdmin):
    inlines = [
        FounderInline,
    ]

@admin.register(Uo)
class UoAdmin(admin.ModelAdmin):
    pass
