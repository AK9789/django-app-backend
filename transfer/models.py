from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class History(models.Model):
    attach = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(blank=True)
    sent_type = models.BooleanField(default=True) # if true income, if false expence
    time = models.DateTimeField(default=timezone.now(), blank=True)



# only the user migrations are created
# history is coded maid but not migrated | do the migration
# create the message models as well for both (report the problem & requesting  new acccount) | do migrations
# start the API | 
# $ start from this point  | auth serilazer and more
# craete Auth api | create a new serilazer and make it json possible
#     login route | get user(pure) route
# create the transfer api | create a new serilazer 
#    FUNCTION
#       * find sender user will be taken from the req.user FUNC
#       * find recever user using the unique account number
#       * 1) Check -> if sender balance is > then sending_limit then_OK | else error message
#       * 2) if (1)=True then minus(-sending_limit) from sender banance and add(+sending_limit) to recever
#       * 3) if (2)=true then create two histry records under recever and sender (sender{type=exprnse}) and (recever{type=income})
# view all the history api | star from here
# create the message API | create the serilazer
#   new accout request is public
#   report problem need  auth
#       both is seen by the admin