# auth:lzy
# create date:7.15
# description:课程评价部分实体类

# Create your models here.
from win32timezone import now
from CoursePart.models import Course
from MySite.models import User
from django.db import models


class Comment(models.Model):
    Comment_ID = models.AutoField(primary_key=True)
    Course_ID = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)  # 评论所属课程
    Comment_User_ID = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)  # 评论者  
    Comment_text = models.CharField(max_length=1024, null=False)
    Time = models.DateTimeField(null=False, default=now)
    To_Comment_ID = models.ForeignKey('self', related_name='to_comment', null=True, blank=True, on_delete=models.CASCADE)  # 回复评论

    def __str__(self):
        return self.Comment_User_ID.UserName + '：' + self.Comment_text

    def getID(self):
        return self.id

    class Meta:
        ordering = ["Comment_User_ID", "Time"]
        verbose_name = "用户评价"
        verbose_name_plural = "用户评价"


# End
