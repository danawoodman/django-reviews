from django.contrib.auth.models import User
from django.db import models


class VoteManager(models.Manager):
    
    def likes(self):
        """
        Returns a QuerySet of the votes for a Review.
        """
        return self.get_query_set().filter(like=True)
    
    def dislikes(self):
        """
        Returns a QuerySet of the votes against a Review.
        """
        return self.get_query_set().filter(like=False)
    
    def likes_count(self):
        """
        Returns the number of the votes for a Review.
        """
        return self.get_query_set().filter(like=True).count()
    
    def dislikes_count(self):
        """
        Returns the number of the votes against a Review.
        """
        return self.get_query_set().filter(like=False).count()


class ReviewManager(models.Manager):
    """
    Allows Reviews to be listed and sorted by various criteria.
    """
    pass
    # def get_for_user(self, user):
    #     try:
    #         return self.get_query_set().filter(user__pk=user.id)
    #     except:
    #         return None

    # def get_for_instance(self, user):
    #     try:
    #         return self.get_query_set().filter(user__pk=user.id)
    #     except:
    #         return None
"""
get_reviews_for_user
get_reviews_for_model
get_reviews_for_model_instance
"""