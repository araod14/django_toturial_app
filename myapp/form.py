from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task Title", max_length=50)
    description = forms.CharField(label="Task description",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label = "Project Title", max_length=50)