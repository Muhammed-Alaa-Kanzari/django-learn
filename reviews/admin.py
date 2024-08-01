from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn13', 'has_isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name__startswith')

    @admin.display(
        ordering='isbn',
        description="ISBN-13",
        empty_value='-/-'
    )
    def isbn13(self, obj):
        return '{}-{}-{}-{}-{}'.format(obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])

    @admin.display(
        boolean=True,
        description='Has ISBN',
    )
    def has_isbn(self, obj):
        return bool(obj.isbn)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    list_filter = ('name',)
