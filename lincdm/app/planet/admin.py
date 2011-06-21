# -*- coding: utf-8 -*-

from django.contrib import admin

from app.planet.models import (Blog, Generator, Feed, FeedLink, Post, PostLink,
    Author, PostAuthorData, Enclosure)


class PostLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "rel", "mime_type", "post", "link")
    list_filter = ("rel", "mime_type")

admin.site.register(PostLink, PostLinkAdmin)


class PostAuthorDataAdmin(admin.ModelAdmin):
    list_display = ("author", "is_contributor", "post")
    list_filter = ("is_contributor", "author")

admin.site.register(PostAuthorData, PostAuthorDataAdmin)


class EnclosureAdmin(admin.ModelAdmin):
    list_display = ("post", "mime_type", "length", "link")
    list_filter = ("mime_type",)

admin.site.register(Enclosure, EnclosureAdmin)

class FeedAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "blog", "language", "generator")
    list_filter = ("language", "generator",)

admin.site.register(Feed, FeedAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

admin.site.register(Author, AuthorAdmin)

class EnclosureInline(admin.StackedInline):
    model = Enclosure
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "feed", "url")
    list_filter = ("feed",)
    # filter_horizontal = ('tags',)

admin.site.register(Post, PostAdmin, inlines=[EnclosureInline])


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "url")

admin.site.register(Blog, BlogAdmin)


class GeneratorAdmin(admin.ModelAdmin):
    list_display = ("name", "version", "link")

admin.site.register(Generator, GeneratorAdmin)


class FeedLinkAdmin(admin.ModelAdmin):
    list_display = ("feed", "mime_type", "rel", "link")
    list_filter = ("mime_type", "rel")

admin.site.register(FeedLink, FeedLinkAdmin)
