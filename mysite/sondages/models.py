import datetime
from django.db import models
from django.utils import timezone




# modification
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.









class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    anonymous = models.BooleanField(default=True)
    comment_option = models.BooleanField(default=True)



    def __str__(self):
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)

    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text


# modification-

class Sondage(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    moderator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)


# tuto1
class Drinker(models.Model):
    def __str__(self):
        return self.user.username


    user = models.OneToOneField(User)
    birthday = models.DateField(null=True)
    name = models.CharField(max_length=100, null=True)


    def __unicode__(self):
        return self.name


class Results(models.Model):
    users = models.ForeignKey('Drinker', null=True)
    questions = models.ForeignKey('Question')
    votes = models.ForeignKey('Choice')
    comment = models.CharField(max_length=100, help_text="This is the grey text", null=True)
    def __str__(self):
        name = ''
        try:
            name = self.users.name
        except AttributeError:
            pass
        return name


class QuestionsGroups(models.Model):

     group_id = models.IntegerField(null=True)
     name = models.CharField(max_length=50, null=True)

     def __str__(self):
        return self.name

class GroupQuestionRelationship (models.Model):

     gqr_group = models.ForeignKey('QuestionsGroups')
     gqr_question = models.ForeignKey('Question')


     def __str__(self):
        return self.gqr_group.name







        # create our user object to attach to our sondages  object  # def create_sondages_user_callback(sender, instance, **kwargs):

# sondages, new = Drinker.objects.get_or_create(user=instance)
#post_save.connect(create_sondages_user_callback,User)
