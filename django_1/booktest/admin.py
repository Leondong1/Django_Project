from django.contrib import admin
from booktest.models import BookInfo,HeroInfo


admin.site.site_header = '东杰书城'
admin.site.site_title = 'Leon书城MIS'
admin.site.index_title = '欢迎使用Leon书城MIS'

# Register your models here.
# 咱们在这里做的目的是为了自定义咱们的模型类里面的展示信息
class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo  # 要编辑的对象
    extra = 1  # 附加编辑的数量


class BookInfoAdmin(admin.ModelAdmin):

    # 注意：这里可以是列表或者元组均可，只要是可以遍历
    list_display = ['id', 'btitle', 'bpub_date']
    # fields = ['btitle','bpub_date']
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date']}),
        ('高级', {
            'fields': ['bread', 'bcomment','logo'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )
    inlines = [HeroInfoStackInline]

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = True
    actions_on_top = True
    # 注意：这里的hbook是以字段的字符串表现方式展示
    list_display = ['id','hname','hcomment','hbook','read']
    list_filter = ['hbook','hgender']
    search_fields = ['hname']




admin.site.register(BookInfo,BookInfoAdmin)
# 如果已经使用装饰器进行关联，则不再采用adminz站点注册的方式
# admin.site.register(HeroInfo)

