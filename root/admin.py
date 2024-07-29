from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from reviews.models import Book, Contributor, Publisher, Review


class BookAdminSite(AdminSite):
    site_header = 'Book Adminstration'
    site_title = 'Book Admin'
    index_title = 'Welcome to our BookStore Admin Portal'


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn13', 'has_isbn')
    list_filter = ('publisher', 'publication_date')

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


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)


class UserAdmin(admin.ModelAdmin):
    list_filter = ["is_staff", "is_superuser"]


admin_site = BookAdminSite(name='myAdmin')

admin_site.register(User, UserAdmin)
admin_site.register(Group)


admin_site.register(Book, BookAdmin)
admin_site.register(Publisher, PublisherAdmin)
admin_site.register(Contributor, ContributorAdmin)
admin_site.register(Review)
