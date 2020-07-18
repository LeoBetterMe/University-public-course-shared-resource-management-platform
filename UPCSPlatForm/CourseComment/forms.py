# Begin
# auth:gz
# create date:7.17
# description:评价表单验证

from django import forms


class CommentForm(forms.Form):
    thisComment = forms.CharField(
        label="评论", max_length=1024, min_length=1, widget=forms.Textarea(
            attrs={'rows': 5, 'required': "required"}
        )
    )

# End
