from django.contrib import admin
from .models import Question, Choice

from sondages.models import Sondage
from sondages.models import Drinker
from sondages.models import Results
from sondages.models import QuestionsGroups
from sondages.models import GroupQuestionRelationship


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['question_text', 'anonymous', 'comment_option']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),

    ]
    inlines = [ChoiceInline, ]

    list_display = ('question_text', 'pub_date', 'was_published_recently',)
    list_filter = ['pub_date', ]
    search_fields = ['question_text']


class DrinkerInline(admin.TabularInline):
    model = Drinker
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


class ResultsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questions']})
        , ('Answers', {'fields': ['users'], 'classes': ['wide']})

    ]

    # inlines = [DrinkerInline]


    list_display = ('questions', 'votes', 'comment')
    list_filter = ['users', ]
    search_fields = ['questions']


class QuestionsGroupsAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['name', 'group_id']})
    ]

    list_display = ('group_id', 'name')
    list_filter = ('name',)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3

class QuestionGroupInline(admin.TabularInline):
    model = Question
    extra = 3


class GroupQuestionRelationshipAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['gqr_group', 'gqr_question']})
    ]

    list_display = ('gqr_group', 'gqr_question')
    list_filter = ('gqr_group',)




admin.site.register(Drinker)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(QuestionsGroups, QuestionsGroupsAdmin)
admin.site.register(GroupQuestionRelationship, GroupQuestionRelationshipAdmin)

#







