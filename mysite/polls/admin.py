from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):  # defines how the Choice model will be displayed inline within the Question admin inteface
    model = Choice  # model to be displayed inline
    extra = 3  # indicates no of blank forms to display for adding choice objects inline


class QuestionAdmin(admin.ModelAdmin):  # ALlows me to customixe how the Question model id presented and managed in the Dlango admin interface
    fieldsets = [
        (None, {"fields": ["question_text"]}),   # none indicates that this section does not have a title
        ("Date information", {"fields": ["pub_date"], "classes" : ["collapse"]}),  
        # Date information is the title of the section. the tuple shoes that the only field inclued in the section is pun_date
        # the classes : collapse colapses the fieldset by default until the user chooses to exapand it
    ]
    inlines = [ChoiceInLine]
      # property of the above class where each tuple shows a section of the fields displayed in the admin interface
    list_display = ["question_text", "pub_date", "was_published_recently"]  # how the model will be displayed
    list_filter = ["pub_date"]  # adds filters
    search_fields = ["question_text"]  # adds a searhcch box


admin.site.register(Question, QuestionAdmin)  #   registers the Question model with the QuestionAdmin class, indicating that you want to use the custom admin options defined in QuestionAdmin for managing Question
# create a model admin class then pass it as the second argument to admin.site.register()

