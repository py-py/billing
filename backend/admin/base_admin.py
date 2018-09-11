from django.contrib import admin


class BaseGroupAdmin(admin.ModelAdmin):
    exclude = ('group', )

    def get_queryset(self, request):
        queryset = super(BaseGroupAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            group = request.user.groups.first()
            queryset = queryset.filter(group=group)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.group = request.user.groups.first()
        super().save_model(request, obj, form, change)

