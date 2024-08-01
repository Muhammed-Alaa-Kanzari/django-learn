from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from reviews.models import Book, Contributor, Publisher, Review
from reviews.admin import BookAdmin, PublisherAdmin


class BookAdminSite(AdminSite):
    site_header = 'Book Adminstration'
    site_title = 'Book Admin'
    index_title = 'Welcome to our BookStore Admin Portal'


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
